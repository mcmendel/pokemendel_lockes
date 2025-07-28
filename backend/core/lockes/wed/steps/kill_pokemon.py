
from typing import Tuple, List, Optional
from definitions import Pokemon
from definitions.runs.inputs_options import InputOptions
from core.steps.kill_pokemon_step import KillPokemonStep as KillPokemonStepOg
from core.lockes.unique.utils import get_party_pokemons_with_intersected_types
from core.run import Run


class KillPokemonStep(KillPokemonStepOg):
    pass
