
from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from core.run import Run
from core.steps.add_to_party_step import AddToPartyStep as AddToPartyStepOg
from core.lockes.unique.utils import can_pokemon_be_in_party


class AddToPartyStep(AddToPartyStepOg):

    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        """Check if the Pokemon can be added to the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to check
            
        Returns:
            bool: True if the Pokemon can be added to the party, False otherwise
        """
        return super().is_step_relevant(run, pokemon) and can_pokemon_be_in_party(pokemon, run)
