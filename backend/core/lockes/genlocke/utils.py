from pokemendel_core.utils.definitions.regions import Regions
from core.lockes.lockes_factory_no_gen import LOCKE_INSTANCES
from games import get_game, Game, get_games_from_gen
from typing import List
SELECTED_LOCKE = "_selected_locke"

_GEN_TO_REGION = {
    1: Regions.KANTO,
    2: Regions.JOHTO,
    3: Regions.HOENN,
}

REGION_TO_GEN = {region: gen for gen, region in _GEN_TO_REGION.items()}


def get_game_locke_gen(game_name: str):
    game = get_game(game_name)
    return REGION_TO_GEN[game.region]


def get_generation_potential_games(generation: int, inner_locke_name: str) -> List[Game]:
    locke = LOCKE_INSTANCES[inner_locke_name]
    return [
        game for game in get_games_from_gen(locke.min_gen)
        if game.region == _GEN_TO_REGION[generation]
    ]
