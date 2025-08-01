"""Step implementation for choosing pokemon gender

This step allows setting pokemon's gender if not already set
"""

from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from core.run import Run


class ChooseGenderStep(StepInterface):
    """Step for setting pokemon gender.

    This step is relevant when:
    - The pokemon wasn't set with a gender

    The step requires text as pokemon's gender (Male/Female/Genderless).
    """

    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        """Check if the Pokemon already set a gender.

        Args:
            run: The current run instance
            pokemon: The Pokemon to check

        Returns:
            bool: True if the Pokemon already has a gender, False otherwise
        """
        return not pokemon.metadata.gender

    def step_options(self, run: Run, pokemon: Pokemon, is_randomized: bool) -> Tuple[InputOptions, List[str]]:
        """Get the options for pokemon's gender

        Args:
            run: The current run instance
            pokemon: The Pokemon to be set with gender

        Returns:
            Tuple[InputOptions, List[str]]: A tuple containing:
                - InputOptions.ONE_OF: Depends on pokemon potential genders
                - Empty list: combinations of Male/FEMALE/GENDERLESS
        """
        return InputOptions.ONE_OF, pokemon.supported_genders

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        """Set pokemon gender.

        Args:
            run: The current run instance
            pokemon: The Pokemon to set gender to
            value: Should be one of Male/Female/Genderless and that the pokemon supports that gender

        Returns:
            ExecutionReturnValue: The pokemon with the new gender

        Raises:
            AssertionError: If value not in supported genders
        """
        assert value in pokemon.supported_genders, f"Gender {value} is not supported for pokemon {pokemon.name}"
        pokemon.metadata.gender = value
        return ExecutionReturnValue(pokemons_to_update=[pokemon.metadata.id])
