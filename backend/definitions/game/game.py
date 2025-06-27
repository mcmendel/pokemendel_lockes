from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional
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
    egg_pokemons: Set[str] = field(default_factory=set)

    def potential_encounters(self, route: Optional[str]) -> Set[str]:
        route_encounters = set()
        route_encounters.update(self.egg_pokemons)
        if route:
            assert route in self.encounters, f"Route {route} does not exist in game {self.name}"
            route_encounters.update(self.encounters[route])
        else:
            for route, route_values in self.encounters.items():
                route_encounters.update(route_values)
        return route_encounters

