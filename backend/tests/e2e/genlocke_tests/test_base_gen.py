from pokemendel_core.utils.definitions.abilities import Abilities
from pokemendel_core.utils.definitions.natures import Natures
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
        game_name="Fire Red",
        locke_name=BaseLocke.name,
        extra_info=False,
        specific_pokemons=False,
    )
    charmander_id = choose_gen_starter(
        client=client_fixture,
        run_id=run_id,
        expected_starter_options=GEN1_STARTERS,
        starter_pokemon=PokemonGen1.CHARMANDER,
        nickname="Sandra",
        gender="Male",
        ability=Abilities.BLAZE,
        nature=Natures.BOLD,
    )


if __name__ == '__main__':
    pytest.main([__file__])
