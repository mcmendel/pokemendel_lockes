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


TEST_LOCKE = "MonoLocke"


@pytest.mark.parametrize("test_type,potential_starters,starter_name,num_encounters,starter_has_evolution", [
    (Types.NORMAL, {PokemonGen1.RATTATA, PokemonGen1.CHANSEY, PokemonGen1.CLEFAIRY, PokemonGen1.DITTO, PokemonGen1.DODUO, PokemonGen1.EEVEE, PokemonGen1.FARFETCHD, PokemonGen1.JIGGLYPUFF, PokemonGen1.KANGASKHAN, PokemonGen1.LICKITUNG, PokemonGen1.MEOWTH, PokemonGen1.PIDGEY, PokemonGen1.PORYGON, PokemonGen1.SNORLAX, PokemonGen1.SPEAROW, PokemonGen1.TAUROS}, PokemonGen2.RATTATA, 16, True),
    (Types.BUG, {PokemonGen1.WEEDLE, PokemonGen1.SCYTHER, PokemonGen1.CATERPIE, PokemonGen1.VENONAT, PokemonGen1.PARAS, PokemonGen1.PINSIR}, PokemonGen1.CATERPIE, 7, True),
    (Types.FIRE, {PokemonGen1.CHARMANDER}, PokemonGen1.CHARMANDER, 5, True),
    (Types.ICE, {PokemonGen1.JYNX, PokemonGen1.ARTICUNO, PokemonGen1.LAPRAS, PokemonGen1.SEEL, PokemonGen1.SHELLDER}, PokemonGen1.ARTICUNO, 5, False),
    (Types.ROCK, {PokemonGen1.RHYHORN, PokemonGen1.ONIX, PokemonGen1.AERODACTYL, PokemonGen1.GEODUDE, PokemonGen1.KABUTO, PokemonGen1.OMANYTE}, PokemonGen1.AERODACTYL, 6, False),
    (Types.DRAGON, {PokemonGen1.DRATINI}, PokemonGen1.DRATINI, 0, True),
    (Types.FIGHTING, {PokemonGen1.POLIWAG, PokemonGen1.HITMONLEE, PokemonGen1.HITMONCHAN, PokemonGen1.MACHOP, PokemonGen1.MANKEY}, PokemonGen1.HITMONLEE, 5, False),
    (Types.POISON, {PokemonGen1.BULBASAUR}, PokemonGen1.BULBASAUR, 17, True),
    (Types.PSYCHIC, {PokemonGen1.JYNX, PokemonGen1.ABRA, PokemonGen1.STARYU, PokemonGen1.DROWZEE, PokemonGen1.SLOWPOKE, PokemonGen1.EXEGGCUTE, PokemonGen1.MEW, PokemonGen1.MEWTWO, PokemonGen1.MR_MIME}, PokemonGen1.ABRA, 6, True),
    (Types.FLYING, {PokemonGen1.CHARMANDER}, PokemonGen1.CHARMANDER, 15, True),
    (Types.GRASS, {PokemonGen1.BULBASAUR}, PokemonGen1.BULBASAUR, 6, True),
    (Types.GROUND, {PokemonGen1.SANDSHREW, PokemonGen1.DIGLETT, PokemonGen1.CUBONE, PokemonGen1.RHYHORN, PokemonGen1.GEODUDE, PokemonGen1.NIDORAN_F, PokemonGen1.NIDORAN_M, PokemonGen1.ONIX}, PokemonGen1.CUBONE, 10, True),
    (Types.ELECTRIC, {PokemonGen1.ELECTABUZZ, PokemonGen1.EEVEE, PokemonGen1.ZAPDOS, PokemonGen1.VOLTORB, PokemonGen1.MAGNEMITE, PokemonGen1.PIKACHU}, PokemonGen1.PIKACHU, 6, True),
    (Types.GHOST, {PokemonGen1.GASTLY}, PokemonGen1.GASTLY, 0, True),
    (Types.WATER, {PokemonGen1.SQUIRTLE}, PokemonGen1.SQUIRTLE, 22, True),
])
def test_base_gen1(client_fixture, test_type, potential_starters, starter_name, num_encounters, starter_has_evolution):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture, GEN1_GAME_NAME, test_type)
    starter_id = _choose_starter(
        client_fixture=client_fixture,
        run_id=run_id,
        expected_starter_options=potential_starters,
        starter_name=starter_name,
        starter_has_evolution=starter_has_evolution,
        num_encounters=num_encounters,
        nickname="mystarter",
    )
    print("TEST Finished")


@pytest.mark.parametrize("test_type,potential_starters,starter_name,num_encounters,starter_has_evolution", [
    (Types.NORMAL, {PokemonGen2.TEDDIURSA, PokemonGen2.SPEAROW, PokemonGen2.TOGEPI, PokemonGen2.SENTRET, PokemonGen2.STANTLER, PokemonGen2.TAUROS, PokemonGen2.CHANSEY, PokemonGen2.SNORLAX, PokemonGen2.SNUBBULL, PokemonGen2.SMEARGLE, PokemonGen2.RATTATA, PokemonGen2.PORYGON, PokemonGen2.PIDGEY, PokemonGen2.MILTANK, PokemonGen2.LICKITUNG, PokemonGen2.MEOWTH, PokemonGen2.KANGASKHAN, PokemonGen2.IGGLYBUFF, PokemonGen2.HOOTHOOT, PokemonGen2.GIRAFARIG, PokemonGen2.FARFETCHD, PokemonGen2.EEVEE, PokemonGen2.AIPOM, PokemonGen2.CLEFFA, PokemonGen2.DITTO, PokemonGen2.DODUO, PokemonGen2.DUNSPARCE}, PokemonGen2.EEVEE, 28, False),
    (Types.BUG, {PokemonGen2.YANMA, PokemonGen2.WEEDLE, PokemonGen2.SPINARAK, PokemonGen2.SHUCKLE, PokemonGen2.VENONAT, PokemonGen2.SCYTHER, PokemonGen2.PINECO, PokemonGen2.PINSIR, PokemonGen2.PARAS, PokemonGen2.CATERPIE, PokemonGen2.LEDYBA, PokemonGen2.HERACROSS}, PokemonGen2.CATERPIE, 16, True),
    (Types.FIRE, {PokemonGen2.CYNDAQUIL}, PokemonGen2.CYNDAQUIL, 5, True),
    (Types.ICE, {PokemonGen2.SNEASEL, PokemonGen2.SMOOCHUM, PokemonGen2.SWINUB, PokemonGen2.SEEL, PokemonGen2.SHELLDER, PokemonGen2.ARTICUNO, PokemonGen2.DELIBIRD, PokemonGen2.LAPRAS}, PokemonGen2.LAPRAS, 8, False),
    (Types.ROCK, {PokemonGen2.SUDOWOODO, PokemonGen2.SLUGMA, PokemonGen2.SHUCKLE, PokemonGen2.RHYHORN, PokemonGen2.ONIX, PokemonGen2.OMANYTE, PokemonGen2.KABUTO, PokemonGen2.LARVITAR, PokemonGen2.AERODACTYL, PokemonGen2.CORSOLA, PokemonGen2.GEODUDE}, PokemonGen2.ONIX, 7, False),
    (Types.DRAGON, {PokemonGen2.DRATINI, PokemonGen2.HORSEA}, PokemonGen2.DRATINI, 2, True),
    (Types.FIGHTING, {PokemonGen2.POLIWAG, PokemonGen2.MANKEY, PokemonGen2.MACHOP, PokemonGen2.HERACROSS, PokemonGen2.TYROGUE}, PokemonGen2.HERACROSS, 5, False),
    (Types.POISON, {PokemonGen2.ZUBAT, PokemonGen2.WEEDLE, PokemonGen2.VENONAT, PokemonGen2.TENTACOOL, PokemonGen2.SPINARAK, PokemonGen2.QWILFISH, PokemonGen2.NIDORAN_M, PokemonGen2.NIDORAN_F, PokemonGen2.KOFFING, PokemonGen2.GRIMER, PokemonGen2.GASTLY, PokemonGen2.EKANS, PokemonGen2.ODDISH, PokemonGen2.BELLSPROUT, PokemonGen2.BULBASAUR}, PokemonGen2.ODDISH, 18, True),
    (Types.PSYCHIC, {PokemonGen2.UNOWN, PokemonGen2.WOBBUFFET, PokemonGen2.STARYU, PokemonGen2.SMOOCHUM, PokemonGen2.SLOWPOKE, PokemonGen2.NATU, PokemonGen2.MR_MIME, PokemonGen2.MEW, PokemonGen2.MEWTWO, PokemonGen2.LUGIA, PokemonGen2.GIRAFARIG, PokemonGen2.EXEGGCUTE, PokemonGen2.DROWZEE, PokemonGen2.ABRA, PokemonGen2.CELEBI, PokemonGen2.EEVEE}, PokemonGen2.EEVEE, 13, True),
    (Types.FLYING, {PokemonGen2.CHARMANDER, PokemonGen2.ZUBAT, PokemonGen2.TOGEPI, PokemonGen2.YANMA, PokemonGen2.ZAPDOS, PokemonGen2.SPEAROW, PokemonGen2.SKARMORY, PokemonGen2.SCYTHER, PokemonGen2.PIDGEY, PokemonGen2.NATU, PokemonGen2.MOLTRES, PokemonGen2.MURKROW, PokemonGen2.MANTINE, PokemonGen2.MAGIKARP, PokemonGen2.LUGIA, PokemonGen2.LEDYBA, PokemonGen2.HOPPIP, PokemonGen2.HOOTHOOT, PokemonGen2.CATERPIE, PokemonGen2.HO_OH, PokemonGen2.GLIGAR, PokemonGen2.FARFETCHD, PokemonGen2.AERODACTYL, PokemonGen2.ARTICUNO, PokemonGen2.DELIBIRD, PokemonGen2.DODUO, PokemonGen2.DRATINI}, PokemonGen2.AERODACTYL, 30, False),
    (Types.GRASS, {PokemonGen2.CHIKORITA}, PokemonGen2.CHIKORITA, 9, True),
    (Types.GROUND, {PokemonGen2.WOOPER, PokemonGen2.SWINUB, PokemonGen2.SANDSHREW, PokemonGen2.RHYHORN, PokemonGen2.PHANPY, PokemonGen2.ONIX, PokemonGen2.NIDORAN_M, PokemonGen2.NIDORAN_F, PokemonGen2.LARVITAR, PokemonGen2.GLIGAR, PokemonGen2.CUBONE, PokemonGen2.DIGLETT, PokemonGen2.GEODUDE}, PokemonGen2.CUBONE, 13, True),
    (Types.ELECTRIC, {PokemonGen2.VOLTORB, PokemonGen2.RAIKOU, PokemonGen2.ZAPDOS, PokemonGen2.MAREEP, PokemonGen2.MAGNEMITE, PokemonGen2.EEVEE, PokemonGen2.CHINCHOU, PokemonGen2.ELEKID, PokemonGen2.PICHU}, PokemonGen2.PICHU, 7, True),
    (Types.GHOST, {PokemonGen2.MISDREAVUS, PokemonGen2.GASTLY}, PokemonGen2.GASTLY, 0, True),
    (Types.WATER, {PokemonGen2.TOTODILE}, PokemonGen2.TOTODILE, 29, True),
    (Types.DARK, {PokemonGen2.EEVEE, PokemonGen2.SNEASEL, PokemonGen2.MURKROW, PokemonGen2.LARVITAR, PokemonGen2.HOUNDOUR}, PokemonGen2.HOUNDOUR,  2, True),
    (Types.STEEL, {PokemonGen2.SKARMORY, PokemonGen2.SCYTHER, PokemonGen2.PINECO, PokemonGen2.MAGNEMITE, PokemonGen2.ONIX}, PokemonGen2.ONIX, 4, True),
])
def test_base_gen2(client_fixture, test_type, potential_starters, starter_name, num_encounters, starter_has_evolution):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture, GEN2_GAME_NAME, test_type)
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


def _create_run(client_fixture, game_name, mono_type):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)
    continue_locke_creation_not_finished(client_fixture, None, None, 'GAME', game_name)
    continue_locke_creation_not_finished(client_fixture, 'GAME', game_name, "mono_type", mono_type)
    run_id = continue_locke_creation_finished(client_fixture, "mono_type", mono_type)
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

