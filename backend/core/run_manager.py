from dataclasses import dataclass
from core.locke import Locke
from core.run import Run
from games import Game

@dataclass
class RunManager:
    run: Run
    locke: Locke
    game: Game