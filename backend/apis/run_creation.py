"""Service for creating new runs."""

from models.run_creation import RunCreation, fetch_run_creation, update_run_creation
from models.run import Run as DBRun, save_run
from core.lockes import LOCKE_INSTANCES, get_run_creator_class, GenLocke, list_all_lockes
from games import get_games_from_gen, get_game
from .exceptions import RunAlreadyExistsError, InvalidLockeTypeError, RunNotFoundError, InvalidGameError
from typing import TypedDict, Optional

# Constants for run creation keys
GAME_KEY = "GAME"
STARTER_KEY = "STARTER"

class RunUpdateResponse(TypedDict):
    next_key: str
    potential_values: list[str]
    finished: bool
    id: Optional[str]

def _handle_game_update(run: RunCreation, game_name: str) -> RunUpdateResponse:
    """Handle updating a run with a game.
    
    Args:
        run: The run to update
        game_name: The name of the game to set
            
    Returns:
        A RunUpdateResponse with the next key and potential values
            
    Raises:
        InvalidGameError: If the game name is invalid
    """
    try:
        # Validate game name
        game = get_game(game_name)
        # Update run with game
        run.game = game.name
        update_run_creation(run)
        
        return {
            "next_key": STARTER_KEY,
            "potential_values": [pokemon.name for pokemon in game.starters],
            "finished": False
        }
    except StopIteration:
        raise InvalidGameError(game_name)

def start_run_creation(run_name: str, locke_type: str, duplicate_clause: bool, is_randomized: bool) -> list[str]:
    """Create a new run with the specified parameters.
    
    Args:
        run_name: Name of the run
        locke_type: Type of locke challenge
        duplicate_clause: Whether duplicate Pokemon are allowed
        is_randomized: Whether the game is randomized
            
    Returns:
        List of available games that meet the locke's minimum generation requirement
            
    Raises:
        RunAlreadyExistsError: If a run with the same name already exists
        InvalidLockeTypeError: If the locke type is invalid
        Exception: For any other errors that occur during run creation
    """
    # Check if run already exists
    existing_run = fetch_run_creation(run_name)
    if existing_run is not None:
        raise RunAlreadyExistsError()
    
    # Validate locke type
    if locke_type not in LOCKE_INSTANCES:
        raise InvalidLockeTypeError(locke_type, list(LOCKE_INSTANCES.keys()))
    
    # Get the locke instance to check minimum generation
    locke = LOCKE_INSTANCES[locke_type]
    
    # Create and save the run creation
    run_creation = RunCreation(
        name=run_name,
        locke=locke_type,
        duplicate_clause=duplicate_clause,
        randomized=is_randomized,
        finished=False
    )
    
    update_run_creation(run_creation)

    if locke.name == GenLocke.name:
        return [locke for locke in list_all_lockes() if locke != GenLocke.name]
    
    # Get available games based on locke's minimum generation
    available_games = get_games_from_gen(locke.min_gen)
    return [game.name for game in available_games]

def continue_run_creation(run_name: str, key: Optional[str] = None, val: Optional[str] = None) -> RunUpdateResponse:
    """Continue the run creation process by updating a specific field.
    
    Args:
        run_name: Name of the run to update
        key: The key to update (optional)
        val: The value to set (optional)
            
    Returns:
        A dictionary containing:
            - next_key: The next key to update (if not finished)
            - potential_values: List of potential values for the next key (if not finished)
            - finished: Whether the run creation is complete
            - id: The ID of the created run (only when finished is True)
            
    Raises:
        RunNotFoundError: If the run doesn't exist
        InvalidGameError: If the game name is invalid
        Exception: For any other errors that occur during run update
    """
    # Check if run exists
    existing_run = fetch_run_creation(run_name)
    if existing_run is None:
        raise RunNotFoundError(run_name)
    
    # Get the appropriate run creator class and create an instance
    creator_class = get_run_creator_class(existing_run.locke)
    creator = creator_class(existing_run)
    
    # Update the run with the new value if both key and val are provided
    if key is not None and val is not None:
        creator.update_progress(key, val)
    
    # Get the current progress
    locke = LOCKE_INSTANCES[existing_run.locke]
    progress = creator.get_progress(locke.min_gen)
    locke.extra_info = existing_run.extra_info
    
    # Return appropriate response based on progress
    if progress.has_all_info:
        # Create the run and get its ID
        core_run = creator.finish_creation(locke)
        
        # Get the game instance to get its generation
        try:
            game = get_game(existing_run.game)
        except StopIteration:
            raise InvalidGameError(existing_run.game)
        
        # Convert core Run to database Run
        db_run = DBRun(
            run_id=core_run.id,
            created_date=core_run.creation_date,
            name=core_run.run_name,
            locke=existing_run.locke,
            game=existing_run.game,
            gen=game.gen,
            randomized=existing_run.randomized or False,
            party=[pokemon.metadata.id for pokemon in core_run.party.pokemons],
            box=[pokemon.metadata.id for pokemon in core_run.box.pokemons],
            battles=[],  # Empty array as battles are added during run progress
            encounters=[],  # Empty array as encounters are added during run progress
            locke_extra_info=existing_run.extra_info,
            restarts=core_run.restarts,
            duplicate_clause=existing_run.duplicate_clause or False,
            finished=core_run.finished,
            starter=str(core_run.starter.metadata.id) if core_run.starter else None
        )
        
        # Save the run to the database
        save_run(db_run)
        return {
            "finished": True,
            "id": db_run.run_id,
            "next_key": None,
            "potential_values": []
        }
    
    return {
        "next_key": progress.missing_key,
        "potential_values": progress.missing_key_options or [],
        "finished": False,
        "id": existing_run.name  # Include id even when not finished
    } 
