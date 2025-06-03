"""Tests for the run creation API."""

import unittest
from unittest.mock import patch, MagicMock
from models.run_creation import RunCreation
from apis.run_creation import start_run_creation, continue_run_creation
from apis.exceptions import RunAlreadyExistsError, InvalidLockeTypeError, RunNotFoundError, InvalidGameError
from games import Game, get_game
from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.utils.definitions.regions import Regions
from definitions import GymTrainer, EliteTrainer, TrainerPokemon, Pokemon, PokemonMetadata
from core.run import Run
from core.party import Party
from core.box import Box
from datetime import datetime


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


class TestContinueRunCreation(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.run_name = "test_run"
        self.locke_type = "nuzlocke"
        self.game_name = "red"
        
        # Create a mock run creation
        self.run_creation = RunCreation(
            name=self.run_name,
            locke=self.locke_type,
            game=self.game_name,
            duplicate_clause=False,
            randomized=True,
            extra_info={"difficulty": "hard"}
        )
        
        # Mock the database functions
        self.fetch_patcher = patch('apis.run_creation.fetch_run_creation')
        self.update_patcher = patch('models.run_creation.update_run_creation')
        self.save_patcher = patch('apis.run_creation.save_run')
        self.get_game_patcher = patch('apis.run_creation.get_game')
        self.get_run_creator_patcher = patch('apis.run_creation.get_run_creator_class')
        
        self.mock_fetch = self.fetch_patcher.start()
        self.mock_update = self.update_patcher.start()
        self.mock_save = self.save_patcher.start()
        self.mock_get_game = self.get_game_patcher.start()
        self.mock_get_run_creator = self.get_run_creator_patcher.start()
        
        # Set up default mock returns
        self.mock_fetch.return_value = self.run_creation
        
        # Mock game
        mock_game = MagicMock(spec=Game)
        mock_game.name = self.game_name
        mock_game.gen = 1
        self.mock_get_game.return_value = mock_game
        
        # Mock run creator
        mock_creator = MagicMock()
        mock_creator.get_progress.return_value = MagicMock(has_all_info=True)
        mock_creator.finish_creation.return_value = Run(
            id=self.run_name,
            run_name=self.run_name,
            creation_date=datetime.now(),
            party=Party(pokemons=[]),
            box=Box(pokemons=[])
        )
        self.mock_get_run_creator.return_value = lambda x: mock_creator

    def tearDown(self):
        """Clean up test fixtures."""
        self.fetch_patcher.stop()
        self.update_patcher.stop()
        self.save_patcher.stop()
        self.get_game_patcher.stop()
        self.get_run_creator_patcher.stop()

    def test_continue_run_creation_success(self):
        """Test successful run creation continuation."""
        # Act
        response = continue_run_creation(self.run_name, "GAME", "red")
        
        # Assert
        self.assertTrue(response["finished"])
        self.assertEqual(response["run_id"], self.run_name)
        self.assertIsNone(response["next_key"])
        self.assertEqual(response["potential_values"], [])
        
        # Verify database calls
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_get_game.assert_called_once_with(self.game_name)
        self.mock_save.assert_called_once()
        
        # Verify saved run
        saved_run = self.mock_save.call_args[0][0]
        self.assertEqual(saved_run.run_id, self.run_name)
        self.assertEqual(saved_run.name, self.run_name)
        self.assertEqual(saved_run.locke, self.locke_type)
        self.assertEqual(saved_run.game, self.game_name)
        self.assertEqual(saved_run.gen, 1)
        self.assertTrue(saved_run.randomized)
        self.assertFalse(saved_run.duplicate_clause)
        self.assertEqual(saved_run.party, [])
        self.assertEqual(saved_run.box, [])
        self.assertEqual(saved_run.battles, [])
        self.assertEqual(saved_run.encounters, [])
        self.assertEqual(saved_run.locke_extra_info, {"difficulty": "hard"})
        self.assertEqual(saved_run.restarts, 0)
        self.assertFalse(saved_run.finished)
        self.assertIsNone(saved_run.starter)

    def test_continue_run_creation_not_found(self):
        """Test that RunNotFoundError is raised when run doesn't exist."""
        # Arrange
        self.mock_fetch.return_value = None
        
        # Act & Assert
        with self.assertRaises(RunNotFoundError) as context:
            continue_run_creation(self.run_name, "GAME", "red")
        
        self.assertEqual(str(context.exception), f"Run '{self.run_name}' not found")
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_get_game.assert_not_called()
        self.mock_save.assert_not_called()

    def test_continue_run_creation_invalid_game(self):
        """Test that InvalidGameError is raised for invalid game."""
        # Arrange
        self.mock_get_game.side_effect = StopIteration()
        
        # Act & Assert
        with self.assertRaises(InvalidGameError) as context:
            continue_run_creation(self.run_name, "GAME", "red")
        
        self.assertEqual(str(context.exception), "Invalid game name: red")
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_get_game.assert_called_once_with("red")
        self.mock_save.assert_not_called()

    def test_continue_run_creation_database_error(self):
        """Test that database errors are propagated."""
        # Arrange
        self.mock_fetch.side_effect = Exception("Database error")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            continue_run_creation(self.run_name, "GAME", "red")
        
        self.assertEqual(str(context.exception), "Database error")
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_get_game.assert_not_called()
        self.mock_save.assert_not_called()

    def test_continue_run_creation_save_error(self):
        """Test that save errors are propagated."""
        # Arrange
        self.mock_save.side_effect = Exception("Save error")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            continue_run_creation(self.run_name, "GAME", "red")
        
        self.assertEqual(str(context.exception), "Save error")
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_get_game.assert_called_once_with(self.game_name)
        self.mock_save.assert_called_once()

    def test_continue_run_creation_not_finished(self):
        """Test that run creation continues when not finished."""
        # Arrange
        mock_creator = MagicMock()
        progress_mock = MagicMock()
        progress_mock.has_all_info = False
        progress_mock.missing_key = "STARTER"
        progress_mock.missing_key_options = ["bulbasaur", "charmander"]
        mock_creator.get_progress.return_value = progress_mock
        self.mock_get_run_creator.return_value = lambda x: mock_creator
        
        # Act
        response = continue_run_creation(self.run_name, "STARTER", "bulbasaur")
        
        # Assert
        self.assertFalse(response["finished"])
        self.assertEqual(response["run_id"], self.run_name)  # run_id should be included even when not finished
        self.assertEqual(response["next_key"], "STARTER")
        self.assertEqual(response["potential_values"], ["bulbasaur", "charmander"])
        
        # Verify database calls
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_get_game.assert_not_called()
        self.mock_save.assert_not_called()

    def test_continue_run_creation_finish_error(self):
        """Test that assertion errors from finish_creation are propagated."""
        # Arrange
        mock_creator = MagicMock()
        mock_creator.get_progress.return_value = MagicMock(has_all_info=True)
        mock_creator.finish_creation.side_effect = AssertionError("Missing required data")
        self.mock_get_run_creator.return_value = lambda x: mock_creator
        
        # Act & Assert
        with self.assertRaises(AssertionError) as context:
            continue_run_creation(self.run_name, "GAME", "red")
        
        self.assertEqual(str(context.exception), "Missing required data")
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_get_game.assert_not_called()  # get_game is called after finish_creation, so it shouldn't be called
        self.mock_save.assert_not_called()

    def test_continue_run_creation_progress_error(self):
        """Test that assertion errors from get_progress are propagated."""
        # Arrange
        mock_creator = MagicMock()
        mock_creator.get_progress.side_effect = AssertionError("Invalid progress state")
        self.mock_get_run_creator.return_value = lambda x: mock_creator
        
        # Act & Assert
        with self.assertRaises(AssertionError) as context:
            continue_run_creation(self.run_name, "GAME", "red")
        
        self.assertEqual(str(context.exception), "Invalid progress state")
        self.mock_fetch.assert_called_once_with(self.run_name)
        self.mock_get_game.assert_not_called()
        self.mock_save.assert_not_called()


if __name__ == '__main__':
    unittest.main() 