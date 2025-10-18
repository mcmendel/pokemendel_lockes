"""
Pokemendel Core - A Python package providing comprehensive data structures and utilities
for working with Pokémon from Generations 1 and 2.

This package provides access to detailed Pokémon data including types, stats,
evolution chains, and more. It supports both Generation 1 (151 Pokémon) and
Generation 2 (251 Pokémon total).

Example:
    >>> from pokemendel_core.data.gen2 import PokemonGen2, NAME_TO_POKEMON
    >>> tyranitar = NAME_TO_POKEMON[PokemonGen2.TYRANITAR]
    >>> print([t.value for t in tyranitar.types])
    ['ROCK', 'DARK']
"""

__version__ = "0.3.0"

from pokemendel_core.data.gen1 import PokemonGen1
from pokemendel_core.data.gen2 import PokemonGen2, NAME_TO_POKEMON
from pokemendel_core.models.pokemon import Pokemon
from pokemendel_core.models.evolution import Evolution, EvolutionType
from pokemendel_core.utils.definitions.stats import Stats
from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.utils.definitions.colors import Colors
from pokemendel_core.utils.definitions.categories import Categories
from pokemendel_core.utils.definitions.genders import Genders

__all__ = [
    'PokemonGen1',
    'PokemonGen2',
    'NAME_TO_POKEMON',
    'Pokemon',
    'Evolution',
    'EvolutionType',
    'Stats',
    'Types',
    'Colors',
    'Categories',
    'Genders',
] 