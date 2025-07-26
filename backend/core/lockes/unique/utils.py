from core.run import Run
from definitions import Pokemon
from typing import List, Set


def can_pokemon_be_in_party(pokemon: Pokemon, run: Run) -> bool:
    for party_pokemon in run.party.pokemons:
        party_types = set(party_pokemon.types)
        pokemon_types = set(pokemon.types)
        if party_types.intersection(pokemon_types):
            return False
    return True


def get_party_pokemons_with_intersected_types(types: Set[str], run: Run) -> List[Pokemon]:
    return [
        pokemon for pokemon in run.party.pokemons
        if set(pokemon.types).intersection(types)
    ]
