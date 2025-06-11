from datetime import datetime
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field
from . import DB_NAME
from .db_helper import insert_document, fetch_documents_by_query, update_document_by_id, delete_documents_by_query


_COLLECTIONS_NAME = "runs_pokemons_options"


@dataclass
class RunPokemonsOptions:
    run_id: str
    pokemon_name: str
    base_pokemon: str

    def __post_init__(self):
        """Validate the run data after initialization."""
        if not self.run_id:
            raise ValueError("Run ID cannot be empty")
        if not self.pokemon_name:
            raise ValueError("Pokemon name cannot be empty")
        if not self.base_pokemon:
            raise ValueError("Base pokemon cannot be empty")

    def to_dict(self) -> Dict[str, Any]:
        """Convert the RunPokemonsOptions object to a dictionary.

        Returns:
            Dict[str, Any]: A dictionary representation of the RunPokemonsOptions object.
        """
        return {
            "run_id": self.run_id,
            "pokemon_name": self.pokemon_name,
            "base_pokemon": self.base_pokemon,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RunPokemonsOptions':
        """Create a RunPokemonsOptions object from a dictionary.

        Args:
            data (Dict[str, Any]): A dictionary representation of a RunPokemonsOptions object.

        Returns:
            RunPokemonsOptions: A RunPokemonsOptions object.
        """
        return cls(
            run_id=data["run_id"],
            pokemon_name=data["_id"],
            base_pokemon=data["base_pokemon"],
        )


def save_run_options(run: RunPokemonsOptions) -> None:
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
        insert_document(DB_NAME, _COLLECTIONS_NAME, run_dict)
    except Exception as e:
        raise Exception(f"Failed to save run: {str(e)}")


def list_runs_options(run_id: str) -> List[RunPokemonsOptions]:
    """List all RunPokemonsOptions from the database, optionally filtered by run_id.

    Args:
        query: Optional query dictionary to filter runs

    Returns:
        List[Run]: List of Run instances matching the query

    Raises:
        Exception: If database operation fails
    """
    try:
        results = list(fetch_documents_by_query(DB_NAME, _COLLECTIONS_NAME, {'run_id': run_id}))
        return [RunPokemonsOptions.from_dict(result) for result in results]
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
