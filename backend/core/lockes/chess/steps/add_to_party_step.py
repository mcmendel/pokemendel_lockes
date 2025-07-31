from definitions import Pokemon
from core.run import Run
from core.steps.add_to_party_step import AddToPartyStep as AddToPartyStepOg
from core.lockes.chess.utils import get_party_roles


class AddToPartyStep(AddToPartyStepOg):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        return super().is_step_relevant(run, pokemon) and pokemon.metadata.chesslocke_role not in get_party_roles(run)
