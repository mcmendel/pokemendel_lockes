"""Step implementation for choosing pokemon nature

This step allows setting pokemon's nature if not already set
"""

from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from pokemendel_core.utils.definitions.natures import Natures
from core.run import Run


class ChooseNatureStep(StepInterface):
    """Step for setting pokemon nature.

    This step is relevant when:
    - The pokemon wasn't set with a nature

    The step requires text as pokemon's nature (From Natures enum).
    """

    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        """Check if the Pokemon already set a nature.

        Args:
            run: The current run instance
            pokemon: The Pokemon to check

        Returns:
            bool: True if the Pokemon already has a nature, False otherwise
        """
        return not pokemon.nature and run.gen >= 3

    def step_options(self, run: Run, pokemon: Pokemon) -> Tuple[InputOptions, List[str]]:
        """Get the options for pokemon's nature

        Args:
            run: The current run instance
            pokemon: The Pokemon to be set with nature

        Returns:
            Tuple[InputOptions, List[str]]: A tuple containing:
                - InputOptions.ONE_OF: Select an option from optional list
                - Natures list all: all natures are optional
        """
        return InputOptions.ONE_OF, Natures.list_all()

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        """Set pokemon nature.

        Args:
            run: The current run instance
            pokemon: The Pokemon to set nature to
            value: Should be an option from Natures EnumList

        Returns:
            ExecutionReturnValue: The pokemon with the new nature
        """
        pokemon.nature = value
        return ExecutionReturnValue(pokemons_to_update=[pokemon.metadata.id])
