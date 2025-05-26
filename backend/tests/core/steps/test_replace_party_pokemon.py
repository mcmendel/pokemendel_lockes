"""Tests for the ReplacePartyPokemon class.

This module contains tests for the ReplacePartyPokemon class, verifying its functionality
for replacing Pokemon in the player's party.
"""

import unittest
from unittest.mock import MagicMock, patch
from core.steps.replace_party_pokemon import ReplacePartyPokemon
from core.run import Run
from definitions import Pokemon
from definitions.runs.inputs_options import InputOptions


class TestReplacePartyPokemon(unittest.TestCase):
    """Test cases for the ReplacePartyPokemon class."""

    def setUp(self):
        """Set up test fixtures."""
        self.step = ReplacePartyPokemon()
        self.run = MagicMock(spec=Run)
        self.party = MagicMock()
        self.run.party = self.party
        self.pokemon = MagicMock(spec=Pokemon)
        self.pokemon.metadata.id = "new_pokemon"
        
        # Create mock party Pokemon
        self.party_pokemon1 = MagicMock(spec=Pokemon)
        self.party_pokemon1.metadata.id = "pokemon1"
        self.party_pokemon2 = MagicMock(spec=Pokemon)
        self.party_pokemon2.metadata.id = "pokemon2"
        self.party.pokemons = [self.party_pokemon1, self.party_pokemon2]

    def test_is_step_relevant_when_not_in_party(self):
        """Test is_step_relevant when Pokemon is not in party."""
        self.party.is_pokemon_in_party.return_value = False
        
        result = self.step.is_step_relevant(self.run, self.pokemon)
        
        self.assertTrue(result)
        self.party.is_pokemon_in_party.assert_called_once_with(self.pokemon)

    def test_is_step_relevant_when_in_party(self):
        """Test is_step_relevant when Pokemon is already in party."""
        self.party.is_pokemon_in_party.return_value = True
        
        result = self.step.is_step_relevant(self.run, self.pokemon)
        
        self.assertFalse(result)
        self.party.is_pokemon_in_party.assert_called_once_with(self.pokemon)

    def test_step_options(self):
        """Test step_options returns correct options."""
        options, choices = self.step.step_options(self.run, self.pokemon)
        
        self.assertEqual(options, InputOptions.ONE_OF)
        self.assertEqual(choices, ["pokemon1", "pokemon2"])

    def test_step_options_empty_party(self):
        """Test step_options with empty party."""
        self.party.pokemons = []
        options, choices = self.step.step_options(self.run, self.pokemon)
        
        self.assertEqual(options, InputOptions.ONE_OF)
        self.assertEqual(choices, [])

    def test_execute_step_success_full_party(self):
        """Test execute_step successfully replaces Pokemon in full party."""
        self.party.is_party_full.return_value = True
        self.run.get_pokemon_by_id.return_value = self.party_pokemon1
        
        result = self.step.execute_step(self.run, self.pokemon, "pokemon1")
        
        self.party.remove_pokemon.assert_called_once_with(self.party_pokemon1)
        self.party.add_pokemon.assert_called_once_with(self.pokemon)
        self.assertEqual(result.pokemons_to_update, [])

    def test_execute_step_success_not_full_party(self):
        """Test execute_step successfully replaces Pokemon in not full party."""
        self.party.is_party_full.return_value = False
        self.run.get_pokemon_by_id.return_value = self.party_pokemon1
        
        result = self.step.execute_step(self.run, self.pokemon, "pokemon1")
        
        self.party.add_pokemon.assert_called_once_with(self.pokemon)
        self.party.remove_pokemon.assert_called_once_with(self.party_pokemon1)
        self.assertEqual(result.pokemons_to_update, [])

    def test_execute_step_with_none_value(self):
        """Test execute_step raises AssertionError when value is None."""
        with self.assertRaises(AssertionError) as context:
            self.step.execute_step(self.run, self.pokemon, None)
        
        self.assertEqual(str(context.exception), "Value is required when replacing pokemon in party")
        self.party.add_pokemon.assert_not_called()
        self.party.remove_pokemon.assert_not_called()

    def test_execute_step_with_invalid_pokemon_id(self):
        """Test execute_step raises AssertionError when Pokemon ID is invalid."""
        with self.assertRaises(AssertionError) as context:
            self.step.execute_step(self.run, self.pokemon, "invalid_id")
        
        self.assertEqual(str(context.exception), "Given pokemon invalid_id is not in party")
        self.party.add_pokemon.assert_not_called()
        self.party.remove_pokemon.assert_not_called()

    def test_party_pokemon_ids(self):
        """Test _party_pokemon_ids returns correct list of IDs."""
        ids = self.step._party_pokemon_ids(self.run)
        
        self.assertEqual(ids, ["pokemon1", "pokemon2"])

    def test_party_pokemon_ids_empty(self):
        """Test _party_pokemon_ids with empty party."""
        self.party.pokemons = []
        ids = self.step._party_pokemon_ids(self.run)
        
        self.assertEqual(ids, [])

    def test_execute_step_operation_order_full_party(self):
        """Test the order of operations when party is full."""
        self.party.is_party_full.return_value = True
        self.run.get_pokemon_by_id.return_value = self.party_pokemon1
        
        self.step.execute_step(self.run, self.pokemon, "pokemon1")
        
        # Verify operation order
        calls = [call[0] for call in self.party.method_calls]
        self.assertEqual(calls, ['is_party_full', 'remove_pokemon', 'add_pokemon'])

    def test_execute_step_operation_order_not_full_party(self):
        """Test the order of operations when party is not full."""
        self.party.is_party_full.return_value = False
        self.run.get_pokemon_by_id.return_value = self.party_pokemon1
        
        self.step.execute_step(self.run, self.pokemon, "pokemon1")
        
        # Verify operation order
        calls = [call[0] for call in self.party.method_calls]
        self.assertEqual(calls, ['is_party_full', 'add_pokemon', 'remove_pokemon'])

    def test_execute_step_with_empty_string(self):
        """Test execute_step raises AssertionError when value is empty string."""
        with self.assertRaises(AssertionError) as context:
            self.step.execute_step(self.run, self.pokemon, "")
        
        self.assertEqual(str(context.exception), "Given pokemon  is not in party")
        self.party.add_pokemon.assert_not_called()
        self.party.remove_pokemon.assert_not_called()

    def test_execute_step_return_value_immutable(self):
        """Test that execute_step returns a new ExecutionReturnValue instance each time."""
        self.party.is_party_full.return_value = True
        self.run.get_pokemon_by_id.return_value = self.party_pokemon1
        
        result1 = self.step.execute_step(self.run, self.pokemon, "pokemon1")
        result2 = self.step.execute_step(self.run, self.pokemon, "pokemon1")
        
        self.assertIsNot(result1, result2)
        self.assertEqual(result1.pokemons_to_update, result2.pokemons_to_update)


if __name__ == '__main__':
    unittest.main() 