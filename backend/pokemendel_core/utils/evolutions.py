"""
Utility functions for working with Pokemon evolution chains.

This module provides functions to analyze and iterate through Pokemon evolution chains,
supporting both forward (base to final) and reverse (final to base) traversal.
"""
from pokemendel_core.models.pokemon import Pokemon
from pokemendel_core.data import list_gen_pokemons, fetch_pokemon
from typing import Dict, Set, List, Generator, Tuple
from dataclasses import dataclass


def _find_base_pokemons(pokemon_map: dict[str, Pokemon]) -> set[str]:
    """Find all base/root Pokemon that don't evolve from any other Pokemon.
    
    Args:
        pokemon_map: Dictionary mapping Pokemon names to Pokemon objects
        
    Returns:
        A set of Pokemon names that are base forms (don't evolve from any other Pokemon)
    """
    all_names = set(pokemon_map.keys())
    evolved_names = {evo.name for p in pokemon_map.values() for evo in p.evolves_to}
    roots = all_names - evolved_names
    return roots


def _trace_pokemon_evolutions(pokemon_map: dict[str, Pokemon], start: str) -> list[list[str]]:
    """Trace all possible evolution chains from a starting Pokemon using depth-first search.
    
    This function finds all possible evolution paths from a given Pokemon to its final forms.
    For example, for Bulbasaur it would return [['Bulbasaur', 'Ivysaur', 'Venusaur']].
    
    Args:
        pokemon_map: Dictionary mapping Pokemon names to Pokemon objects
        start: Name of the Pokemon to start tracing from
        
    Returns:
        A list of evolution chains, where each chain is a list of Pokemon names
        
    Example:
        >>> pokemon_map = {name: pokemon for name, pokemon in ...}
        >>> for root in _find_base_pokemons(pokemon_map):
        ...     for chain in _trace_pokemon_evolutions(pokemon_map, root):
        ...         print(" -> ".join(chain))
        Bulbasaur -> Ivysaur -> Venusaur
        Charmander -> Charmeleon -> Charizard
    """
    chains = []

    def dfs(path):
        last = path[-1]
        if not pokemon_map[last].evolves_to:
            chains.append(path)
            return
        for evo in pokemon_map[last].evolves_to:
            dfs(path + [evo.name])

    dfs([start])
    return chains


def iterate_gen_evolution_lines(gen: int, reversed: bool = False) -> Generator[List[str], None, None]:
    """Iterate through all evolution chains in a given generation.
    
    This function yields evolution chains for all Pokemon in the specified generation.
    Each chain is a list of Pokemon names representing a complete evolution line.
    
    Args:
        gen: The generation number to get evolution chains for (1 or 2)
        reversed: If True, chains are returned from final form to base form.
                 If False (default), chains are returned from base form to final form.
    
    Yields:
        Lists of Pokemon names representing evolution chains
        
    Example:
        >>> # Get all evolution chains in Gen 1 from base to final form
        >>> for chain in iterate_gen_evolution_lines(1, reversed=False):
        ...     print(" -> ".join(chain))
        Bulbasaur -> Ivysaur -> Venusaur
        Charmander -> Charmeleon -> Charizard
        
        >>> # Get all evolution chains in Gen 1 from final to base form
        >>> for chain in iterate_gen_evolution_lines(1, reversed=True):
        ...     print(" -> ".join(chain))
        Venusaur -> Ivysaur -> Bulbasaur
        Charizard -> Charmeleon -> Charmander
    """
    pokemon_map = {pokemon.name: pokemon for pokemon in list_gen_pokemons(gen)}
    for base_pokemon in _find_base_pokemons(pokemon_map):
        for evolution_chain in _trace_pokemon_evolutions(pokemon_map, base_pokemon):
            yield evolution_chain[::-1] if reversed else evolution_chain
        
