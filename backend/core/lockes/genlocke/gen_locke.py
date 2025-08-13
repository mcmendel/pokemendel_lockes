from core.lockes.base.base_locke import BaseLocke
from core.lockes.genlocke.utils import SELECTED_LOCKE
from core.lockes.lockes_factory_no_gen import LOCKE_INSTANCES
from definitions.runs.steps_info import StepInfo
from definitions.runs.steps_names import StepsNames
from definitions.runs.steps_interface import StepInterface
from pokemendel_core.utils.class_property import classproperty
from pokemendel_core.models.pokemon import Pokemon
from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from core.run import Run


class GenLocke(BaseLocke):
    def rules(self) -> List[str]:
        inner_locke = self._get_inner_locke()
        rules = [
            "For each game generation, apply the next rules:",
        ]
        rules.extend(inner_locke.rules())
        return rules

    def steps(self, gen: int) -> List[StepInfo]:
        inner_locke = self._get_inner_locke()
        return inner_locke.steps(gen)

    @property
    def steps_mapper(self) -> Dict[StepsNames, StepInterface]:
        inner_locke = self._get_inner_locke()
        return inner_locke.steps_mapper

    def is_pokemon_relevant(self, pokemon: Pokemon) -> bool:
        inner_locke = self._get_inner_locke()
        return inner_locke.is_pokemon_relevant(pokemon)

    def catch_pokemon(self, pokemon: Pokemon, run: Run):
        inner_locke = self._get_inner_locke()
        return inner_locke.catch_pokemon(pokemon, run)

    @property
    def auto_add_to_party(self) -> bool:
        inner_locke = self._get_inner_locke()
        return inner_locke.auto_add_to_party

    def _get_inner_locke(self) -> BaseLocke:
        inner_locke_name = self.extra_info[SELECTED_LOCKE]
        return LOCKE_INSTANCES[inner_locke_name]
