
from typing import Tuple, List
from definitions import Pokemon
from definitions.runs.inputs_options import InputOptions
from core.steps.replace_party_pokemon import ReplacePartyPokemon as ReplacePartyPokemonOg
from core.lockes.wrap.utils import get_sorted_party
from core.run import Run


class ReplacePartyPokemon(ReplacePartyPokemonOg):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        return super().is_step_relevant(run, pokemon) and len(run.party.pokemons) > 4

    def step_options(self, run: Run, pokemon: Pokemon, is_randomized: bool) -> Tuple[InputOptions, List[str]]:
        sorted_party = get_sorted_party(run)
        assert len(sorted_party) >= 4, "Can't replace wrap pokemons. Must have at least one meat pokemon"
        relevant_party_members = [
            party_pokemon.metadata.id
            for party_pokemon in sorted_party[2:-2]
        ]
        return InputOptions.ONE_OF, relevant_party_members
