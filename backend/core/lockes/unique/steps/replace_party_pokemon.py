
from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from core.steps.replace_party_pokemon import ReplacePartyPokemon as ReplacePartyPokemonOg
from core.lockes.unique.utils import get_party_pokemons_with_intersected_types
from core.run import Run


class ReplacePartyPokemon(ReplacePartyPokemonOg):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        """Check if the Pokemon can be added to the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to check
            
        Returns:
            bool: True if the Pokemon is not already in the party, False otherwise
        """
        return super().is_step_relevant(run,pokemon) and len(get_party_pokemons_with_intersected_types(set(pokemon.types), run)) < 2

    def step_options(self, run: Run, pokemon: Pokemon, is_randomized: bool) -> Tuple[InputOptions, List[str]]:
        intersected_porty_pokemons = get_party_pokemons_with_intersected_types(set(pokemon.types), run)
        assert len(intersected_porty_pokemons) < 2, "Can't replace pokemon if there are more than one pokemon in party with same type"
        return InputOptions.ONE_OF, (
            self._party_pokemon_ids(run)
            if len(intersected_porty_pokemons) == 0
            else
            [intersected_porty_pokemons[0].metadata.id]
        )
