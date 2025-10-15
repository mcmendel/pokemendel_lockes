
from typing import Optional
from definitions import Pokemon
from definitions.runs.steps_interface import ExecutionReturnValue
from core.run import Run
from core.steps.add_to_party_step import AddToPartyStep as AddToPartyStepOg
from core.lockes.wed.utils import get_party_pairs, get_pokemon_partner


class AddToPartyStep(AddToPartyStepOg):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        all_pairs = get_party_pairs(run, check_emptiness=False)
        return super().is_step_relevant(run, pokemon) and any(pair is None for pair in all_pairs)

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        pokemon_partner = get_pokemon_partner(run, pokemon)
        return_value = super().execute_step(run, pokemon, value)
        if pokemon_partner:
            return_value_partner = super().execute_step(run, pokemon_partner, value)
            return_value.pokemons_to_update.extend(return_value_partner.pokemons_to_update)
        return return_value
