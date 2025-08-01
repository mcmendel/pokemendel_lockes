from typing import Tuple, List
from definitions import Pokemon
from definitions.runs.inputs_options import InputOptions
from core.run import Run
from core.steps.evolve_pokemon_step import EvolvePokemonStep as EvolvePokemonStepOg
from core.lockes.unique.utils import get_party_pokemons_with_intersected_types
from pokemendel_core.data import fetch_pokemon


class EvolvePokemonStep(EvolvePokemonStepOg):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        if not super().is_step_relevant(run, pokemon):
            return False
        return bool(self._get_empty_intersection_evolutions(pokemon, run))

    def step_options(self, run: Run, pokemon: Pokemon, is_randomized: bool) -> Tuple[InputOptions, List[str]]:
        return InputOptions.ONE_OF, self._get_empty_intersection_evolutions(pokemon, run)

    def _get_empty_intersection_evolutions(self, pokemon: Pokemon, run: Run) -> List[str]:
        empty_intersection_evolutions = []
        for potential_evolution_name in self._get_pokemon_potential_evolutions(run, pokemon):
            potential_evolution = fetch_pokemon(potential_evolution_name, run.gen)
            party_pokemons = [
                intersected_party_pokemon for intersected_party_pokemon
                in get_party_pokemons_with_intersected_types(set(potential_evolution.types), run)
                if intersected_party_pokemon.metadata.id != pokemon.metadata.id
            ]

            if not party_pokemons:
                empty_intersection_evolutions.append(potential_evolution_name)

        return empty_intersection_evolutions

