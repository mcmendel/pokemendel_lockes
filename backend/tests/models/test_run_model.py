"""Tests for the Run model and its database operations."""

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from models.run import Run, save_run, update_run, fetch_run, list_runs, delete_run


class TestRun(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.valid_run = Run(
            run_id="test_run_1",
            created_date=datetime.now(),
            name="Test Run",
            locke="nuzlocke",
            game="red",
            gen=1,
            randomized=True,
            party=["pikachu", "charizard"],
            box=["bulbasaur", "squirtle"],
            battles=[{"won": True, "rival": "Gary"}],
            encounters=[{"pokemon": "pikachu", "route": "route1", "status": "caught"}],
            locke_extra_info={"difficulty": "hard"},
            restarts=0,
            duplicate_clause=False,
            finished=False,
            starter="pikachu"
        )

    def test_init_with_valid_data(self):
        """Test Run initialization with valid data."""
        self.assertEqual(self.valid_run.run_id, "test_run_1")
        self.assertEqual(self.valid_run.name, "Test Run")
        self.assertEqual(self.valid_run.locke, "nuzlocke")
        self.assertEqual(self.valid_run.game, "red")
        self.assertEqual(self.valid_run.gen, 1)
        self.assertTrue(self.valid_run.randomized)
        self.assertEqual(self.valid_run.party, ["pikachu", "charizard"])
        self.assertEqual(self.valid_run.box, ["bulbasaur", "squirtle"])
        self.assertEqual(self.valid_run.battles, [{"won": True, "rival": "Gary"}])
        self.assertEqual(self.valid_run.encounters, [{"pokemon": "pikachu", "route": "route1", "status": "caught"}])
        self.assertEqual(self.valid_run.locke_extra_info, {"difficulty": "hard"})
        self.assertEqual(self.valid_run.restarts, 0)
        self.assertFalse(self.valid_run.duplicate_clause)
        self.assertFalse(self.valid_run.finished)
        self.assertEqual(self.valid_run.starter, "pikachu")

    def test_init_with_empty_id(self):
        """Test Run initialization with empty ID raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Run(
                run_id="",
                created_date=datetime.now(),
                name="Test Run",
                locke="nuzlocke",
                game="red",
                gen=1,
                randomized=True
            )
        self.assertEqual(str(context.exception), "Run ID cannot be empty")

    def test_init_with_empty_name(self):
        """Test Run initialization with empty name raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Run(
                run_id="test_run_1",
                created_date=datetime.now(),
                name="",
                locke="nuzlocke",
                game="red",
                gen=1,
                randomized=True
            )
        self.assertEqual(str(context.exception), "Run name cannot be empty")

    def test_init_with_future_date(self):
        """Test Run initialization with future date raises ValueError."""
        future_date = datetime.now() + timedelta(days=1)
        with self.assertRaises(ValueError) as context:
            Run(
                run_id="test_run_1",
                created_date=future_date,
                name="Test Run",
                locke="nuzlocke",
                game="red",
                gen=1,
                randomized=True
            )
        self.assertEqual(str(context.exception), "Creation date cannot be in the future")

    def test_init_with_negative_restarts(self):
        """Test Run initialization with negative restarts raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Run(
                run_id="test_run_1",
                created_date=datetime.now(),
                name="Test Run",
                locke="nuzlocke",
                game="red",
                gen=1,
                randomized=True,
                restarts=-1
            )
        self.assertEqual(str(context.exception), "Restarts cannot be negative")

    def test_to_dict(self):
        """Test that to_dict returns the correct dictionary structure."""
        run_dict = self.valid_run.to_dict()
        self.assertEqual(run_dict["_id"], "test_run_1")
        self.assertEqual(run_dict["name"], "Test Run")
        self.assertEqual(run_dict["locke"], "nuzlocke")
        self.assertEqual(run_dict["game"], "red")
        self.assertEqual(run_dict["gen"], 1)
        self.assertTrue(run_dict["randomized"])
        self.assertEqual(run_dict["party"], ["pikachu", "charizard"])
        self.assertEqual(run_dict["box"], ["bulbasaur", "squirtle"])
        self.assertEqual(run_dict["battles"], [{"won": True, "rival": "Gary"}])
        self.assertEqual(run_dict["encounters"], [{"pokemon": "pikachu", "route": "route1", "status": "caught"}])
        self.assertEqual(run_dict["locke_extra_info"], {"difficulty": "hard"})
        self.assertEqual(run_dict["restarts"], 0)
        self.assertFalse(run_dict["duplicate_clause"])
        self.assertFalse(run_dict["finished"])
        self.assertEqual(run_dict["starter"], "pikachu")

    def test_from_dict(self):
        """Test that from_dict creates a valid Run instance."""
        run_dict = {
            "_id": "test_run_1",
            "created_date": datetime.now(),
            "name": "Test Run",
            "locke": "nuzlocke",
            "game": "red",
            "gen": 1,
            "randomized": True,
            "party": ["pikachu", "charizard"],
            "box": ["bulbasaur", "squirtle"],
            "battles": [{"won": True, "rival": "Gary"}],
            "encounters": [{"pokemon": "pikachu", "route": "route1", "status": "caught"}],
            "locke_extra_info": {"difficulty": "hard"},
            "restarts": 0,
            "duplicate_clause": False,
            "finished": False,
            "starter": "pikachu"
        }
        run = Run.from_dict(run_dict)
        self.assertEqual(run.run_id, "test_run_1")
        self.assertEqual(run.name, "Test Run")
        self.assertEqual(run.locke, "nuzlocke")
        self.assertEqual(run.game, "red")
        self.assertEqual(run.gen, 1)
        self.assertTrue(run.randomized)
        self.assertEqual(run.party, ["pikachu", "charizard"])
        self.assertEqual(run.box, ["bulbasaur", "squirtle"])
        self.assertEqual(run.battles, [{"won": True, "rival": "Gary"}])
        self.assertEqual(run.encounters, [{"pokemon": "pikachu", "route": "route1", "status": "caught"}])
        self.assertEqual(run.locke_extra_info, {"difficulty": "hard"})
        self.assertEqual(run.restarts, 0)
        self.assertFalse(run.duplicate_clause)
        self.assertFalse(run.finished)
        self.assertEqual(run.starter, "pikachu")


class TestRunDatabaseOperations(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.test_run = Run(
            run_id="test_run_1",
            created_date=datetime.now(),
            name="Test Run",
            locke="nuzlocke",
            game="red",
            gen=1,
            randomized=True
        )
        self.patcher = patch('models.run.insert_document')
        self.mock_insert = self.patcher.start()
        self.patcher2 = patch('models.run.update_document_by_id')
        self.mock_update = self.patcher2.start()
        self.patcher3 = patch('models.run.fetch_documents_by_query')
        self.mock_fetch = self.patcher3.start()
        self.patcher4 = patch('models.run.delete_documents_by_query')
        self.mock_delete = self.patcher4.start()

    def tearDown(self):
        """Clean up test fixtures."""
        self.patcher.stop()
        self.patcher2.stop()
        self.patcher3.stop()
        self.patcher4.stop()

    def test_save_run(self):
        """Test that save_run calls insert_document correctly."""
        save_run(self.test_run)
        self.mock_insert.assert_called_once()
        call_args = self.mock_insert.call_args[0]
        self.assertEqual(call_args[1], "runs")
        self.assertEqual(call_args[2]["_id"], "test_run_1")

    def test_save_run_error(self):
        """Test that save_run handles errors correctly."""
        self.mock_insert.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            save_run(self.test_run)
        self.assertEqual(str(context.exception), "Failed to save run: Database error")

    def test_update_run(self):
        """Test that update_run calls update_document_by_id correctly."""
        update_run(self.test_run)
        self.mock_update.assert_called_once()
        call_args = self.mock_update.call_args[0]
        self.assertEqual(call_args[1], "runs")
        self.assertEqual(call_args[2], "test_run_1")
        self.assertEqual(call_args[3]["_id"], "test_run_1")

    def test_update_run_error(self):
        """Test that update_run handles errors correctly."""
        self.mock_update.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            update_run(self.test_run)
        self.assertEqual(str(context.exception), "Failed to update run: Database error")

    def test_fetch_run(self):
        """Test that fetch_run returns a Run instance when found."""
        self.mock_fetch.return_value = [self.test_run.to_dict()]
        run = fetch_run("test_run_1")
        self.assertEqual(run.run_id, "test_run_1")
        self.assertEqual(run.name, "Test Run")
        self.mock_fetch.assert_called_once()

    def test_fetch_run_not_found(self):
        """Test that fetch_run returns None when run is not found."""
        self.mock_fetch.return_value = []
        run = fetch_run("test_run_1")
        self.assertIsNone(run)
        self.mock_fetch.assert_called_once()

    def test_fetch_run_error(self):
        """Test that fetch_run handles errors correctly."""
        self.mock_fetch.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            fetch_run("test_run_1")
        self.assertEqual(str(context.exception), "Failed to fetch run: Database error")

    def test_list_runs(self):
        """Test that list_runs returns a list of Run instances."""
        self.mock_fetch.return_value = [self.test_run.to_dict()]
        runs = list_runs()
        self.assertEqual(len(runs), 1)
        self.assertEqual(runs[0].run_id, "test_run_1")
        self.mock_fetch.assert_called_once()

    def test_list_runs_with_query(self):
        """Test that list_runs filters results with query."""
        query = {"name": "Test Run"}
        self.mock_fetch.return_value = [self.test_run.to_dict()]
        runs = list_runs(query)
        self.assertEqual(len(runs), 1)
        self.assertEqual(runs[0].name, "Test Run")
        self.mock_fetch.assert_called_once()

    def test_list_runs_error(self):
        """Test that list_runs handles errors correctly."""
        self.mock_fetch.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            list_runs()
        self.assertEqual(str(context.exception), "Failed to list runs: Database error")

    def test_delete_run(self):
        """Test that delete_run calls delete_documents_by_query correctly."""
        delete_run("test_run_1")
        self.mock_delete.assert_called_once()
        call_args = self.mock_delete.call_args[0]
        self.assertEqual(call_args[1], "runs")
        self.assertEqual(call_args[2], {"_id": "test_run_1"})

    def test_delete_run_error(self):
        """Test that delete_run handles errors correctly."""
        self.mock_delete.side_effect = Exception("Database error")
        with self.assertRaises(Exception) as context:
            delete_run("test_run_1")
        self.assertEqual(str(context.exception), "Failed to delete run: Database error")


if __name__ == '__main__':
    unittest.main() 