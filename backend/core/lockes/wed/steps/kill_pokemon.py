
from typing import Optional
from definitions import Pokemon
from definitions.runs.steps_interface import ExecutionReturnValue
from core.steps.kill_pokemon_step import KillPokemonStep as KillPokemonStepOg
from core.lockes.wed.utils import get_pokemon_partner
from core.run import Run


class KillPokemonStep(KillPokemonStepOg):
    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        pokemon_partner = get_pokemon_partner(run, pokemon)
        return_value = super().execute_step(run, pokemon, value)
        if pokemon_partner:
            pokemon.metadata.paired = None
            pokemon_partner.metadata.paired = None
            return_value.pokemons_to_update.extend([pokemon.metadata.id, pokemon_partner.metadata.id])
            return_value.pokemons_to_update = list(set(return_value.pokemons_to_update))
        return return_value
