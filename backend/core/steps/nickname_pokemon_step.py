"""Step implementation for nicknaming pokemon

This step allows nicknaming pokemon if nickname was not already given
"""

from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from core.run import Run


class NicknamePokemonStep(StepInterface):
    """Step for nicknaming pokemon.
    
    This step is relevant when:
    - The pokemon doesn't have already a nickname

    The step requires text as pokemon's nickname.
    """

    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        """Check if the Pokemon already has a nickname.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to check
            
        Returns:
            bool: True if the Pokemon can be nicknamed, False otherwise
        """
        return not pokemon.metadata.nickname

    def step_options(self, run: Run, pokemon: Pokemon, is_randomized: bool) -> Tuple[InputOptions, List[str]]:
        """Get the options for nicknaming a pokemon.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to be nicknamed
            
        Returns:
            Tuple[InputOptions, List[str]]: A tuple containing:
                - InputOptions.FREE_TEXT: Free text from user
                - Empty list: No options to choose from
        """
        return InputOptions.FREE_TEXT, []

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        """Nickname pokemon.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to nickname
            value: Should be non empty string
            
        Returns:
            ExecutionReturnValue: The pokemon with the new nickname
            
        Raises:
            AssertionError: If value is empty
        """
        assert value, "Nickname is expected to be not empty"
        pokemon.metadata.nickname = value
        return ExecutionReturnValue(pokemons_to_update=[pokemon.metadata.id])
