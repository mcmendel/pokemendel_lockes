"""Tests for the run creation API."""

import unittest
from unittest.mock import patch, MagicMock
from models.run_creation import RunCreation
from apis.run_creation import start_run_creation
from apis.exceptions import RunAlreadyExistsError, InvalidLockeTypeError
from games import Game
from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.utils.definitions.regions import Regions
from definitions import GymTrainer, EliteTrainer, TrainerPokemon, Pokemon, PokemonMetadata


class TestStartRunCreation(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.run_name = "test_run"
        self.locke_type = "nuzlocke"
        self.duplicate_clause = False
        self.is_randomized = True
        
        # Mock the locke instances
        self.mock_locke = MagicMock()
        self.mock_locke.min_gen = 1
        self.locke_patcher = patch('apis.run_creation.LOCKE_INSTANCES', {
            'nuzlocke': self.mock_locke,
            'wonderlocke': MagicMock()
        })
        self.mock_lockes = self.locke_patcher.start()
        
        # Mock the database functions
        self.fetch_patcher = patch('apis.run_creation.fetch_run_creation')
        self.update_patcher = patch('apis.run_creation.update_run_creation')
        self.games_patcher = patch('apis.run_creation.get_games_from_gen')
        
        self.mock_fetch = self.fetch_patcher.start()
        self.mock_update = self.update_patcher.start()
        self.mock_games = self.games_patcher.start()
        
        # Create mock games with all required fields
        mock_starter = Pokemon(
            name="Bulbasaur",
            gen=1,
            types=[Types.GRASS, Types.POISON],
            metadata=PokemonMetadata(id="bulbasaur", nickname="Bulbasaur")
        )
        mock_gym = GymTrainer(
            leader="Brock",
            type=Types.ROCK,
            pokemons=[TrainerPokemon("Geodude", 12)],
            location="Pewter City",
            badge="Boulder Badge"
        )
        mock_elite4 = EliteTrainer(
            leader="Lorelei",
            type=Types.ICE,
            pokemons=[TrainerPokemon("Dewgong", 54)]
        )
        
        mock_game = Game(
            name="red",
            gen=1,
            region=Regions.KANTO,
            gyms=[mock_gym],
            elite4=[mock_elite4],
            routes=["Route 1", "Route 2"],
            starters=[mock_starter],
            important_battles=["Route 22 - Rival (9)"],
            encounters={"Route 1": {"Pidgey", "Rattata"}}
        )
        
        # Set up default mock returns
        self.mock_fetch.return_value = None  # No existing run
        self.mock_games.return_value = [mock_game]

    def tearDown(self):
        """Clean up test fixtures."""
        self.locke_patcher.stop()
        self.fetch_patcher.stop()
        self.update_patcher.stop()
        self.games_patcher.stop()

    def test_start_run_creation_success(self):
        """Test successful run creation."""
        # Act
        games = start_run_creation(
            self.run_name,
            self.locke_type,
            self.duplicate_clause,
            self.is_randomized
        )
        
        # Assert
        self.assertEqual(games, ["red"])
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_update.assert_called_once()
        self.mock_games.assert_called_once_with(1)
        
        # Verify the run creation object
        call_args = self.mock_update.call_args[0]
        run_creation = call_args[0]
        self.assertIsInstance(run_creation, RunCreation)
        self.assertEqual(run_creation.name, self.run_name)
        self.assertEqual(run_creation.locke, self.locke_type)
        self.assertEqual(run_creation.duplicate_clause, self.duplicate_clause)
        self.assertEqual(run_creation.randomized, self.is_randomized)
        self.assertFalse(run_creation.finished)

    def test_start_run_creation_existing_run(self):
        """Test that RunAlreadyExistsError is raised when run already exists."""
        # Arrange
        self.mock_fetch.return_value = RunCreation(name=self.run_name)
        
        # Act & Assert
        with self.assertRaises(RunAlreadyExistsError):
            start_run_creation(
                self.run_name,
                self.locke_type,
                self.duplicate_clause,
                self.is_randomized
            )
        
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_update.assert_not_called()
        self.mock_games.assert_not_called()

    def test_start_run_creation_invalid_locke(self):
        """Test that InvalidLockeTypeError is raised for invalid locke type."""
        # Act & Assert
        with self.assertRaises(InvalidLockeTypeError) as context:
            start_run_creation(
                self.run_name,
                "invalid_locke",
                self.duplicate_clause,
                self.is_randomized
            )
        
        self.assertEqual(
            str(context.exception),
            "Invalid locke type: invalid_locke. Available types: ['nuzlocke', 'wonderlocke']"
        )
        
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_update.assert_not_called()
        self.mock_games.assert_not_called()

    def test_start_run_creation_database_error(self):
        """Test that database errors are propagated."""
        # Arrange
        self.mock_fetch.side_effect = Exception("Database error")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            start_run_creation(
                self.run_name,
                self.locke_type,
                self.duplicate_clause,
                self.is_randomized
            )
        
        self.assertEqual(str(context.exception), "Database error")
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_update.assert_not_called()
        self.mock_games.assert_not_called()

    def test_start_run_creation_update_error(self):
        """Test that update errors are propagated."""
        # Arrange
        self.mock_update.side_effect = Exception("Update error")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            start_run_creation(
                self.run_name,
                self.locke_type,
                self.duplicate_clause,
                self.is_randomized
            )
        
        self.assertEqual(str(context.exception), "Update error")
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_update.assert_called_once()
        self.mock_games.assert_not_called()


if __name__ == '__main__':
    unittest.main() 