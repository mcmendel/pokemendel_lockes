from models.run import fetch_run, update_run as update_run_db, _COLLECTIONS_SAVE_NAME, Run as DbRun
from models.pokemon import list_pokemon_by_run, backup_pokemons, restore_pokemons
from core.run import Run as CoreRun
from core.party import Party
from core.box import Box
from definitions.runs.battles import Battle
from definitions.runs.encounters import Encounter, EncounterStatus
from dataclasses import asdict
from games import get_game
from typing import Set, Dict
from apis.exceptions import RunNotFoundError, InvalidGameError

def _get_run_encounters(db_run, all_pokemons, game):
    """Helper function to build the encounters list for a run.
    
    Args:
        db_run: The database run object
        all_pokemons: Dictionary mapping pokemon IDs to Pokemon objects
        game: The game instance containing routes and encounters
        
    Returns:
        List of Encounter objects, one for each route in the game.
        Each encounter has a status (UNMET, MET, KILLED, RAN, or CAUGHT) and
        optionally a pokemon if one was caught.
    """
    # Create a dictionary of existing encounters for quick lookup
    existing_encounters = {
        e['route']: (e['status'], e.get('pokemon'))
        for e in db_run.encounters
    }
    
    # Create encounters for all routes in the game
    encounters = []
    for route in game.routes:
        if route in existing_encounters:
            # Route has been encountered
            status, pokemon_id = existing_encounters[route]
            pokemon = all_pokemons.get(pokemon_id) if pokemon_id else None
            encounters.append(Encounter(route=route, status=status, pokemon=pokemon))
        else:
            # Route hasn't been encountered yet
            encounters.append(Encounter(route=route, status=EncounterStatus.UNMET, pokemon=None))
    
    return encounters

def get_run_api(run_id):
    """Get a run by its ID.
    
    Args:
        run_id: The ID of the run to fetch
        
    Returns:
        The run data as a dictionary
        
    Raises:
        RunNotFoundError: If the run is not found
        InvalidGameError: If the game (for the run) does not exist
    """
    db_run = fetch_run(run_id)

    # Fetch all pokemons for this run
    return asdict(_convert_db_run_to_core_run(db_run, run_id))


def _convert_db_run_to_core_run(db_run: DbRun, run_id: str) -> CoreRun:

    if not db_run:
        raise RunNotFoundError(run_id)
    try:
        game = get_game(db_run.game)
    except Exception:
        raise InvalidGameError(db_run.game)

    all_pokemons = {p.metadata.id: p for p in list_pokemon_by_run(run_id)}
    # Build party and box
    party_pokemons = [all_pokemons[pid] for pid in db_run.party if pid in all_pokemons]
    box_pokemons = [all_pokemons[pid] for pid in db_run.box if pid in all_pokemons]
    party = Party(pokemons=party_pokemons)
    box = Box(pokemons=box_pokemons)
    # Battles and encounters
    battles = [Battle(**b) for b in db_run.battles]
    encounters = _get_run_encounters(db_run, all_pokemons, game)
    # Starter
    starter = all_pokemons.get(db_run.starter) if db_run.starter else None
    # Build core Run
    core_run = CoreRun(
        id=db_run.run_id,
        run_name=db_run.name,
        creation_date=db_run.created_date,
        party=party,
        box=box,
        battles=battles,
        encounters=encounters,
        starter=starter,
        restarts=db_run.restarts,
        finished=db_run.finished
    )
    return core_run


def save_run(run_id) -> None:
    print("Saving run %s" % run_id)
    db_run = fetch_run(run_id)
    update_run_db(db_run, _COLLECTIONS_SAVE_NAME)
    backup_pokemons(run_id)


def load_run(run_id) -> Dict:
    print("Loading run %s" % run_id)
    db_run_to_load = fetch_run(run_id, _COLLECTIONS_SAVE_NAME)
    restore_pokemons(run_id)
    db_run_to_load.restarts += 1
    update_run_db(db_run_to_load)
    update_run_db(db_run_to_load, _COLLECTIONS_SAVE_NAME)
    return asdict(_convert_db_run_to_core_run(db_run_to_load, run_id))

