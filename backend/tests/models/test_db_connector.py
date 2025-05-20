import unittest
from unittest.mock import patch, MagicMock
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from models.db_connector import get_client, get_db, close_connection

class TestDBConnector(unittest.TestCase):
    def setUp(self):
        # Reset the client before each test
        close_connection()
        
    def tearDown(self):
        # Clean up after each test
        close_connection()

    @patch('models.db_connector.MongoClient')
    def test_get_client_success(self, mock_mongo_client):
        # Setup mock
        mock_client = MagicMock()
        mock_mongo_client.return_value = mock_client
        mock_client.admin.command.return_value = True

        # Test
        client = get_client()
        
        # Assertions
        self.assertIsNotNone(client)
        mock_mongo_client.assert_called_once()
        mock_client.admin.command.assert_called_once_with('ping')

    @patch('models.db_connector.MongoClient')
    def test_get_client_connection_failure(self, mock_mongo_client):
        # Setup mock to raise ConnectionFailure
        mock_mongo_client.side_effect = ConnectionFailure("Connection failed")

        # Test and assert
        with self.assertRaises(ConnectionFailure):
            get_client()

    @patch('models.db_connector.get_client')
    def test_get_db(self, mock_get_client):
        # Setup mock
        mock_client = MagicMock()
        mock_db = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.__getitem__.return_value = mock_db

        # Test
        db = get_db("test_db")

        # Assertions
        self.assertEqual(db, mock_db)
        mock_client.__getitem__.assert_called_once_with("test_db")

    def test_environment_variables(self):
        # Test with environment variables
        test_host = "test_host"
        test_port = "27018"
        test_db = "test_db"

        with patch.dict(os.environ, {
            "MONGO_HOST": test_host,
            "MONGO_PORT": test_port,
            "MONGO_DB_NAME": test_db
        }):
            with patch('models.db_connector.MongoClient') as mock_mongo_client:
                mock_client = MagicMock()
                mock_mongo_client.return_value = mock_client
                mock_client.admin.command.return_value = True

                get_client()
                mock_mongo_client.assert_called_once_with(
                    host=test_host,
                    port=int(test_port),
                    maxPoolSize=50,
                    minPoolSize=10,
                    serverSelectionTimeoutMS=5000
                )

    def test_close_connection(self):
        # Setup
        with patch('models.db_connector.MongoClient') as mock_mongo_client:
            mock_client = MagicMock()
            mock_mongo_client.return_value = mock_client
            mock_client.admin.command.return_value = True

            # Get a client first
            client = get_client()
            self.assertIsNotNone(client)

            # Test close_connection
            close_connection()
            
            # Assert
            mock_client.close.assert_called_once()

if __name__ == '__main__':
    unittest.main() 