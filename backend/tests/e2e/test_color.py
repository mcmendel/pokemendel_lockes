from pokemendel_core.data.gen2 import PokemonGen2
from pokemendel_core.utils.definitions.colors import Colors
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


TEST_LOCKE = "ColorLocke"


@pytest.mark.parametrize("test_color,potential_starters,starter_name,num_encounters,starter_has_evolution", [
    (Colors.RED, {PokemonGen2.CYNDAQUIL}, PokemonGen2.CYNDAQUIL, 30, True),
    (Colors.BLUE, {PokemonGen2.CYNDAQUIL, PokemonGen2.TOTODILE}, PokemonGen2.CYNDAQUIL, 40, True),
    (Colors.GREEN, {PokemonGen2.CHIKORITA}, PokemonGen2.CHIKORITA, 22, True),
    (Colors.YELLOW, {PokemonGen2.CHIKORITA, PokemonGen2.CYNDAQUIL, PokemonGen2.TOTODILE}, PokemonGen2.CHIKORITA, 37, True),
    (Colors.PURPLE, {PokemonGen2.ZUBAT, PokemonGen2.STARYU, PokemonGen2.SNEASEL, PokemonGen2.VENONAT, PokemonGen2.SMOOCHUM, PokemonGen2.SUICUNE, PokemonGen2.MEWTWO, PokemonGen2.SHELLDER, PokemonGen2.AERODACTYL, PokemonGen2.RATTATA, PokemonGen2.NIDORAN_M, PokemonGen2.EKANS, PokemonGen2.KOFFING, PokemonGen2.MANTINE, PokemonGen2.AIPOM, PokemonGen2.TYROGUE, PokemonGen2.GASTLY, PokemonGen2.GRIMER, PokemonGen2.CATERPIE}, PokemonGen2.AERODACTYL, 23, False),
    (Colors.BROWN, {PokemonGen2.WEEDLE, PokemonGen2.VULPIX, PokemonGen2.TEDDIURSA, PokemonGen2.TAUROS, PokemonGen2.SWINUB, PokemonGen2.SUNKERN, PokemonGen2.STARYU, PokemonGen2.STANTLER, PokemonGen2.SUDOWOODO, PokemonGen2.SQUIRTLE, PokemonGen2.SPEAROW, PokemonGen2.SANDSHREW, PokemonGen2.SENTRET, PokemonGen2.SMEARGLE, PokemonGen2.RATTATA, PokemonGen2.PINSIR, PokemonGen2.PIDGEY, PokemonGen2.OMANYTE, PokemonGen2.MANKEY, PokemonGen2.TYROGUE, PokemonGen2.KANGASKHAN, PokemonGen2.KABUTO, PokemonGen2.GIRAFARIG, PokemonGen2.HOOTHOOT, PokemonGen2.FARFETCHD, PokemonGen2.EXEGGCUTE, PokemonGen2.ENTEI, PokemonGen2.ABRA, PokemonGen2.CUBONE, PokemonGen2.DIGLETT, PokemonGen2.EEVEE, PokemonGen2.DODUO, PokemonGen2.DROWZEE}, PokemonGen2.DROWZEE, 31, False),
    (Colors.BLACK, {PokemonGen2.WEEDLE, PokemonGen2.SPINARAK, PokemonGen2.SHELLDER, PokemonGen2.UNOWN, PokemonGen2.RAIKOU, PokemonGen2.PICHU, PokemonGen2.PHANPY, PokemonGen2.MAREEP, PokemonGen2.KABUTO, PokemonGen2.HOUNDOUR, PokemonGen2.MURKROW, PokemonGen2.LEDYBA, PokemonGen2.GROWLITHE, PokemonGen2.GASTLY, PokemonGen2.EEVEE, PokemonGen2.GOLDEEN, PokemonGen2.ELEKID}, PokemonGen2.EEVEE, 18, True),
    (Colors.WHITE, {PokemonGen2.CYNDAQUIL}, PokemonGen2.CYNDAQUIL, 57, True),
    (Colors.GRAY, {PokemonGen2.SLUGMA, PokemonGen2.PHANPY, PokemonGen2.MEWTWO, PokemonGen2.SLOWPOKE, PokemonGen2.SKARMORY, PokemonGen2.RHYHORN, PokemonGen2.SHELLDER, PokemonGen2.PINECO, PokemonGen2.ONIX, PokemonGen2.MAGNEMITE, PokemonGen2.GEODUDE, PokemonGen2.ENTEI, PokemonGen2.MACHOP, PokemonGen2.LARVITAR, PokemonGen2.AERODACTYL, PokemonGen2.LAPRAS}, PokemonGen2.LAPRAS, 16, False),
    (Colors.ORANGE, {PokemonGen2.PICHU, PokemonGen2.PARAS, PokemonGen2.CHARMANDER, PokemonGen2.DRATINI, PokemonGen2.MOLTRES, PokemonGen2.KRABBY, PokemonGen2.GROWLITHE, PokemonGen2.GOLDEEN}, PokemonGen2.DRATINI, 7, True),
    (Colors.PINK, {PokemonGen2.CHIKORITA}, PokemonGen2.CHIKORITA, 14, True),
])
def test_base_gen2(client_fixture, test_color, potential_starters, starter_name, num_encounters, starter_has_evolution):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture, GEN2_GAME_NAME, test_color)
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


def _create_run(client_fixture, game_name, test_category):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)
    continue_locke_creation_not_finished(client_fixture, None, None, 'GAME', game_name)
    continue_locke_creation_not_finished(client_fixture, 'GAME', game_name, "color_type", test_category)
    run_id = continue_locke_creation_finished(client_fixture, "color_type", test_category)
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

