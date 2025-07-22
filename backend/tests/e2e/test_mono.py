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
)
import pytest


TEST_LOCKE = "MonoLocke"
RED_NUM_ENCOUNTER = 89
BLUE_NUM_ENCOUNTER = 93


@pytest.mark.parametrize("test_type", [
    Types.NORMAL,
    Types.BUG,
    Types.FIRE,
    Types.ICE,
    Types.ROCK,
    Types.DRAGON,
    Types.FIGHTING,
    Types.POISON,
    Types.PSYCHIC,
    Types.FLYING,
    Types.GRASS,
    Types.GROUND,
    Types.ELECTRIC,
    Types.GHOST,
    Types.WATER,
])
def test_base_gen1(client_fixture, test_type):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture, GEN1_GAME_NAME, test_type)
    print("TEST Finished")


def _create_run(client_fixture, game_name, mono_type):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)
    continue_locke_creation_not_finished(client_fixture, None, None, 'GAME', game_name)
    continue_locke_creation_not_finished(client_fixture, 'GAME', game_name, "mono_type", mono_type)
    run_id = continue_locke_creation_finished(client_fixture, "mono_type", mono_type)
    return run_id


if __name__ == '__main__':
    pytest.main([__file__])

