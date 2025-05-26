"""Interface for implementing steps in a Pokemon game run manager.

This module defines the abstract interface that all step implementations must follow.
Steps represent discrete actions or decisions that can be taken during a Pokemon game run,
such as choosing a starter, battling a gym leader, or catching a Pokemon.

The interface ensures that all steps provide consistent methods for:
- Determining if they are relevant to the current game state
- Providing available options for the step
- Executing the step and returning affected Pokemon
"""

from abc import ABCMeta, abstractmethod
from typing import Tuple, List, Optional
from dataclasses import dataclass

from definitions import Pokemon
from definitions.runs.inputs_options import InputOptions
from core.run import Run


@dataclass
class ExecutionReturnValue:
    """Return value for step execution, indicating which Pokemon need to be updated.
    
    Attributes:
        pokemons_to_update: List of Pokemon names that need to be updated after step execution.
            These Pokemon may have changed stats, moves, or other attributes.
    """
    pokemons_to_update: List[str]


class StepInterface(metaclass=ABCMeta):
    """Abstract base class defining the interface for all step implementations.
    
    This interface ensures that all steps provide consistent methods for:
    - Determining if they are relevant to the current game state
    - Providing available options for the step
    - Executing the step and returning affected Pokemon
    
    All concrete step implementations must implement all abstract methods.
    """

    @abstractmethod
    def step_options(self, run: Run, pokemon: Pokemon) -> Tuple[InputOptions, List[str]]:
        """Get the available options for this step.
        
        Args:
            run: The current run instance containing game state.
            pokemon: The Pokemon this step is being considered for.
            
        Returns:
            A tuple containing:
            - InputOptions: The options configuration for this step. Can be one of:
                - FREE_TEXT: Allows any text input from the user
                - ONE_OF: User must select from the provided list of options
                - NOTHING: No input is required from the user
            - List[str]: The list of available options:
                - For FREE_TEXT or NOTHING: Returns an empty list []
                - For ONE_OF: Returns the list of valid options to choose from
        """
        pass

    @abstractmethod
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        """Determine if this step is relevant to the current game state.
        
        Args:
            run: The current run instance containing game state.
            pokemon: The Pokemon this step is being considered for.
            
        Returns:
            bool: True if this step is relevant and should be presented as an option,
                 False otherwise.
        """
        pass

    @abstractmethod
    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        """Execute this step with the chosen option.
        
        Args:
            run: The current run instance containing game state.
            pokemon: The Pokemon this step is being executed for.
            value: The chosen option for this step. May be None if no choice is needed.
            
        Returns:
            ExecutionReturnValue: Contains a list of Pokemon names that need to be
                                updated after this step's execution.
        """
        pass 