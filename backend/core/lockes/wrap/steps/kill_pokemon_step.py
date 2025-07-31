
from typing import Optional
from definitions import Pokemon
from definitions.runs.steps_interface import ExecutionReturnValue
from core.steps.kill_pokemon_step import KillPokemonStep as KillPokemonStepOg
from core.lockes.chess.utils import ChessRoles
from responses.exceptions import BlackoutException
from core.run import Run


class KillPokemonStep(KillPokemonStepOg):
    pass
