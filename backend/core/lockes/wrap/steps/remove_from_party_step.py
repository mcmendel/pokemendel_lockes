from definitions import Pokemon
from definitions.runs.steps_interface import ExecutionReturnValue
from core.run import Run
from typing import Optional
from core.steps.remove_from_party_step import RemoveFromPartyStep as RemoveFromPartyStepOg
from core.lockes.wed.utils import get_party_pairs


class RemoveFromPartyStep(RemoveFromPartyStepOg):
    pass
