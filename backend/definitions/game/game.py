from dataclasses import dataclass, field
from typing import List, Dict, Set
from .. import GymTrainer, EliteTrainer, Pokemon

@dataclass
class Game:
    name: str
    gen: int
    region: str
    gyms: List[GymTrainer]
    elite4: List[EliteTrainer]
    routes: List[str]
    starters: List[Pokemon]
    important_battles: List[str] = field(default_factory=list)
    encounters: Dict[str, Set[str]] = field(default_factory=dict)