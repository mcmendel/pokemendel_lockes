"""Tests for the Box class.

This module contains tests for the Box class, verifying its functionality
for managing collections of Pokemon.
"""

import unittest
from unittest.mock import MagicMock
from core.box import Box
from definitions import Pokemon, PokemonStatus


class TestBox(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        # Create mock Pokemon
        self.pokemon1 = MagicMock(spec=Pokemon)
        self.pokemon1.metadata.id = "pokemon1"
        self.pokemon1.status = PokemonStatus.ALIVE

        self.pokemon2 = MagicMock(spec=Pokemon)
        self.pokemon2.metadata.id = "pokemon2"
        self.pokemon2.status = PokemonStatus.DEAD

        self.pokemon3 = MagicMock(spec=Pokemon)
        self.pokemon3.metadata.id = "pokemon3"
        self.pokemon3.status = PokemonStatus.ALIVE

        # Create box with initial Pokemon
        self.box = Box(pokemons=[self.pokemon1, self.pokemon2])

    def test_init_with_none(self):
        """Test Box initialization with None pokemons list."""
        box = Box(pokemons=None)
        self.assertEqual(box.pokemons, [])

    def test_init_with_empty_list(self):
        """Test Box initialization with empty pokemons list."""
        box = Box(pokemons=[])
        self.assertEqual(box.pokemons, [])

    def test_add_pokemon(self):
        """Test adding a Pokemon to the box."""
        self.box.add_pokemon(self.pokemon3)
        self.assertIn(self.pokemon3, self.box.pokemons)
        self.assertEqual(len(self.box.pokemons), 3)

    def test_add_duplicate_pokemon(self):
        """Test adding a duplicate Pokemon raises AssertionError."""
        with self.assertRaises(AssertionError):
            self.box.add_pokemon(self.pokemon1)

    def test_remove_pokemon(self):
        """Test removing a Pokemon from the box."""
        self.box.remove_pokemon(self.pokemon1)
        self.assertNotIn(self.pokemon1, self.box.pokemons)
        self.assertEqual(len(self.box.pokemons), 1)

    def test_remove_nonexistent_pokemon(self):
        """Test removing a nonexistent Pokemon raises AssertionError."""
        with self.assertRaises(AssertionError):
            self.box.remove_pokemon(self.pokemon3)

    def test_is_pokemon_in_box(self):
        """Test checking if a Pokemon is in the box."""
        self.assertTrue(self.box._is_pokemon_in_box("pokemon1"))
        self.assertFalse(self.box._is_pokemon_in_box("pokemon3"))

    def test_get_pokemon_by_id(self):
        """Test getting a Pokemon by ID."""
        pokemon = self.box.get_pokemon_by_id("pokemon1")
        self.assertEqual(pokemon, self.pokemon1)

        pokemon = self.box.get_pokemon_by_id("nonexistent")
        self.assertIsNone(pokemon)

    def test_get_alive_pokemons(self):
        """Test getting all alive Pokemon."""
        alive_pokemons = self.box.get_alive_pokemons()
        self.assertEqual(len(alive_pokemons), 1)
        self.assertIn(self.pokemon1, alive_pokemons)
        self.assertNotIn(self.pokemon2, alive_pokemons)

    def test_get_dead_pokemons(self):
        """Test getting all dead Pokemon."""
        dead_pokemons = self.box.get_dead_pokemons()
        self.assertEqual(len(dead_pokemons), 1)
        self.assertIn(self.pokemon2, dead_pokemons)
        self.assertNotIn(self.pokemon1, dead_pokemons)

    def test_get_pokemons_by_status(self):
        """Test getting Pokemon by status."""
        alive_pokemons = self.box.get_pokemons_by_status(PokemonStatus.ALIVE)
        self.assertEqual(len(alive_pokemons), 1)
        self.assertIn(self.pokemon1, alive_pokemons)

        dead_pokemons = self.box.get_pokemons_by_status(PokemonStatus.DEAD)
        self.assertEqual(len(dead_pokemons), 1)
        self.assertIn(self.pokemon2, dead_pokemons)

    def test_get_pokemon_count(self):
        """Test getting the total number of Pokemon."""
        self.assertEqual(self.box.get_pokemon_count(), 2)
        
        self.box.add_pokemon(self.pokemon3)
        self.assertEqual(self.box.get_pokemon_count(), 3)
        
        self.box.remove_pokemon(self.pokemon1)
        self.assertEqual(self.box.get_pokemon_count(), 2)

    def test_is_empty(self):
        """Test checking if the box is empty."""
        self.assertFalse(self.box.is_empty())
        
        empty_box = Box(pokemons=[])
        self.assertTrue(empty_box.is_empty())


if __name__ == '__main__':
    unittest.main() 