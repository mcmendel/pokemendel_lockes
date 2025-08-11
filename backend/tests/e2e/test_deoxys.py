from pokemendel_core.data.gen3 import PokemonGen3
from pokemendel_core.utils.definitions.natures import Natures
from pokemendel_core.utils.definitions.abilities import Abilities
from tests.e2e.gen3_helpers import GAME_NAME as GEN3_GAME_NAME
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


TEST_LOCKE = "DeoxysLocke"


def test_base_gen3(client_fixture):
    run_id = _create_run(client_fixture, GEN3_GAME_NAME)
    deoxys_id = _verify_run_created(
        client_fixture=client_fixture,
        run_id=run_id,
    )

   # nickname starter
    next_actions = get_next_actions(client_fixture, run_id, deoxys_id)
    assert next_actions == ["Nickname Pokemon"]
    nickname_options = get_action_options(client_fixture, run_id, deoxys_id, "Nickname Pokemon")
    assert nickname_options == {
        "input_options": [],
        "input_type": "Free text"
    }
    execute_action(client_fixture, run_id, deoxys_id, "Nickname Pokemon", "mystarter")

    # verify mandatory actions
    ### 1. gender
    next_actions = get_next_actions(client_fixture, run_id, deoxys_id)
    assert next_actions == ['Gender', 'Nature', 'Ability']
    action_options = get_action_options(client_fixture, run_id, deoxys_id, "Gender")
    assert action_options == {
        "input_options": ["Genderless"],
        "input_type": "One of"
    }
    execute_action(client_fixture, run_id, deoxys_id, "Gender", "Genderless")
    run_response = get_run(client_fixture, run_id)
    assert run_response["pokemons"][deoxys_id]["metadata"]["gender"] == "Genderless"

    ### 2. nature
    next_actions = get_next_actions(client_fixture, run_id, deoxys_id)
    assert next_actions == ['Nature', 'Ability']
    action_options = get_action_options(client_fixture, run_id, deoxys_id, "Nature")
    assert action_options["input_type"] == "One of"
    assert len(action_options["input_options"]) == len(Natures.list_all())
    assert "Docile" in action_options["input_options"]
    execute_action(client_fixture, run_id, deoxys_id, "Nature", "Docile")
    run_response = get_run(client_fixture, run_id)
    assert run_response["pokemons"][deoxys_id]["nature"] == "Docile"

    ### 3. ability
    next_actions = get_next_actions(client_fixture, run_id, deoxys_id)
    assert next_actions == ['Ability']
    action_options = get_action_options(client_fixture, run_id, deoxys_id, "Ability")
    assert action_options == {
        "input_options": [Abilities.PRESSURE],
        "input_type": "One of"
    }
    execute_action(client_fixture, run_id, deoxys_id, "Ability", Abilities.PRESSURE)
    run_response = get_run(client_fixture, run_id)
    assert run_response["pokemons"][deoxys_id]["metadata"]["ability"] == Abilities.PRESSURE

    # run actions
    next_actions = get_next_actions(client_fixture, run_id, deoxys_id)
    assert next_actions == ["Remove from Party", "Kill Pokemon"]


def _create_run(client_fixture, game_name):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)
    continue_locke_creation_not_finished(client_fixture, None, None, 'GAME', game_name)
    run_id = continue_locke_creation_finished(client_fixture, 'GAME', game_name, all_pokemons_caught=True)
    return run_id


def _verify_run_created(client_fixture, run_id):
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 4  # deoxys and its 3 forms
    deoxys_id = run_response['run']['starter']
    assert run_response['pokemons'][deoxys_id]['name'] == PokemonGen3.DEOXYS

    all_pokemons = {
        run_response['pokemons'][pokemon_id]['name']
        for pokemon_id in run_response['pokemons'].keys()
    }
    assert all_pokemons == {PokemonGen3.DEOXYS}
    return deoxys_id


if __name__ == '__main__':
    pytest.main([__file__])

