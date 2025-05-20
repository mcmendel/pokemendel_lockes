import unittest
from unittest.mock import patch, MagicMock
from bson import ObjectId
from pymongo.errors import PyMongoError
from models.db_helper import (
    insert_documents,
    insert_document,
    fetch_documents_by_query,
    fetch_document_by_id,
    fetch_all_documents,
    update_document_by_id,
    delete_documents_by_query
)

class TestDBHelper(unittest.TestCase):
    def setUp(self):
        self.test_db_name = "test_db"
        self.test_collection = "test_collection"
        self.test_document = {"name": "test", "value": 123}
        self.test_documents = [
            {"name": "test1", "value": 1},
            {"name": "test2", "value": 2}
        ]
        self.test_id = str(ObjectId())

    @patch('models.db_helper.db_connector.get_db')
    def test_insert_document(self, mock_get_db):
        # Setup mock
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_get_db.return_value = mock_db
        mock_collection.insert_one.return_value.inserted_id = ObjectId()

        # Test
        result = insert_document(self.test_db_name, self.test_collection, self.test_document)

        # Assertions
        self.assertIsInstance(result, str)
        mock_collection.insert_one.assert_called_once_with(self.test_document)

    @patch('models.db_helper.db_connector.get_db')
    def test_insert_documents(self, mock_get_db):
        # Setup mock
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_get_db.return_value = mock_db
        mock_collection.insert_many.return_value.inserted_ids = [ObjectId(), ObjectId()]

        # Test
        result = insert_documents(self.test_db_name, self.test_collection, self.test_documents)

        # Assertions
        self.assertEqual(len(result), 2)
        mock_collection.insert_many.assert_called_once_with(self.test_documents)

    @patch('models.db_helper.db_connector.get_db')
    def test_fetch_document_by_id(self, mock_get_db):
        # Setup mock
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_get_db.return_value = mock_db
        mock_collection.find_one.return_value = self.test_document

        # Test
        result = fetch_document_by_id(self.test_db_name, self.test_collection, self.test_id)

        # Assertions
        self.assertEqual(result, self.test_document)
        mock_collection.find_one.assert_called_once_with({'_id': ObjectId(self.test_id)})

    @patch('models.db_helper.db_connector.get_db')
    def test_fetch_document_by_id_not_found(self, mock_get_db):
        # Setup mock
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_get_db.return_value = mock_db
        mock_collection.find_one.return_value = None

        # Test
        result = fetch_document_by_id(self.test_db_name, self.test_collection, self.test_id)

        # Assertions
        self.assertIsNone(result)

    @patch('models.db_helper.db_connector.get_db')
    def test_fetch_documents_by_query(self, mock_get_db):
        # Setup mock
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_get_db.return_value = mock_db
        mock_collection.find.return_value = self.test_documents

        # Test
        query = {"name": "test"}
        result = list(fetch_documents_by_query(self.test_db_name, self.test_collection, query))

        # Assertions
        self.assertEqual(result, self.test_documents)
        mock_collection.find.assert_called_once_with(query, projection=frozenset())

    @patch('models.db_helper.db_connector.get_db')
    def test_update_document_by_id(self, mock_get_db):
        # Setup mock
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_get_db.return_value = mock_db
        mock_collection.update_one.return_value.modified_count = 1

        # Test
        new_data = {"value": 456}
        result = update_document_by_id(self.test_db_name, self.test_collection, self.test_id, new_data)

        # Assertions
        self.assertTrue(result)
        mock_collection.update_one.assert_called_once_with(
            {"_id": ObjectId(self.test_id)},
            {"$set": new_data},
            upsert=True
        )

    @patch('models.db_helper.db_connector.get_db')
    def test_delete_documents_by_query(self, mock_get_db):
        # Setup mock
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_get_db.return_value = mock_db
        mock_collection.delete_many.return_value.deleted_count = 2

        # Test
        query = {"name": "test"}
        result = delete_documents_by_query(self.test_db_name, self.test_collection, query)

        # Assertions
        self.assertEqual(result, 2)
        mock_collection.delete_many.assert_called_once_with(query)

    @patch('models.db_helper.db_connector.get_db')
    def test_error_handling(self, mock_get_db):
        # Setup mock to raise PyMongoError
        mock_collection = MagicMock()
        mock_db = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_get_db.return_value = mock_db
        mock_collection.insert_one.side_effect = PyMongoError("Test error")

        # Test and assert
        with self.assertRaises(PyMongoError):
            insert_document(self.test_db_name, self.test_collection, self.test_document)

if __name__ == '__main__':
    unittest.main() 