from pokemendel_core.models.pokemon import Pokemon as CorePokemon
from dataclasses import dataclass
from typing import Optional
from .pokemon_metadata import PokemonMetadata
from .pokemon_status import PokemonStatus

@dataclass
class Pokemon(CorePokemon):
    metadata: Optional[PokemonMetadata] = None
    status: str = PokemonStatus.ALIVE

    def __post_init__(self):
        """Validate that metadata is not None and status is a valid PokemonStatus value."""
        if self.metadata is None:
            raise ValueError("metadata cannot be None and must include a valid id")
        if self.status not in PokemonStatus.list_all():
            raise ValueError(f"Invalid status: {self.status}")
