"""Database operations for Pokemon."""

from typing import List, Optional, TypeAlias, Dict
from dataclasses import asdict
from definitions.pokemons.pokemon import Pokemon as PokemonDef
from definitions.pokemons.pokemon_metadata import PokemonMetadata
from definitions.pokemons.pokemon_status import PokemonStatus
from pokemendel_core.utils.definitions.genders import Genders
from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.models.pokemon import Pokemon as CorePokemon
from .db_helper import (
    insert_document,
    update_document_by_id,
    fetch_documents_by_query,
    delete_documents_by_query
)

# Type aliases
Pokemon: TypeAlias = PokemonDef

# Database constants
DB_NAME = "locke_manager"
_COLLECTIONS_NAME = "pokemons"

def _create_pokemon_document(run_id: str, pokemon: Pokemon) -> Dict:
    """Flatten (or merge) metadata (using asdict) and overwrite (or add) "name", "gen", "types" (and "status") from the Pokémon instance.
    (This helper is used by save_pokemon and update_pokemon.)"""
    pokemon_doc = asdict(pokemon.metadata)
    pokemon_doc["_id"] = pokemon_doc.pop("id")  # MongoDB uses _id
    pokemon_doc["run_id"] = run_id
    pokemon_doc["name"] = pokemon.name
    pokemon_doc["gen"] = pokemon.gen
    # Handle both enum and string types robustly
    pokemon_doc["types"] = [t.value if hasattr(t, 'value') else t for t in pokemon.types]
    pokemon_doc["status"] = pokemon.status
    return pokemon_doc

def _db_dict_to_pokemon(data: dict) -> Pokemon:
    """Convert a database dict (created by _create_pokemon_document) back to a Pokemon definition.
    (This helper is used by fetch_pokemon and list_pokemon_by_run.)"""
    # (1) "Flatten" (or "merge") metadata (using asdict) so that "_id" is renamed "id" (and "nickname" is included).
    metadata_dict = {k: v for k, v in data.items() if k not in ["_id", "run_id", "status", "name", "gen", "types"]}
    metadata_dict["id"] = data["_id"]
    metadata = PokemonMetadata(**metadata_dict)
    # (2) "Overwrite" (or "add") "name", "gen", "types" (and "status") from the database dict.
    def to_type_enum(t):
        if isinstance(t, Types):
            return t
        try:
            return Types(t)
        except Exception:
            return getattr(Types, t.upper())
    return Pokemon(
        name=data["name"],
        gen=data.get("gen", 1),
        types=[to_type_enum(t) for t in data.get("types", [])],
        metadata=metadata,
        status=data["status"]
    )

def save_pokemon(pokemon: Pokemon, run_id: str) -> None:
    """Save a Pokemon (using _create_pokemon_document) to the database.
    (This function is used by save_pokemon.)"""
    try:
        pokemon_dict = _create_pokemon_document(run_id, pokemon)
        insert_document(DB_NAME, _COLLECTIONS_NAME, pokemon_dict)
    except Exception as e:
        raise Exception(f"Failed to save Pokemon: {str(e)}")

def update_pokemon(pokemon: Pokemon, run_id: str) -> None:
    """Update an existing Pokemon (using _create_pokemon_document) in the database.
    (This function is used by update_pokemon.)"""
    try:
        pokemon_dict = _create_pokemon_document(run_id, pokemon)
        update_document_by_id(DB_NAME, _COLLECTIONS_NAME, pokemon.metadata.id, pokemon_dict)
    except Exception as e:
        raise Exception(f"Failed to update Pokemon: {str(e)}")

def fetch_pokemon(pokemon_id: str) -> Optional[Pokemon]:
    """Fetch a Pokemon (using _db_dict_to_pokemon) from the database.
    (This function is used by fetch_pokemon.)"""
    try:
        results = list(fetch_documents_by_query(DB_NAME, _COLLECTIONS_NAME, {'_id': pokemon_id}))
        if not results:
            return None
        return _db_dict_to_pokemon(results[0])
    except Exception as e:
        raise Exception(f"Failed to fetch Pokemon: {str(e)}")

def list_pokemon_by_run(run_id: str) -> List[Pokemon]:
    """List all Pokemon (using _db_dict_to_pokemon) for a specific run.
    (This function is used by list_pokemon_by_run.)"""
    try:
        results = list(fetch_documents_by_query(DB_NAME, _COLLECTIONS_NAME, {'run_id': run_id}))
        return [_db_dict_to_pokemon(data) for data in results]
    except Exception as e:
        raise Exception(f"Failed to list Pokemon for run: {str(e)}")

def delete_run_pokemons(run_id: str) -> None:
    """Delete all Pokemon associated with a run (using delete_documents_by_query)."""
    try:
        delete_documents_by_query(DB_NAME, _COLLECTIONS_NAME, {'run_id': run_id})
    except Exception as e:
        raise Exception(f"Failed to delete Pokemon for run {run_id}: {str(e)}") 