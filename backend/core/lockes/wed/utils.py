from core.run import Run
from definitions.pokemons.pokemon import Pokemon
from dataclasses import dataclass
from typing import Optional, Tuple, Set


@dataclass
class PairedPokemons:
    pokemon1: Pokemon
    pokemon2: Optional[Pokemon] = None

    def is_pokemon_in_pair(self, pokemon: Pokemon):
        return pokemon.compare_pokemon(self.pokemon1) or pokemon.compare_pokemon(self.pokemon2)


def get_party_pairs(run: Run, check_emptiness: bool = True) -> Tuple[PairedPokemons, Optional[PairedPokemons], Optional[PairedPokemons]]:
    assert not check_emptiness or not run.party.is_empty(), "Can't extract pairs from empty party"
    if run.party.is_empty():
        return None, None, None
    first_pokemon = run.party.pokemons[0]
    added_pokemons = {first_pokemon.metadata.id}
    pair1 = PairedPokemons(pokemon1=first_pokemon)
    pair2 = None
    pair3 = None

    _add_partner_to_paired_couple(run, pair1, added_pokemons)

    for party_pokemon in run.party.pokemons[1:]:
        if party_pokemon.metadata.id in added_pokemons:
            continue

        if pair2 is None:
            pair2 = PairedPokemons(pokemon1=party_pokemon)
            _add_partner_to_paired_couple(run, pair2, added_pokemons)
        elif pair3 is None:
            pair3 = PairedPokemons(pokemon1=party_pokemon)
            _add_partner_to_paired_couple(run, pair3, added_pokemons)
        else:
            assert False, "All pairs in party were set. There is a pokemon that is not a part of a pair"

    return pair1, pair2, pair3


def _add_partner_to_paired_couple(run: Run, paired_couple: PairedPokemons, added_pokemons: Set[str]):
    assert paired_couple.pokemon1, "Can add partner to not existing pokemon"
    assert not paired_couple.pokemon2, "Can't add partner if already added"
    pokemon_partner = get_pokemon_partner(run, paired_couple.pokemon1)
    if pokemon_partner:
        assert run.party.is_pokemon_in_party(pokemon_partner), f"Partner {pokemon_partner.metadata.id} for pokemon {paired_couple.pokemon1.metadata.id} must be in party"
        added_pokemons.add(pokemon_partner.metadata.id)
        paired_couple.pokemon2 = pokemon_partner


def get_pokemon_partner(run: Run, pokemon: Pokemon) -> Optional[Pokemon]:
    if pokemon.metadata.paired:
        return run.box.get_pokemon_by_id(pokemon.metadata.paired)
