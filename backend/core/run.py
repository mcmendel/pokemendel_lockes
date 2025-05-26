"""Run module for managing Pokemon game runs.

This module provides the Run class which represents a complete Pokemon game run,
including the player's party, box, battles, encounters, and run status.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from definitions import Battle, Encounter, Pokemon
from core.party import Party
from core.box import Box


@dataclass
class Run:
    """A container for managing a Pokemon game run.
    
    The Run class tracks all aspects of a Pokemon game run, including:
    - Basic run information (ID, name, creation date)
    - Player's Pokemon (party and box)
    - Run progress (battles and encounters)
    - Run status (starter, restarts, completion)
    
    Attributes:
        id: Unique identifier for the run
        run_name: Name of the run
        creation_date: When the run was created
        party: The player's active Pokemon team
        box: Storage for Pokemon not in the party
        battles: List of battles completed in the run
        encounters: List of Pokemon encounters in the run
        starter: The player's starter Pokemon, if chosen
        restarts: Number of times the run has been restarted
        finished: Whether the run has been completed
    """
    id: str
    run_name: str
    creation_date: datetime
    party: Party
    box: Box
    battles: List[Battle] = field(default_factory=list)
    encounters: List[Encounter] = field(default_factory=list)
    starter: Optional[Pokemon] = None
    restarts: int = 0
    finished: bool = False

    def __post_init__(self):
        """Validate run initialization."""
        assert self.id, "Run ID cannot be empty"
        assert self.run_name, "Run name cannot be empty"
        assert self.creation_date <= datetime.now(), "Creation date cannot be in the future"
        assert self.restarts >= 0, "Restarts cannot be negative"

    def add_battle(self, battle: Battle) -> None:
        """Add a battle to the run.
        
        Args:
            battle: The battle to add
        """
        self.battles.append(battle)


    def get_pokemon_by_id(self, id: str) -> Pokemon:
        """Get a Pokemon by its ID.
        
        Args:
            id: The ID of the Pokemon to get
        """
        return self.box.get_pokemon_by_id(id)

    def add_encounter(self, encounter: Encounter) -> None:
        """Add an encounter to the run.
        
        Args:
            encounter: The encounter to add
        """
        self.encounters.append(encounter)

    def get_battle_count(self) -> int:
        """Get the total number of battles in the run.
        
        Returns:
            int: The number of battles
        """
        return len(self.battles)

    def get_encounter_count(self) -> int:
        """Get the total number of encounters in the run.
        
        Returns:
            int: The number of encounters
        """
        return len(self.encounters)

    def get_total_pokemon_count(self) -> int:
        """Get the total number of Pokemon in the run.
        
        Returns:
            int: The number of Pokemon in party and box combined
        """
        return len(self.box.get_alive_pokemons())

    def is_active(self) -> bool:
        """Check if the run is still active.
        
        Returns:
            bool: True if the run is not finished, False otherwise
        """
        return not self.finished

    def finish(self) -> None:
        """Mark the run as finished."""
        self.finished = True

    def restart(self) -> None:
        """Increment the restart counter."""
        self.restarts += 1
