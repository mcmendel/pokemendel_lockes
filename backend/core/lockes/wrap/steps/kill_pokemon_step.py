from typing import Optional
from definitions import Pokemon
from definitions.runs.steps_interface import ExecutionReturnValue
from core.steps.kill_pokemon_step import KillPokemonStep as KillPokemonStepOg
from core.lockes.wrap.utils import refresh_pokemons_in_party
from core.run import Run


class KillPokemonStep(KillPokemonStepOg):
    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        return_value = super().execute_step(run, pokemon, value)
        refresh_pokemons_in_party(run)
        return return_value
