from typing import Optional
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

# Default configuration
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 27017
DEFAULT_DB_NAME = "locke_manager"

_client: Optional[MongoClient] = None

def get_client() -> MongoClient:
    """
    Get or create a MongoDB client instance with connection pooling.
    
    Returns:
        MongoClient: A MongoDB client instance
        
    Raises:
        ConnectionFailure: If unable to connect to the MongoDB server
    """
    global _client
    if _client is None:
        # Read environment variables at call time
        mongo_host = os.getenv("MONGO_HOST", DEFAULT_HOST)
        mongo_port = int(os.getenv("MONGO_PORT", str(DEFAULT_PORT)))
        try:
            _client = MongoClient(
                host=mongo_host,
                port=mongo_port,
                maxPoolSize=50,
                minPoolSize=10,
                serverSelectionTimeoutMS=5000
            )
            # Verify the connection
            _client.admin.command('ping')
        except ConnectionFailure as e:
            raise ConnectionFailure(f"Failed to connect to MongoDB at {mongo_host}:{mongo_port}") from e
    return _client

def get_db(db_name: str = None):
    """
    Get a database instance from the MongoDB client.
    
    Args:
        db_name (str): Name of the database to connect to. Defaults to MONGO_DB_NAME.
        
    Returns:
        Database: A MongoDB database instance
        
    Raises:
        ConnectionFailure: If unable to connect to the MongoDB server
    """
    # Read environment variable at call time
    if db_name is None:
        db_name = os.getenv("MONGO_DB_NAME", DEFAULT_DB_NAME)
    client = get_client()
    return client[db_name]

def close_connection():
    """
    Close the MongoDB client connection.
    """
    global _client
    if _client is not None:
        _client.close()
        _client = None
