from models.run import fetch_run, update_run as update_run_db, _COLLECTIONS_SAVE_NAME, Run
from models.pokemon import backup_pokemons, restore_pokemons, fetch_pokemon
from models.run_pokemons_options import unmark_caught_pokemon
from responses.run import RunResponse
from core.run import convert_db_run_to_core_run
from core.lockes import LOCKE_INSTANCES
from games import get_game
from apis.exceptions import InvalidGameError


def get_run_api(run_id: str) -> RunResponse:
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
    core_run = convert_db_run_to_core_run(db_run, run_id)
    game = get_game(db_run.game)
    locke = LOCKE_INSTANCES[db_run.locke]
    locke.extra_info = db_run.locke_extra_info
    response_run = RunResponse.from_core_run(core_run, game, locke)
    return response_run


def save_run(run_id) -> None:
    print("Saving run %s" % run_id)
    db_run = fetch_run(run_id)
    update_run_db(db_run, _COLLECTIONS_SAVE_NAME)
    backup_pokemons(run_id)


def load_run(run_id) -> RunResponse:
    print("Loading run %s" % run_id)
    db_run_to_load = fetch_run(run_id, _COLLECTIONS_SAVE_NAME)
    pre_load_run = fetch_run(run_id)
    _restore_pokemon_options(pre_load_run=pre_load_run, post_load_run=db_run_to_load)
    restore_pokemons(run_id)
    db_run_to_load.restarts += 1
    update_run_db(db_run_to_load)
    update_run_db(db_run_to_load, _COLLECTIONS_SAVE_NAME)
    core_run = convert_db_run_to_core_run(db_run_to_load, run_id)
    game = get_game(db_run_to_load.game)
    locke = LOCKE_INSTANCES[db_run_to_load.locke]
    locke.extra_info = db_run_to_load.locke_extra_info
    response_run = RunResponse.from_core_run(core_run, game, locke)
    return response_run


def _restore_pokemon_options(pre_load_run: Run, post_load_run: Run):
    newly_caught_pokemons = set(pre_load_run.box) - set(post_load_run.box)
    for pokemon_id in newly_caught_pokemons:
        pokemon = fetch_pokemon(pokemon_id)
        unmark_caught_pokemon(pre_load_run.run_id, pokemon.name)


def finish_run(run_id: str) -> RunResponse:
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
    core_run = convert_db_run_to_core_run(db_run, run_id)
    game = get_game(db_run.game)
    locke = LOCKE_INSTANCES[db_run.locke]
    locke.extra_info = db_run.locke_extra_info
    response_run = RunResponse.from_core_run(core_run, game, locke)
    return response_run

