from pokemendel_core.data.gen1 import PokemonGen1
from pokemendel_core.data.gen2 import PokemonGen2
from pokemendel_core.utils.definitions.categories import Categories
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


TEST_LOCKE = "CategoryLocke"


@pytest.mark.parametrize("test_category,potential_starters,starter_name,num_encounters,starter_has_evolution", [
    (Categories.APE, {PokemonGen2.MANKEY, PokemonGen2.ABRA, PokemonGen2.AIPOM}, PokemonGen2.MANKEY, 2, True),
    (Categories.BEAR, {PokemonGen2.SNORLAX, PokemonGen2.TEDDIURSA}, PokemonGen2.SNORLAX, 2, False),
    (Categories.BIRD, {PokemonGen2.HO_OH, PokemonGen2.DELIBIRD, PokemonGen2.NATU, PokemonGen2.HOOTHOOT, PokemonGen2.MOLTRES, PokemonGen2.MURKROW, PokemonGen2.PIDGEY, PokemonGen2.SPEAROW, PokemonGen2.ARTICUNO, PokemonGen2.ZAPDOS, PokemonGen2.MAGBY, PokemonGen2.FARFETCHD, PokemonGen2.DODUO, PokemonGen2.PSYDUCK}, PokemonGen2.PIDGEY, 12, True),
    (Categories.BUG, {PokemonGen2.SLUGMA, PokemonGen2.HERACROSS, PokemonGen2.GLIGAR, PokemonGen2.YANMA, PokemonGen2.SPINARAK, PokemonGen2.LEDYBA, PokemonGen2.PSYDUCK, PokemonGen2.CATERPIE, PokemonGen2.WEEDLE, PokemonGen2.SCYTHER, PokemonGen2.PINSIR, PokemonGen2.VENONAT, PokemonGen2.DIGLETT}, PokemonGen2.CATERPIE, 14, True),
    (Categories.BUNNY, {PokemonGen2.NIDORAN_F, PokemonGen2.NIDORAN_M}, PokemonGen2.NIDORAN_F, 0, True),
    (Categories.CAT, {PokemonGen2.MEOWTH, PokemonGen2.RAIKOU, PokemonGen2.ENTEI, PokemonGen2.SUICUNE}, PokemonGen2.MEOWTH, 3, True),
    (Categories.CATTLE, {PokemonGen2.MILTANK, PokemonGen2.MAREEP, PokemonGen2.TAUROS}, PokemonGen2.TAUROS, 1, False),
    (Categories.COW, {PokemonGen2.TAUROS, PokemonGen2.MILTANK}, PokemonGen2.TAUROS, 1, False),
    (Categories.CRAB, {PokemonGen2.PARAS, PokemonGen2.KRABBY, PokemonGen2.KABUTO}, PokemonGen2.PARAS, 2, True),
    (Categories.DOG, {PokemonGen2.HOUNDOUR, PokemonGen2.SNUBBULL, PokemonGen2.SMEARGLE, PokemonGen2.EEVEE, PokemonGen2.VULPIX, PokemonGen2.GROWLITHE, PokemonGen2.SEEL}, PokemonGen2.VULPIX, 5, True),
    (Categories.DRAGON, {PokemonGen2.YANMA, PokemonGen2.LUGIA, PokemonGen2.DRATINI, PokemonGen2.MAGIKARP, PokemonGen2.CHARMANDER, PokemonGen2.HORSEA}, PokemonGen2.CHARMANDER, 8, True),
    (Categories.DUCK, {PokemonGen2.MAGBY, PokemonGen2.PSYDUCK, PokemonGen2.FARFETCHD}, PokemonGen2.PSYDUCK, 2, True),
    (Categories.FANTASY, {PokemonGen2.DELIBIRD, PokemonGen2.CELEBI, PokemonGen2.LAPRAS, PokemonGen2.SMOOCHUM, PokemonGen2.LARVITAR, PokemonGen2.MURKROW, PokemonGen2.CLEFFA, PokemonGen2.DRATINI}, PokemonGen2.CLEFFA, 7, True),
    (Categories.FISH, {PokemonGen2.MANTINE, PokemonGen2.CHINCHOU, PokemonGen2.HORSEA, PokemonGen2.REMORAID, PokemonGen2.QWILFISH, PokemonGen2.GOLDEEN, PokemonGen2.MAGIKARP}, PokemonGen2.HORSEA, 6, True),
    (Categories.FOOD, {PokemonGen2.MANTINE, PokemonGen2.SLUGMA, PokemonGen2.STANTLER, PokemonGen2.MILTANK, PokemonGen2.MAREEP, PokemonGen2.SWINUB, PokemonGen2.TOGEPI, PokemonGen2.SHUCKLE, PokemonGen2.UNOWN, PokemonGen2.DITTO, PokemonGen2.GOLDEEN, PokemonGen2.TANGELA, PokemonGen2.KABUTO, PokemonGen2.OMANYTE, PokemonGen2.TAUROS, PokemonGen2.MAGBY, PokemonGen2.MAGIKARP, PokemonGen2.CHANSEY, PokemonGen2.EXEGGCUTE, PokemonGen2.NIDORAN_M, PokemonGen2.KRABBY, PokemonGen2.PARAS, PokemonGen2.SHELLDER, PokemonGen2.TENTACOOL, PokemonGen2.FARFETCHD, PokemonGen2.GEODUDE, PokemonGen2.PSYDUCK, PokemonGen2.IGGLYBUFF, PokemonGen2.ODDISH, PokemonGen2.SQUIRTLE, PokemonGen2.SPEAROW, PokemonGen2.REMORAID, PokemonGen2.POLIWAG, PokemonGen2.NIDORAN_F, PokemonGen2.PIDGEY, PokemonGen2.EKANS}, PokemonGen2.ODDISH, 35, False),
    (Categories.FROG, {PokemonGen2.WOOPER, PokemonGen2.BULBASAUR, PokemonGen2.POLIWAG, PokemonGen2.LICKITUNG}, PokemonGen2.BULBASAUR, 5, True),
    (Categories.HORSE, {PokemonGen2.PONYTA}, PokemonGen2.PONYTA, 0, True),
    (Categories.HUMAN, {PokemonGen2.SMOOCHUM, PokemonGen2.MEWTWO, PokemonGen2.MISDREAVUS , PokemonGen2.ODDISH, PokemonGen2.CLEFFA, PokemonGen2.ELEKID, PokemonGen2.MACHOP, PokemonGen2.MR_MIME, PokemonGen2.CHANSEY, PokemonGen2.TYROGUE, PokemonGen2.DROWZEE}, PokemonGen2.CLEFFA, 8, True),
    (Categories.ITEM, {PokemonGen2.ELEKID, PokemonGen2.SKARMORY, PokemonGen2.CORSOLA, PokemonGen2.WOBBUFFET, PokemonGen2.TOGEPI, PokemonGen2.GASTLY, PokemonGen2.UNOWN, PokemonGen2.IGGLYBUFF, PokemonGen2.PORYGON, PokemonGen2.VOLTORB, PokemonGen2.STARYU, PokemonGen2.DITTO, PokemonGen2.GEODUDE, PokemonGen2.KOFFING, PokemonGen2.MAGNEMITE, PokemonGen2.GRIMER}, PokemonGen2.IGGLYBUFF, 15, True),
    (Categories.MAMMAL, {PokemonGen2.CYNDAQUIL}, PokemonGen2.CYNDAQUIL, 39, True),
    (Categories.MOUSE, {PokemonGen2.MARILL, PokemonGen2.RATTATA, PokemonGen2.PICHU, PokemonGen2.MEW, PokemonGen2.SANDSHREW}, PokemonGen2.RATTATA, 4, True),
    (Categories.PIG, {PokemonGen2.SWINUB, PokemonGen2.DROWZEE}, PokemonGen2.DROWZEE, 1, True),
    (Categories.PLANT, {PokemonGen2.CHIKORITA}, PokemonGen2.CHIKORITA, 10, True),
    (Categories.PREHISTORIC, {PokemonGen2.CHIKORITA}, PokemonGen2.CHIKORITA, 8, True),
    (Categories.REPTILE, {PokemonGen2.CHIKORITA, PokemonGen2.TOTODILE}, PokemonGen2.CHIKORITA, 14, True),
    (Categories.RODENT, {PokemonGen2.MARILL, PokemonGen2.MEW, PokemonGen2.RATTATA, PokemonGen2.PICHU, PokemonGen2.SANDSHREW}, PokemonGen2.RATTATA, 4, True),
    (Categories.SLOTH, {PokemonGen2.SLOWPOKE}, PokemonGen2.SLOWPOKE, 0, True),
    (Categories.SNAKE, {PokemonGen2.ONIX, PokemonGen2.EKANS, PokemonGen2.DRATINI, PokemonGen2.DUNSPARCE}, PokemonGen2.EKANS, 4, True),
    (Categories.TURTLE, {PokemonGen2.SHUCKLE, PokemonGen2.SQUIRTLE, PokemonGen2.LAPRAS, PokemonGen2.GEODUDE,}, PokemonGen2.SQUIRTLE, 4, True),
    (Categories.WATERMON, {PokemonGen2.TOTODILE}, PokemonGen2.TOTODILE, 35, True),
    (Categories.WEAPON, {PokemonGen2.SKARMORY, PokemonGen2.SQUIRTLE, PokemonGen2.SCYTHER, PokemonGen2.WEEDLE, PokemonGen2.KABUTO, PokemonGen2.NIDORAN_M, PokemonGen2.CUBONE, PokemonGen2.FARFETCHD}, PokemonGen2.FARFETCHD, 6, False),
    (Categories.WING, {PokemonGen2.CELEBI, PokemonGen2.HO_OH, PokemonGen2.LUGIA, PokemonGen2.SKARMORY, PokemonGen2.HERACROSS, PokemonGen2.NATU, PokemonGen2.MANTINE, PokemonGen2.TOGEPI, PokemonGen2.MURKROW, PokemonGen2.YANMA, PokemonGen2.LEDYBA, PokemonGen2.HOOTHOOT, PokemonGen2.DODUO, PokemonGen2.SCYTHER, PokemonGen2.DRATINI, PokemonGen2.ARTICUNO, PokemonGen2.PSYDUCK, PokemonGen2.ZAPDOS, PokemonGen2.MOLTRES, PokemonGen2.AERODACTYL, PokemonGen2.VENONAT, PokemonGen2.CHARMANDER, PokemonGen2.FARFETCHD, PokemonGen2.CATERPIE, PokemonGen2.ZUBAT, PokemonGen2.SPEAROW, PokemonGen2.CLEFFA, PokemonGen2.WEEDLE, PokemonGen2.PIDGEY}, PokemonGen2.CHARMANDER, 35, True),
])
def test_base_gen2(client_fixture, test_category, potential_starters, starter_name, num_encounters, starter_has_evolution):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture, GEN2_GAME_NAME, test_category)
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
    continue_locke_creation_not_finished(client_fixture, 'GAME', game_name, "category_type", test_category)
    run_id = continue_locke_creation_finished(client_fixture, "category_type", test_category)
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

