from typing import Tuple, List, Optional
from definitions import Pokemon, PokemonStatus
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from models.run_pokemons_options import list_runs_options_by_query
from core.run import Run
from responses.exceptions import BlackoutException


class KillPokemonStep(StepInterface):
    pass
