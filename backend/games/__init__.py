from .gen1 import Game, BLUE, RED, YELLOW
from .gen2 import GOLD, SILVER, CRYSTAL
from .gen3 import RUBY, SAPPHIRE, EMERALD
from typing import List
GAMES = [
    BLUE, RED, YELLOW,
    GOLD, SILVER, CRYSTAL,
    RUBY, SAPPHIRE, EMERALD,
]


def get_game(game_name: str) -> Game:
    relevant_game = next(game for game in GAMES if game.name == game_name)
    return relevant_game


def get_games_from_gen(gen: int) -> List[Game]:
    return [
        game for game in GAMES if game.gen >= gen
    ]
