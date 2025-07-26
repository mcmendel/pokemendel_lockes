"""Abstract base class for implementing different types of Locke challenges.
Cannot be instantiated directly. Subclasses must implement _mandatory_steps.

A Locke challenge defines:
- A set of rules that must be followed
- A sequence of steps that must be completed
- The minimum generation of Pokemon games it supports
- Additional information specific to the Locke challenge (extra_info), such as:
  - 'type' for Monolocke
  - 'color' for Colorlocke
  - etc.

Subclasses must implement:
- _mandatory_steps: A list of steps that must be completed in order
- Any additional rules or constraints specific to the Locke type
"""

from abc import ABC, abstractmethod
from definitions.runs.steps_info import StepInfo
from definitions.runs.steps_names import StepsNames
from definitions.runs.steps_interface import StepInterface
from pokemendel_core.utils.class_property import classproperty
from pokemendel_core.models.pokemon import Pokemon
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from core.run import Run

@dataclass
class Locke(ABC):
    """Abstract base class for implementing different types of Locke challenges.
    Cannot be instantiated directly. Subclasses must implement _mandatory_steps.
    """
    extra_info: Optional[Dict[str, Any]] = None

    @classproperty
    @abstractmethod
    def name(cls) -> str:
        """Get the name of the Locke challenge.
        Returns:
            str: The name of the Locke challenge, derived from the class name
        """
        pass

    @classproperty
    @abstractmethod
    def min_gen(cls) -> int:
        """Get the minimum generation of Pokemon games supported by this Locke.
        Returns:
            int: The minimum generation number (1-9)
        """
        pass

    @abstractmethod
    def rules(self) -> List[str]:
        """Get the list of rules for this Locke challenge.
        Returns:
            List[str]: A list of rules that must be followed
        """
        pass

    @abstractmethod
    def steps(self, gen: int) -> List[StepInfo]:
        """Get all steps for this Locke challenge, including mandatory and optional steps.
        Args:
            gen: generation of the run where the locke is running
        Returns:
            List[StepInfo]: A list of all steps with their prerequisites
        """
        pass

    @abstractmethod
    def _mandatory_steps(self, gen: int) -> List[StepInfo]:
        """Abstract property. Must be implemented by subclasses."""
        pass

    @classproperty
    @abstractmethod
    def steps_mapper(cls) -> Dict[StepsNames, StepInterface]:
        """Get a mapping of step names to their implementations.
        Returns:
            Dict[StepsNames, StepInterface]: A dictionary mapping step names to their implementations
        """
        pass

    def is_pokemon_relevant(self, pokemon: Pokemon) -> bool:
        return True

    @abstractmethod
    def catch_pokemon(self, pokemon: Pokemon, run: Run):
        pass

    @property
    def auto_add_to_party(self) -> bool:
        return True
