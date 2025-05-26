"""Step implementation for removing a Pokemon from the player's party.

This step allows removing a Pokemon from the player's party if:
- The Pokemon is currently in the party
- It's not the last Pokemon in the party (to prevent having an empty party)
"""

from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from core.run import Run


class RemoveFromPartyStep(StepInterface):
    """Step for removing a Pokemon from the player's party.
    
    This step is relevant when:
    - The Pokemon is currently in the party
    - It's not the last Pokemon in the party (to prevent having an empty party)
    
    The step requires no user input as it simply removes the Pokemon from the party.
    """

    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        """Check if the Pokemon can be removed from the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to check
            
        Returns:
            bool: True if the Pokemon can be removed from the party, False otherwise
        """
        return not run.party.is_last_pokemon_in_party() and run.party.is_pokemon_in_party(pokemon)

    def step_options(self, run: Run, pokemon: Pokemon) -> Tuple[InputOptions, List[str]]:
        """Get the options for removing a Pokemon from the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to remove
            
        Returns:
            Tuple[InputOptions, List[str]]: A tuple containing:
                - InputOptions.NOTHING: No user input is required
                - Empty list: No options to choose from
        """
        return InputOptions.NOTHING, []

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        """Remove the Pokemon from the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to remove
            value: Should be None as no input is required
            
        Returns:
            ExecutionReturnValue: Empty list as no Pokemon need to be updated
            
        Raises:
            AssertionError: If value is not None
        """
        assert not value, "Value is not expected when removing pokemon from party"
        run.party.remove_pokemon(pokemon)
        return ExecutionReturnValue(pokemons_to_update=[])