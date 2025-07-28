from core.lockes.base.base_locke import BaseLocke
from pokemendel_core.utils.class_property import classproperty
from pokemendel_core.models.pokemon import Pokemon, Genders
from typing import List, Dict
from definitions.runs.steps_info import StepInfo
from definitions.runs.steps_names import StepsNames
from definitions.runs.steps_interface import StepInterface
from .steps import (
    ReplacePartyPokemon,
    AddToPartyStep,
    KillPokemonStep,
    PairPokemonStep,
    RemoveFromPartyStep,
)


class WedLocke(BaseLocke):

    def rules(self) -> List[str]:
        locke_rules = super().rules()
        locke_rules.extend([
            "Pokemon are assigned into “pairs” based on gender",
            "If you currently have an “unpaired” Pokemon in your party, only wild Pokemon of the opposite gender to the unpaired Pokemon count as encounters",
            "Once two Pokemon of opposite genders are obtained in this manner, they form a “couple”",
            "Once one member of a couple enters a battle, only that couple may be used in that encounter",
            "If a Pokemon is knocked out, its partner must “avenge it” or die trying",
            "Genderless Pokemon may not be used in this variant"
        ])
        return locke_rules

    @classproperty
    def min_gen(cls) -> int:
        return 2

    def steps(self, gen: int) -> List[StepInfo]:
        current_steps = super().steps(gen)
        mandatory_steps = self._mandatory_steps(gen)
        prerequisites = [step_info.step_name for step_info in mandatory_steps]
        current_steps.append(StepInfo(StepsNames.WEDLOCKE_PAIR, prerequisites=prerequisites))
        return current_steps

    @classproperty
    def steps_mapper(cls) -> Dict[StepsNames, StepInterface]:
        """Get a mapping of step names to their implementations.
        Returns:
            Dict[StepsNames, StepInterface]: A dictionary mapping step names to their implementations
        """
        locke_steps_map = super().steps_mapper
        locke_steps_map[StepsNames.ADD_TO_PARTY] = AddToPartyStep()
        locke_steps_map[StepsNames.SWITCH_PARTY_POKEMONS] = ReplacePartyPokemon()
        locke_steps_map[StepsNames.WEDLOCKE_PAIR] = PairPokemonStep()
        locke_steps_map[StepsNames.KILL] = KillPokemonStep()
        locke_steps_map[StepsNames.REMOVE_FROM_PARTY] = RemoveFromPartyStep()
        return locke_steps_map

    def is_pokemon_relevant(self, pokemon: Pokemon) -> bool:
        return pokemon.supported_genders != [Genders.GENDERLESS]

    @property
    def auto_add_to_party(self) -> bool:
        return False


