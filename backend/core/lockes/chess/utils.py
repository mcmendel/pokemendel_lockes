from pokemendel_core.utils.enum_list import EnumList
from core.run import Run
from typing import Set


class ChessRoles(EnumList):
    KING = "King"      # The starter Pokémon. The King must remain in the party at all times, and if it faints, the run is considered lost
    QUEEN = "Queen"    # The Queen is not subject to any restrictions in battle and may be used as normal
    BISHOP = "Bishop"  # A Bishop may only know two damaging moves at any time.
    KNIGHT = "Knight"  # A Knight may not use any moves with a Base Power greater than 60.
    ROOK = "Rook"      # A Rook may not use any damaging moves with secondary effects
    PAWN = "Pawn"      # A Pawn may never evolve, and must be its line’s lowest evolution


def get_party_roles(run: Run) -> Set[str]:
    return {
        pokemon.metadata.chesslocke_role for pokemon in run.party.pokemons
    }
