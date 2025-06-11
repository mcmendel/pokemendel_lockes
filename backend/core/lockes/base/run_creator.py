"""Base module for run creation functionality.

This module provides the foundation for creating and managing Pokemon game runs.
It defines the RunCreationProgress class which tracks the state of run creation,
including what information has been provided and what is still needed.

The RunCreationProgress class is used by concrete implementations of run creators
to manage the step-by-step process of creating a new run, ensuring all required
information is collected before the run can begin.
"""

from dataclasses import dataclass
from typing import Optional, List, Any, Set
from models.run_creation import RunCreation, update_run_creation
from models.run_pokemons_options import RunPokemonsOptions, save_run_options
from pokemendel_core.utils.enum_list import EnumList
from pokemendel_core.utils.evolutions import iterate_gen_evolution_lines
from pokemendel_core.data import list_gen_pokemons, fetch_pokemon
from core.lockes.base.base_locke import BaseLocke
from core.run import Run
from core.party import Party
from core.box import Box
from games import get_games_from_gen, get_game
from datetime import datetime
from uuid import uuid4


class InfoKeys(EnumList):
    GAME = 'GAME'


@dataclass
class RunCreationProgress:
    """Tracks the progress of creating a new Pokemon game run.
    
    This class is used to manage the state of run creation, tracking what information
    has been provided and what is still needed. It serves as a state container that
    concrete run creators can use to guide users through the run creation process.

    The class maintains:
    - The current state of the run creation
    - Whether all required information has been provided
    - What information is still needed (if any)
    - Available options for the next required field (if applicable)

    Attributes:
        run_creation: The RunCreation instance being built. This contains all the
            information collected so far about the run, including its name, game,
            and any additional settings.
        has_all_info: A boolean flag indicating whether all required information
            has been provided. When True, the run creation is complete and ready
            to begin.
        missing_key: The name of the next required field that needs to be filled,
            if any. This is None when has_all_info is True or when no specific
            field is currently being requested.
        missing_key_options: A list of valid options for the missing_key field,
            if applicable. This is None when the field doesn't have predefined
            options or when no field is currently missing.
    """
    run_creation: RunCreation
    has_all_info: bool = False
    missing_key: Optional[str] = None
    missing_key_options: Optional[List[str]] = None


class RunCreator:
    """Base class for creating Pokemon game runs.
    
    This class provides the basic functionality for creating and managing runs.
    Concrete implementations should override _get_creation_missing_extra_info to
    handle their specific requirements.
    """
    
    def __init__(self, run_creation: RunCreation):
        """Initialize the run creator with a RunCreation instance.
        
        Args:
            run_creation: The RunCreation instance to manage
        """
        self.run_creation = run_creation

    def get_progress(self, locke_min_gen: int) -> RunCreationProgress:
        """Get the current progress of run creation.
        
        Returns:
            RunCreationProgress indicating what information is still needed
        """
        if self.run_creation.finished:
            return RunCreationProgress(run_creation=self.run_creation, has_all_info=True)

        if self.run_creation.game is None:
            return RunCreationProgress(run_creation=self.run_creation, missing_key=InfoKeys.GAME, missing_key_options=[
                game.name for game in get_games_from_gen(locke_min_gen)
            ])
        
        return self._get_creation_missing_extra_info()
    
    def update_progress(self, key: str, value: Any) -> None:
        """Update the run creation with new information.
        
        Args:
            key: The field being updated
            value: The new value for the field
        """
        if key == InfoKeys.GAME:
            self.run_creation.game = str(value)
        
        # Store the raw value in extra_info
        self.run_creation.extra_info[key] = str(value)
        
        update_run_creation(self.run_creation)

    def finish_creation(self, locke: BaseLocke) -> Run:
        """Mark the run creation as complete and return a Run instance.
        
        This method:
        1. Marks the run creation as finished
        2. Updates the run creation in the database
        3. Creates and returns a Run instance for the run
        
        Returns:
            Run: A new Run instance ready to be managed
            
        Raises:
            AssertionError: If the run creation is not finished or missing required data
            StopIteration: If the game name is invalid
        """
        self.run_creation.finished = True
        update_run_creation(self.run_creation)
        return self._create_run(locke)

    def _create_run(self, locke: BaseLocke) -> Run:
        """Create a Run instance from the RunCreation.
        
        This method creates a Run with:
        - ID and name from the run creation
        - Current timestamp as creation date
        - Empty party and box
        
        Returns:
            Run: A new Run instance ready to be managed
            
        Raises:
            AssertionError: If the run creation is not finished or missing required data
            StopIteration: If the game name is invalid
        """
        # Verify run creation is complete
        assert self.run_creation.finished, "Cannot create run from unfinished run creation"
        assert self.run_creation.game is not None, "Run creation must have a game set"
        assert self.run_creation.locke is not None, "Run creation must have a locke type set"
        run_id = uuid4().hex
        print("Creating run id %s for locke %s" % (run_id, locke.name))
        self._populate_run_optional_pokemons(run_id=run_id, locke=locke)
        
        # Create a new run with empty party and box
        return Run(
            id=run_id,
            run_name=self.run_creation.name,
            creation_date=datetime.now(),
            party=Party(pokemons=[]),
            box=Box(pokemons=[])
        )

    def _populate_run_optional_pokemons(self, run_id: str, locke: BaseLocke):
        game = get_game(self.run_creation.game)
        gen_pokemons = list_gen_pokemons(game.gen)
        print("Creating run with potential %s pokemons" % len(gen_pokemons))
        stored_pokemons = set()
        for evolution_line in iterate_gen_evolution_lines(game.gen, reversed=True):
            self._populate_evolution_line_if_relevant(
                run_id, game.gen, evolution_line, locke, stored_pokemons
            )

    def _populate_evolution_line_if_relevant(self, run_id: str, gen: int, evolution_line: List[str], locke: BaseLocke, stored_pokemons: Set[str]):
        relevant_pokemons = False
        for pokemon_name in evolution_line:
            pokemon = fetch_pokemon(pokemon_name, gen)
            if relevant_pokemons or locke.is_pokemon_relevant(pokemon):
                if pokemon_name in stored_pokemons:
                    continue
                stored_pokemons.add(pokemon_name)
                run_options = RunPokemonsOptions(
                    run_id=run_id,
                    pokemon_name=pokemon_name,
                    base_pokemon=evolution_line[-1]
                )
                save_run_options(run_options)
                relevant_pokemons = True

    def _get_creation_missing_extra_info(self) -> RunCreationProgress:
        """Get any additional information needed for run creation.
        
        This method should be overridden by concrete implementations to handle
        their specific requirements.
        
        Returns:
            RunCreationProgress indicating what additional information is needed
        """
        return RunCreationProgress(run_creation=self.run_creation, has_all_info=True)

