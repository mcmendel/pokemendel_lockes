from pokemendel_core.data.gen3 import PokemonGen3
from pokemendel_core.utils.definitions.natures import Natures
from pokemendel_core.utils.definitions.abilities import Abilities
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


def test_base_gen(client_fixture):
    run_id = _create_run(client_fixture, GEN3_GAME_NAME)


def _create_run(client_fixture, game_name):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    with pytest.raises(AssertionError, match=f"Failed to continue run creation with game {game_name}"):
        start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)

    continue_locke_creation_not_finished(client_fixture, None, None, '_selected_locke', "BaseLocke")
    return None


if __name__ == '__main__':
    pytest.main([__file__])

