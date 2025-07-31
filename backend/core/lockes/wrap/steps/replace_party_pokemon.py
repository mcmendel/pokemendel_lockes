
from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from definitions.runs.inputs_options import InputOptions
from core.steps.replace_party_pokemon import ReplacePartyPokemon as ReplacePartyPokemonOg
from core.lockes.unique.utils import get_party_pokemons_with_intersected_types
from core.run import Run


class ReplacePartyPokemon(ReplacePartyPokemonOg):
    pass
