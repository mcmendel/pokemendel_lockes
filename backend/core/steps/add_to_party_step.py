"""Step implementation for adding a Pokemon to the player's party.

This step allows adding a Pokemon to the player's party if there is space available
and the Pokemon is not already in the party.
"""

from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from core.run import Run


class AddToPartyStep(StepInterface):
    """Step for adding a Pokemon to the player's party.
    
    This step is relevant when:
    - The party is not full
    - The Pokemon is not already in the party
    
    The step requires no user input as it simply adds the Pokemon to the party.
    """

    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        """Check if the Pokemon can be added to the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to check
            
        Returns:
            bool: True if the Pokemon can be added to the party, False otherwise
        """
        return not run.party.is_party_full() and not run.party.is_pokemon_in_party(pokemon)

    def step_options(self, run: Run, pokemon: Pokemon, is_randomized: bool) -> Tuple[InputOptions, List[str]]:
        """Get the options for adding a Pokemon to the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to add
            
        Returns:
            Tuple[InputOptions, List[str]]: A tuple containing:
                - InputOptions.NOTHING: No user input is required
                - Empty list: No options to choose from
        """
        return InputOptions.NOTHING, []

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        """Add the Pokemon to the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to add
            value: Should be None as no input is required
            
        Returns:
            ExecutionReturnValue: Empty list as no Pokemon need to be updated
            
        Raises:
            AssertionError: If value is not None
        """
        assert not value, "Value is not expected when adding pokemon to party"
        run.party.add_pokemon(pokemon)
        return ExecutionReturnValue(pokemons_to_update=[])
