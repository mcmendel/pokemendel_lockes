from typing import List, Dict, Optional, Any
from dataclasses import dataclass
from . import DB_NAME
from .db_helper import insert_document, fetch_documents_by_query, delete_documents_by_query, update_document_by_id
import functools


_COLLECTIONS_NAME = "runs_pokemons_options"


@dataclass
class RunPokemonsOptions:
    index: int
    run_id: str
    pokemon_name: str
    base_pokemon: str
    caught: bool = False

    def __post_init__(self):
        """Validate the run data after initialization."""
        if not self.run_id:
            raise ValueError("Run ID cannot be empty")
        if not self.pokemon_name:
            raise ValueError("Pokemon name cannot be empty")
        if not self.base_pokemon:
            raise ValueError("Base pokemon cannot be empty")

    @staticmethod
    def generate_id(run_id: str, pokemon_name: str) -> str:
        return f"{run_id}_{pokemon_name}"

    @property
    def id(self):
        return self.generate_id(self.run_id, self.pokemon_name)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the RunPokemonsOptions object to a dictionary.

        Returns:
            Dict[str, Any]: A dictionary representation of the RunPokemonsOptions object.
        """
        return {
            "_id": self.id,
            "index": self.index,
            "run_id": self.run_id,
            "pokemon_name": self.pokemon_name,
            "base_pokemon": self.base_pokemon,
            "caught": self.caught,
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
            pokemon_name=data["pokemon_name"],
            base_pokemon=data["base_pokemon"],
            index=data.get("index", -1),
            caught=data.get("caught", False),
        )


def save_run_options(run: RunPokemonsOptions, create: bool = True) -> None:
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
def list_runs_options(run_id: str) -> List[RunPokemonsOptions]:
    """List all RunPokemonsOptions from the database, optionally filtered by run_id.

    Args:
        query: Optional query dictionary to filter runs

    Returns:
        List[Run]: List of Run instances matching the query

    Raises:
        Exception: If database operation fails
    """
    return list_runs_options_by_query(run_id)


def list_runs_options_by_query(run_id: str, query: Optional[Dict] = None) -> List[RunPokemonsOptions]:
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
        results = list(fetch_documents_by_query(DB_NAME, _COLLECTIONS_NAME, fetch_query, sort_key="index"))
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


def mark_caught_pokemon(run_id: str, pokemon_name: str):
    pokemon_options = list_runs_options_by_query(
        run_id, {'_id': RunPokemonsOptions.generate_id(run_id, pokemon_name)}
    )
    assert len(pokemon_options) == 1
    pokemon_base = pokemon_options[0].base_pokemon
    for pokemon_same_base in list_runs_options_by_query(run_id, {'base_pokemon': pokemon_base}):
        pokemon_same_base.caught = True
        save_run_options(pokemon_same_base, create=False)
