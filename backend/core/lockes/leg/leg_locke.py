from core.lockes.base.base_locke import BaseLocke
from definitions.pokemons.pokemon import Pokemon
from typing import List
from .utils import NumLegs, LEG_TYPE_KEY


class LegLocke(BaseLocke):
    def rules(self) -> List[str]:
        locke_rules = super().rules()
        locke_rules.extend([
            f"Only pokemons that have {self.extra_info[LEG_TYPE_KEY]} legs in their evolution line can be caught",
            f"If pokemon loses his {self.extra_info[LEG_TYPE_KEY]} legs in their evolution, they cannot be evolved",
        ])
        return locke_rules

    def is_pokemon_relevant(self, pokemon: Pokemon) -> bool:
        if self.extra_info[LEG_TYPE_KEY] == NumLegs.ZERO:
            return pokemon.num_legs == 0
        if self.extra_info[LEG_TYPE_KEY] == NumLegs.ONE:
            return pokemon.num_legs == 1
        if self.extra_info[LEG_TYPE_KEY] == NumLegs.TWO:
            return pokemon.num_legs == 2
        if self.extra_info[LEG_TYPE_KEY] == NumLegs.FOUR:
            return pokemon.num_legs == 4
        return pokemon.num_legs == 3 or pokemon.num_legs > 4
