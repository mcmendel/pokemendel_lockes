"""Service for creating new runs."""

from models.run_creation import RunCreation, fetch_run_creation, update_run_creation
from core.lockes import LOCKE_INSTANCES
from games import get_games_from_gen
from .exceptions import RunAlreadyExistsError, InvalidLockeTypeError


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
        finished=True
    )
    
    update_run_creation(run_creation)
    
    # Get available games based on locke's minimum generation
    available_games = get_games_from_gen(locke.min_gen)
    return [game.name for game in available_games] 