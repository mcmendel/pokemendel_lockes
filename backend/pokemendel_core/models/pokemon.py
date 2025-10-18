from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.utils.definitions.colors import Colors
from pokemendel_core.utils.definitions.genders import Genders
from pokemendel_core.utils.definitions.categories import Categories
from pokemendel_core.utils.definitions.stats import Stats
from pokemendel_core.utils.definitions.natures import Natures
from pokemendel_core.utils.definitions.abilities import Abilities
from .evolution.evolution import Evolution


@dataclass
class Pokemon:
    """Class representing a Pokémon.
    
    Attributes:
        name (str): The Pokémon's name
        gen (int): The generation this Pokémon was introduced in
        types (List[Types]): The Pokémon's type(s)
        stats (Optional[Stats]): The Pokémon's base stats
        evolves_to (List[Evolution]): List of possible evolutions
        colors (List[Colors]): The Pokémon's colors
        supported_genders (List[Genders]): The Pokémon's possible genders
        categories (List[Categories]): The Pokémon's categories
        num_legs (int): Number of legs the Pokémon has
    """
    
    name: str
    gen: int
    types: List[Types]
    stats: Optional[Stats] = None
    evolves_to: List[Evolution] = field(default_factory=list)
    colors: List[Colors] = field(default_factory=list)
    supported_genders: List[Genders] = field(default_factory=list)
    categories: List[Categories] = field(default_factory=list)
    num_legs: int = -1
    nature: Optional[Natures] = None
    supported_abilities: List[Abilities] = field(default_factory=list)

    def evolve_pokemon(self, evolution_pokemon: 'Pokemon') -> None:
        """Evolve this Pokemon into another Pokemon."""
        self.types = evolution_pokemon.types
        self.stats = evolution_pokemon.stats
        self.evolves_to = evolution_pokemon.evolves_to
        self.name = evolution_pokemon.name
        self.colors = evolution_pokemon.colors
        self.categories = evolution_pokemon.categories
        self.supported_genders = (
            evolution_pokemon.supported_genders
            if evolution_pokemon.supported_genders
            else self.supported_genders
        )
        self.num_legs = evolution_pokemon.num_legs
        self.nature = evolution_pokemon.nature
        self.supported_abilities = (
            evolution_pokemon.supported_abilities
            if evolution_pokemon.supported_abilities
            else self.supported_abilities
        )
