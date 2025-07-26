from core.lockes.base.base_locke import BaseLocke
from pokemendel_core.utils.class_property import classproperty
from typing import List, Dict
from definitions.runs.steps_names import StepsNames
from definitions.runs.steps_interface import StepInterface
from copy import copy
from core.run import Run
from core.locke import Pokemon
from .utils import can_pokemon_be_in_party
from .steps import (
    ReplacePartyPokemon,
    AddToPartyStep,
    EvolvePokemonStep,
)


class UniqueLocke(BaseLocke):

    def rules(self) -> List[str]:
        locke_rules = super().rules()
        locke_rules.extend([
           "Two pokemons in the party cannot share a type",
        ])
        return locke_rules

    @classproperty
    def steps_mapper(cls) -> Dict[StepsNames, StepInterface]:
        """Get a mapping of step names to their implementations.
        Returns:
            Dict[StepsNames, StepInterface]: A dictionary mapping step names to their implementations
        """
        locke_steps_map = copy(super().steps_mapper)
        locke_steps_map[StepsNames.ADD_TO_PARTY] = AddToPartyStep()
        locke_steps_map[StepsNames.SWITCH_PARTY_POKEMONS] = ReplacePartyPokemon()
        locke_steps_map[StepsNames.EVOLVE] = EvolvePokemonStep()
        return locke_steps_map

    def catch_pokemon(self, pokemon: Pokemon, run: Run):
        super().catch_pokemon(pokemon, run)
        if can_pokemon_be_in_party(pokemon, run) and not run.party.is_party_full():
            run.party.add_pokemon(pokemon)

    @property
    def auto_add_to_party(self) -> bool:
        return False


