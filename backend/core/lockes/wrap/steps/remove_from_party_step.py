from definitions import Pokemon
from core.run import Run
from core.steps.remove_from_party_step import RemoveFromPartyStep as RemoveFromPartyStepOg
from core.lockes.wrap.utils import is_pokemon_in_wrap


class RemoveFromPartyStep(RemoveFromPartyStepOg):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        return super().is_step_relevant(run, pokemon) and not is_pokemon_in_wrap(run, pokemon)
