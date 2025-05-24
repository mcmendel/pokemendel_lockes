"""Module for managing run creation data in the database.

This module provides functionality for creating, updating, and retrieving run creation data.
A run creation represents the initial configuration for a Pokemon game run, including
game settings and optional rules.
"""

from . import DB_NAME
from .db_helper import insert_document, fetch_documents_by_query, update_document_by_id
from dataclasses import dataclass, asdict, field
from typing import Optional, Dict, Any


_COLLECTIONS_NAME = "run_creation"


@dataclass
class RunCreation:
    """Represents the configuration for a Pokemon game run.
    
    Attributes:
        name: Unique identifier for the run
        locke: Optional name of the locke (challenge) being attempted
        game: Optional name of the Pokemon game being played
        randomized: Optional flag indicating if the game is randomized
        duplicate_clause: Optional flag indicating if duplicate Pokemon are allowed
        extra_info: Additional configuration options as key-value pairs
    """
    name: str
    locke: Optional[str] = None
    game: Optional[str] = None
    randomized: Optional[bool] = None
    duplicate_clause: Optional[bool] = None
    extra_info: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self):
        """Validate the run creation data after initialization."""
        if not self.name:
            raise ValueError("Run name cannot be empty")
        
        # Ensure extra_info is a dictionary
        if not isinstance(self.extra_info, dict):
            raise TypeError("extra_info must be a dictionary")

    def to_dict(self) -> Dict[str, Any]:
        """Convert the run creation to a dictionary for database storage.
        
        Returns:
            Dict containing the run creation data with _id set to the run name.
        """
        dict_run = asdict(self)
        dict_run['_id'] = self.name
        return dict_run

    @staticmethod
    def from_dict(run_dict: Dict[str, Any]) -> 'RunCreation':
        """Create a RunCreation instance from a dictionary.
        
        Args:
            run_dict: Dictionary containing run creation data
            
        Returns:
            RunCreation instance with data from the dictionary
            
        Raises:
            ValueError: If required fields are missing or invalid
        """
        if not isinstance(run_dict, dict):
            raise TypeError("run_dict must be a dictionary")
            
        if 'name' not in run_dict:
            raise ValueError("run_dict must contain a 'name' field")
            
        return RunCreation(**{
            k: v
            for k, v in run_dict.items()
            if k != '_id'
        })


def save_run_creation(run_creation: RunCreation) -> None:
    """Save a run creation to the database.
    
    Args:
        run_creation: RunCreation instance to save
        
    Raises:
        Exception: If database operation fails
    """
    try:
        run_dict = run_creation.to_dict()
        insert_document(DB_NAME, _COLLECTIONS_NAME, run_dict)
    except Exception as e:
        raise Exception(f"Failed to save run creation: {str(e)}")


def update_run_creation(run_creation: RunCreation) -> None:
    """Update an existing run creation in the database.
    
    Args:
        run_creation: RunCreation instance to update
        
    Raises:
        Exception: If database operation fails
    """
    try:
        run_dict = run_creation.to_dict()
        update_document_by_id(DB_NAME, _COLLECTIONS_NAME, run_creation.name, run_dict)
    except Exception as e:
        raise Exception(f"Failed to update run creation: {str(e)}")


def fetch_or_create_run_creation(name: str) -> RunCreation:
    """Fetch an existing run creation or create a new one if it doesn't exist.
    
    Args:
        name: Name of the run to fetch or create
        
    Returns:
        RunCreation instance
        
    Raises:
        Exception: If database operation fails
    """
    try:
        results = list(fetch_documents_by_query(DB_NAME, _COLLECTIONS_NAME, {'name': name}))
        if not results:
            print("Creating run creation", name)
            run_creation = RunCreation(name)
            save_run_creation(run_creation)
            return run_creation

        print("Returning run creation", name)
        run_creation = RunCreation.from_dict(results[0])
        run_creation.extra_info = run_creation.extra_info or {}
        return run_creation
    except Exception as e:
        raise Exception(f"Failed to fetch or create run creation: {str(e)}")
