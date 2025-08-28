from typing import List, Dict, Optional, Any
from dataclasses import dataclass
from . import DB_NAME
from .db_helper import insert_document, fetch_documents_by_query, delete_documents_by_query, update_document_by_id
from .pokemon import Pokemon, _create_pokemon_document, _db_dict_to_pokemon
import functools


_COLLECTIONS_NAME = "runs_reports"


@dataclass
class Report:
    run_id: str
    game_name: str
    party: List[Pokemon]
    caught: List[Pokemon]
    died: List[Pokemon]

    def __post_init__(self):
        """Validate the run data after initialization."""
        if not self.run_id:
            raise ValueError("Run ID cannot be empty")
        if not self.game_name:
            raise ValueError("Game name cannot be empty")

    @staticmethod
    def generate_id(run_id: str, game_name: str) -> str:
        return f"{run_id}_{game_name}"

    @property
    def id(self):
        return self.generate_id(self.run_id, self.game_name)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Report object to a dictionary.

        Returns:
            Dict[str, Any]: A dictionary representation of the RunPokemonsOptions object.
        """
        return {
            "_id": self.id,
            "run_id": self.run_id,
            "game_name": self.game_name,
            "party": [_create_pokemon_document(self.run_id, p) for p in self.party],
            "caught": [_create_pokemon_document(self.run_id, p) for p in self.caught],
            "dead": [_create_pokemon_document(self.run_id, p) for p in self.died],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Report':
        """Create a RunPokemonsOptions object from a dictionary.

        Args:
            data (Dict[str, Any]): A dictionary representation of a RunPokemonsOptions object.

        Returns:
            RunPokemonsOptions: A RunPokemonsOptions object.
        """
        return cls(
            run_id=data["run_id"],
            game_name=data["game_name"],
            party=[_db_dict_to_pokemon(p) for p in data.get("party", [])],
            caught=[_db_dict_to_pokemon(p) for p in data.get("caught", [])],
            died=[_db_dict_to_pokemon(p) for p in data.get("dead", [])],
        )


def save_report(run: Report, create: bool = True) -> None:
    """Save a RunPokemonsOptions to the database.

    Args:
        run: Run instance to save
        collection_name: collection to save in [default: runs]
            valid options: [runs, runs_save]

    Raises:
        Exception: If database operation fails
    """
    try:
        run_dict = run.to_dict()
        if create:
            insert_document(DB_NAME, _COLLECTIONS_NAME, run_dict)
        else:
            update_document_by_id(DB_NAME, _COLLECTIONS_NAME, run.id, run_dict)
    except Exception as e:
        raise Exception(f"Failed to save run: {str(e)}")


@functools.lru_cache(10)
def list_runs_options(run_id: str) -> List[Report]:
    """List all RunPokemonsOptions from the database, optionally filtered by run_id.

    Args:
        query: Optional query dictionary to filter runs

    Returns:
        List[Run]: List of Run instances matching the query

    Raises:
        Exception: If database operation fails
    """
    return list_runs_options_by_query(run_id)


def list_runs_options_by_query(run_id: str, query: Optional[Dict] = None) -> List[Report]:
    """List all RunPokemonsOptions from the database, optionally filtered by run_id.

    Args:
        query: Optional query dictionary to filter runs

    Returns:
        List[Run]: List of Run instances matching the query

    Raises:
        Exception: If database operation fails
    """
    try:
        fetch_query = {'run_id': run_id}
        query = query or {}
        fetch_query.update(query)
        results = list(fetch_documents_by_query(DB_NAME, _COLLECTIONS_NAME, fetch_query))
        return [Report.from_dict(result) for result in results]
    except Exception as e:
        raise Exception(f"Failed to list runs: {str(e)}")


def delete_run_pokemons(run_id: str) -> None:
    """Delete a run from the database.

    Args:
        run_id: ID of the run to delete

    Raises:
        Exception: If database operation fails
    """
    try:
        delete_documents_by_query(DB_NAME, _COLLECTIONS_NAME, {'run_id': run_id})
    except Exception as e:
        raise Exception(f"Failed to delete run: {str(e)}")
