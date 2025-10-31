
from definitions import Pokemon
from core.steps.evolve_pokemon_step import EvolvePokemonStep as EvolvePokemonStepOg
from core.lockes.chess.utils import ChessRoles
from core.run import Run


class EvolvePokemonStep(EvolvePokemonStepOg):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        return (
            super().is_step_relevant(run, pokemon) and
            not pokemon.metadata.chesslocke_role == ChessRoles.PAWN
        )
