from core.lockes.lockes_factory import *
from tests.e2e.genlocke_tests.utils import *
from tests.e2e.helpers import client_fixture
from tests.e2e.gen1_helpers import (
    PokemonGen1,
    STARTERS as GEN1_STARTERS,
)
import pytest


def test_base_genlocke(client_fixture):
    run_id = create_genlocke_run(
        client=client_fixture,
        game_name="Blue",
        locke_name=BaseLocke.name,
        extra_info=False,
        specific_pokemons=False,
    )
    _first_gen_run(client_fixture, run_id)
    finish_gen_run(client_fixture, run_id, False)
    skip_to_next_gen(client_fixture, run_id, "Crystal", False)
    skip_to_next_gen(client_fixture, run_id, "Crystal", True)


def _first_gen_run(client_fixture, run_id):
    charmander_id = choose_gen_starter(
        client=client_fixture,
        run_id=run_id,
        expected_starter_options=GEN1_STARTERS,
        starter_pokemon=PokemonGen1.CHARMANDER,
        nickname="Sandra",
    )
    next_actions = get_next_actions(client_fixture, run_id, charmander_id)
    assert next_actions == ["Evolve Pokemon", "Kill Pokemon"]

    caterpie_id = catch_pokemon(
        client=client_fixture,
        run_id=run_id,
        route="Route 2",
        encounter_name=PokemonGen1.CATERPIE,
        num_expected_encounters=3,
        num_current_box=1,
        num_new_party=2,
        is_pokemon_in_party=True,
        nickname="Lilly",
    )
    next_actions = get_next_actions(client_fixture, run_id, caterpie_id)
    assert next_actions == ["Remove from Party", "Evolve Pokemon", "Kill Pokemon"]
    save_run(client_fixture, run_id)
    win_battle(client_fixture, run_id, 'Brock')

    geodude_id = catch_pokemon(
        client=client_fixture,
        run_id=run_id,
        route="Mt. Moon",
        encounter_name=PokemonGen1.GEODUDE,
        num_expected_encounters=6,
        num_current_box=2,
        num_new_party=3,
        is_pokemon_in_party=True,
        nickname="Fairplay",
    )

    bellsprout_id = catch_pokemon(
        client=client_fixture,
        run_id=run_id,
        route="Route 24",
        encounter_name=PokemonGen1.BELLSPROUT,
        num_expected_encounters=8,
        num_current_box=3,
        num_new_party=4,
        is_pokemon_in_party=True,
        nickname="Derrah",
    )

    kill_pokemon(
        client=client_fixture,
        run_id=run_id,
        pokemon_id=bellsprout_id,
        num_party=3,
        num_box=4,
    )
    save_run(client_fixture, run_id)
    win_battle(client_fixture, run_id, 'Misty')

    drowzee_id = catch_pokemon(
        client=client_fixture,
        run_id=run_id,
        route="Route 11",
        encounter_name=PokemonGen1.DROWZEE,
        num_expected_encounters=9,
        num_current_box=4,
        num_new_party=4,
        is_pokemon_in_party=True,
        nickname="X1",
    )
    win_battle(client_fixture, run_id, 'Lt. Surge')

    gastly_id = catch_pokemon(
        client=client_fixture,
        run_id=run_id,
        route="Pokemon Tower",
        encounter_name=PokemonGen1.GASTLY,
        num_expected_encounters=3,
        num_current_box=5,
        num_new_party=5,
        is_pokemon_in_party=True,
        nickname="X2",
    )

    vulpix_id = catch_pokemon(
        client=client_fixture,
        run_id=run_id,
        route="Route 7",
        encounter_name=PokemonGen1.VULPIX,
        num_expected_encounters=3,
        num_current_box=6,
        num_new_party=6,
        is_pokemon_in_party=True,
        nickname="X3",
    )
    win_battle(client_fixture, run_id, 'Erika')

    machop_id = catch_pokemon(
        client=client_fixture,
        run_id=run_id,
        route="Rock Tunnel",
        encounter_name=PokemonGen1.MACHOP,
        num_expected_encounters=3,
        num_current_box=7,
        num_new_party=6,
        is_pokemon_in_party=False,
        nickname="X3",
    )
    win_battle(client_fixture, run_id, 'Sabrina')
    win_battle(client_fixture, run_id, 'Koga')
    win_battle(client_fixture, run_id, 'Blaine')
    win_battle(client_fixture, run_id, 'Giovanni')

    # Finish Elite 4
    win_battle(client_fixture, run_id, 'Lorelei')
    win_battle(client_fixture, run_id, 'Bruno')
    win_battle(client_fixture, run_id, 'Agatha')
    win_battle(client_fixture, run_id, 'Lance')


if __name__ == '__main__':
    pytest.main([__file__])
