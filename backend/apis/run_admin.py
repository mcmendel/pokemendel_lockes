from models.run import fetch_run, update_run as update_run_db, _COLLECTIONS_SAVE_NAME
from models.pokemon import backup_pokemons, restore_pokemons
from core.run import convert_db_run_to_core_run
from dataclasses import asdict
from games import get_game
from typing import Dict
from apis.exceptions import InvalidGameError


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
    return asdict(convert_db_run_to_core_run(db_run, run_id))


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
    return asdict(convert_db_run_to_core_run(db_run_to_load, run_id))


def finish_run(run_id: str) -> Dict:
    print("Run %s had finished" % run_id)
    db_run = fetch_run(run_id)
    assert not db_run.finished, "Run %s is already finished" % run_id
    try:
        game = get_game(db_run.game)
    except Exception:
        raise InvalidGameError(db_run.game)
    expected_num_battles = len(game.gyms) + len(game.elite4)
    assert len(db_run.battles) == expected_num_battles, (
            "Run %s did not finish all battles. "
            "It has total %s battles, but only %s was battles" % (run_id, expected_num_battles, len(db_run.battles))
    )
    db_run.finished = True
    update_run_db(db_run)
    save_run(run_id)
    return asdict(convert_db_run_to_core_run(db_run, run_id))

