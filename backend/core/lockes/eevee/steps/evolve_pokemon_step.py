from definitions import Pokemon
from core.run import Run
from core.steps.evolve_pokemon_step import EvolvePokemonStep as EvolvePokemonStepOg


class EvolvePokemonStep(EvolvePokemonStepOg):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        return False
