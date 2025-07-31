
from typing import Optional
from definitions import Pokemon
from definitions.runs.steps_interface import ExecutionReturnValue
from core.run import Run
from core.steps.add_to_party_step import AddToPartyStep as AddToPartyStepOg
from core.lockes.wed.utils import get_party_pairs, get_pokemon_partner


class AddToPartyStep(AddToPartyStepOg):
    pass
