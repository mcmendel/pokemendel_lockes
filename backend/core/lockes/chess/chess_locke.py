from core.lockes.base.base_locke import BaseLocke
from pokemendel_core.utils.class_property import classproperty
from typing import List, Dict
from definitions.runs.steps_info import StepInfo
from definitions.runs.steps_names import StepsNames
from definitions.runs.steps_interface import StepInterface
from .steps import (
    ReplacePartyPokemon,
    AddToPartyStep,
    KillPokemonStep,
    SetChessRoleStep,
)


class ChessLocke(BaseLocke):
    def rules(self) -> List[str]:
        locke_rules = super().rules()
        locke_rules.extend([
            "Only sixteen Pokémon may be acquired throughout the entire run (the player’s starter, and fifteen others)",
            "The player must assign each Pokémon a role before it can enter a battle",
            "These roles include a King, Queen, two Bishops, two Knights, two Rooks, and eight Pawns.",
            "A player may only have one Pokémon of each role on their team at a time.",
            "King: The starter Pokémon. The King must remain in the party at all times, and if it faints, the run is considered lost.",
            "Queen: The Queen is not subject to any restrictions in battle and may be used as normal. However, the Queen must be a female Pokémon.",
            "Bishops: A Bishop may only know two damaging moves at any time.",
            "Knights: A Knight may not use any moves with a Base Power greater than 60.",
            "Rooks: A Rook may not use any damaging moves with secondary effects",
            "Pawns: A Pawn may never evolve, and must be its line’s lowest evolution",
            "If the Pawn wins a Gym Leader, Elite Four, or Rival battle by itself (without any other Pokémon participating) it may be “promoted” to one of the other roles",
        ])
        return locke_rules

    @classproperty
    def min_gen(cls) -> int:
        return 2

    def _mandatory_steps(self, gen: int) -> List[StepInfo]:
        mandatory_steps = super()._mandatory_steps(gen)
        mandatory_steps.append(StepInfo(step_name=StepsNames.CHESSLOCKE_SET_ROLE, prerequisites=[StepsNames.GENDER]))
        return mandatory_steps

    @property
    def steps_mapper(self) -> Dict[StepsNames, StepInterface]:
        """Get a mapping of step names to their implementations.
        Returns:
            Dict[StepsNames, StepInterface]: A dictionary mapping step names to their implementations
        """
        locke_steps_map = super().steps_mapper
        locke_steps_map[StepsNames.ADD_TO_PARTY] = AddToPartyStep()
        locke_steps_map[StepsNames.SWITCH_PARTY_POKEMONS] = ReplacePartyPokemon()
        locke_steps_map[StepsNames.CHESSLOCKE_SET_ROLE] = SetChessRoleStep()
        locke_steps_map[StepsNames.KILL] = KillPokemonStep()
        return locke_steps_map

    def auto_add_to_party(self) -> bool:
        return False
