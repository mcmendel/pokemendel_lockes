from typing import List, Dict, Optional, Union, Tuple, Set
from models.run import fetch_run
from models.run_pokemons_options import list_runs_options, list_runs_options_by_query, delete_run_pokemons
from models.report import save_report, Report
from games import get_game, Game
from core.lockes import LOCKE_INSTANCES, BaseLocke
from core.lockes.genlocke.utils import get_generation_potential_games, REGION_TO_GEN, SELECTED_LOCKE
from core.run import convert_db_run_to_core_run, Run
from models.pokemon import Pokemon
from core.run_manager import RunManager
from apis.run_admin import finish_run as finish_run_admin, RunResponse
from responses.exceptions import ContinueCreationException
import random


def jump_to_next_gen(run_id: str, game_name: Optional[str]) -> Tuple[bool, List[str]]:
    db_run = fetch_run(run_id)
    game = get_game(db_run.game)
    locke = LOCKE_INSTANCES[db_run.locke]
    locke.extra_info = db_run.locke_extra_info
    core_run = convert_db_run_to_core_run(db_run, run_id)
    return (
        _jump_to_next_gen(core_run, game)
        if game_name
        else _get_next_gen_game_options(run_id, game, locke)
    )


def _get_next_gen_game_options(run_id: str, game: Game, locke: BaseLocke) -> Tuple[bool, List[str]]:
    current_gen = REGION_TO_GEN[game.region]
    next_gen = current_gen + 1
    print("Get games to move run", run_id, "to gen", next_gen)
    gen_inner_locke = locke.extra_info[SELECTED_LOCKE]
    return False, [
        game.name for game in get_generation_potential_games(next_gen, gen_inner_locke)
    ]


def _jump_to_next_gen(run: Run, game: Game) -> Tuple[bool, List[str]]:
    run_id = run.id
    game_gen = REGION_TO_GEN[game.region]
    print("Move run", run_id, "to game", game.name, "in gen", game_gen)
    delete_run_pokemons(run_id)
    _generate_report(run, game)
    return False, [game.name]


def _generate_report(run: Run, game: Game):
    report = Report(
        run_id=run.id,
        game_name=game.name,
        party=run.party.pokemons,
        caught=run.box.pokemons,
        died=run.box.get_dead_pokemons(),
    )
    save_report(report, create=True)
