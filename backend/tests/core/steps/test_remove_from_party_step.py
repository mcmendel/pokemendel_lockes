"""Tests for the RemoveFromPartyStep class.

This module contains tests for the RemoveFromPartyStep class, verifying its functionality
for removing Pokemon from the player's party.
"""

import unittest
from unittest.mock import MagicMock, patch
from core.steps.remove_from_party_step import RemoveFromPartyStep
from core.run import Run
from definitions import Pokemon
from definitions.runs.inputs_options import InputOptions


class TestRemoveFromPartyStep(unittest.TestCase):
    """Test cases for the RemoveFromPartyStep class."""

    def setUp(self):
        """Set up test fixtures."""
        self.step = RemoveFromPartyStep()
        self.run = MagicMock(spec=Run)
        self.party = MagicMock()
        self.run.party = self.party
        self.pokemon = MagicMock(spec=Pokemon)

    def test_is_step_relevant_when_can_remove(self):
        """Test is_step_relevant when Pokemon can be removed from party."""
        self.party.is_last_pokemon_in_party.return_value = False
        self.party.is_pokemon_in_party.return_value = True
        
        result = self.step.is_step_relevant(self.run, self.pokemon)
        
        self.assertTrue(result)
        self.party.is_last_pokemon_in_party.assert_called_once()
        self.party.is_pokemon_in_party.assert_called_once_with(self.pokemon)

    def test_is_step_relevant_when_last_pokemon(self):
        """Test is_step_relevant when it's the last Pokemon in party."""
        self.party.is_last_pokemon_in_party.return_value = True
        self.party.is_pokemon_in_party.return_value = True
        
        result = self.step.is_step_relevant(self.run, self.pokemon)
        
        self.assertFalse(result)
        self.party.is_last_pokemon_in_party.assert_called_once()
        self.party.is_pokemon_in_party.assert_not_called()

    def test_is_step_relevant_when_not_in_party(self):
        """Test is_step_relevant when Pokemon is not in party."""
        self.party.is_last_pokemon_in_party.return_value = False
        self.party.is_pokemon_in_party.return_value = False
        
        result = self.step.is_step_relevant(self.run, self.pokemon)
        
        self.assertFalse(result)
        self.party.is_last_pokemon_in_party.assert_called_once()
        self.party.is_pokemon_in_party.assert_called_once_with(self.pokemon)

    def test_is_step_relevant_method_order(self):
        """Test that is_last_pokemon_in_party is checked before is_pokemon_in_party."""
        self.party.is_last_pokemon_in_party.return_value = True
        self.party.is_pokemon_in_party.return_value = True
        
        self.step.is_step_relevant(self.run, self.pokemon)
        
        # Verify the order of method calls
        self.assertEqual(
            [call[0] for call in self.party.method_calls],
            ['is_last_pokemon_in_party']
        )

    def test_step_options(self):
        """Test step_options returns correct options."""
        options, choices = self.step.step_options(self.run, self.pokemon)
        
        self.assertEqual(options, InputOptions.NOTHING)
        self.assertEqual(choices, [])

    def test_step_options_immutable(self):
        """Test that step_options returns a new list each time."""
        _, choices1 = self.step.step_options(self.run, self.pokemon)
        _, choices2 = self.step.step_options(self.run, self.pokemon)
        
        self.assertIsNot(choices1, choices2)
        self.assertEqual(choices1, choices2)

    def test_execute_step_success(self):
        """Test execute_step successfully removes Pokemon from party."""
        result = self.step.execute_step(self.run, self.pokemon, None)
        
        self.party.remove_pokemon.assert_called_once_with(self.pokemon)
        self.assertEqual(result.pokemons_to_update, [])

    def test_execute_step_with_value(self):
        """Test execute_step raises AssertionError when value is provided."""
        with self.assertRaises(AssertionError) as context:
            self.step.execute_step(self.run, self.pokemon, "some_value")
        
        self.assertEqual(str(context.exception), "Value is not expected when removing pokemon from party")
        self.party.remove_pokemon.assert_not_called()

    def test_execute_step_with_empty_string(self):
        """Test execute_step raises AssertionError when empty string is provided."""
        with self.assertRaises(AssertionError) as context:
            self.step.execute_step(self.run, self.pokemon, "")
        
        self.assertEqual(str(context.exception), "Value is not expected when removing pokemon from party")
        self.party.remove_pokemon.assert_not_called()

    def test_execute_step_return_value_immutable(self):
        """Test that execute_step returns a new ExecutionReturnValue each time."""
        result1 = self.step.execute_step(self.run, self.pokemon, None)
        result2 = self.step.execute_step(self.run, self.pokemon, None)
        
        self.assertIsNot(result1, result2)
        self.assertEqual(result1.pokemons_to_update, result2.pokemons_to_update)


if __name__ == '__main__':
    unittest.main() 