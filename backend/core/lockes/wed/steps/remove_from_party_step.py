from definitions import Pokemon
from definitions.runs.steps_interface import ExecutionReturnValue, StepInterface
from definitions.runs.inputs_options import InputOptions
from pokemendel_core.utils.definitions.genders import Genders
from core.run import Run
from typing import Tuple, List, Optional
from core.steps.remove_from_party_step import RemoveFromPartyStep as RemoveFromPartyStepOg
from core.lockes.wed.utils import get_party_pairs


class RemoveFromPartyStep(RemoveFromPartyStepOg):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        if not super().is_step_relevant(run, pokemon):
            return False
        pair1, pair2, pair3 = get_party_pairs(run)
        if pair1.is_pokemon_in_pair(pokemon):
            return bool(pair2 or pair3)
        if pair2 and pair2.is_pokemon_in_pair(pokemon):
            return bool(pair1 or pair3)
        assert pair3 and pair3.is_pokemon_in_pair(pokemon)
        return bool(pair1 or pair2)

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        return_value = super().execute_step(run, pokemon, value)
        if pokemon.metadata.paired:
            partner = run.box.get_pokemon_by_id(pokemon.metadata.paired)
            partner_return_value = super().execute_step(run, partner)
            return_value.pokemons_to_update.extend(partner_return_value.pokemons_to_update)
        return return_value
