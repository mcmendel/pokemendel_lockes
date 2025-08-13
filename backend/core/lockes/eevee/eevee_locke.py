from core.lockes.base.base_locke import BaseLocke
from core.locke import Pokemon
from definitions.runs.steps_names import StepsNames
from definitions.runs.steps_interface import StepInterface
from .steps import (
    EvolvePokemonStep,
)
from pokemendel_core.utils.class_property import classproperty
from typing import List, Dict


class EeveeLocke(BaseLocke):

    def rules(self) -> List[str]:
        locke_rules = super().rules()
        locke_rules.append("Only Eevee and it's evolution can be part of the team")
        return locke_rules

    def is_pokemon_relevant(self, pokemon: Pokemon) -> bool:
        return False

    @property
    def steps_mapper(self) -> Dict[StepsNames, StepInterface]:
        """Get a mapping of step names to their implementations.
        Returns:
            Dict[StepsNames, StepInterface]: A dictionary mapping step names to their implementations
        """
        locke_steps_map = super().steps_mapper
        locke_steps_map[StepsNames.EVOLVE] = EvolvePokemonStep()
        return locke_steps_map


