from dataclasses import dataclass
from typing import Optional
from pokemendel_core.utils.definitions.genders import Genders
from pokemendel_core.utils.definitions.types import Types

@dataclass
class PokemonMetadata:
    id: str
    nickname: str = ""
    caught_index: Optional[int] = None
    starlocke_type: Optional[Types] = None
    gender: Optional[Genders] = None
    paired: Optional[str] = None
    chesslocke_role: Optional[str] = None
    chesslocke_role_og: Optional[str] = None

    def __post_init__(self):
        """Validate that id and nickname are not empty or whitespace-only."""
        if not self.id or not self.id.strip():
            raise ValueError("id cannot be empty")
