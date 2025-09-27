from core.lockes.base.base_locke import BaseLocke
from core.locke import Pokemon
from typing import List


class StarterLocke(BaseLocke):

    def rules(self) -> List[str]:
        locke_rules = super().rules()
        locke_rules.append("Only Games starter pokemons are eligible")
        return locke_rules

    def is_pokemon_relevant(self, pokemon: Pokemon) -> bool:
        return False
