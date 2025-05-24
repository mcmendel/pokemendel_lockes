"""Tests for the base run creator functionality.

This module contains tests for the RunCreator and RunCreationProgress classes,
verifying their behavior in managing the run creation process.
"""

import unittest
from unittest.mock import patch, MagicMock
from core.lockes.base.run_creator import RunCreator, RunCreationProgress, InfoKeys
from models.run_creation import RunCreation


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
        self.run_name = "test_run"
        self.mock_run_creation = RunCreation(name=self.run_name)
        
        # Mock the database functions
        self.fetch_patcher = patch('core.lockes.base.run_creator.fetch_or_create_run_creation')
        self.update_patcher = patch('core.lockes.base.run_creator.update_run_creation')
        
        self.mock_fetch = self.fetch_patcher.start()
        self.mock_update = self.update_patcher.start()
        
        self.mock_fetch.return_value = self.mock_run_creation
        self.run_creator = RunCreator(self.run_name)

    def tearDown(self):
        """Clean up test fixtures."""
        self.fetch_patcher.stop()
        self.update_patcher.stop()

    def test_init(self):
        """Test RunCreator initialization."""
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.assertEqual(self.run_creator.run_creation, self.mock_run_creation)

    def test_get_progress_finished(self):
        """Test get_progress when run is finished."""
        self.mock_run_creation.finished = True
        progress = self.run_creator.get_progress()
        
        self.assertTrue(progress.has_all_info)
        self.assertEqual(progress.run_creation, self.mock_run_creation)

    def test_get_progress_missing_locke(self):
        """Test get_progress when locke is missing."""
        self.mock_run_creation.finished = False
        self.mock_run_creation.locke = None
        progress = self.run_creator.get_progress()
        
        self.assertFalse(progress.has_all_info)
        self.assertEqual(progress.missing_key, InfoKeys.LOCKE)

    def test_get_progress_missing_game(self):
        """Test get_progress when game is missing."""
        self.mock_run_creation.finished = False
        self.mock_run_creation.locke = "test_locke"
        self.mock_run_creation.game = None
        progress = self.run_creator.get_progress()
        
        self.assertFalse(progress.has_all_info)
        self.assertEqual(progress.missing_key, InfoKeys.GAME)

    def test_get_progress_missing_randomized(self):
        """Test get_progress when randomized is missing."""
        self.mock_run_creation.finished = False
        self.mock_run_creation.locke = "test_locke"
        self.mock_run_creation.game = "test_game"
        self.mock_run_creation.randomized = None
        progress = self.run_creator.get_progress()
        
        self.assertFalse(progress.has_all_info)
        self.assertEqual(progress.missing_key, InfoKeys.RANDOMIZE)

    def test_get_progress_missing_duplicate(self):
        """Test get_progress when duplicate_clause is missing."""
        self.mock_run_creation.finished = False
        self.mock_run_creation.locke = "test_locke"
        self.mock_run_creation.game = "test_game"
        self.mock_run_creation.randomized = True
        self.mock_run_creation.duplicate_clause = None
        progress = self.run_creator.get_progress()
        
        self.assertFalse(progress.has_all_info)
        self.assertEqual(progress.missing_key, InfoKeys.DUPLICATE)

    def test_update_progress_locke(self):
        """Test update_progress for locke field."""
        self.run_creator.update_progress(InfoKeys.LOCKE, "test_locke")
        
        self.assertEqual(self.mock_run_creation.locke, "test_locke")
        self.assertEqual(self.mock_run_creation.extra_info[InfoKeys.LOCKE], "test_locke")
        self.mock_update.assert_called_once_with(self.mock_run_creation)

    def test_update_progress_game(self):
        """Test update_progress for game field."""
        self.run_creator.update_progress(InfoKeys.GAME, "test_game")
        
        self.assertEqual(self.mock_run_creation.game, "test_game")
        self.assertEqual(self.mock_run_creation.extra_info[InfoKeys.GAME], "test_game")
        self.mock_update.assert_called_once_with(self.mock_run_creation)

    def test_update_progress_randomized(self):
        """Test update_progress for randomized field."""
        self.run_creator.update_progress(InfoKeys.RANDOMIZE, "true")
        
        self.assertTrue(self.mock_run_creation.randomized)
        self.assertEqual(self.mock_run_creation.extra_info[InfoKeys.RANDOMIZE], "true")
        self.mock_update.assert_called_once_with(self.mock_run_creation)

    def test_update_progress_duplicate(self):
        """Test update_progress for duplicate_clause field."""
        self.run_creator.update_progress(InfoKeys.DUPLICATE, "true")
        
        self.assertTrue(self.mock_run_creation.duplicate_clause)
        self.assertEqual(self.mock_run_creation.extra_info[InfoKeys.DUPLICATE], "true")
        self.mock_update.assert_called_once_with(self.mock_run_creation)

    def test_finish_creation(self):
        """Test finish_creation method."""
        self.run_creator.finish_creation()
        
        self.assertTrue(self.mock_run_creation.finished)
        self.mock_update.assert_called_once_with(self.mock_run_creation)

    def test_get_creation_missing_extra_info(self):
        """Test _get_creation_missing_extra_info method."""
        progress = self.run_creator._get_creation_missing_extra_info()
        
        self.assertTrue(progress.has_all_info)
        self.assertEqual(progress.run_creation, self.mock_run_creation)


if __name__ == '__main__':
    unittest.main() 