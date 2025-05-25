"""Tests for the AddToPartyStep class.

This module contains tests for the AddToPartyStep class, verifying its functionality
for adding Pokemon to the player's party.
"""

import unittest
from unittest.mock import MagicMock, patch
from core.steps.add_to_party_step import AddToPartyStep
from core.run import Run
from definitions import Pokemon
from definitions.runs.inputs_options import InputOptions


class TestAddToPartyStep(unittest.TestCase):
    """Test cases for the AddToPartyStep class."""

    def setUp(self):
        """Set up test fixtures."""
        self.step = AddToPartyStep()
        self.run = MagicMock(spec=Run)
        self.party = MagicMock()
        self.run.party = self.party
        self.pokemon = MagicMock(spec=Pokemon)

    def test_is_step_relevant_when_can_add(self):
        """Test is_step_relevant when Pokemon can be added to party."""
        self.party.is_party_full.return_value = False
        self.party.is_pokemon_in_party.return_value = False
        
        result = self.step.is_step_relevant(self.run, self.pokemon)
        
        self.assertTrue(result)
        self.party.is_party_full.assert_called_once()
        self.party.is_pokemon_in_party.assert_called_once_with(self.pokemon)

    def test_is_step_relevant_when_party_full(self):
        """Test is_step_relevant when party is full."""
        self.party.is_party_full.return_value = True
        self.party.is_pokemon_in_party.return_value = False
        
        result = self.step.is_step_relevant(self.run, self.pokemon)
        
        self.assertFalse(result)
        self.party.is_party_full.assert_called_once()
        self.party.is_pokemon_in_party.assert_not_called()

    def test_is_step_relevant_when_pokemon_in_party(self):
        """Test is_step_relevant when Pokemon is already in party."""
        self.party.is_party_full.return_value = False
        self.party.is_pokemon_in_party.return_value = True
        
        result = self.step.is_step_relevant(self.run, self.pokemon)
        
        self.assertFalse(result)
        self.party.is_party_full.assert_called_once()
        self.party.is_pokemon_in_party.assert_called_once_with(self.pokemon)

    def test_step_options(self):
        """Test step_options returns correct options."""
        options, choices = self.step.step_options(self.run, self.pokemon)
        
        self.assertEqual(options, InputOptions.NOTHING)
        self.assertEqual(choices, [])

    def test_execute_step_success(self):
        """Test execute_step successfully adds Pokemon to party."""
        result = self.step.execute_step(self.run, self.pokemon, None)
        
        self.party.add_pokemon.assert_called_once_with(self.pokemon)
        self.assertEqual(result.pokemons_to_update, [])

    def test_execute_step_with_value(self):
        """Test execute_step raises AssertionError when value is provided."""
        with self.assertRaises(AssertionError) as context:
            self.step.execute_step(self.run, self.pokemon, "some_value")
        
        self.assertEqual(str(context.exception), "Value is not expected when adding pokemon to party")
        self.party.add_pokemon.assert_not_called()


if __name__ == '__main__':
    unittest.main() 