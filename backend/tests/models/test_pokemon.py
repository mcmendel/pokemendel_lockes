"""Tests for Pokemon database operations."""

import pytest
from datetime import datetime
from unittest.mock import patch, MagicMock
from models.pokemon import (
    save_pokemon,
    update_pokemon,
    fetch_pokemon,
    list_pokemon_by_run,
    delete_run_pokemons,
    _create_pokemon_document,
    _db_dict_to_pokemon,
    Pokemon
)
from definitions.pokemons.pokemon import Pokemon as PokemonDef
from definitions.pokemons.pokemon_metadata import PokemonMetadata
from definitions.pokemons.pokemon_status import PokemonStatus
from pokemendel_core.utils.definitions.genders import Genders
from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.models.pokemon import Pokemon as CorePokemon

# Test data
TEST_RUN_ID = "test_run_123"
TEST_POKEMON_ID = "test_pokemon_123"
TEST_NICKNAME = "TestMon"
TEST_POKEMON_NAME = "Charmander"
TEST_GEN = 1
TEST_TYPES = [Types.FIRE]

@pytest.fixture
def sample_pokemon():
    """Create a sample Pokemon for testing."""
    # Create metadata
    metadata = PokemonMetadata(
        id=TEST_POKEMON_ID,
        nickname=TEST_NICKNAME,
        caught_index=1,
        starlocke_type=Types.FIRE,
        gender=Genders.MALE,
        paired_partner=None
    )
    
    # Create our Pokemon with metadata and status
    return Pokemon(
        name=TEST_POKEMON_NAME,
        gen=TEST_GEN,
        types=[Types.FIRE],
        metadata=metadata,
        status=PokemonStatus.ALIVE
    )

@pytest.fixture
def sample_db_dict():
    """Create a sample database dictionary for testing."""
    return {
        "_id": TEST_POKEMON_ID,
        "run_id": TEST_RUN_ID,
        "nickname": TEST_NICKNAME,
        "caught_index": 1,
        "starlocke_type": "Fire",  # Use string value
        "gender": "Male",         # Use string value
        "paired_partner": None,
        "status": "alive",  # Status value as string
        "name": TEST_POKEMON_NAME,
        "gen": TEST_GEN,
        "types": ["Fire"]
    }

def test_create_pokemon_document(sample_pokemon):
    """Test converting a Pokemon to a database dictionary."""
    result = _create_pokemon_document(TEST_RUN_ID, sample_pokemon)
    
    assert result["_id"] == TEST_POKEMON_ID
    assert result["run_id"] == TEST_RUN_ID
    assert result["nickname"] == TEST_NICKNAME
    assert result["caught_index"] == 1
    assert result["starlocke_type"] == "Fire"
    assert result["gender"] == "Male"
    assert result["paired_partner"] is None
    assert result["status"] == "alive"
    assert result["name"] == TEST_POKEMON_NAME
    assert result["gen"] == TEST_GEN
    assert result["types"] == ["Fire"]

def test_db_dict_to_pokemon(sample_db_dict):
    """Test converting a database dictionary to a Pokemon."""
    result = _db_dict_to_pokemon(sample_db_dict)
    
    assert result.metadata.id == TEST_POKEMON_ID
    assert result.metadata.nickname == TEST_NICKNAME
    assert result.metadata.caught_index == 1
    assert result.metadata.starlocke_type == Types.FIRE
    assert result.metadata.gender == Genders.MALE
    assert result.metadata.paired_partner is None
    assert result.status == "alive"
    assert result.name == TEST_POKEMON_NAME
    assert result.gen == 1
    assert result.types == [Types.FIRE]

@patch('models.pokemon.insert_document')
def test_save_pokemon(mock_insert, sample_pokemon):
    """Test saving a Pokemon to the database."""
    save_pokemon(sample_pokemon, TEST_RUN_ID)
    
    mock_insert.assert_called_once()
    args = mock_insert.call_args[0]
    assert args[0] == "locke_manager"  # DB_NAME
    assert args[1] == "pokemons"  # _COLLECTIONS_NAME
    assert args[2]["_id"] == TEST_POKEMON_ID
    assert args[2]["run_id"] == TEST_RUN_ID

@patch('models.pokemon.update_document_by_id')
def test_update_pokemon(mock_update, sample_pokemon):
    """Test updating a Pokemon in the database."""
    update_pokemon(sample_pokemon, TEST_RUN_ID)
    
    mock_update.assert_called_once()
    args = mock_update.call_args[0]
    assert args[0] == "locke_manager"  # DB_NAME
    assert args[1] == "pokemons"  # _COLLECTIONS_NAME
    assert args[2] == TEST_POKEMON_ID
    assert args[3]["_id"] == TEST_POKEMON_ID
    assert args[3]["run_id"] == TEST_RUN_ID

@patch('models.pokemon.fetch_documents_by_query')
def test_fetch_pokemon(mock_fetch, sample_db_dict):
    """Test fetching a Pokemon from the database."""
    mock_fetch.return_value = [sample_db_dict]
    
    result = fetch_pokemon(TEST_POKEMON_ID)
    
    assert result is not None
    assert result.metadata.id == TEST_POKEMON_ID
    assert result.metadata.nickname == TEST_NICKNAME
    mock_fetch.assert_called_once_with("locke_manager", "pokemons", {"_id": TEST_POKEMON_ID})

@patch('models.pokemon.fetch_documents_by_query')
def test_fetch_pokemon_not_found(mock_fetch):
    """Test fetching a non-existent Pokemon."""
    mock_fetch.return_value = []
    
    result = fetch_pokemon(TEST_POKEMON_ID)
    
    assert result is None
    mock_fetch.assert_called_once_with("locke_manager", "pokemons", {"_id": TEST_POKEMON_ID})

@patch('models.pokemon.fetch_documents_by_query')
def test_list_pokemon_by_run(mock_fetch, sample_db_dict):
    """Test listing Pokemon for a run."""
    mock_fetch.return_value = [sample_db_dict]
    
    results = list_pokemon_by_run(TEST_RUN_ID)
    
    assert len(results) == 1
    assert results[0].metadata.id == TEST_POKEMON_ID
    assert results[0].metadata.nickname == TEST_NICKNAME
    mock_fetch.assert_called_once_with("locke_manager", "pokemons", {"run_id": TEST_RUN_ID})

@patch('models.pokemon.delete_documents_by_query')
def test_delete_run_pokemons(mock_delete):
    """Test deleting all Pokemon for a run."""
    delete_run_pokemons(TEST_RUN_ID)
    
    mock_delete.assert_called_once_with("locke_manager", "pokemons", {"run_id": TEST_RUN_ID})

@pytest.mark.parametrize("operation,args,expected_error", [
    (save_pokemon, (MagicMock(), TEST_RUN_ID), "Failed to save Pokemon"),
    (update_pokemon, (MagicMock(), TEST_RUN_ID), "Failed to update Pokemon"),
    (fetch_pokemon, (TEST_POKEMON_ID,), "Failed to fetch Pokemon"),
    (list_pokemon_by_run, (TEST_RUN_ID,), "Failed to list Pokemon for run"),
    (delete_run_pokemons, (TEST_RUN_ID,), f"Failed to delete Pokemon for run {TEST_RUN_ID}")
])
@patch('models.pokemon.insert_document')
@patch('models.pokemon.update_document_by_id')
@patch('models.pokemon.fetch_documents_by_query')
@patch('models.pokemon.delete_documents_by_query')
def test_database_errors(mock_delete, mock_fetch, mock_update, mock_insert, operation, args, expected_error):
    """Test error handling for all database operations."""
    # Make all database operations raise an exception
    mock_insert.side_effect = Exception("Database error")
    mock_update.side_effect = Exception("Database error")
    mock_fetch.side_effect = Exception("Database error")
    mock_delete.side_effect = Exception("Database error")
    
    with pytest.raises(Exception) as exc_info:
        operation(*args)
    
    assert expected_error in str(exc_info.value) 