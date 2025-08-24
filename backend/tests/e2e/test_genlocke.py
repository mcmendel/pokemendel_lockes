from core.lockes.lockes_factory import *
from core.lockes.genlocke.utils import _GEN_TO_REGION
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


TEST_LOCKE = "GenLocke"

_GEN_TO_GAME = {
    1: "Fire Red",
    2: "Crystal",
    3: "Ruby",
}


@pytest.mark.parametrize("locke,extra_info,specific_pokemons", [
    (BaseLocke.name, False, False),
    (CastformLocke.name, False, True),
    (CategoryLocke.name, True, False),
    (ChessLocke.name, False, False),
    (ColorLocke.name, True, False),
    (DeoxysLocke.name, False, True),
    (EeveeLocke.name, False, True),
    (LegLocke.name, True, False),
    (MonoLocke.name, True, False),
    (StarLocke.name, True, False),
    (UniqueLocke.name, False, False),
    (WedLocke.name, False, False),
    (WrapLocke.name, False, False),
])
def test_base_gen(client_fixture, locke, extra_info, specific_pokemons):
    run_id = _create_run(client_fixture, GEN3_GAME_NAME, locke, extra_info, specific_pokemons)
    assert run_id


def _create_run(client_fixture, game_name, locke, extra_info, specific_pokemons):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    with pytest.raises(AssertionError, match=f"Failed to continue run creation with game {game_name}"):
        start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)

    continue_locke_creation_not_finished(client_fixture, None, None, '_selected_locke', locke)
    continue_locke_creation_not_finished(client_fixture, '_selected_locke', locke, "GAME", "Fire Red")
    if extra_info:
        continue_locke_creation_not_finished(client_fixture, "GAME", "Fire Red", None, None)
        return "run_id"
    return continue_locke_creation_finished(client_fixture, "GAME", "Fire Red", all_pokemons_caught=specific_pokemons)


if __name__ == '__main__':
    pytest.main([__file__])

