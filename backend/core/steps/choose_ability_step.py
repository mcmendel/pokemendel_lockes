"""Step implementation for choosing pokemon ability

This step allows setting pokemon's bility if not already set
"""

from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from pokemendel_core.utils.definitions.abilities import Abilities
from core.run import Run


class ChooseAbilityStep(StepInterface):
    """Step for setting pokemon nature.

    This step is relevant when:
    - The pokemon wasn't set with a nature

    The step requires text as pokemon's nature (From Natures enum).
    """

    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        """Check if the Pokemon already set an ability.

        Args:
            run: The current run instance
            pokemon: The Pokemon to check

        Returns:
            bool: True if the Pokemon already has a nature, False otherwise
        """
        return not pokemon.metadata.ability and run.gen >= 3

    def step_options(self, run: Run, pokemon: Pokemon, is_randomized: bool) -> Tuple[InputOptions, List[str]]:
        """Get the options for pokemon's ability

        Args:
            run: The current run instance
            pokemon: The Pokemon to be set with ability

        Returns:
            Tuple[InputOptions, List[str]]: A tuple containing:
                - InputOptions.ONE_OF: Select an option from optional list
                - Natures list all: all natures are optional
        """
        abilities_options = (
            Abilities.list_all()
            if is_randomized
            else
            pokemon.supported_abilities
        )
        return InputOptions.ONE_OF, abilities_options

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        """Set pokemon ability.

        Args:
            run: The current run instance
            pokemon: The Pokemon to set ability to
            value: Should be an option from Abilities EnumList

        Returns:
            ExecutionReturnValue: The pokemon with the new ability
        """
        pokemon.metadata.ability = value
        return ExecutionReturnValue(pokemons_to_update=[pokemon.metadata.id])
