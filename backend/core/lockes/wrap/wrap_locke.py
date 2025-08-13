from core.lockes.base.base_locke import BaseLocke
from pokemendel_core.utils.class_property import classproperty
from typing import List, Dict
from definitions.runs.steps_names import StepsNames
from definitions.runs.steps_interface import StepInterface
from definitions.pokemons.pokemon import Pokemon
from copy import copy
from core.run import Run
from .utils import get_pokemon_max_index, get_sorted_party
from .steps import (
    ReplacePartyPokemon,
    KillPokemonStep,
    RemoveFromPartyStep,
)


class WrapLocke(BaseLocke):

    def rules(self) -> List[str]:
        locke_rules = super().rules()
        locke_rules.extend([
            "Party must include first 2 caught pokemons (including starter)",
            "Party must include last 2 caught pokemons",
            "2 remaining party pokemons are for the trainer's choice (HM slave should be part of this 2 pokemons)",
        ])
        return locke_rules

    @property
    def steps_mapper(self) -> Dict[StepsNames, StepInterface]:
        """Get a mapping of step names to their implementations.
        Returns:
            Dict[StepsNames, StepInterface]: A dictionary mapping step names to their implementations
        """
        locke_steps_map = copy(super().steps_mapper)
        locke_steps_map[StepsNames.SWITCH_PARTY_POKEMONS] = ReplacePartyPokemon()
        locke_steps_map[StepsNames.REMOVE_FROM_PARTY] = RemoveFromPartyStep()
        locke_steps_map[StepsNames.KILL] = KillPokemonStep()
        return locke_steps_map

    def catch_pokemon(self, pokemon: Pokemon, run: Run):
        super().catch_pokemon(pokemon, run)
        max_index = get_pokemon_max_index(run)
        pokemon.metadata.caught_index = max_index + 1
        if not run.party.is_pokemon_in_party(pokemon):
            sorted_party = get_sorted_party(run)
            assert len(sorted_party) == 6, "Pokemon should be in party if it's not full"
            run.party.remove_pokemon(sorted_party[-2])
            run.party.add_pokemon(pokemon)
