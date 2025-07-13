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
    get_next_actions,
    get_action_options,
    execute_action,
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
    starter_id = run['starter']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=1,
        num_party=1,
        pokemon_id=run['starter'],
        pokemon_name=starter_options[0],
        is_pokemon_in_party=True,
        nickname="Sandra",
    )
    next_actions = get_next_actions(client_fixture, run_id, starter_id)
    assert next_actions == ['Evolve Pokemon']


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
        won_gyms=8,
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
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == "Route 2")
    encounter_id = encounter['pokemon']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=2,
        num_party=2,
        pokemon_id=encounter_id,
        pokemon_name=PokemonGen1.CATERPIE,
        is_pokemon_in_party=True,
        nickname="Lilly",
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon"]


def _handle_caught_pokemon(client, run_response: dict, run_id: str, num_box: int, num_party: int, pokemon_id: str, pokemon_name: str, is_pokemon_in_party: bool, nickname: str):
    assert len(run_response['run']['box']) == num_box
    assert len(run_response['run']['party']) == num_party
    assert pokemon_id in run_response['run']['box']
    assert bool(pokemon_id in run_response['run']['party']) == is_pokemon_in_party
    assert_pokemon(
        run_response=run_response,
        pokemon_id=pokemon_id,
        pokemon_name=pokemon_name,
    )
    next_actions = get_next_actions(client, run_id, pokemon_id)
    assert next_actions == ["Nickname Pokemon"]

    nickname_options = get_action_options(client, run_id, pokemon_id, "Nickname Pokemon")
    assert nickname_options == {
        "input_options": [],
        "input_type": "Free text"
    }
    execute_action(client, run_id, pokemon_id, "Nickname Pokemon", nickname)
    run_response = get_run(client, run_id)
    assert_pokemon(
        run_response=run_response,
        pokemon_id=pokemon_id,
        pokemon_name=pokemon_name,
        nickname=nickname,
    )


def assert_pokemon(run_response: dict, pokemon_id: str, pokemon_name: str, nickname: str = ''):
    assert pokemon_id in run_response['pokemons']
    run_pokemon = run_response['pokemons'][pokemon_id]
    assert run_pokemon['name'] == pokemon_name
    assert run_pokemon['metadata']['id'] == pokemon_id
    assert run_pokemon['metadata']['nickname'] == nickname


if __name__ == '__main__':
    pytest.main([__file__])

