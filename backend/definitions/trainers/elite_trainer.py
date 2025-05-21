from typing import List, Optional
from dataclasses import dataclass
from pokemendel_core.utils.definitions.types import Types
from .trainer_pokemon import TrainerPokemon

@dataclass
class EliteTrainer:
    leader: str
    type: Optional[Types]
    pokemons: List[TrainerPokemon]