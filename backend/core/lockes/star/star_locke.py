from core.lockes.base.base_locke import BaseLocke
from definitions.runs.steps_info import StepInfo
from definitions.runs.steps_names import StepsNames
from typing import List


class StarLocke(BaseLocke):

    def rules(self) -> List[str]:
        locke_rules = super().rules()
        locke_rules.extend([
            "You may never catch any encounter/gift pokemons",
            "The player starts with pokemon of each type",
            "The player may not switch party pokemon with box pokemon",
            "Optional: Randomize pokemon of each type instead of choosing each pokemon"
        ])
        return locke_rules

    def steps(self, gen: int) -> List[StepInfo]:
        current_steps = super().steps(gen)
        new_steps = [
            step_info for step_info in current_steps
            if step_info.step_name not in {StepsNames.REMOVE_FROM_PARTY, StepsNames.SWITCH_PARTY_POKEMONS}
        ]
        return new_steps


