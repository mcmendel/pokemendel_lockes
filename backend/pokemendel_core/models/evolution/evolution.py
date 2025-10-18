"""
Module containing the Evolution class for representing Pokemon evolution requirements.
"""

from dataclasses import dataclass
from typing import Optional
from .evolution_type import EvolutionType
from .items import Item


@dataclass
class Evolution:
    """
    Represents the evolution requirements and details for a Pokemon.

    This class encapsulates all the information needed for a Pokemon's evolution,
    including the target evolution name, evolution method, level requirements,
    item requirements, and any special conditions.

    Attributes:
        name (str): The name of the Pokemon that this evolution leads to.
        evolution_type (Optional[EvolutionType]): The method of evolution (e.g., STONE, LEVEL, TRADE).
            Defaults to LEVEL.
        level (Optional[int]): The level requirement for the evolution, if any.
            Defaults to None.
        should_hold (bool): Whether the Pokemon needs to hold an item during evolution.
            Defaults to False.
        item (Optional[Item]): The specific item required for evolution, if any.
            Defaults to None.
        special_information (Optional[str]): Any additional requirements or information
            about the evolution process. Defaults to None.

    Examples:
        >>> # Level-based evolution (Charmander to Charmeleon)
        >>> charmeleon = Evolution(
        ...     name="Charmeleon",
        ...     level=16
        ... )

        >>> # Stone-based evolution (Eevee to Vaporeon)
        >>> vaporeon = Evolution(
        ...     name="Vaporeon",
        ...     evolution_type=EvolutionType.STONE,
        ...     item=Item.WATER_STONE
        ... )

        >>> # Trade with held item (Scyther to Scizor)
        >>> scizor = Evolution(
        ...     name="Scizor",
        ...     evolution_type=EvolutionType.TRADE,
        ...     should_hold=True,
        ...     item=Item.METAL_COAT
        ... )
    """

    name: str
    evolution_type: EvolutionType = EvolutionType.LEVEL  # Default to level-based evolution
    level: Optional[int] = None
    should_hold: bool = False
    item: Optional[Item] = None
    special_information: Optional[str] = None