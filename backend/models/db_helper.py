from . import db_connector
from typing import List, Dict, Generator, Set, Optional, Any
from bson import ObjectId
from pymongo.errors import PyMongoError
import logging

logger = logging.getLogger(__name__)


def insert_documents(db_name: str, collection_name: str, documents: List[Dict]) -> List[str]:
    """
    Insert multiple documents into a MongoDB collection.
    
    Args:
        db_name (str): Name of the database
        collection_name (str): Name of the collection
        documents (List[Dict]): List of documents to insert
        
    Returns:
        List[str]: List of inserted document IDs
        
    Raises:
        PyMongoError: If there's an error during insertion
    """
    try:
        db = db_connector.get_db(db_name)
        collection = db[collection_name]
        result = collection.insert_many(documents)
        return [str(id) for id in result.inserted_ids]
    except PyMongoError as e:
        logger.error(f"Error inserting documents into {db_name}.{collection_name}: {str(e)}")
        raise


def insert_document(db_name: str, collection_name: str, document: Dict) -> str:
    """
    Insert a single document into a MongoDB collection.
    
    Args:
        db_name (str): Name of the database
        collection_name (str): Name of the collection
        document (Dict): Document to insert
        
    Returns:
        str: ID of the inserted document
        
    Raises:
        PyMongoError: If there's an error during insertion
    """
    try:
        db = db_connector.get_db(db_name)
        collection = db[collection_name]
        result = collection.insert_one(document)
        return str(result.inserted_id)
    except PyMongoError as e:
        logger.error(f"Error inserting document into {db_name}.{collection_name}: {str(e)}")
        raise


def fetch_documents_by_query(
    db_name: str, 
    collection_name: str, 
    query: Dict, 
    keys: Set = frozenset()
) -> Generator[Dict, None, None]:
    """
    Fetch documents from a MongoDB collection based on a query.
    
    Args:
        db_name (str): Name of the database
        collection_name (str): Name of the collection
        query (Dict): Query to filter documents
        keys (Set): Set of field names to include in the result
        
    Yields:
        Dict: Matching documents
        
    Raises:
        PyMongoError: If there's an error during fetching
    """
    try:
        db = db_connector.get_db(db_name)
        collection = db[collection_name]
        yield from collection.find(query, projection=keys)
    except PyMongoError as e:
        logger.error(f"Error fetching documents from {db_name}.{collection_name}: {str(e)}")
        raise


def fetch_document_by_id(db_name: str, collection_name: str, doc_id: str) -> Optional[Dict]:
    """
    Fetch a single document by its ID.
    
    Args:
        db_name (str): Name of the database
        collection_name (str): Name of the collection
        doc_id (str): ID of the document to fetch
        
    Returns:
        Optional[Dict]: The document if found, None otherwise
        
    Raises:
        PyMongoError: If there's an error during fetching
    """
    try:
        db = db_connector.get_db(db_name)
        collection = db[collection_name]
        result = collection.find_one({'_id': ObjectId(doc_id)})
        if result is None:
            logger.warning(f"Document with id {doc_id} not found in {db_name}.{collection_name}")
        return result
    except PyMongoError as e:
        logger.error(f"Error fetching document from {db_name}.{collection_name}: {str(e)}")
        raise


def fetch_all_documents(
    db_name: str, 
    collection_name: str, 
    keys: Set = frozenset()
) -> Generator[Dict, None, None]:
    """
    Fetch all documents from a MongoDB collection.
    
    Args:
        db_name (str): Name of the database
        collection_name (str): Name of the collection
        keys (Set): Set of field names to include in the result
        
    Yields:
        Dict: All documents in the collection
        
    Raises:
        PyMongoError: If there's an error during fetching
    """
    try:
        db = db_connector.get_db(db_name)
        collection = db[collection_name]
        yield from collection.find(projection=keys)
    except PyMongoError as e:
        logger.error(f"Error fetching all documents from {db_name}.{collection_name}: {str(e)}")
        raise


def update_document_by_id(
    db_name: str, 
    collection_name: str, 
    doc_id: str, 
    new_data: Dict
) -> bool:
    """
    Update a document by its ID.
    
    Args:
        db_name (str): Name of the database
        collection_name (str): Name of the collection
        doc_id (str): ID of the document to update
        new_data (Dict): New data to update the document with
        
    Returns:
        bool: True if document was updated, False if it was inserted
        
    Raises:
        PyMongoError: If there's an error during update
    """
    try:
        query = {"_id": ObjectId(doc_id)}
        new_values = {"$set": new_data}
        db = db_connector.get_db(db_name)
        collection = db[collection_name]
        result = collection.update_one(query, new_values, upsert=True)
        return result.modified_count > 0
    except PyMongoError as e:
        logger.error(f"Error updating document in {db_name}.{collection_name}: {str(e)}")
        raise


def delete_documents_by_query(
    db_name: str, 
    collection_name: str, 
    query: Dict
) -> int:
    """
    Delete documents matching a query.
    
    Args:
        db_name (str): Name of the database
        collection_name (str): Name of the collection
        query (Dict): Query to match documents for deletion
        
    Returns:
        int: Number of documents deleted
        
    Raises:
        PyMongoError: If there's an error during deletion
    """
    try:
        db = db_connector.get_db(db_name)
        collection = db[collection_name]
        result = collection.delete_many(query)
        return result.deleted_count
    except PyMongoError as e:
        logger.error(f"Error deleting documents from {db_name}.{collection_name}: {str(e)}")
        raise
