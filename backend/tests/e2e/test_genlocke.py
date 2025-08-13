from core.lockes.lockes_factory import *
from core.lockes.genlocke.run_creator import _GEN_TO_REGION
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


@pytest.mark.parametrize("locke,extra_info,relevant_games_gens", [
    (BaseLocke.name, False, [2, 3]),
    (CastformLocke.name, False, [3]),
    (CategoryLocke.name, True, [2, 3]),
    (ChessLocke.name, False, [2, 3]),
    (ColorLocke.name, True, [2, 3]),
    (DeoxysLocke.name, False, [1, 3]),
    (EeveeLocke.name, False, [2, 3]),
    (LegLocke.name, True, [2, 3]),
    (MonoLocke.name, True, [2, 3]),
    (StarLocke.name, True, [2, 3]),
    (UniqueLocke.name, False, [2, 3]),
    (WedLocke.name, False, [2, 3]),
    (WrapLocke.name, False, [2, 3]),
])
def test_base_gen(client_fixture, locke, extra_info, relevant_games_gens):
    run_id = _create_run(client_fixture, GEN3_GAME_NAME, locke, extra_info, relevant_games_gens)
    assert run_id


def _create_run(client_fixture, game_name, locke, extra_info, relevant_games_gens):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    with pytest.raises(AssertionError, match=f"Failed to continue run creation with game {game_name}"):
        start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)

    continue_locke_creation_not_finished(client_fixture, None, None, '_selected_locke', locke)
    continue_locke_creation_not_finished(client_fixture, '_selected_locke', locke, "GAME", "Fire Red")
    if extra_info:
        continue_locke_creation_not_finished(client_fixture, "GAME", "Fire Red", None, None)
        return "run_id"
    return continue_locke_creation_finished(client_fixture, "GAME", "Fire Red")


if __name__ == '__main__':
    pytest.main([__file__])

