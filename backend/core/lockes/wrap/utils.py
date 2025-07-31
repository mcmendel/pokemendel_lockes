from core.run import Run
from definitions.pokemons.pokemon import Pokemon
from typing import List


def get_pokemon_max_index(run: Run) -> int:
    pokemon_indices = [pokemon.metadata.caught_index for pokemon in run.box.pokemons if pokemon.metadata.caught_index is not None]
    return (
        max(pokemon_indices)
        if pokemon_indices
        else -1
    )


def get_sorted_party(run: Run) -> List[Pokemon]:
    return sorted(run.party.pokemons, key=lambda x: x.metadata.caught_index)
