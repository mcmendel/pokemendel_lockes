"""Tests for the base run creator functionality.

This module contains tests for the RunCreator and RunCreationProgress classes,
verifying their behavior in managing the run creation process.
"""

import unittest
from unittest.mock import patch, MagicMock
from core.lockes.base.run_creator import RunCreator, RunCreationProgress, InfoKeys
from models.run_creation import RunCreation
from datetime import datetime
from core.party import Party
from core.box import Box


class TestRunCreationProgress(unittest.TestCase):
    def test_init_default_values(self):
        """Test RunCreationProgress initialization with default values."""
        run_creation = RunCreation(name="test_run")
        progress = RunCreationProgress(run_creation=run_creation)
        
        self.assertEqual(progress.run_creation, run_creation)
        self.assertFalse(progress.has_all_info)
        self.assertIsNone(progress.missing_key)
        self.assertIsNone(progress.missing_key_options)

    def test_init_with_values(self):
        """Test RunCreationProgress initialization with all values."""
        run_creation = RunCreation(name="test_run")
        progress = RunCreationProgress(
            run_creation=run_creation,
            has_all_info=True,
            missing_key="TEST_KEY",
            missing_key_options=["option1", "option2"]
        )
        
        self.assertEqual(progress.run_creation, run_creation)
        self.assertTrue(progress.has_all_info)
        self.assertEqual(progress.missing_key, "TEST_KEY")
        self.assertEqual(progress.missing_key_options, ["option1", "option2"])


class TestRunCreator(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.mock_run_creation = RunCreation(name="test_run")
        
        # Mock the database function
        self.update_patcher = patch('core.lockes.base.run_creator.update_run_creation')
        self.mock_update = self.update_patcher.start()
        
        self.run_creator = RunCreator(self.mock_run_creation)

    def tearDown(self):
        """Clean up test fixtures."""
        self.update_patcher.stop()

    def test_init(self):
        """Test RunCreator initialization."""
        self.assertEqual(self.run_creator.run_creation, self.mock_run_creation)

    def test_get_progress_finished(self):
        """Test get_progress when run is finished."""
        self.mock_run_creation.finished = True
        progress = self.run_creator.get_progress()
        
        self.assertTrue(progress.has_all_info)
        self.assertEqual(progress.run_creation, self.mock_run_creation)

    def test_get_progress_missing_game(self):
        """Test get_progress when game is missing."""
        self.mock_run_creation.finished = False
        self.mock_run_creation.game = None
        progress = self.run_creator.get_progress()
        
        self.assertFalse(progress.has_all_info)
        self.assertEqual(progress.missing_key, InfoKeys.GAME)

    def test_get_progress_complete(self):
        """Test get_progress when all required fields are present."""
        self.mock_run_creation.finished = False
        self.mock_run_creation.game = "test_game"
        progress = self.run_creator.get_progress()
        
        self.assertTrue(progress.has_all_info)
        self.assertEqual(progress.run_creation, self.mock_run_creation)

    def test_update_progress_game(self):
        """Test update_progress for game field."""
        self.run_creator.update_progress(InfoKeys.GAME, "test_game")
        
        self.assertEqual(self.mock_run_creation.game, "test_game")
        self.assertEqual(self.mock_run_creation.extra_info[InfoKeys.GAME], "test_game")
        self.mock_update.assert_called_once_with(self.mock_run_creation)

    def test_update_progress_extra_info(self):
        """Test update_progress stores any key in extra_info."""
        self.run_creator.update_progress("CUSTOM_KEY", "custom_value")
        
        self.assertEqual(self.mock_run_creation.extra_info["CUSTOM_KEY"], "custom_value")
        self.mock_update.assert_called_once_with(self.mock_run_creation)

    def test_finish_creation(self):
        """Test finish_creation method returns a Run instance."""
        # Set up required fields
        self.mock_run_creation.game = "red"
        self.mock_run_creation.locke = "nuzlocke"
        self.mock_run_creation.duplicate_clause = False
        self.mock_run_creation.randomized = True
        
        # Call finish_creation
        run = self.run_creator.finish_creation()
        
        # Verify run creation was marked as finished
        self.assertTrue(self.mock_run_creation.finished)
        self.mock_update.assert_called_once_with(self.mock_run_creation)
        
        # Verify returned Run instance
        self.assertEqual(run.id, self.mock_run_creation.name)
        self.assertEqual(run.run_name, self.mock_run_creation.name)
        self.assertIsInstance(run.creation_date, datetime)
        self.assertIsInstance(run.party, Party)
        self.assertEqual(len(run.party.pokemons), 0)
        self.assertIsInstance(run.box, Box)
        self.assertEqual(len(run.box.pokemons), 0)

    def test_finish_creation_missing_required_fields(self):
        """Test finish_creation raises AssertionError when required fields are missing."""
        # Test missing game
        with self.assertRaises(AssertionError) as context:
            self.run_creator.finish_creation()
        self.assertEqual(str(context.exception), "Run creation must have a game set")
        
        # Test missing locke
        self.mock_run_creation.game = "red"
        with self.assertRaises(AssertionError) as context:
            self.run_creator.finish_creation()
        self.assertEqual(str(context.exception), "Run creation must have a locke type set")

    def test_create_run(self):
        """Test _create_run method creates a Run instance with correct data."""
        # Set up required fields
        self.mock_run_creation.finished = True
        self.mock_run_creation.game = "red"
        self.mock_run_creation.locke = "nuzlocke"
        self.mock_run_creation.duplicate_clause = False
        self.mock_run_creation.randomized = True
        
        # Call _create_run
        run = self.run_creator._create_run()
        
        # Verify Run instance
        self.assertEqual(run.id, self.mock_run_creation.name)
        self.assertEqual(run.run_name, self.mock_run_creation.name)
        self.assertIsInstance(run.creation_date, datetime)
        self.assertIsInstance(run.party, Party)
        self.assertEqual(len(run.party.pokemons), 0)
        self.assertIsInstance(run.box, Box)
        self.assertEqual(len(run.box.pokemons), 0)

    def test_create_run_unfinished(self):
        """Test _create_run raises AssertionError when run creation is not finished."""
        with self.assertRaises(AssertionError) as context:
            self.run_creator._create_run()
        self.assertEqual(str(context.exception), "Cannot create run from unfinished run creation")

    def test_get_creation_missing_extra_info(self):
        """Test _get_creation_missing_extra_info method."""
        progress = self.run_creator._get_creation_missing_extra_info()
        
        self.assertTrue(progress.has_all_info)
        self.assertEqual(progress.run_creation, self.mock_run_creation)


if __name__ == '__main__':
    unittest.main() 