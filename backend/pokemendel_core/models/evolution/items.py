"""
Module containing evolution item definitions and related functionality.
"""

from enum import Enum


class InvalidItemError(ValueError):
    """Raised when an invalid evolution item string is provided."""
    pass


class Item(Enum):
    """
    Enumeration of evolution-related items in the Pokemon games.
    
    This includes evolution stones and special items that trigger specific Pokemon evolutions.
    Each item is represented by its official in-game name.
    """
    WATER_STONE = "Water Stone"
    FIRE_STONE = "Fire Stone"
    LEAF_STONE = "Leaf Stone"
    THUNDER_STONE = "Thunder Stone"
    MOON_STONE = "Moon Stone"
    SUN_STONE = "Sun Stone"
    KINGS_ROCK = "Kings Rock"
    METAL_COAT = "Metal Coat"
    DRAGON_SCALE = "Dragon Scale"
    UPGRADE = "Upgrade"
    PRISM_SCALE = "Prism Scale"
    DEEP_SEA_TOOTH = "Depp Sea Tooth"
    DEEP_SEA_SCALE = "Deep Sea Scale"

    @staticmethod
    def from_str(val: str) -> 'Item':
        """
        Convert a string to an Item enum value.

        Args:
            val: The string value to convert. Case-insensitive.
                 Spaces in the input will be converted to underscores for matching.

        Returns:
            Item: The corresponding item enum value.

        Raises:
            InvalidItemError: If the string doesn't match any valid item.
            TypeError: If the input is not a string.

        Examples:
            >>> Item.from_str("Water Stone")
            Item.WATER_STONE
            >>> Item.from_str("WATER_STONE")
            Item.WATER_STONE
            >>> Item.from_str("water stone")
            Item.WATER_STONE
        """
        if not isinstance(val, str):
            raise TypeError(f"Item must be a string, got {type(val).__name__}")

        try:
            val_to_key = val.upper().replace(" ", "_")
            return Item[val_to_key]
        except KeyError:
            valid_items = ", ".join(item.value for item in Item)
            raise InvalidItemError(
                f"Invalid item '{val}'. Valid items are: {valid_items}"
            ) 
