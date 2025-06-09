import pytest
from models import db_connector
from unittest.mock import patch

def clear_e2e_collections():
    """Clear all collections that start with 'e2e_'."""
    db = db_connector.get_db("locke_manager")
    for collection_name in db.list_collection_names():
        if collection_name.startswith('e2e_'):
            collection = db[collection_name]
            before_count = collection.count_documents({})
            print(f"Clearing collection: {collection_name} (had {before_count} documents)")
            result = collection.delete_many({})
            after_count = collection.count_documents({})
            print(f"Deleted {result.deleted_count} documents from {collection_name}, now has {after_count} documents")
            assert after_count == 0, f"Collection {collection_name} still has {after_count} documents after deletion"

@pytest.fixture(autouse=True)
def clear_collections():
    """Clear all e2e collections before and after each test."""
    clear_e2e_collections()
    yield
    clear_e2e_collections()

@pytest.fixture(autouse=True)
def patch_db_collections(monkeypatch):
    """Automatically patch all database collection names in e2e tests to use 'e2e_' prefix."""
    original_get_db = db_connector.get_db

    def patched_get_db(db_name):
        db = original_get_db(db_name)
        # Create a wrapper around the database that prefixes collection names
        class PatchedDB:
            def __init__(self, db):
                self._db = db

            def __getitem__(self, collection_name):
                # Prefix the collection name with 'e2e_'
                prefixed_name = f"e2e_{collection_name}"
                print(f"Accessing collection: {prefixed_name}")  # Debug print
                return self._db[prefixed_name]

            def __getattr__(self, name):
                return getattr(self._db, name)

        return PatchedDB(db)

    # Apply the patch
    monkeypatch.setattr(db_connector, "get_db", patched_get_db)
    yield
    # No cleanup needed as monkeypatch automatically restores the original 
