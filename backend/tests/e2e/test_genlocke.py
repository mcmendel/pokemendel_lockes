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
    (BaseLocke.name, False, [1, 2, 3]),
    (CastformLocke.name, False, [1, 3]),
    (CategoryLocke.name, True, [1, 2, 3]),
    (ChessLocke.name, False, [1, 2, 3]),
    (ColorLocke.name, True, [1, 2, 3]),
    (DeoxysLocke.name, False, [1, 3]),
    (EeveeLocke.name, False, [1, 2, 3]),
    (LegLocke.name, True, [1, 2, 3]),
    (MonoLocke.name, True, [1, 2, 3]),
    (StarLocke.name, True, [1, 2, 3]),
    (UniqueLocke.name, False, [1, 2, 3]),
    (WedLocke.name, False, [1, 2, 3]),
    (WrapLocke.name, False, [1, 2, 3]),
])
def test_base_gen(client_fixture, locke, extra_info, relevant_games_gens):
    run_id = _create_run(client_fixture, GEN3_GAME_NAME, locke, extra_info, relevant_games_gens)


def _create_run(client_fixture, game_name, locke, extra_info, relevant_games_gens):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    with pytest.raises(AssertionError, match=f"Failed to continue run creation with game {game_name}"):
        start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)

    last_gen = max(_GEN_TO_REGION.keys())
    continue_locke_creation_not_finished(client_fixture, None, None, '_selected_locke', locke)
    continue_locke_creation_not_finished(client_fixture, '_selected_locke', locke, "_game_1", "Fire Red")
    for idx, relevant_gen in enumerate(relevant_games_gens):
        assert relevant_gen <= last_gen
        if relevant_gen < last_gen:
            next_gen = relevant_games_gens[idx + 1]
            continue_locke_creation_not_finished(
                client_fixture,
                f"_game_{relevant_gen}", _GEN_TO_GAME[relevant_gen],
                f"_game_{next_gen}", _GEN_TO_GAME[next_gen],
            )
            continue
        if extra_info:
            continue_locke_creation_not_finished(
                client_fixture, f"_game_{last_gen}", _GEN_TO_GAME[last_gen], None, None
            )
        else:
            return continue_locke_creation_finished(client_fixture, f"_game_{last_gen}", _GEN_TO_GAME[last_gen])
    return None


if __name__ == '__main__':
    pytest.main([__file__])

