from pokemendel_core.utils.class_property import classproperty
from core.lockes.base.base_locke import BaseLocke
from core.locke import Pokemon
from typing import List


class RottomLocke(BaseLocke):

    def rules(self) -> List[str]:
        locke_rules = super().rules()
        locke_rules.append("Only Rottom and its forms can be in the team")
        return locke_rules

    @classproperty
    def min_gen(cls) -> int:
        return 4

    def is_pokemon_relevant(self, pokemon: Pokemon) -> bool:
        return False
