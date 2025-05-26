from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from models.run import Run

@dataclass
class ListRuns:
    """Response model for listing runs.
    
    This class represents the data structure returned when listing runs.
    It contains a subset of run information focused on high-level details.
    
    Attributes:
        created_at: When the run was created
        game_name: Name of the game being played
        locke_name: Type of Locke challenge
        run_id: Unique identifier for the run
        run_name: User-given name for the run
        randomized: Whether the game is randomized
        starter: The chosen starter Pokemon (if any)
        num_deaths: Number of Pokemon deaths in the run
        num_pokemons: Total number of Pokemon in the box (includes party Pokemon)
        num_gyms: Number of gyms completed
        num_restarts: Number of times the run has been restarted
        finished: Whether the run has been completed
    """
    created_at: datetime
    game_name: str
    locke_name: str
    run_id: str
    run_name: str
    randomized: bool
    starter: Optional[str]
    num_deaths: int
    num_pokemons: int
    num_gyms: int
    num_restarts: int
    finished: bool

    def __post_init__(self):
        """Validate the data after initialization."""
        if not self.run_id:
            raise ValueError("run_id cannot be empty")
        if not self.run_name:
            raise ValueError("run_name cannot be empty")
        if not self.game_name:
            raise ValueError("game_name cannot be empty")
        if not self.locke_name:
            raise ValueError("locke_name cannot be empty")
        if self.num_deaths < 0:
            raise ValueError("num_deaths cannot be negative")
        if self.num_pokemons < 0:
            raise ValueError("num_pokemons cannot be negative")
        if self.num_gyms < 0:
            raise ValueError("num_gyms cannot be negative")
        if self.num_restarts < 0:
            raise ValueError("num_restarts cannot be negative")

    @classmethod
    def from_run(cls, run: Run) -> 'ListRuns':
        """Create a ListRuns instance from a Run model.
        
        Args:
            run: The Run model instance to convert
            
        Returns:
            A new ListRuns instance with data from the Run model
        """
        return cls(
            created_at=run.created_date,
            game_name=run.game,
            locke_name=run.locke,
            run_id=run.run_id,
            run_name=run.name,
            randomized=run.randomized,
            starter=run.starter,
            num_deaths=0,  # Set to 0 until we have Pokemon status information
            num_pokemons=len(run.box),  # Box includes party Pokemon
            num_gyms=len([b for b in run.battles if b.get('type') == 'gym']),
            num_restarts=run.restarts,
            finished=run.finished
        )
