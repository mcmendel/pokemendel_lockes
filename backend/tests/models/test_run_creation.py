import unittest
from unittest.mock import patch, MagicMock
from models.run_creation import RunCreation, save_run_creation, update_run_creation, fetch_or_create_run_creation, fetch_run_creation


class TestRunCreation(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.valid_run = RunCreation(
            name="test_run",
            locke="nuzlocke",
            game="red",
            randomized=True,
            duplicate_clause=False,
            extra_info={"difficulty": "hard"}
        )

    def test_run_creation_initialization(self):
        """Test that RunCreation can be initialized with valid data."""
        self.assertEqual(self.valid_run.name, "test_run")
        self.assertEqual(self.valid_run.locke, "nuzlocke")
        self.assertEqual(self.valid_run.game, "red")
        self.assertTrue(self.valid_run.randomized)
        self.assertFalse(self.valid_run.duplicate_clause)
        self.assertEqual(self.valid_run.extra_info, {"difficulty": "hard"})

    def test_run_creation_minimal(self):
        """Test that RunCreation can be initialized with only required fields."""
        minimal_run = RunCreation(name="minimal_run")
        self.assertEqual(minimal_run.name, "minimal_run")
        self.assertIsNone(minimal_run.locke)
        self.assertIsNone(minimal_run.game)
        self.assertIsNone(minimal_run.randomized)
        self.assertIsNone(minimal_run.duplicate_clause)
        self.assertEqual(minimal_run.extra_info, {})

    def test_run_creation_empty_name(self):
        """Test that RunCreation raises ValueError for empty name."""
        with self.assertRaises(ValueError) as context:
            RunCreation(name="")
        self.assertEqual(str(context.exception), "Run name cannot be empty")

    def test_run_creation_invalid_extra_info(self):
        """Test that RunCreation raises TypeError for invalid extra_info."""
        with self.assertRaises(TypeError) as context:
            RunCreation(name="test", extra_info="not_a_dict")
        self.assertEqual(str(context.exception), "extra_info must be a dictionary")

    def test_to_dict(self):
        """Test that to_dict returns the correct dictionary structure."""
        run_dict = self.valid_run.to_dict()
        self.assertEqual(run_dict["_id"], "test_run")
        self.assertEqual(run_dict["name"], "test_run")
        self.assertEqual(run_dict["locke"], "nuzlocke")
        self.assertEqual(run_dict["game"], "red")
        self.assertTrue(run_dict["randomized"])
        self.assertFalse(run_dict["duplicate_clause"])
        self.assertEqual(run_dict["extra_info"], {"difficulty": "hard"})

    def test_from_dict_valid(self):
        """Test that from_dict creates a valid RunCreation instance."""
        run_dict = {
            "_id": "test_run",
            "name": "test_run",
            "locke": "nuzlocke",
            "game": "red",
            "randomized": True,
            "duplicate_clause": False,
            "extra_info": {"difficulty": "hard"}
        }
        run = RunCreation.from_dict(run_dict)
        self.assertEqual(run.name, "test_run")
        self.assertEqual(run.locke, "nuzlocke")
        self.assertEqual(run.game, "red")
        self.assertTrue(run.randomized)
        self.assertFalse(run.duplicate_clause)
        self.assertEqual(run.extra_info, {"difficulty": "hard"})

    def test_from_dict_missing_name(self):
        """Test that from_dict raises ValueError for missing name."""
        with self.assertRaises(ValueError) as context:
            RunCreation.from_dict({"locke": "nuzlocke"})
        self.assertEqual(str(context.exception), "run_dict must contain a 'name' field")

    def test_from_dict_invalid_type(self):
        """Test that from_dict raises TypeError for invalid input type."""
        with self.assertRaises(TypeError) as context:
            RunCreation.from_dict("not_a_dict")
        self.assertEqual(str(context.exception), "run_dict must be a dictionary")


class TestRunCreationDatabaseOperations(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.test_run = RunCreation(name="test_run")
        self.patcher = patch('models.run_creation.insert_document')
        self.mock_insert = self.patcher.start()
        self.patcher2 = patch('models.run_creation.update_document_by_id')
        self.mock_update = self.patcher2.start()
        self.patcher3 = patch('models.run_creation.fetch_documents_by_query')
        self.mock_fetch = self.patcher3.start()

    def tearDown(self):
        """Clean up test fixtures."""
        self.patcher.stop()
        self.patcher2.stop()
        self.patcher3.stop()

    def test_save_run_creation(self):
        """Test that save_run_creation calls insert_document correctly."""
        save_run_creation(self.test_run)
        self.mock_insert.assert_called_once_with(
            "locke_manager",
            "run_creation",
            {
                "_id": "test_run",
                "name": "test_run",
                "locke": None,
                "game": None,
                "randomized": None,
                "duplicate_clause": None,
                "extra_info": {},
                "finished": False
            }
        )

    def test_save_run_creation_error(self):
        """Test that save_run_creation handles errors correctly."""
        self.mock_insert.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            save_run_creation(self.test_run)
        self.assertEqual(str(context.exception), "Failed to save run creation: Database error")

    def test_update_run_creation(self):
        """Test that update_run_creation calls update_document_by_id correctly."""
        update_run_creation(self.test_run)
        self.mock_update.assert_called_once_with(
            "locke_manager",
            "run_creation",
            "test_run",
            {
                "_id": "test_run",
                "name": "test_run",
                "locke": None,
                "game": None,
                "randomized": None,
                "duplicate_clause": None,
                "extra_info": {},
                "finished": False
            }
        )

    def test_update_run_creation_error(self):
        """Test that update_run_creation handles errors correctly."""
        self.mock_update.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            update_run_creation(self.test_run)
        self.assertEqual(str(context.exception), "Failed to update run creation: Database error")

    def test_fetch_or_create_run_creation_existing(self):
        """Test that fetch_or_create_run_creation returns existing run."""
        self.mock_fetch.return_value = [{"name": "test_run", "locke": "nuzlocke"}]
        run = fetch_or_create_run_creation("test_run")
        self.assertEqual(run.name, "test_run")
        self.assertEqual(run.locke, "nuzlocke")
        self.mock_fetch.assert_called_once()

    def test_fetch_or_create_run_creation_new(self):
        """Test that fetch_or_create_run_creation creates new run if none exists."""
        self.mock_fetch.return_value = []
        run = fetch_or_create_run_creation("test_run")
        self.assertEqual(run.name, "test_run")
        self.assertIsNone(run.locke)
        self.mock_fetch.assert_called_once()
        self.mock_insert.assert_called_once()

    def test_fetch_or_create_run_creation_error(self):
        """Test that fetch_or_create_run_creation handles errors correctly."""
        self.mock_fetch.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            fetch_or_create_run_creation("test_run")
        self.assertEqual(str(context.exception), "Failed to fetch or create run creation: Database error")

    def test_fetch_run_creation_success(self):
        """Test that fetch_run_creation returns a RunCreation instance when found."""
        self.mock_fetch.return_value = [self.test_run.to_dict()]
        run = fetch_run_creation("test_run")
        self.assertEqual(run.name, "test_run")
        self.mock_fetch.assert_called_once_with(
            "locke_manager",
            "run_creation",
            {"name": "test_run"}
        )

    def test_fetch_run_creation_not_found(self):
        """Test that fetch_run_creation returns None when run is not found."""
        self.mock_fetch.return_value = []
        run = fetch_run_creation("test_run")
        self.assertIsNone(run)
        self.mock_fetch.assert_called_once()

    def test_fetch_run_creation_error(self):
        """Test that fetch_run_creation handles database errors correctly."""
        self.mock_fetch.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            fetch_run_creation("test_run")
        self.assertEqual(str(context.exception), "Failed to fetch run creation: Database error")
        self.mock_fetch.assert_called_once()

    def test_fetch_run_creation_multiple_results(self):
        """Test that fetch_run_creation raises AssertionError when multiple runs exist."""
        self.mock_fetch.return_value = [self.test_run.to_dict(), self.test_run.to_dict()]
        with self.assertRaises(AssertionError) as context:
            fetch_run_creation("test_run")
        self.assertEqual(str(context.exception), "Found 2 runs with name test_run, expected exactly 1")
        self.mock_fetch.assert_called_once()

    def test_fetch_run_creation_initializes_extra_info(self):
        """Test that fetch_run_creation initializes extra_info as empty dict if None."""
        run_dict = self.test_run.to_dict()
        run_dict["extra_info"] = None
        self.mock_fetch.return_value = [run_dict]
        run = fetch_run_creation("test_run")
        self.assertEqual(run.extra_info, {})
        self.mock_fetch.assert_called_once()


if __name__ == '__main__':
    unittest.main() 