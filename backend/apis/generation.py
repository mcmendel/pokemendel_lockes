from typing import List, Optional, Tuple
from models.run import fetch_run, update_run
from models.run_pokemons_options import mark_caught_pokemon, list_runs_options_by_query, delete_run_pokemons
from models.report import save_report, Report
from games import get_game, Game
from core.lockes import LOCKE_INSTANCES, BaseLocke
from core.lockes.genlocke.utils import get_generation_potential_games, REGION_TO_GEN, SELECTED_LOCKE
from core.lockes.genlocke.run_creator import GenRunCreator
from core.lockes.genlocke.gen_locke import GenLocke
from core.run import convert_db_run_to_core_run, Run
from models.run_creation import fetch_run_creation


def jump_to_next_gen(run_id: str, game_name: Optional[str]) -> Tuple[bool, List[str]]:
    db_run = fetch_run(run_id)
    locke = LOCKE_INSTANCES[db_run.locke]
    locke.extra_info = db_run.locke_extra_info
    core_run = convert_db_run_to_core_run(db_run, run_id)
    return (
        _jump_to_next_gen(core_run, get_game(db_run.game), get_game(game_name))
        if game_name
        else _get_next_gen_game_options(run_id, get_game(db_run.game), locke)
    )


def _get_next_gen_game_options(run_id: str, game: Game, locke: BaseLocke) -> Tuple[bool, List[str]]:
    current_gen = REGION_TO_GEN[game.region]
    next_gen = current_gen + 1
    print("Get games to move run", run_id, "to gen", next_gen)
    gen_inner_locke = locke.extra_info[SELECTED_LOCKE]
    return False, [
        game.name for game in get_generation_potential_games(next_gen, gen_inner_locke)
    ]


def _jump_to_next_gen(run: Run, origin_game: Game, new_game: Game) -> Tuple[bool, List[str]]:
    run_id = run.id
    game_gen = REGION_TO_GEN[new_game.region]
    print("Move run", run_id, "to game", new_game.name, "in gen", game_gen)
    current_db_run = fetch_run(run_id)
    base_caught_pokemons = {pokemon_option.base_pokemon for pokemon_option in list_runs_options_by_query(run_id, query={'caught': True})}
    delete_run_pokemons(run_id)
    _generate_report(run, origin_game)
    original_run_creator = fetch_run_creation(run.run_name)
    gen_creator = GenRunCreator(run_creation=original_run_creator)
    created_run = gen_creator.finish_creation_existing_run(run_id, new_game.name)
    update_run(created_run.to_db_run(
        gen=new_game.gen,
        locke_name=GenLocke.name,
        game_name=new_game.name,
        is_randomize=current_db_run.randomized,
        duplicate_clause=current_db_run.duplicate_clause,
        extra_info=current_db_run.locke_extra_info,
    ))
    _remark_caught_pokemons(run_id, list(base_caught_pokemons))
    return False, [new_game.name]


def _generate_report(run: Run, game: Game):
    report = Report(
        run_id=run.id,
        game_name=game.name,
        party=run.party.pokemons,
        caught=run.box.pokemons,
        died=run.box.get_dead_pokemons(),
    )
    save_report(report, create=True)


def _remark_caught_pokemons(run_id: str, base_pokemons: List[str]):
    for pokemon_name in base_pokemons:
        mark_caught_pokemon(run_id, pokemon_name)
