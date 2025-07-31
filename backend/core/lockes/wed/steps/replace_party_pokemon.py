
from typing import Optional
from definitions import Pokemon
from definitions.runs.steps_interface import ExecutionReturnValue
from core.steps.replace_party_pokemon import ReplacePartyPokemon as ReplacePartyPokemonOg
from core.run import Run


class ReplacePartyPokemon(ReplacePartyPokemonOg):
    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        returned_value = super().execute_step(run, pokemon, value)
        replaced_pokemon = run.box.get_pokemon_by_id(value)
        if replaced_pokemon.metadata.paired and pokemon.metadata.paired:
            partner = run.box.get_pokemon_by_id(pokemon.metadata.paired)
            partners_return_value = super().execute_step(run, partner, replaced_pokemon.metadata.paired)
            returned_value.pokemons_to_update.extend(partners_return_value.pokemons_to_update)
        elif replaced_pokemon.metadata.paired:
            replaced_pokemon_partner = run.box.get_pokemon_by_id(replaced_pokemon.metadata.paired)
            run.party.remove_pokemon(replaced_pokemon_partner)
        elif pokemon.metadata.paired:
            partner = run.box.get_pokemon_by_id(pokemon.metadata.paired)
            run.party.add_pokemon(partner)

        return returned_value
