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
    starter_id = _choose_starter(client_fixture, run_id)
    caterpie_id = _catch_pokemon1(client_fixture, run_id)
    evolve_pokemon(client_fixture, run_id, caterpie_id, PokemonGen1.METAPOD, "Lilly")
    save_run(client_fixture, run_id)
    win_battle(client_fixture, run_id, 'Brock')
    evolve_pokemon(client_fixture, run_id, starter_id, PokemonGen1.CHARMELEON, "Sandra")
    save_run(client_fixture, run_id)
    geodude_id = _catch_pokemon2(client_fixture, run_id)
    save_run(client_fixture, run_id)
    bellsprout_id = _catch_pokemon3(client_fixture, run_id)
    _kill_pokemon(
        client_fixture=client_fixture,
        run_id=run_id,
        pokemon_id=caterpie_id,
        num_party=3,
        num_box=4,
    )
    save_run(client_fixture, run_id)
    _kill_pokemon(
        client_fixture=client_fixture,
        run_id=run_id,
        pokemon_id=bellsprout_id,
        num_party=2,
        num_box=4,
    )
    run_response = load_run(client_fixture, run_id)
    assert_run(
        run_response=run_response,
        id=run_id,
        party_size=3,
        box_size=4,
        won_gyms=12,
        num_encounters=3,
        starter=PokemonGen1.CHARMELEON,
        num_restarts=1,
    )
    save_run(client_fixture, run_id)
    win_battle(client_fixture, run_id, 'Misty')
    _ran_pokemon1(client_fixture, run_id)
    drowzee_id = _catch_pokemon4(client_fixture, run_id)
    execute_action(client_fixture, run_id, geodude_id, "Remove from Party", "")
    run_response = get_run(client_fixture, run_id)
    assert_run(
        run_response=run_response,
        id=run_id,
        party_size=3,
        box_size=5,
        won_gyms=12,
        num_encounters=5,
        starter=PokemonGen1.CHARMELEON,
        num_restarts=1,
    )
    next_actions = get_next_actions(client_fixture, run_id, geodude_id)
    assert next_actions == ["Add to Party", "Replace Pokemon with Party", "Evolve Pokemon", "Kill Pokemon"]
    action_options = get_action_options(client_fixture, run_id, geodude_id, "Replace Pokemon with Party")
    assert action_options['input_type'] == 'One of'
    assert set(action_options['input_options']) == {starter_id, bellsprout_id, drowzee_id}
    execute_action(client_fixture, run_id, geodude_id, "Replace Pokemon with Party", drowzee_id)
    run_response = get_run(client_fixture, run_id)
    assert_run(
        run_response=run_response,
        id=run_id,
        party_size=3,
        box_size=5,
        won_gyms=12,
        num_encounters=5,
        starter=PokemonGen1.CHARMELEON,
        num_restarts=1,
    )
    execute_action(client_fixture, run_id, drowzee_id, "Add to Party", "")
    run_response = get_run(client_fixture, run_id)
    assert_run(
        run_response=run_response,
        id=run_id,
        party_size=4,
        box_size=5,
        won_gyms=12,
        num_encounters=5,
        starter=PokemonGen1.CHARMELEON,
        num_restarts=1,
    )
    win_battle(client_fixture, run_id, 'Lt. Surge')
    gastly_id = _catch_pokemon5(client_fixture, run_id)
    vulpix_id = _catch_pokemon6(client_fixture, run_id)
    save_run(client_fixture, run_id)
    win_battle(client_fixture, run_id, 'Erika')
    machop_id = _catch_pokemon7(client_fixture, run_id)
    win_battle(client_fixture, run_id, 'Sabrina')
    save_run(client_fixture, run_id)
    win_battle(client_fixture, run_id, 'Koga')
    tangela_id = _catch_pokemon8(client_fixture, run_id)
    save_run(client_fixture, run_id)
    win_battle(client_fixture, run_id, 'Blaine')
    save_run(client_fixture, run_id)
    win_battle(client_fixture, run_id, 'Giovanni')
    save_run(client_fixture, run_id)
    win_battle(client_fixture, run_id, 'Lorelei')
    win_battle(client_fixture, run_id, 'Bruno')
    win_battle(client_fixture, run_id, 'Agatha')
    win_battle(client_fixture, run_id, 'Lance')
    finish_run(client_fixture, run_id)

    print("TEST Finished")


def _choose_starter(client_fixture, run_id):
    starter_options = get_starter_options(client_fixture, run_id)
    assert set(starter_options) == {'Bulbasaur', 'Charmander', 'Squirtle'}
    choose_starter(client_fixture, run_id, PokemonGen1.CHARMANDER, PokemonGen1.CHARMANDER)
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
        pokemon_name=PokemonGen1.CHARMANDER,
        is_pokemon_in_party=True,
        nickname="Sandra",
    )
    next_actions = get_next_actions(client_fixture, run_id, starter_id)
    assert next_actions == ['Evolve Pokemon', "Kill Pokemon"]
    return starter_id


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
        won_gyms=12,
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
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    return encounter_id


def _catch_pokemon2(client_fixture, run_id):
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, "Mt. Moon", 6)
    assert PokemonGen1.GEODUDE in potential_encounters
    encounter_pokemon(client_fixture, run_id, "Mt. Moon", PokemonGen1.GEODUDE)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 2
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == "Mt. Moon")
    assert encounter['pokemon'] == PokemonGen1.GEODUDE
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, "Mt. Moon", "Caught")
    run_response = get_run(client_fixture, run_id)
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == "Mt. Moon")
    encounter_id = encounter['pokemon']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=3,
        num_party=3,
        pokemon_id=encounter_id,
        pokemon_name=PokemonGen1.GEODUDE,
        is_pokemon_in_party=True,
        nickname="Fairplay",
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    return encounter_id


def _catch_pokemon3(client_fixture, run_id):
    route = "Route 24"
    pokemon_to_catch = PokemonGen1.BELLSPROUT
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, route, 8)
    assert pokemon_to_catch in potential_encounters
    encounter_pokemon(client_fixture, run_id, route, pokemon_to_catch)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 3
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == pokemon_to_catch
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
        num_party=4,
        pokemon_id=encounter_id,
        pokemon_name=pokemon_to_catch,
        is_pokemon_in_party=True,
        nickname="Derrah",
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    return encounter_id


def _catch_pokemon4(client_fixture, run_id):
    route = "Route 11"
    pokemon_to_catch = PokemonGen1.DROWZEE
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, route, 9)
    assert pokemon_to_catch in potential_encounters
    encounter_pokemon(client_fixture, run_id, route, pokemon_to_catch)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 4
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == pokemon_to_catch
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, route, "Caught")
    run_response = get_run(client_fixture, run_id)
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    encounter_id = encounter['pokemon']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=5,
        num_party=4,
        pokemon_id=encounter_id,
        pokemon_name=pokemon_to_catch,
        is_pokemon_in_party=True,
        nickname="X1",
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    return encounter_id


def _catch_pokemon5(client_fixture, run_id):
    route = "Pokemon Tower"
    pokemon_to_catch = PokemonGen1.GASTLY
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, route, 3)
    assert pokemon_to_catch in potential_encounters
    encounter_pokemon(client_fixture, run_id, route, pokemon_to_catch)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 5
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == pokemon_to_catch
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, route, "Caught")
    run_response = get_run(client_fixture, run_id)
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    encounter_id = encounter['pokemon']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=6,
        num_party=5,
        pokemon_id=encounter_id,
        pokemon_name=pokemon_to_catch,
        is_pokemon_in_party=True,
        nickname="X1",
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    return encounter_id


def _catch_pokemon6(client_fixture, run_id):
    route = "Route 7"
    pokemon_to_catch = PokemonGen1.VULPIX
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, route, 3)
    assert pokemon_to_catch in potential_encounters
    encounter_pokemon(client_fixture, run_id, route, pokemon_to_catch)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 6
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == pokemon_to_catch
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, route, "Caught")
    run_response = get_run(client_fixture, run_id)
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    encounter_id = encounter['pokemon']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=7,
        num_party=6,
        pokemon_id=encounter_id,
        pokemon_name=pokemon_to_catch,
        is_pokemon_in_party=True,
        nickname="X1",
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    return encounter_id


def _catch_pokemon7(client_fixture, run_id):
    route = "Rock Tunnel"
    pokemon_to_catch = PokemonGen1.MACHOP
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, route, 3)
    assert pokemon_to_catch in potential_encounters
    encounter_pokemon(client_fixture, run_id, route, pokemon_to_catch)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 7
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == pokemon_to_catch
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, route, "Caught")
    run_response = get_run(client_fixture, run_id)
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    encounter_id = encounter['pokemon']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=8,
        num_party=6,
        pokemon_id=encounter_id,
        pokemon_name=pokemon_to_catch,
        is_pokemon_in_party=False,
        nickname="x4",
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Replace Pokemon with Party", "Evolve Pokemon", "Kill Pokemon"]
    return encounter_id


def _catch_pokemon8(client_fixture, run_id):
    route = "Pallet Town"
    pokemon_to_catch = PokemonGen1.TANGELA
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, route, 5)
    assert pokemon_to_catch in potential_encounters
    encounter_pokemon(client_fixture, run_id, route, pokemon_to_catch)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 8
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == pokemon_to_catch
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, route, "Caught")
    run_response = get_run(client_fixture, run_id)
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    encounter_id = encounter['pokemon']
    _handle_caught_pokemon(
        client=client_fixture,
        run_response=run_response,
        run_id=run_id,
        num_box=9,
        num_party=6,
        pokemon_id=encounter_id,
        pokemon_name=pokemon_to_catch,
        is_pokemon_in_party=False,
        nickname="x5",
    )
    next_actions = get_next_actions(client_fixture, run_id, encounter_id)
    assert next_actions == ["Replace Pokemon with Party", "Kill Pokemon"]
    return encounter_id


def _ran_pokemon1(client_fixture, run_id):
    route = "Diglet's Cave"
    pokemon_to_catch = PokemonGen1.DIGLETT
    potential_encounters = get_run_potential_encounters(client_fixture, run_id, route, 2)
    assert pokemon_to_catch in potential_encounters
    encounter_pokemon(client_fixture, run_id, route, pokemon_to_catch)
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['run']['box']) == 4
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == pokemon_to_catch
    assert encounter['status'] == "Met"
    update_encounter(client_fixture, run_id, route, "Ran")
    run_response = get_run(client_fixture, run_id)
    encounter = next(encounter for encounter in run_response['run']['encounters'] if encounter['route'] == route)
    assert encounter['pokemon'] == PokemonGen1.DIGLETT
    assert encounter['status'] == 'Ran'


def _kill_pokemon(client_fixture, run_id, pokemon_id, num_party, num_box):
    execute_action(client_fixture, run_id, pokemon_id, "Kill Pokemon", "")
    run_response = get_run(client_fixture, run_id)
    assert pokemon_id in run_response['pokemons']
    run_pokemon = run_response['pokemons'][pokemon_id]
    assert run_pokemon['status'] == 'dead'
    assert len(run_response['run']['party']) == num_party
    assert len(run_response['run']['box']) == num_box


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
    assert run_pokemon['status'] == 'alive'


def evolve_pokemon(client, run_id, pokemon_id, evolution_name, nickname):
    execute_action(client, run_id, pokemon_id, "Evolve Pokemon", evolution_name)
    run_response = get_run(client, run_id)
    assert_pokemon(
        run_response=run_response,
        pokemon_id=pokemon_id,
        pokemon_name=evolution_name,
        nickname=nickname,
    )


if __name__ == '__main__':
    pytest.main([__file__])

