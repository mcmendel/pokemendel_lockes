from tests.e2e.helpers import (
    client_fixture,
    list_runs,
    list_lockes,
    start_locke_creation,
    continue_locke_creation_not_finished,
    continue_locke_creation_finished,
    get_run,
    save_run,
    get_starter_options,
    choose_starter,
    assert_run,
    assert_saved_run,
    assert_run_potential_pokemons,
)
import pytest


TEST_LOCKE = "BaseLocke"
TEST_GAME = "Red"


def test_base_gen1(client_fixture):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # The collection access will automatically use 'e2e_runs' instead of 'runs'
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    start_locke_creation(client_fixture, TEST_LOCKE, TEST_GAME, False, False)
    continue_locke_creation_not_finished(client_fixture, None, None, 'GAME', TEST_GAME)
    run_id = continue_locke_creation_finished(client_fixture, 'GAME', TEST_GAME)
    assert_run_potential_pokemons(run_id, 151)
    run = get_run(client_fixture, run_id)
    assert_run(run, run_id, 0, 0, 0, 0, None)
    assert_saved_run(run_id, 0, 0, 0, 0, None)
    starter_options = get_starter_options(client_fixture, run_id)
    assert set(starter_options) == {'Bulbasaur', 'Charmander', 'Squirtle'}
    choose_starter(client_fixture, run_id, starter_options[0])

    run = get_run(client_fixture, run_id)
    assert run['starter']
    assert len(run['party']['pokemons']) == 1
    assert len(run['box']['pokemons']) == 1
    for new_pokemon in [
        run['starter'],
        run['party']['pokemons'][0],
        run['box']['pokemons'][0]
    ]:
        assert new_pokemon['name'] == starter_options[0]
        assert new_pokemon['metadata']['id']
        assert not new_pokemon['metadata']['nickname']

    print("TEST Finished")


if __name__ == '__main__':
    pytest.main([__file__])

