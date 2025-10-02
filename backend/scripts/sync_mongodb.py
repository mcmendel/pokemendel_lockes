#!/usr/bin/env python3
"""
MongoDB Sync Script

This script syncs all Pokemon Locke Manager collections between local and remote MongoDB.
Collections synced:
- runs
- runs_save  
- pokemons
- pokemons_save
- run_creation
- runs_pokemons_options
- runs_reports

Usage:
    python sync_mongodb.py [--dry-run] [--collections collection1,collection2] [--reverse]
    
Environment Variables:
    MONGODB_PASSWORD - Password for the remote MongoDB cluster
"""

import os
import sys
import argparse
from datetime import datetime
from typing import List, Dict, Any
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('mongodb_sync.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Database and collection configuration
DB_NAME = "locke_manager"
COLLECTIONS = [
    "runs",
    "runs_save", 
    "pokemons",
    "pokemons_save",
    "run_creation",
    "runs_pokemons_options",
    "runs_reports"
]

# Connection strings
LOCAL_CONNECTION_STRING = "mongodb://localhost:27017/"
REMOTE_CONNECTION_STRING_TEMPLATE = "mongodb+srv://mcmendel_db_user:{password}@mcmendel-locke-manager.3ynuh71.mongodb.net/"

def get_remote_connection_string(password: str) -> str:
    """Get the remote connection string with password."""
    return REMOTE_CONNECTION_STRING_TEMPLATE.format(password=password)

def connect_to_mongodb(connection_string: str, name: str) -> MongoClient:
    """Connect to MongoDB and return the client."""
    try:
        client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)
        # Test the connection
        client.admin.command('ping')
        logger.info(f"Successfully connected to {name} MongoDB")
        return client
    except (ConnectionFailure, ServerSelectionTimeoutError) as e:
        logger.error(f"Failed to connect to {name} MongoDB: {e}")
        raise

def get_collection_stats(client: MongoClient, db_name: str, collection_name: str) -> Dict[str, Any]:
    """Get statistics for a collection."""
    try:
        db = client[db_name]
        collection = db[collection_name]
        count = collection.count_documents({})
        return {
            "count": count,
            "exists": True
        }
    except Exception as e:
        logger.warning(f"Collection {collection_name} does not exist or error accessing: {e}")
        return {
            "count": 0,
            "exists": False
        }

def sync_collection(
    source_client: MongoClient, 
    target_client: MongoClient, 
    db_name: str, 
    collection_name: str,
    dry_run: bool = False
) -> Dict[str, Any]:
    """Sync a single collection from source to target."""
    logger.info(f"Syncing collection: {collection_name}")
    
    source_db = source_client[db_name]
    target_db = target_client[db_name]
    
    source_collection = source_db[collection_name]
    target_collection = target_db[collection_name]
    
    # Get source collection stats
    source_count = source_collection.count_documents({})
    logger.info(f"Source collection {collection_name} has {source_count} documents")
    
    if source_count == 0:
        logger.info(f"No documents to sync in {collection_name}")
        return {
            "collection": collection_name,
            "source_count": 0,
            "target_count_before": 0,
            "target_count_after": 0,
            "documents_synced": 0,
            "errors": 0
        }
    
    # Get target collection stats before sync
    target_count_before = target_collection.count_documents({})
    logger.info(f"Target collection {collection_name} has {target_count_before} documents before sync")
    
    if dry_run:
        logger.info(f"DRY RUN: Would sync {source_count} documents from {collection_name}")
        return {
            "collection": collection_name,
            "source_count": source_count,
            "target_count_before": target_count_before,
            "target_count_after": target_count_before,
            "documents_synced": source_count,
            "errors": 0,
            "dry_run": True
        }
    
    # Clear target collection
    logger.info(f"Clearing target collection {collection_name}")
    target_collection.delete_many({})
    
    # Copy all documents from source to target
    documents_synced = 0
    errors = 0
    
    try:
        # Get all documents from source
        source_documents = list(source_collection.find({}))
        
        if source_documents:
            # Insert all documents into target
            result = target_collection.insert_many(source_documents)
            documents_synced = len(result.inserted_ids)
            logger.info(f"Successfully synced {documents_synced} documents to {collection_name}")
        else:
            logger.info(f"No documents found in source collection {collection_name}")
            
    except Exception as e:
        logger.error(f"Error syncing collection {collection_name}: {e}")
        errors += 1
    
    # Get target collection stats after sync
    target_count_after = target_collection.count_documents({})
    
    return {
        "collection": collection_name,
        "source_count": source_count,
        "target_count_before": target_count_before,
        "target_count_after": target_count_after,
        "documents_synced": documents_synced,
        "errors": errors
    }

def main():
    """Main function to sync MongoDB collections."""
    parser = argparse.ArgumentParser(description="Sync MongoDB collections between local and remote")
    parser.add_argument(
        "--dry-run", 
        action="store_true", 
        help="Perform a dry run without actually syncing data"
    )
    parser.add_argument(
        "--collections", 
        type=str, 
        help="Comma-separated list of collections to sync (default: all collections)"
    )
    parser.add_argument(
        "--password", 
        type=str, 
        help="Remote MongoDB password (can also use MONGODB_PASSWORD env var)"
    )
    parser.add_argument(
        "--reverse", 
        action="store_true", 
        help="Sync from remote to local (default: local to remote)"
    )
    
    args = parser.parse_args()
    
    # Get password from args or environment variable
    password = args.password or os.getenv('MONGODB_PASSWORD')
    if not password:
        logger.error("MongoDB password is required. Use --password or set MONGODB_PASSWORD environment variable")
        sys.exit(1)
    
    # Determine which collections to sync
    collections_to_sync = COLLECTIONS
    if args.collections:
        requested_collections = [c.strip() for c in args.collections.split(',')]
        collections_to_sync = [c for c in requested_collections if c in COLLECTIONS]
        if not collections_to_sync:
            logger.error(f"No valid collections specified. Available: {', '.join(COLLECTIONS)}")
            sys.exit(1)
    
    # Determine sync direction
    if args.reverse:
        sync_direction = "remote to local"
        source_name = "remote"
        target_name = "local"
    else:
        sync_direction = "local to remote"
        source_name = "local"
        target_name = "remote"
    
    logger.info(f"Starting MongoDB sync {'(DRY RUN)' if args.dry_run else ''}")
    logger.info(f"Sync direction: {sync_direction}")
    logger.info(f"Collections to sync: {', '.join(collections_to_sync)}")
    
    # Connect to MongoDB instances
    try:
        local_client = connect_to_mongodb(LOCAL_CONNECTION_STRING, "local")
        remote_client = connect_to_mongodb(get_remote_connection_string(password), "remote")
    except Exception as e:
        logger.error(f"Failed to connect to MongoDB: {e}")
        sys.exit(1)
    
    # Determine source and target clients based on sync direction
    if args.reverse:
        source_client = remote_client
        target_client = local_client
    else:
        source_client = local_client
        target_client = remote_client
    
    # Get initial stats
    logger.info("Getting initial collection statistics...")
    for collection_name in collections_to_sync:
        local_stats = get_collection_stats(local_client, DB_NAME, collection_name)
        remote_stats = get_collection_stats(remote_client, DB_NAME, collection_name)
        
        logger.info(f"{collection_name}: Local={local_stats['count']}, Remote={remote_stats['count']}")
    
    # Sync collections
    sync_results = []
    start_time = datetime.now()
    
    try:
        for collection_name in collections_to_sync:
            result = sync_collection(
                source_client, 
                target_client, 
                DB_NAME, 
                collection_name,
                args.dry_run
            )
            sync_results.append(result)
            
    except KeyboardInterrupt:
        logger.info("Sync interrupted by user")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Unexpected error during sync: {e}")
        sys.exit(1)
    finally:
        # Close connections
        local_client.close()
        remote_client.close()
    
    # Print summary
    end_time = datetime.now()
    duration = end_time - start_time
    
    logger.info("=" * 60)
    logger.info("SYNC SUMMARY")
    logger.info("=" * 60)
    
    total_documents_synced = 0
    total_errors = 0
    
    for result in sync_results:
        logger.info(f"Collection: {result['collection']}")
        logger.info(f"  Source documents: {result['source_count']}")
        logger.info(f"  Target before: {result['target_count_before']}")
        logger.info(f"  Target after: {result['target_count_after']}")
        logger.info(f"  Documents synced: {result['documents_synced']}")
        logger.info(f"  Errors: {result['errors']}")
        logger.info("")
        
        total_documents_synced += result['documents_synced']
        total_errors += result['errors']
    
    logger.info(f"Total documents synced: {total_documents_synced}")
    logger.info(f"Total errors: {total_errors}")
    logger.info(f"Duration: {duration}")
    logger.info(f"Sync direction: {sync_direction}")
    logger.info(f"Status: {'DRY RUN' if args.dry_run else 'COMPLETED'}")
    
    if total_errors > 0:
        logger.warning(f"Sync completed with {total_errors} errors")
        sys.exit(1)
    else:
        logger.info("Sync completed successfully!")

if __name__ == "__main__":
    main()
