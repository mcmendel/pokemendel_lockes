"""Party module for managing the player's active Pokemon team.

This module provides the Party class which represents the player's active team of Pokemon.
It extends the Box class with party-specific functionality and constraints.
"""

from definitions import Pokemon
from core.box import Box
from typing import Optional


class Party(Box):
    """A container for managing the player's active Pokemon team.
    
    The Party class extends Box with party-specific functionality, including:
    - Maximum party size limit (6 Pokemon)
    - Prevention of empty parties
    - Party-specific validation rules
    
    Attributes:
        MAX_PARTY_SIZE: The maximum number of Pokemon allowed in the party
    """
    MAX_PARTY_SIZE = 6

    def add_pokemon(self, pokemon: Pokemon) -> None:
        """Add a Pokemon to the party.
        
        Args:
            pokemon: The Pokemon to add
            
        Raises:
            AssertionError: If the Pokemon is already in party or if party is full
        """
        assert not self.is_pokemon_in_party(pokemon), "Pokemon is already in party"
        assert not self.is_party_full(), "Can't add pokemon to full party"
        return super().add_pokemon(pokemon)

    def remove_pokemon(self, pokemon: Pokemon) -> None:
        """Remove a Pokemon from the party.
        
        Args:
            pokemon: The Pokemon to remove
            
        Raises:
            AssertionError: If the Pokemon is not in party or if it's the last Pokemon
        """
        assert self.is_pokemon_in_party(pokemon), "Pokemon is not in party"
        assert not self.is_last_pokemon_in_party(), "Can't leave party empty"
        return super().remove_pokemon(pokemon)

    def is_party_full(self) -> bool:
        """Check if the party is at maximum capacity.
        
        Returns:
            bool: True if the party has 6 Pokemon, False otherwise
        """
        assert len(self.pokemons) <= self.MAX_PARTY_SIZE, "Party can't have more than 6 pokemons"
        return len(self.pokemons) == self.MAX_PARTY_SIZE

    def is_last_pokemon_in_party(self) -> bool:
        """Check if there is only one Pokemon in the party.
        
        Returns:
            bool: True if there is exactly one Pokemon, False otherwise
        """
        return len(self.pokemons) == 1

    def is_pokemon_in_party(self, pokemon: Pokemon) -> bool:
        """Check if a Pokemon is in the party.
        
        Args:
            pokemon: The Pokemon to check
            
        Returns:
            bool: True if the Pokemon is in the party, False otherwise
        """
        return any(party_pokemon.metadata.id == pokemon.metadata.id for party_pokemon in self.pokemons)
