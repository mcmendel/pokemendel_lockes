"""Tests for the Party class.

This module contains tests for the Party class, verifying its functionality
for managing the player's active Pokemon team.
"""

import unittest
from unittest.mock import MagicMock
from core.party import Party
from definitions import Pokemon, PokemonStatus


class TestParty(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        # Create mock Pokemon
        self.pokemon1 = MagicMock(spec=Pokemon)
        self.pokemon1.metadata.id = "pokemon1"
        self.pokemon1.status = PokemonStatus.ALIVE

        self.pokemon2 = MagicMock(spec=Pokemon)
        self.pokemon2.metadata.id = "pokemon2"
        self.pokemon2.status = PokemonStatus.ALIVE

        self.pokemon3 = MagicMock(spec=Pokemon)
        self.pokemon3.metadata.id = "pokemon3"
        self.pokemon3.status = PokemonStatus.ALIVE

        # Create party with initial Pokemon
        self.party = Party(pokemons=[self.pokemon1])

    def test_add_pokemon(self):
        """Test adding a Pokemon to the party."""
        self.party.add_pokemon(self.pokemon2)
        self.assertIn(self.pokemon2, self.party.pokemons)
        self.assertEqual(len(self.party.pokemons), 2)

    def test_add_duplicate_pokemon(self):
        """Test adding a duplicate Pokemon raises AssertionError."""
        with self.assertRaises(AssertionError):
            self.party.add_pokemon(self.pokemon1)

    def test_add_to_full_party(self):
        """Test adding to a full party raises AssertionError."""
        # Fill the party
        for i in range(2, 7):
            pokemon = MagicMock(spec=Pokemon)
            pokemon.metadata.id = f"pokemon{i}"
            self.party.add_pokemon(pokemon)

        # Try to add one more
        with self.assertRaises(AssertionError):
            self.party.add_pokemon(self.pokemon3)

    def test_remove_pokemon(self):
        """Test removing a Pokemon from the party."""
        self.party.add_pokemon(self.pokemon2)  # Add a second Pokemon first
        self.party.remove_pokemon(self.pokemon1)
        self.assertNotIn(self.pokemon1, self.party.pokemons)
        self.assertEqual(len(self.party.pokemons), 1)

    def test_remove_nonexistent_pokemon(self):
        """Test removing a nonexistent Pokemon raises AssertionError."""
        with self.assertRaises(AssertionError):
            self.party.remove_pokemon(self.pokemon2)

    def test_remove_last_pokemon(self):
        """Test removing the last Pokemon raises AssertionError."""
        with self.assertRaises(AssertionError):
            self.party.remove_pokemon(self.pokemon1)

    def test_is_party_full(self):
        """Test checking if party is full."""
        self.assertFalse(self.party.is_party_full())
        
        # Fill the party
        for i in range(2, 7):
            pokemon = MagicMock(spec=Pokemon)
            pokemon.metadata.id = f"pokemon{i}"
            self.party.add_pokemon(pokemon)
        
        self.assertTrue(self.party.is_party_full())

    def test_is_last_pokemon_in_party(self):
        """Test checking if there is only one Pokemon."""
        self.assertTrue(self.party.is_last_pokemon_in_party())
        
        self.party.add_pokemon(self.pokemon2)
        self.assertFalse(self.party.is_last_pokemon_in_party())

    def test_is_pokemon_in_party(self):
        """Test checking if a Pokemon is in the party."""
        self.assertTrue(self.party.is_pokemon_in_party(self.pokemon1))
        self.assertFalse(self.party.is_pokemon_in_party(self.pokemon2))


if __name__ == '__main__':
    unittest.main() 