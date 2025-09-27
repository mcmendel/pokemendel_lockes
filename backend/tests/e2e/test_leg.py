from pokemendel_core.data.gen2 import PokemonGen2
from core.lockes.leg.utils import LEG_TYPE_KEY, NumLegs
from tests.e2e.gen2_helpers import GAME_NAME as GEN2_GAME_NAME
from tests.e2e.helpers import (
    client_fixture,
    list_runs,
    list_lockes,
    start_locke_creation,
    continue_locke_creation_not_finished,
    continue_locke_creation_finished,
    get_run,
    get_starter_options,
    get_run_potential_encounters,
    choose_starter,
    get_next_actions,
    get_action_options,
    execute_action,
    assert_pokemon,
)
import pytest


TEST_LOCKE = "LegLocke"


@pytest.mark.parametrize("test_num_legs,potential_starters,starter_name,num_encounters,starter_has_evolution", [
    (NumLegs.ZERO, {PokemonGen2.LARVITAR, PokemonGen2.STARYU, PokemonGen2.TENTACOOL, PokemonGen2.WEEDLE, PokemonGen2.ZUBAT, PokemonGen2.VOLTORB, PokemonGen2.OMANYTE, PokemonGen2.VENONAT, PokemonGen2.UNOWN, PokemonGen2.SUNKERN, PokemonGen2.SLUGMA, PokemonGen2.SHUCKLE, PokemonGen2.SEEL, PokemonGen2.SHELLDER, PokemonGen2.REMORAID, PokemonGen2.QWILFISH, PokemonGen2.PORYGON, PokemonGen2.PINECO, PokemonGen2.MISDREAVUS, PokemonGen2.MANTINE, PokemonGen2.ONIX, PokemonGen2.MAGNEMITE, PokemonGen2.MAGIKARP, PokemonGen2.LAPRAS, PokemonGen2.KABUTO, PokemonGen2.KOFFING, PokemonGen2.HORSEA, PokemonGen2.GRIMER, PokemonGen2.GASTLY, PokemonGen2.GEODUDE, PokemonGen2.EXEGGCUTE, PokemonGen2.GOLDEEN, PokemonGen2.EKANS, PokemonGen2.DUNSPARCE, PokemonGen2.DRATINI, PokemonGen2.DIGLETT, PokemonGen2.DITTO, PokemonGen2.BELLSPROUT, PokemonGen2.CATERPIE, PokemonGen2.CHINCHOU}, PokemonGen2.EXEGGCUTE, 41, False),
    # (NumLegs.ONE, {}, PokemonGen2., 0, True),
    (NumLegs.TWO, {PokemonGen2.TOTODILE}, PokemonGen2.TOTODILE, 79, True),
    (NumLegs.FOUR, {PokemonGen2.CYNDAQUIL, PokemonGen2.CHIKORITA}, PokemonGen2.CYNDAQUIL, 29, True),
    (NumLegs.OTHER, {PokemonGen2.WEEDLE, PokemonGen2.LEDYBA, PokemonGen2.YANMA, PokemonGen2.TENTACOOL, PokemonGen2.REMORAID, PokemonGen2.SPINARAK, PokemonGen2.CATERPIE, PokemonGen2.OMANYTE, PokemonGen2.GLIGAR}, PokemonGen2.CATERPIE, 4, False),
])
def test_base_gen2(client_fixture, test_num_legs, potential_starters, starter_name, num_encounters, starter_has_evolution):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture, GEN2_GAME_NAME, test_num_legs)
    starter_id = _choose_starter(
        client_fixture=client_fixture,
        run_id=run_id,
        expected_starter_options=potential_starters,
        starter_name=starter_name,
        starter_has_evolution=starter_has_evolution,
        num_encounters=num_encounters,
        nickname="mystarter",
        gender="Male",
    )
    print("TEST Finished")


def _create_run(client_fixture, game_name, test_num_legs):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)
    continue_locke_creation_not_finished(client_fixture, None, None, 'GAME', game_name)
    continue_locke_creation_not_finished(client_fixture, 'GAME', game_name, LEG_TYPE_KEY, test_num_legs)
    run_id = continue_locke_creation_finished(client_fixture, LEG_TYPE_KEY, test_num_legs)
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

