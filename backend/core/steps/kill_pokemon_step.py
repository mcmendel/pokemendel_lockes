from typing import Tuple, List, Optional
from definitions import Pokemon, PokemonStatus
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from models.run_pokemons_options import list_runs_options_by_query
from core.run import Run
from responses.exceptions import BlackoutException


class KillPokemonStep(StepInterface):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        return pokemon.status != PokemonStatus.DEAD

    def step_options(self, run: Run, pokemon: Pokemon, is_randomized: bool) -> Tuple[InputOptions, List[str]]:
        return InputOptions.NOTHING, []

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        pokemon.status = PokemonStatus.DEAD
        if run.party.is_pokemon_in_party(pokemon):
            try:
                run.party.remove_pokemon(pokemon)
            except:
                print("Last pokemon in party died. Blackouttt")
                raise BlackoutException()
        return ExecutionReturnValue(pokemons_to_update=[pokemon.metadata.id])

    def _get_pokemon_potential_evolutions(self, run: Run, pokemon: Pokemon) -> List[str]:
        pokemon_evolutions = [evolution.name for evolution in pokemon.evolves_to]
        if not pokemon_evolutions:
            return []

        run_options = list_runs_options_by_query(run.id, {'pokemon_name': {"$in": pokemon_evolutions}})
        return [
            option.pokemon_name for option in run_options
        ]
