from .gen1 import NAME_TO_POKEMON as GEN1_NAME_TO_POKEMON, Pokemon
from .gen2 import NAME_TO_POKEMON as GEN2_NAME_TO_POKEMON
from .gen3 import NAME_TO_POKEMON as GEN3_NAME_TO_POKEMON
from typing import Dict, Optional

__all__ = ["GEN1_NAME_TO_POKEMON", "GEN2_NAME_TO_POKEMON"]


def fetch_pokemon(name: str, gen: int) -> Pokemon:
    if gen == 1:
        return GEN1_NAME_TO_POKEMON[name]
    elif gen == 2:
        return GEN2_NAME_TO_POKEMON[name]
    elif gen == 3:
        return GEN3_NAME_TO_POKEMON[name]
    raise ValueError(f"No data for generation {gen}")


def map_gen_pokemons(gen: int) -> Dict[str, Pokemon]:
    if gen == 1:
        return GEN1_NAME_TO_POKEMON
    elif gen == 2:
        return GEN2_NAME_TO_POKEMON
    elif gen == 3:
        return GEN3_NAME_TO_POKEMON
    raise ValueError(f"No data for generation {gen}")

def list_gen_pokemons(gen: int) -> list[Pokemon]:
    pokemons_mapper = map_gen_pokemons(gen)
    return pokemons_mapper.values()


def get_pokemon_evolves_from(gen: int, pokemon_name: str) -> Optional[str]:
    pokemons_mapper = map_gen_pokemons(gen)
    for cur_pokemon_name, pokemon in pokemons_mapper.items():
        for evolution_pokemon in pokemon.evolves_to:
            if pokemon_name == evolution_pokemon.name:
                return cur_pokemon_name
    return None
