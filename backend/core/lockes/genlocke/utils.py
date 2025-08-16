from pokemendel_core.utils.definitions.regions import Regions
from games import get_game
SELECTED_LOCKE = "_selected_locke"

_GEN_TO_REGION = {
    1: Regions.KANTO,
    2: Regions.JOHTO,
    3: Regions.HOENN,
}

_REGION_TO_GEN = {region: gen for gen, region in _GEN_TO_REGION.items()}


def get_game_locke_gen(game_name: str):
    game = get_game(game_name)
    return _REGION_TO_GEN[game.region]
