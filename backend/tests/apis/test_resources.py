"""Tests for the resource API functions."""

import unittest
from unittest.mock import patch, MagicMock
import os
from apis.resources import get_pokemon_info, get_gym_leader_info, get_type_info


class TestResourceApis(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.test_resources_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'resources')
        self.test_image_path = os.path.join(self.test_resources_path, 'test_image.jpeg')

    @patch('apis.resources.download_pokemon_from_google_search')
    def test_get_pokemon_info_success(self, mock_download):
        """Test that get_pokemon_info returns the image path when successful."""
        # Arrange
        mock_download.return_value = self.test_image_path
        
        # Act
        result = get_pokemon_info('pikachu')
        
        # Assert
        self.assertEqual(result, self.test_image_path)
        mock_download.assert_called_once_with('pikachu', self.test_resources_path)

    @patch('apis.resources.download_pokemon_from_google_search')
    def test_get_pokemon_info_not_found(self, mock_download):
        """Test that get_pokemon_info returns None when Pokemon not found."""
        # Arrange
        mock_download.return_value = None
        
        # Act
        result = get_pokemon_info('nonexistent')
        
        # Assert
        self.assertIsNone(result)
        mock_download.assert_called_once_with('nonexistent', self.test_resources_path)

    @patch('apis.resources.download_gym_from_google_search')
    def test_get_gym_leader_info_success(self, mock_download):
        """Test that get_gym_leader_info returns the image path when successful."""
        # Arrange
        mock_download.return_value = self.test_image_path
        
        # Act
        result = get_gym_leader_info('blue', 'misty')
        
        # Assert
        self.assertEqual(result, self.test_image_path)
        mock_download.assert_called_once_with(
            gym_name='misty',
            badge_name='misty',
            location='blue',
            resources_path=self.test_resources_path
        )

    @patch('apis.resources.download_gym_from_google_search')
    def test_get_gym_leader_info_not_found(self, mock_download):
        """Test that get_gym_leader_info returns None when gym leader not found."""
        # Arrange
        mock_download.return_value = None
        
        # Act
        result = get_gym_leader_info('blue', 'nonexistent')
        
        # Assert
        self.assertIsNone(result)
        mock_download.assert_called_once_with(
            gym_name='nonexistent',
            badge_name='nonexistent',
            location='blue',
            resources_path=self.test_resources_path
        )

    @patch('apis.resources.download_pokemon_type_from_google_search')
    def test_get_type_info_success(self, mock_download):
        """Test that get_type_info returns the image path when successful."""
        # Arrange
        mock_download.return_value = self.test_image_path
        
        # Act
        result = get_type_info('water')
        
        # Assert
        self.assertEqual(result, self.test_image_path)
        mock_download.assert_called_once_with('water', self.test_resources_path)

    @patch('apis.resources.download_pokemon_type_from_google_search')
    def test_get_type_info_not_found(self, mock_download):
        """Test that get_type_info returns None when type not found."""
        # Arrange
        mock_download.return_value = None
        
        # Act
        result = get_type_info('nonexistent')
        
        # Assert
        self.assertIsNone(result)
        mock_download.assert_called_once_with('nonexistent', self.test_resources_path)

    @patch('apis.resources.download_pokemon_from_google_search')
    def test_get_pokemon_info_error(self, mock_download):
        """Test that get_pokemon_info propagates download errors."""
        # Arrange
        mock_download.side_effect = Exception("Download error")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            get_pokemon_info('pikachu')
        self.assertEqual(str(context.exception), "Download error")
        mock_download.assert_called_once_with('pikachu', self.test_resources_path)

    @patch('apis.resources.download_gym_from_google_search')
    def test_get_gym_leader_info_error(self, mock_download):
        """Test that get_gym_leader_info propagates download errors."""
        # Arrange
        mock_download.side_effect = Exception("Download error")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            get_gym_leader_info('blue', 'misty')
        self.assertEqual(str(context.exception), "Download error")
        mock_download.assert_called_once_with(
            gym_name='misty',
            badge_name='misty',
            location='blue',
            resources_path=self.test_resources_path
        )

    @patch('apis.resources.download_pokemon_type_from_google_search')
    def test_get_type_info_error(self, mock_download):
        """Test that get_type_info propagates download errors."""
        # Arrange
        mock_download.side_effect = Exception("Download error")
        
        # Act & Assert
        with self.assertRaises(Exception) as context:
            get_type_info('water')
        self.assertEqual(str(context.exception), "Download error")
        mock_download.assert_called_once_with('water', self.test_resources_path)


if __name__ == '__main__':
    unittest.main() 