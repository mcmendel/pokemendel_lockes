from core.lockes.base.base_locke import BaseLocke
from definitions.pokemons.pokemon import Pokemon
from typing import List
from .utils import MONO_TYPE_KEY


class MonoLocke(BaseLocke):
    def rules(self) -> List[str]:
        locke_rules = super().rules()
        locke_rules.extend([
            f"Only pokemons that have {self.extra_info[MONO_TYPE_KEY]} type in their evolution line can be caught",
            f"If pokemon loses his {self.extra_info[MONO_TYPE_KEY]} type in their evolution, they cannot be evolved",
        ])
        return locke_rules

    def is_pokemon_relevant(self, pokemon: Pokemon) -> bool:
        return self.extra_info[MONO_TYPE_KEY] in pokemon.types
