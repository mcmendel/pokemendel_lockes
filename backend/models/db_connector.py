from typing import Optional
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

# Default configuration
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 27017
DEFAULT_DB_NAME = "locke_manager"

# Remote MongoDB configuration
REMOTE_CONNECTION_STRING_TEMPLATE = "mongodb+srv://mcmendel_db_user:{password}@mcmendel-locke-manager.3ynuh71.mongodb.net/?retryWrites=true&w=majority"

_client: Optional[MongoClient] = None

def get_client() -> MongoClient:
    """
    Get or create a MongoDB client instance with connection pooling.
    Uses local MongoDB if LOCAL env var is true, otherwise uses remote MongoDB.
    
    Returns:
        MongoClient: A MongoDB client instance
        
    Raises:
        ConnectionFailure: If unable to connect to the MongoDB server
    """
    global _client
    if _client is None:
        # Check if we should use local MongoDB
        use_local = os.getenv("LOCAL", "false").lower() in ("true", "1", "yes")
        
        if use_local:
            # Use local MongoDB
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
                print(f"Connected to LOCAL MongoDB at {mongo_host}:{mongo_port}")
            except ConnectionFailure as e:
                raise ConnectionFailure(f"Failed to connect to LOCAL MongoDB at {mongo_host}:{mongo_port}") from e
        else:
            # Use remote MongoDB
            password = os.getenv("MONGODB_PASSWORD")
            print(f"DEBUG: LOCAL env var: {os.getenv('LOCAL')}")
            print(f"DEBUG: MONGODB_PASSWORD length: {len(password) if password else 'None'}")
            print(f"DEBUG: MONGODB_PASSWORD first 3 chars: {password[:3] if password else 'None'}")
            
            if not password:
                raise ConnectionFailure("MONGODB_PASSWORD environment variable is required for remote MongoDB connection")
            
            connection_string = REMOTE_CONNECTION_STRING_TEMPLATE.format(password=password)
            print(f"DEBUG: Connection string (masked): {connection_string[:50]}...")
            
            try:
                _client = MongoClient(
                    connection_string,
                    maxPoolSize=50,
                    minPoolSize=10,
                    serverSelectionTimeoutMS=15000,  # Longer timeout for remote
                    connectTimeoutMS=15000,
                    socketTimeoutMS=15000
                )
                # Verify the connection
                _client.admin.command('ping')
                print("Connected to REMOTE MongoDB cluster")
            except ConnectionFailure as e:
                print(f"DEBUG: Connection error details: {e}")
                raise ConnectionFailure(f"Failed to connect to REMOTE MongoDB cluster: {e}") from e
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
