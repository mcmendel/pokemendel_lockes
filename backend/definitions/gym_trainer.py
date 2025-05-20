from typing import List, Optional
from dataclasses import dataclass
from pokemendel_core.utils.definitions.types import Types
from .trainer_pokemon import TrainerPokemon

@dataclass
class GymTrainer:
    """Represents a gym trainer in the game."""
    name: str
    type: Types
    pokemons: List[TrainerPokemon]
    badge: str
    level: int 