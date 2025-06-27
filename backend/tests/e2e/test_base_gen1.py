from pokemendel_core.data.gen1 import PokemonGen1
from tests.e2e.helpers import (
    client_fixture,
    list_runs,
    list_lockes,
    start_locke_creation,
    continue_locke_creation_not_finished,
    continue_locke_creation_finished,
    get_run,
    save_run,
    get_starter_options,
    get_run_supported_pokemons,
    get_run_potential_encounters,
    choose_starter,
    encounter_pokemon,
    update_encounter,
    assert_run,
    assert_saved_run,
    assert_run_potential_pokemons,
)
import pytest


TEST_LOCKE = "BaseLocke"
TEST_GAME = "Blue"
RED_NUM_ENCOUNTER = 89
BLUE_NUM_ENCOUNTER = 93


def test_base_gen1(client_fixture):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture)
    _choose_starter(client_fixture, run_id)
    _catch_pokemon1(client_fixture, run_id)

    print("TEST Finished")


def _choose_starter(client_fixture, run_id):
    starter_options = get_starter_options(client_fixture, run_id)
    assert set(starter_options) == {'Bulbasaur', 'Charmander', 'Squirtle'}
    choose_starter(client_fixture, run_id, starter_options[0], starter_options[0])
    get_run_potential_encounters(client_fixture, run_id, None, BLUE_NUM_ENCOUNTER)
    run_response = get_run(client_fixture, run_id)
    run = run_response['run']
    assert run['starter']
    assert len(run['party']) == 1
    assert len(run['box']) == 1
    assert run['starter'] == run['party'][0] == run['box'][0]
    assert run['starter'] in run_response['pokemons']
    assert_pokemon(
        run_response=run_response,
        pokemon_id=run['starter'],
        pokemon_name=starter_options[0],
    )


def _create_run(client_fixture):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    start_locke_creation(client_fixture, TEST_LOCKE, TEST_GAME, True, False)
    continue_locke_creation_not_finished(client_fixture, None, None, 'GAME', TEST_GAME)
    run_id = continue_locke_creation_finished(client_fixture, 'GAME', TEST_GAME)
    assert_run_potential_pokemons(run_id, 151)
    run_response = get_run(client_fixture, run_id)
    assert_run(
        run_response=run_response,
        id=run_id,
        party_size=0,
        box_size=0,
        won_gyms=0,
        won_elites=0,
        num_encounters=0,
        starter=None
    )
    assert_saved_run(run_id, 0, 0, 0, 0, None)

    get_run_supported_pokemons(client_fixture, run_id, 151)
    get_run_potential_encounters(client_fixture, run_id, None, BLUE_NUM_ENCOUNTER)
    return run_id


def _catch_pokemon1(client_fixture, run_id):
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, "Route 2", 3)
    assert PokemonGen1.CATERPIE in potential_encounters
    assert PokemonGen1.PIKACHU not in potential_encounters
    encounter_pokemon(client_fixture, run_id, "Route 2", PokemonGen1.CATERPIE)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 1
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == "Route 2")
    assert encounter['pokemon'] == PokemonGen1.CATERPIE
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, "Route 2", "Caught")
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 2
    assert len(run_response['run']['party']) == 2
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == "Route 2")
    assert_pokemon(
        run_response=run_response,
        pokemon_id=encounter['pokemon'],
        pokemon_name=PokemonGen1.CATERPIE,
    )


def assert_pokemon(run_response: dict, pokemon_id: str, pokemon_name: str, nickname: str = ''):
    assert pokemon_id in run_response['pokemons']
    run_pokemon = run_response['pokemons'][pokemon_id]
    assert run_pokemon['name'] == pokemon_name
    assert run_pokemon['metadata']['id'] == pokemon_id
    assert run_pokemon['metadata']['nickname'] == nickname


if __name__ == '__main__':
    pytest.main([__file__])

