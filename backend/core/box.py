"""Box module for managing collections of Pokemon.

This module provides the Box class which represents a collection of Pokemon,
with functionality for adding, removing, and querying Pokemon in the box.
"""

from definitions import Pokemon, PokemonStatus
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Box:
    """A container for managing a collection of Pokemon.
    
    The Box class provides methods for adding, removing, and querying Pokemon.
    It maintains a list of Pokemon and ensures no duplicates are added.
    
    Attributes:
        pokemons: A list of Pokemon in the box
    """
    pokemons: List[Pokemon]

    def __post_init__(self):
        """Validate the box initialization."""
        if self.pokemons is None:
            self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon) -> None:
        """Add a Pokemon to the box.
        
        Args:
            pokemon: The Pokemon to add
            
        Raises:
            AssertionError: If the Pokemon is already in the box
        """
        assert not self._is_pokemon_in_box(pokemon.metadata.id), f"Pokemon {pokemon.metadata.id} already in box"
        self.pokemons.append(pokemon)

    def remove_pokemon(self, pokemon: Pokemon) -> None:
        """Remove a Pokemon from the box.
        
        Args:
            pokemon: The Pokemon to remove
            
        Raises:
            AssertionError: If the Pokemon is not in the box
        """
        assert self._is_pokemon_in_box(pokemon.metadata.id), f"Pokemon {pokemon.metadata.id} is not in box"
        self.pokemons = [box_pokemon for box_pokemon in self.pokemons if box_pokemon.metadata.id != pokemon.metadata.id]

    def _is_pokemon_in_box(self, pokemon_id: str) -> bool:
        """Check if a Pokemon is in the box.
        
        Args:
            pokemon_id: The ID of the Pokemon to check
            
        Returns:
            bool: True if the Pokemon is in the box, False otherwise
        """
        return bool(self.get_pokemon_by_id(pokemon_id))

    def get_pokemon_by_id(self, pokemon_id: str) -> Optional[Pokemon]:
        """Get a Pokemon by its ID.
        
        Args:
            pokemon_id: The ID of the Pokemon to find
            
        Returns:
            Optional[Pokemon]: The Pokemon if found, None otherwise
        """
        return next((pokemon for pokemon in self.pokemons if pokemon.metadata.id == pokemon_id), None)

    def get_alive_pokemons(self) -> List[Pokemon]:
        """Get all alive Pokemon in the box.
        
        Returns:
            List[Pokemon]: A list of all Pokemon that are not dead
        """
        return [
            box_pokemon
            for box_pokemon
            in self.pokemons
            if box_pokemon.status != PokemonStatus.DEAD
        ]

    def get_dead_pokemons(self) -> List[Pokemon]:
        """Get all dead Pokemon in the box.
        
        Returns:
            List[Pokemon]: A list of all Pokemon that are dead
        """
        return [
            box_pokemon
            for box_pokemon
            in self.pokemons
            if box_pokemon.status == PokemonStatus.DEAD
        ]

    def get_pokemons_by_status(self, status: PokemonStatus) -> List[Pokemon]:
        """Get all Pokemon with a specific status.
        
        Args:
            status: The status to filter by
            
        Returns:
            List[Pokemon]: A list of all Pokemon with the specified status
        """
        return [
            box_pokemon
            for box_pokemon
            in self.pokemons
            if box_pokemon.status == status
        ]

    def get_pokemon_count(self) -> int:
        """Get the total number of Pokemon in the box.
        
        Returns:
            int: The number of Pokemon in the box
        """
        return len(self.pokemons)

    def is_empty(self) -> bool:
        """Check if the box is empty.
        
        Returns:
            bool: True if the box is empty, False otherwise
        """
        return len(self.pokemons) == 0
