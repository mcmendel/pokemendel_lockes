from models.pokemon import generate_locke_pokemon, Pokemon
from pokemendel_core.data.gen1 import PokemonGen1
from pokemendel_core.data.gen2 import PokemonGen2
from pokemendel_core.data.gen3 import PokemonGen3
from typing import List


def get_gen_starters(gen: int) -> List[str]:
    if gen == 1:
        return [
            PokemonGen1.BULBASAUR,
            PokemonGen1.CHARMANDER,
            PokemonGen1.SQUIRTLE,
        ]
    if gen == 2:
        return [
            PokemonGen2.CHIKORITA,
            PokemonGen2.CYNDAQUIL,
            PokemonGen2.TOTODILE,
        ]
    if gen == 3:
        return [
            PokemonGen3.TREECKO,
            PokemonGen3.TORCHIC,
            PokemonGen3.MUDKIP
        ]

    assert False, f"Gen {gen} is not supported"
