from dataclasses import dataclass
from typing import Any
"""
Dataclass for representing Pokemon stats.
"""

@dataclass
class Stats:
    """
    Represents the base stats of a Pokemon.

    All stats must be integers. Attempting to set non-integer values will raise TypeError.

    Attributes:
        attack (int): Base attack stat
        defence (int): Base defence stat
        special_attack (int): Base special attack stat
        special_defence (int): Base special defence stat
    """
    attack: int
    defence: int
    special_attack: int
    special_defence: int

    def __post_init__(self):
        """Validate that all stats are integers."""
        self._validate_int("attack", self.attack)
        self._validate_int("defence", self.defence)
        self._validate_int("special_attack", self.special_attack)
        self._validate_int("special_defence", self.special_defence)

    def __setattr__(self, name: str, value: Any) -> None:
        """Override setattr to enforce integer type validation on modifications."""
        if name in ["attack", "defence", "special_attack", "special_defence"]:
            self._validate_int(name, value)
        super().__setattr__(name, value)

    @staticmethod
    def _validate_int(name: str, value: Any) -> None:
        """
        Validate that a value is an integer.

        Args:
            name: Name of the stat being validated
            value: Value to validate

        Raises:
            TypeError: If the value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer, got {type(value).__name__}")