from pokemendel_core.data.gen1 import PokemonGen1
from pokemendel_core.data.gen2 import PokemonGen2
from tests.e2e.gen1_helpers import GAME_NAME as GEN1_GAME_NAME
from tests.e2e.gen2_helpers import GAME_NAME as GEN2_GAME_NAME
from tests.e2e.helpers import (
    client_fixture,
    list_runs,
    list_lockes,
    start_locke_creation,
    continue_locke_creation_not_finished,
    continue_locke_creation_finished,
    get_run,
    save_run,
    load_run,
    get_starter_options,
    get_run_supported_pokemons,
    get_run_potential_encounters,
    choose_starter,
    encounter_pokemon,
    update_encounter,
    get_next_actions,
    get_action_options,
    execute_action,
    win_battle,
    finish_run,
    assert_run,
    assert_saved_run,
    assert_run_potential_pokemons,
    assert_pokemon,
)
import pytest


TEST_LOCKE = "StarterLocke"


@pytest.mark.parametrize("gen,game_name,expected_pokemons", [
    (1, "Blue", {PokemonGen1.BULBASAUR, PokemonGen1.CHARMANDER, PokemonGen1.SQUIRTLE}),
    (2, "Crystal", {PokemonGen2.BULBASAUR, PokemonGen2.CHARMANDER, PokemonGen2.SQUIRTLE,PokemonGen2.CHIKORITA, PokemonGen2.CYNDAQUIL, PokemonGen2.TOTODILE}),
])
def test_starter(client_fixture, gen, game_name, expected_pokemons):
    run_id = _create_run(client_fixture, game_name)

    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == len(expected_pokemons)
    starter_id = run_response['run']['starter']
    assert run_response['pokemons'][starter_id]['name'] in expected_pokemons
    all_pokemons = {
        run_response['pokemons'][pokemon_id]['name']
        for pokemon_id in run_response['pokemons'].keys()
    }
    assert all_pokemons == expected_pokemons

   # nickname starter
    next_actions = get_next_actions(client_fixture, run_id, starter_id)
    assert next_actions == ["Nickname Pokemon"]
    nickname_options = get_action_options(client_fixture, run_id, starter_id, "Nickname Pokemon")
    assert nickname_options == {
        "input_options": [],
        "input_type": "Free text"
    }
    execute_action(client_fixture, run_id, starter_id, "Nickname Pokemon", "mystarter")

    if gen >= 2:
        # nickname starter
        next_actions = get_next_actions(client_fixture, run_id, starter_id)
        assert next_actions == ["Gender"]
        nickname_options = get_action_options(client_fixture, run_id, starter_id, "Gender")
        assert nickname_options == {
            "input_options": ["Male", "Female"],
            "input_type": "One of"
        }
        execute_action(client_fixture, run_id, starter_id, "Gender", "Male")
    # regular actions - can evolve!
    next_actions = get_next_actions(client_fixture, run_id, starter_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]


def _create_run(client_fixture, game_name):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)
    continue_locke_creation_not_finished(client_fixture, None, None, 'GAME', game_name)
    run_id = continue_locke_creation_finished(client_fixture, 'GAME', game_name, all_pokemons_caught=True)
    return run_id


def _verify_run_created_with_eevolutions(client_fixture, run_id, eevee_name, expected_eevolutions):
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == len(expected_eevolutions) + 1
    eevee_id = run_response['run']['starter']
    assert run_response['pokemons'][eevee_id]['name'] == eevee_name
    expected_eevolutions.add(eevee_name)
    all_eevolutions = {
        run_response['pokemons'][pokemon_id]['name']
        for pokemon_id in run_response['pokemons'].keys()
    }
    assert all_eevolutions == expected_eevolutions
    return eevee_id


if __name__ == '__main__':
    pytest.main([__file__])

