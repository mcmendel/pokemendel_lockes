from definitions import Pokemon
from core.steps.replace_party_pokemon import ReplacePartyPokemon as ReplacePartyPokemonOg
from definitions.runs.inputs_options import InputOptions
from core.run import Run
from core.lockes.chess.utils import get_party_roles
from typing import Tuple, List


class ReplacePartyPokemon(ReplacePartyPokemonOg):
    def step_options(self, run: Run, pokemon: Pokemon, is_randomized: bool) -> Tuple[InputOptions, List[str]]:
        party_roles = get_party_roles(run)
        if pokemon.metadata.chesslocke_role in party_roles:
            same_role_party = [pokemon.metadata.id for pokemon in run.party.pokemons if pokemon.metadata.chesslocke_role == pokemon.metadata.chesslocke_role]
            return InputOptions.ONE_OF, same_role_party
        return super().step_options(run, pokemon, is_randomized)
