from pokemendel_core.data.gen1 import PokemonGen1
from pokemendel_core.data.gen2 import PokemonGen2
from pokemendel_core.utils.definitions.types import Types
from tests.e2e.gen1_helpers import (
    GAME_NAME as GEN1_GAME_NAME,
    NUM_POKEMONS as GEN1_NUM_POKEMONS,
    NUM_ENCOUNTERS as GEN1_NUM_ENCOUNTERS,
    STARTERS as GEN1_STARTERS,
)
from tests.e2e.gen2_helpers import (
    GAME_NAME as GEN2_GAME_NAME,
    NUM_POKEMONS as GEN2_NUM_POKEMONS,
    NUM_ENCOUNTERS as GEN2_NUM_ENCOUNTERS,
    STARTERS as GEN2_STARTERS,
)
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


TEST_LOCKE = "UniqueLocke"


def test_base_gen2(client_fixture):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture, GEN2_GAME_NAME)
    starter_id = _choose_starter(
        client_fixture=client_fixture,
        run_id=run_id,
        expected_starter_options=GEN2_STARTERS,
        starter_name=PokemonGen2.TOTODILE,
        starter_has_evolution=True,
        num_encounters=GEN2_NUM_ENCOUNTERS - 1,
        nickname="Eligabler",
        gender="Male"
    )
    pidgey_id = _catch_pokemon1(client_fixture, run_id)
    spearow_id = _catch_pokemon2(client_fixture, run_id)

    # spearow can replace only pidgey
    nickname_options = get_action_options(client_fixture, run_id, spearow_id, "Replace Pokemon with Party")
    assert nickname_options == {
        "input_options": [pidgey_id],
        "input_type": "One of"
    }
    execute_action(client_fixture, run_id, spearow_id, "Replace Pokemon with Party", pidgey_id)
    caterpie_id = _catch_pokemon3(client_fixture, run_id)

    # caterpie can evolve to metapod
    evolution_options = get_action_options(client_fixture, run_id, caterpie_id, "Evolve Pokemon")
    assert evolution_options == {
        "input_options": [PokemonGen2.METAPOD],
        "input_type": "One of"
    }
    execute_action(client_fixture, run_id, caterpie_id, "Evolve Pokemon", PokemonGen2.METAPOD)

    # metapod cannot evolve to butterfree since spearow is in party
    next_actions = get_next_actions(client_fixture, run_id, caterpie_id)
    assert next_actions == ["Remove from Party", "Kill Pokemon"]

    # try to evolve butterfree after removing spearow
    execute_action(client_fixture, run_id, spearow_id, "Remove from Party", "")
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 4
    assert len(run_response['run']['party']) == 2
    next_actions = get_next_actions(client_fixture, run_id, caterpie_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    print("TEST Finished")


def _create_run(client_fixture, game_name):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)
    continue_locke_creation_not_finished(client_fixture, None, None, 'GAME', game_name)
    run_id = continue_locke_creation_finished(client_fixture, 'GAME', game_name)
    return run_id


def _choose_starter(client_fixture, run_id, expected_starter_options, starter_name, starter_has_evolution, num_encounters, nickname, gender=None):
    starter_options = get_starter_options(client_fixture, run_id)
    if len(expected_starter_options) <= 3:
        assert set(starter_options) == expected_starter_options
    else:
        assert all(x in expected_starter_options for x in starter_options), starter_options
    choose_starter(client_fixture, run_id, starter_name, starter_name)
    get_run_potential_encounters(client_fixture, run_id, None, num_encounters)
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
        pokemon_name=starter_name,
        is_pokemon_in_party=True,
        nickname=nickname,
    )
    next_actions = get_next_actions(client_fixture, run_id, starter_id)
    if gender:
        assert next_actions == ["Gender"]
        gender_options = get_action_options(client_fixture, run_id, starter_id, "Gender")
        assert gender_options["input_type"] == "One of"
        assert gender in gender_options["input_options"]
        execute_action(client_fixture, run_id, starter_id, "Gender", gender)
        next_actions = get_next_actions(client_fixture, run_id, starter_id)

    expected_next_actions = ['Evolve Pokemon', "Kill Pokemon"] if starter_has_evolution else ["Kill Pokemon"]

    assert next_actions == expected_next_actions
    return starter_id


def _catch_pokemon1(client_fixture, run_id):
    pokemon_name = PokemonGen2.PIDGEY
    route = "Route 29"
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, route, 20)
    assert pokemon_name in potential_encounters
    assert PokemonGen1.PIKACHU not in potential_encounters
    encounter_pokemon(client_fixture, run_id, route, pokemon_name)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 1
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == pokemon_name
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, route, "Caught")
    run_response = get_run(client_fixture, run_id)
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    encounter_id = encounter['pokemon']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=2,
        num_party=2,
        pokemon_id=encounter_id,
        pokemon_name=pokemon_name,
        is_pokemon_in_party=True,
        nickname="Diara",
        gender="Male"
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    return encounter_id


def _catch_pokemon2(client_fixture, run_id):
    pokemon_name = PokemonGen2.SPEAROW
    route = "Route 46"
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, route, 15)
    assert pokemon_name in potential_encounters
    assert PokemonGen1.PIKACHU not in potential_encounters
    encounter_pokemon(client_fixture, run_id, route, pokemon_name)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 2
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == pokemon_name
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, route, "Caught")
    run_response = get_run(client_fixture, run_id)
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    encounter_id = encounter['pokemon']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=3,
        num_party=2,
        pokemon_id=encounter_id,
        pokemon_name=pokemon_name,
        is_pokemon_in_party=False,
        nickname="Sharp",
        gender="Female"
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Replace Pokemon with Party", "Kill Pokemon"]
    return encounter_id


def _catch_pokemon3(client_fixture, run_id):
    pokemon_name = PokemonGen2.CATERPIE
    route = "Route 30"
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, route, 24)
    assert pokemon_name in potential_encounters
    assert PokemonGen1.PIKACHU not in potential_encounters
    encounter_pokemon(client_fixture, run_id, route, pokemon_name)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 3
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == pokemon_name
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, route, "Caught")
    run_response = get_run(client_fixture, run_id)
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    encounter_id = encounter['pokemon']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=4,
        num_party=3,
        pokemon_id=encounter_id,
        pokemon_name=pokemon_name,
        is_pokemon_in_party=True,
        nickname="Twist",
        gender="Female"
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    return encounter_id


def _handle_caught_pokemon(client, run_response: dict, run_id: str, num_box: int, num_party: int, pokemon_id: str, pokemon_name: str, is_pokemon_in_party: bool, nickname: str, gender: str = None):
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

    if gender:
        next_actions = get_next_actions(client, run_id, pokemon_id)
        assert next_actions == ["Gender"]
        gender_options = get_action_options(client, run_id, pokemon_id, "Gender")
        assert gender_options["input_type"] == "One of"
        assert gender in gender_options["input_options"]
        execute_action(client, run_id, pokemon_id, "Gender", gender)
        run_response = get_run(client, run_id)
        assert_pokemon(
            run_response=run_response,
            pokemon_id=pokemon_id,
            pokemon_name=pokemon_name,
            nickname=nickname,
            gender=gender,
        )


if __name__ == '__main__':
    pytest.main([__file__])

