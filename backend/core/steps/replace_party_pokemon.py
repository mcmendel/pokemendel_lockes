"""Step implementation for replacing a Pokemon in the player's party.

This step allows replacing a Pokemon in the player's party with another Pokemon.
The user can choose which Pokemon in the party to replace, and the new Pokemon
will take its place.
"""

from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from core.run import Run


class ReplacePartyPokemon(StepInterface):
    """Step for replacing a Pokemon in the player's party.
    
    This step is relevant when:
    - The Pokemon to add is not already in the party
    
    The step requires the user to select which Pokemon in the party to replace.
    If the party is full, the selected Pokemon will be removed and the new one added.
    If the party is not full, the new Pokemon will be added first, then the selected one removed.
    """

    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        """Check if the Pokemon can be added to the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to check
            
        Returns:
            bool: True if the Pokemon is not already in the party, False otherwise
        """
        return not run.party.is_pokemon_in_party(pokemon)

    def step_options(self, run: Run, pokemon: Pokemon) -> Tuple[InputOptions, List[str]]:
        """Get the options for replacing a Pokemon in the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to add
            
        Returns:
            Tuple[InputOptions, List[str]]: A tuple containing:
                - InputOptions.ONE_OF: User must select from the provided list
                - List[str]: List of Pokemon IDs in the party to choose from
        """
        return InputOptions.ONE_OF, self._party_pokemon_ids(run)

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        """Replace a Pokemon in the party.
        
        Args:
            run: The current run instance
            pokemon: The Pokemon to add
            value: The ID of the Pokemon in the party to replace
            
        Returns:
            ExecutionReturnValue: Empty list as no Pokemon need to be updated
            
        Raises:
            AssertionError: If value is None or not a valid Pokemon ID in the party
        """
        assert value is not None, "Value is required when replacing pokemon in party"
        assert value in self._party_pokemon_ids(run), f"Given pokemon {value} is not in party"
            
        to_replace_pokemon = run.get_pokemon_by_id(value)
        if run.party.is_party_full():
            run.party.remove_pokemon(to_replace_pokemon)
            run.party.add_pokemon(pokemon)
        else:
            run.party.add_pokemon(pokemon)
            run.party.remove_pokemon(to_replace_pokemon)
            
        return ExecutionReturnValue(pokemons_to_update=[])

    def _party_pokemon_ids(self, run: Run) -> List[str]:
        """Get a list of Pokemon IDs in the party.
        
        Args:
            run: The current run instance
            
        Returns:
            List[str]: List of Pokemon IDs in the party
        """
        return [party_pokemon.metadata.id for party_pokemon in run.party.pokemons]