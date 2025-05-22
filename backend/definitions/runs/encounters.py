from pokemendel_core.utils.enum_list import EnumList
from dataclasses import dataclass
from typing import Optional
from .. import Pokemon


class EncounterStatus(EnumList):
    UNMET = "Unmet"
    MET = "Met"
    KILLED = "Killed"
    RAN = "Ran"
    CAUGHT = "Caught"


@dataclass
class Encounter:
    route: str
    status: str
    pokemon: Optional[Pokemon] = None

    def is_caught(self) -> bool:
        return self.pokemon is not None and self.status == EncounterStatus.CAUGHT