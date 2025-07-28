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


TEST_LOCKE = "EeveeLocke"


def test_base_gen1(client_fixture):
    run_id = _create_run(client_fixture, GEN1_GAME_NAME)
    eevee_id = _verify_run_created_with_eevolutions(
        client_fixture=client_fixture,
        run_id=run_id,
        eevee_name=PokemonGen1.EEVEE,
        expected_eevolutions={
            PokemonGen1.VAPOREON,
            PokemonGen1.FLAREON,
            PokemonGen1.JOLTEON,
        }
    )

   # nickname starter
    next_actions = get_next_actions(client_fixture, run_id, eevee_id)
    assert next_actions == ["Nickname Pokemon"]
    nickname_options = get_action_options(client_fixture, run_id, eevee_id, "Nickname Pokemon")
    assert nickname_options == {
        "input_options": [],
        "input_type": "Free text"
    }
    execute_action(client_fixture, run_id, eevee_id, "Nickname Pokemon", "mystarter")
    # regular actions - can't evolve!
    next_actions = get_next_actions(client_fixture, run_id, eevee_id)
    assert next_actions == ["Remove from Party", "Kill Pokemon"]


def test_base_gen2(client_fixture):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture, GEN2_GAME_NAME)
    eevee_id = _verify_run_created_with_eevolutions(
        client_fixture=client_fixture,
        run_id=run_id,
        eevee_name=PokemonGen2.EEVEE,
        expected_eevolutions={
            PokemonGen2.VAPOREON,
            PokemonGen2.FLAREON,
            PokemonGen2.JOLTEON,
            PokemonGen2.ESPEON,
            PokemonGen2.UMBREON,
        }
    )

    # nickname starter
    next_actions = get_next_actions(client_fixture, run_id, eevee_id)
    assert next_actions == ["Nickname Pokemon"]
    nickname_options = get_action_options(client_fixture, run_id, eevee_id, "Nickname Pokemon")
    assert nickname_options == {
        "input_options": [],
        "input_type": "Free text"
    }
    execute_action(client_fixture, run_id, eevee_id, "Nickname Pokemon", "mystarter")

    # choose gender
    next_actions = get_next_actions(client_fixture, run_id, eevee_id)
    assert next_actions == ["Gender"]
    nickname_options = get_action_options(client_fixture, run_id, eevee_id, "Gender")
    assert nickname_options == {
        "input_options": ["Male", "Female"],
        "input_type": "One of"
    }
    execute_action(client_fixture, run_id, eevee_id, "Gender", "Male")

    # regular actions - can't evolve!
    next_actions = get_next_actions(client_fixture, run_id, eevee_id)
    assert next_actions == ["Remove from Party", "Kill Pokemon"]

    # # spearow can replace only pidgey
    # nickname_options = get_action_options(client_fixture, run_id, spearow_id, "Replace Pokemon with Party")
    # assert nickname_options == {
    #     "input_options": [pidgey_id],
    #     "input_type": "One of"
    # }
    # execute_action(client_fixture, run_id, spearow_id, "Replace Pokemon with Party", pidgey_id)
    # caterpie_id = _catch_pokemon3(client_fixture, run_id)
    #
    # # caterpie can evolve to metapod
    # evolution_options = get_action_options(client_fixture, run_id, caterpie_id, "Evolve Pokemon")
    # assert evolution_options == {
    #     "input_options": [PokemonGen2.METAPOD],
    #     "input_type": "One of"
    # }
    # execute_action(client_fixture, run_id, caterpie_id, "Evolve Pokemon", PokemonGen2.METAPOD)
    #
    # # metapod cannot evolve to butterfree since spearow is in party
    # next_actions = get_next_actions(client_fixture, run_id, caterpie_id)
    # assert next_actions == ["Remove from Party", "Kill Pokemon"]
    #
    # # try to evolve butterfree after removing spearow
    # execute_action(client_fixture, run_id, spearow_id, "Remove from Party", "")
    # run_response = get_run(client_fixture, run_id)
    # assert len(run_response['run']['box']) == 4
    # assert len(run_response['run']['party']) == 2
    # next_actions = get_next_actions(client_fixture, run_id, caterpie_id)
    # assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    print("TEST Finished")


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

