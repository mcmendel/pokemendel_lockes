import unittest
from unittest.mock import patch, MagicMock
from app import app
import json

class TestRunApi(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.url = '/locke_manager/run'

    @patch('app.start_run_creation')
    def test_create_run_success(self, mock_start):
        mock_start.return_value = ['Red', 'Blue']
        data = {
            'run_name': 'TestRun',
            'locke_type': 'nuzlocke',
            'duplicate_clause': False,
            'is_randomized': False
        }
        resp = self.client.put(self.url, json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json(), ['Red', 'Blue'])
        mock_start.assert_called_once()

    @patch('app.start_run_creation')
    def test_create_run_missing_fields(self, mock_start):
        data = {'run_name': 'TestRun'}  # missing fields
        resp = self.client.put(self.url, json=data)
        self.assertEqual(resp.status_code, 400)
        self.assertIn('Missing required fields', resp.get_data(as_text=True))
        mock_start.assert_not_called()

    @patch('app.start_run_creation')
    def test_create_run_invalid_locke(self, mock_start):
        from apis.exceptions import InvalidLockeTypeError
        mock_start.side_effect = InvalidLockeTypeError('invalid', ['nuzlocke'])
        data = {
            'run_name': 'TestRun',
            'locke_type': 'invalid',
            'duplicate_clause': False,
            'is_randomized': False
        }
        resp = self.client.put(self.url, json=data)
        self.assertEqual(resp.status_code, 400)
        self.assertIn('Invalid locke type', resp.get_data(as_text=True))

    @patch('app.start_run_creation')
    def test_create_run_already_exists(self, mock_start):
        from apis.exceptions import RunAlreadyExistsError
        mock_start.side_effect = RunAlreadyExistsError()
        data = {
            'run_name': 'TestRun',
            'locke_type': 'nuzlocke',
            'duplicate_clause': False,
            'is_randomized': False
        }
        resp = self.client.put(self.url, json=data)
        self.assertEqual(resp.status_code, 409)
        self.assertIn('already exists', resp.get_data(as_text=True))

    @patch('app.continue_run_creation')
    def test_update_run_success(self, mock_continue):
        mock_continue.return_value = {
            'next_key': 'hello',
            'potential_values': [],
            'finished': False,
            'run_id': None
        }
        data = {'run_name': 'TestRun', 'key': 'GAME', 'val': 'Red'}
        resp = self.client.post(self.url, json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json(), {
            'next_key': 'hello',
            'potential_values': [],
            'finished': False,
            'run_id': None
        })
        mock_continue.assert_called_once()

    @patch('app.continue_run_creation')
    def test_update_run_finished(self, mock_continue):
        """Test update_run when run creation is complete."""
        mock_continue.return_value = {
            'next_key': None,
            'potential_values': [],
            'finished': True,
            'run_id': 'TestRun'
        }
        data = {'run_name': 'TestRun', 'key': 'STARTER', 'val': 'Bulbasaur'}
        resp = self.client.post(self.url, json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json(), {
            'next_key': None,
            'potential_values': [],
            'finished': True,
            'run_id': 'TestRun'
        })
        mock_continue.assert_called_once()

    @patch('app.continue_run_creation')
    def test_update_run_missing_run_name(self, mock_continue):
        data = {'key': 'GAME', 'val': 'Red'}
        resp = self.client.post(self.url, json=data)
        self.assertEqual(resp.status_code, 400)
        self.assertIn('Missing required field: run_name', resp.get_data(as_text=True))
        mock_continue.assert_not_called()

    @patch('app.continue_run_creation')
    def test_update_run_not_found(self, mock_continue):
        from apis.exceptions import RunNotFoundError
        mock_continue.side_effect = RunNotFoundError('TestRun')
        data = {'run_name': 'TestRun', 'key': 'GAME', 'val': 'Red'}
        resp = self.client.post(self.url, json=data)
        self.assertEqual(resp.status_code, 404)
        self.assertIn('not found', resp.get_data(as_text=True))

    @patch('app.continue_run_creation')
    def test_update_run_invalid_game(self, mock_continue):
        from apis.exceptions import InvalidGameError
        mock_continue.side_effect = InvalidGameError('NotAGame')
        data = {'run_name': 'TestRun', 'key': 'GAME', 'val': 'NotAGame'}
        resp = self.client.post(self.url, json=data)
        self.assertEqual(resp.status_code, 400)
        self.assertIn('Invalid game name', resp.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main() 