"""Tests for the Run class.

This module contains tests for the Run class, verifying its functionality
for managing Pokemon game runs.
"""

import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime, timedelta
from core.run import Run
from definitions import Battle, Encounter, Pokemon
from core.party import Party
from core.box import Box


class TestRun(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        # Create mock objects
        self.party = MagicMock(spec=Party)
        self.box = MagicMock(spec=Box)
        self.box.get_alive_pokemons.return_value = [MagicMock(spec=Pokemon)]
        
        # Create run with initial data
        self.run = Run(
            id="test_run_1",
            run_name="Test Run",
            creation_date=datetime.now(),
            party=self.party,
            box=self.box,
            battles=[],
            encounters=[]
        )

    def test_init_with_valid_data(self):
        """Test Run initialization with valid data."""
        self.assertEqual(self.run.id, "test_run_1")
        self.assertEqual(self.run.run_name, "Test Run")
        self.assertIsInstance(self.run.creation_date, datetime)
        self.assertEqual(self.run.party, self.party)
        self.assertEqual(self.run.box, self.box)
        self.assertEqual(self.run.battles, [])
        self.assertEqual(self.run.encounters, [])
        self.assertIsNone(self.run.starter)
        self.assertEqual(self.run.restarts, 0)
        self.assertFalse(self.run.finished)

    def test_init_with_empty_id(self):
        """Test Run initialization with empty ID raises AssertionError."""
        with self.assertRaises(AssertionError):
            Run(
                id="",
                run_name="Test Run",
                creation_date=datetime.now(),
                party=self.party,
                box=self.box,
                battles=[],
                encounters=[]
            )

    def test_init_with_empty_name(self):
        """Test Run initialization with empty name raises AssertionError."""
        with self.assertRaises(AssertionError):
            Run(
                id="test_run_1",
                run_name="",
                creation_date=datetime.now(),
                party=self.party,
                box=self.box,
                battles=[],
                encounters=[]
            )

    def test_init_with_future_date(self):
        """Test Run initialization with future date raises AssertionError."""
        future_date = datetime.now() + timedelta(days=1)
        with self.assertRaises(AssertionError):
            Run(
                id="test_run_1",
                run_name="Test Run",
                creation_date=future_date,
                party=self.party,
                box=self.box,
                battles=[],
                encounters=[]
            )

    def test_init_with_negative_restarts(self):
        """Test Run initialization with negative restarts raises AssertionError."""
        with self.assertRaises(AssertionError):
            Run(
                id="test_run_1",
                run_name="Test Run",
                creation_date=datetime.now(),
                party=self.party,
                box=self.box,
                battles=[],
                encounters=[],
                restarts=-1
            )

    def test_add_battle(self):
        """Test adding a battle to the run."""
        battle = MagicMock(spec=Battle)
        self.run.add_battle(battle)
        self.assertIn(battle, self.run.battles)

    def test_add_encounter(self):
        """Test adding an encounter to the run."""
        encounter = MagicMock(spec=Encounter)
        self.run.add_encounter(encounter)
        self.assertIn(encounter, self.run.encounters)

    def test_get_battle_count(self):
        """Test getting the battle count."""
        self.assertEqual(self.run.get_battle_count(), 0)
        
        battle = MagicMock(spec=Battle)
        self.run.add_battle(battle)
        self.assertEqual(self.run.get_battle_count(), 1)

    def test_get_encounter_count(self):
        """Test getting the encounter count."""
        self.assertEqual(self.run.get_encounter_count(), 0)
        
        encounter = MagicMock(spec=Encounter)
        self.run.add_encounter(encounter)
        self.assertEqual(self.run.get_encounter_count(), 1)

    def test_get_total_pokemon_count(self):
        """Test getting the total Pokemon count."""
        self.box.get_alive_pokemons.return_value = [MagicMock(spec=Pokemon), MagicMock(spec=Pokemon)]
        self.assertEqual(self.run.get_total_pokemon_count(), 2)

    def test_is_active(self):
        """Test checking if run is active."""
        self.assertTrue(self.run.is_active())
        
        self.run.finish()
        self.assertFalse(self.run.is_active())

    def test_finish(self):
        """Test finishing the run."""
        self.assertFalse(self.run.finished)
        self.run.finish()
        self.assertTrue(self.run.finished)

    def test_restart(self):
        """Test restarting the run."""
        self.assertEqual(self.run.restarts, 0)
        self.run.restart()
        self.assertEqual(self.run.restarts, 1)


if __name__ == '__main__':
    unittest.main() 