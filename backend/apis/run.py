from typing import List, Dict, Optional, Union, Tuple
from models.run import fetch_run
from models.run_pokemons_options import list_runs_options, list_runs_options_by_query
from games import get_game
from core.lockes import LOCKE_INSTANCES
from core.lockes.genlocke.utils import get_generation_potential_games, REGION_TO_GEN, SELECTED_LOCKE
from core.run import convert_db_run_to_core_run
from core.run_manager import RunManager
from apis.run_admin import finish_run as finish_run_admin, RunResponse
from responses.exceptions import ContinueCreationException
import random


def _get_run_manager(run_id: str) -> RunManager:
    db_run = fetch_run(run_id)
    run = convert_db_run_to_core_run(db_run, run_id)
    game = get_game(db_run.game)
    locke = LOCKE_INSTANCES[db_run.locke]
    locke.extra_info = db_run.locke_extra_info
    run_manager = RunManager(
        run=run,
        locke=locke,
        game=game,
        duplicate_clause=db_run.duplicate_clause,
        randomized=db_run.randomized,
    )
    return run_manager


def get_starter_options(run_id: str) -> List[str]:
    run_manager = _get_run_manager(run_id)
    starter_options = run_manager.get_starter_options()
    num_items = min([len(starter_options), 3])
    preferred_starter_options = random.sample(list(starter_options), num_items)
    return preferred_starter_options


def choose_starter(run_id: str, pokemon_name: str) -> Dict:
    run_manager = _get_run_manager(run_id)
    return run_manager.choose_starter(pokemon_name)


def get_run_potential_pokemons(run_id: str) -> List[str]:
    return [pokemon_option.pokemon_name for pokemon_option in list_runs_options(run_id)]


def get_run_potential_encounters(run_id: str, route: Optional[str]) -> List[str]:
    run_manager = _get_run_manager(run_id)
    run_options = (
        list_runs_options_by_query(run_id, {'caught': False})
        if run_manager.duplicate_clause
        else
        list_runs_options(run_id)
    )
    relevant_encounters = [pokemon_option.pokemon_name for pokemon_option in run_options]
    route_encounters = set(relevant_encounters) if run_manager.randomized else run_manager.game.potential_encounters(route)
    return [encounter_pokemon for encounter_pokemon in relevant_encounters if encounter_pokemon in route_encounters]


def encounter_pokemon(run_id: str, route: str, pokemon_name: str):
    run_manager = _get_run_manager(run_id)
    run_manager.encounter_pokemon(route, pokemon_name)


def update_encounter(run_id: str, route: str, encounter_status: str):
    run_manager = _get_run_manager(run_id)
    run_manager.update_encounter(route, encounter_status)


def get_next_actions(run_id: str, pokemon_id: str) -> List[str]:
    run_manager = _get_run_manager(run_id)
    return run_manager.get_pokemon_next_actions(pokemon_id)


def get_action_options(run_id: str, pokemon_id: str, action: str) -> Dict[str, Union[str, List[str]]]:
    run_manager = _get_run_manager(run_id)
    input_type, input_options = run_manager.get_action_options(pokemon_id, action)
    return {
        'input_type': input_type,
        'input_options': input_options,
    }


def execute_action(run_id: str, pokemon_id: str, action: str, value: str):
    run_manager = _get_run_manager(run_id)
    run_manager.execute_action(pokemon_id, action, value)


def win_battle(run_id: str, leader: str):
    run_manager = _get_run_manager(run_id)
    run_manager.win_battle(leader)


def finish_run(run_id: str) -> RunResponse:
    run_manager = _get_run_manager(run_id)
    if run_manager.locke.finish_locke(run_manager.game.name):
        return finish_run_admin(run_id)

    raise ContinueCreationException()


def jump_to_next_gen(run_id: str, game_name: Optional[str]) -> Tuple[bool, List[str]]:
    run_manager = _get_run_manager(run_id)
    if not game_name:
        current_gen = REGION_TO_GEN[run_manager.game.region]
        next_gen = current_gen + 1
        print("Move run", run_id, "to gen", next_gen)
        gen_inner_locke = run_manager.locke.extra_info[SELECTED_LOCKE]
        return False, [
            game.name for game in get_generation_potential_games(next_gen, gen_inner_locke)
        ]
    return False, [game_name]
