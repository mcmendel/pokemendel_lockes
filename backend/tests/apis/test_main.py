"""Tests for the main API functions."""

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from models.run import Run
from apis.main import list_runs_api
from responses.list_runs import ListRuns


class TestListRunsApi(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.test_run = Run(
            run_id="test_run_1",
            created_date=datetime.now(),
            name="Test Run",
            locke="nuzlocke",
            game="red",
            gen=1,
            randomized=True,
            party=["pikachu", "charizard"],
            box=["bulbasaur", "squirtle"],
            battles=[{"type": "gym", "won": True, "rival": "Gary"}],
            encounters=[{"pokemon": "pikachu", "route": "route1", "status": "caught"}],
            locke_extra_info={"difficulty": "hard"},
            restarts=0,
            duplicate_clause=False,
            finished=False,
            starter="pikachu"
        )

    @patch('apis.main.list_runs')
    def test_list_runs_api_success(self, mock_list_runs):
        """Test that list_runs_api returns a list of ListRuns objects."""
        # Arrange
        mock_list_runs.return_value = [self.test_run]
        
        # Act
        result = list_runs_api()
        
        # Assert
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], ListRuns)
        self.assertEqual(result[0].run_id, "test_run_1")
        self.assertEqual(result[0].run_name, "Test Run")
        self.assertEqual(result[0].game_name, "red")
        self.assertEqual(result[0].locke_name, "nuzlocke")
        self.assertEqual(result[0].randomized, True)
        self.assertEqual(result[0].starter, "pikachu")
        self.assertEqual(result[0].num_deaths, 0)
        self.assertEqual(result[0].num_pokemons, 2)  # Only box Pokemon
        self.assertEqual(result[0].num_gyms, 1)
        self.assertEqual(result[0].num_restarts, 0)
        self.assertEqual(result[0].finished, False)
        mock_list_runs.assert_called_once()

    @patch('apis.main.list_runs')
    def test_list_runs_api_empty(self, mock_list_runs):
        """Test that list_runs_api returns an empty list when no runs exist."""
        # Arrange
        mock_list_runs.return_value = []
        
        # Act
        result = list_runs_api()
        
        # Assert
        self.assertEqual(len(result), 0)
        mock_list_runs.assert_called_once()

    @patch('apis.main.list_runs')
    def test_list_runs_api_error(self, mock_list_runs):
        """Test that list_runs_api propagates database errors."""
        # Arrange
        mock_list_runs.side_effect = Exception("Database error")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            list_runs_api()
        self.assertEqual(str(context.exception), "Database error")
        mock_list_runs.assert_called_once()


if __name__ == '__main__':
    unittest.main() 