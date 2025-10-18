"""
Module containing evolution type definitions and related functionality.
"""

from enum import Enum


class InvalidEvolutionTypeError(ValueError):
    """Raised when an invalid evolution type string is provided."""
    pass


class EvolutionType(Enum):
    """
    Enumeration of different methods by which Pokemon can evolve.
    
    This includes standard evolution methods like using stones, learning moves,
    trading, friendship, and time-based evolution.
    """
    LEVEL = "level"  # Standard level-based evolution
    STONE = "stone"
    MOVE = "move"
    TRADE = "trade"
    FRIENDSHIP = "friendship"
    RANDOM = "Random"
    TIME = "time"  # Evolution based on time of day (day/night)

    @staticmethod
    def from_str(val: str) -> 'EvolutionType':
        """
        Convert a string to an EvolutionType enum value.

        Args:
            val: The string value to convert. Case-insensitive.

        Returns:
            EvolutionType: The corresponding evolution type enum value.

        Raises:
            InvalidEvolutionTypeError: If the string doesn't match any valid evolution type.
            TypeError: If the input is not a string.
        """
        if not isinstance(val, str):
            raise TypeError(f"Evolution type must be a string, got {type(val).__name__}")
        
        try:
            return EvolutionType[val.upper()]
        except KeyError:
            valid_types = ", ".join(t.name.lower() for t in EvolutionType)
            raise InvalidEvolutionTypeError(
                f"Invalid evolution type '{val}'. Valid types are: {valid_types}"
            ) 