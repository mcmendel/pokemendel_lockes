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


def refresh_pokemons_in_party(run: Run) -> List[Pokemon]:
    alive_pokemons = sorted(run.box.get_alive_pokemons(), key=lambda x: x.metadata.caught_index)
    party_pokemons = get_sorted_party(run)
    if len(party_pokemons) >= 4:
        _refresh_old_party_pokemons(run, party_pokemons, alive_pokemons, True)
        _refresh_new_party_pokemons(run, party_pokemons, alive_pokemons, True)
    elif len(party_pokemons) == 3:
        _refresh_old_party_pokemons(run, party_pokemons, alive_pokemons, True)
        _refresh_new_party_pokemons(run, party_pokemons, alive_pokemons, False)
    elif len(party_pokemons) == 2:
        _refresh_old_party_pokemons(run, party_pokemons, alive_pokemons, True)
    else:
        assert party_pokemons[0].compare_pokemon(alive_pokemons[0])

    return get_sorted_party(run)


def _refresh_old_party_pokemons(run: Run, sorted_party: List[Pokemon], alive_pokemons: List[Pokemon], both_pokemons: bool):
    run.party.remove_pokemon(sorted_party[0])
    run.party.add_pokemon(alive_pokemons[0])
    if both_pokemons:
        run.party.remove_pokemon(sorted_party[1])
        run.party.add_pokemon(alive_pokemons[1])


def _refresh_new_party_pokemons(run: Run, sorted_party: List[Pokemon], alive_pokemons: List[Pokemon], both_pokemons: bool):
    run.party.remove_pokemon(sorted_party[-1])
    run.party.add_pokemon(alive_pokemons[-1])
    if both_pokemons:
        run.party.remove_pokemon(sorted_party[-2])
        run.party.add_pokemon(alive_pokemons[-2])
