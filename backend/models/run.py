"""Run model for representing a run object in the database."""

from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from . import DB_NAME
from .db_helper import insert_document, fetch_documents_by_query, update_document_by_id, delete_documents_by_query


_COLLECTIONS_NAME = "runs"


@dataclass
class Run:
    """Run model for representing a run object in the database."""

    run_id: str
    created_date: datetime
    name: str
    locke: str
    game: str
    gen: int
    randomized: bool
    party: List[str] = field(default_factory=list)
    box: List[str] = field(default_factory=list)
    battles: List[Dict[str, Any]] = field(default_factory=list)
    encounters: List[Dict[str, Any]] = field(default_factory=list)
    locke_extra_info: Optional[Dict[str, Any]] = None
    restarts: int = 0
    duplicate_clause: bool = False
    finished: bool = False
    starter: Optional[str] = None

    def __post_init__(self):
        """Validate the run data after initialization."""
        if not self.run_id:
            raise ValueError("Run ID cannot be empty")
        if not self.name:
            raise ValueError("Run name cannot be empty")
        if self.created_date > datetime.now():
            raise ValueError("Creation date cannot be in the future")
        if self.restarts < 0:
            raise ValueError("Restarts cannot be negative")

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Run object to a dictionary.

        Returns:
            Dict[str, Any]: A dictionary representation of the Run object.
        """
        return {
            "_id": self.run_id,
            "created_date": self.created_date,
            "name": self.name,
            "locke": self.locke,
            "game": self.game,
            "gen": self.gen,
            "randomized": self.randomized,
            "party": self.party,
            "box": self.box,
            "battles": self.battles,
            "encounters": self.encounters,
            "locke_extra_info": self.locke_extra_info,
            "restarts": self.restarts,
            "duplicate_clause": self.duplicate_clause,
            "finished": self.finished,
            "starter": self.starter
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Run':
        """Create a Run object from a dictionary.

        Args:
            data (Dict[str, Any]): A dictionary representation of a Run object.

        Returns:
            Run: A Run object.
        """
        return cls(
            run_id=data["_id"],
            created_date=data["created_date"],
            name=data["name"],
            locke=data["locke"],
            game=data["game"],
            gen=data["gen"],
            randomized=data["randomized"],
            party=data["party"],
            box=data["box"],
            battles=data["battles"],
            encounters=data["encounters"],
            locke_extra_info=data.get("locke_extra_info"),
            restarts=data.get("restarts", 0),
            duplicate_clause=data.get("duplicate_clause", False),
            finished=data.get("finished", False),
            starter=data.get("starter")
        )


def save_run(run: Run) -> None:
    """Save a run to the database.
    
    Args:
        run: Run instance to save
        
    Raises:
        Exception: If database operation fails
    """
    try:
        run_dict = run.to_dict()
        insert_document(DB_NAME, _COLLECTIONS_NAME, run_dict)
    except Exception as e:
        raise Exception(f"Failed to save run: {str(e)}")


def update_run(run: Run) -> None:
    """Update an existing run in the database.
    
    Args:
        run: Run instance to update
        
    Raises:
        Exception: If database operation fails
    """
    try:
        run_dict = run.to_dict()
        update_document_by_id(DB_NAME, _COLLECTIONS_NAME, run.run_id, run_dict)
    except Exception as e:
        raise Exception(f"Failed to update run: {str(e)}")


def fetch_run(run_id: str) -> Optional[Run]:
    """Fetch a run from the database.
    
    Args:
        run_id: ID of the run to fetch
        
    Returns:
        Optional[Run]: Run instance if found, None otherwise
        
    Raises:
        Exception: If database operation fails
    """
    try:
        results = list(fetch_documents_by_query(DB_NAME, _COLLECTIONS_NAME, {'_id': run_id}))
        if not results:
            return None
        return Run.from_dict(results[0])
    except Exception as e:
        raise Exception(f"Failed to fetch run: {str(e)}")


def list_runs(query: Optional[Dict[str, Any]] = None) -> List[Run]:
    """List all runs from the database, optionally filtered by query.
    
    Args:
        query: Optional query dictionary to filter runs
        
    Returns:
        List[Run]: List of Run instances matching the query
        
    Raises:
        Exception: If database operation fails
    """
    try:
        results = list(fetch_documents_by_query(DB_NAME, _COLLECTIONS_NAME, query or {}))
        return [Run.from_dict(result) for result in results]
    except Exception as e:
        raise Exception(f"Failed to list runs: {str(e)}")


def delete_run(run_id: str) -> None:
    """Delete a run from the database.
    
    Args:
        run_id: ID of the run to delete
        
    Raises:
        Exception: If database operation fails
    """
    try:
        delete_documents_by_query(DB_NAME, _COLLECTIONS_NAME, {'_id': run_id})
    except Exception as e:
        raise Exception(f"Failed to delete run: {str(e)}") 