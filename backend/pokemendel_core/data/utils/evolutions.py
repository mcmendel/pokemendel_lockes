from pokemendel_core.models.pokemon import Pokemon
from pokemendel_core.models.evolution.evolution import Evolution
from typing import Dict


def update_evolution(pokemons_map: Dict[str, Pokemon], pokemon_name: str, evolution_name: str, new_evolution: Evolution):
    new_evolutions = [cur_evolution for cur_evolution in pokemons_map[pokemon_name].evolves_to if cur_evolution.name != evolution_name]
    new_evolution.name = evolution_name
    new_evolutions.append(new_evolution)
    pokemons_map[pokemon_name].evolves_to = new_evolutions
