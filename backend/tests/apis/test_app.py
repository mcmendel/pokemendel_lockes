"""Tests for the Flask app API endpoints."""

import unittest
from unittest.mock import patch
import json
from app import app


class TestAppApis(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.list_all_lockes')
    def test_get_lockes_success(self, mock_list_lockes):
        """Test that get_lockes returns a list of locke names."""
        # Arrange
        mock_list_lockes.return_value = ['BaseLocke', 'Nuzlocke']
        
        # Act
        response = self.app.get('/locke_manager/lockes')
        
        # Assert
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, ['BaseLocke', 'Nuzlocke'])
        mock_list_lockes.assert_called_once()

    @patch('app.list_all_lockes')
    def test_get_lockes_empty(self, mock_list_lockes):
        """Test that get_lockes returns an empty list when no lockes exist."""
        # Arrange
        mock_list_lockes.return_value = []
        
        # Act
        response = self.app.get('/locke_manager/lockes')
        
        # Assert
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data, [])
        mock_list_lockes.assert_called_once()

    @patch('app.list_all_lockes')
    def test_get_lockes_error(self, mock_list_lockes):
        """Test that get_lockes handles errors properly."""
        # Arrange
        mock_list_lockes.side_effect = Exception("Database error")
        
        # Act
        response = self.app.get('/locke_manager/lockes')
        
        # Assert
        self.assertEqual(response.status_code, 500)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['message'], 'Database error')
        mock_list_lockes.assert_called_once()


if __name__ == '__main__':
    unittest.main() 