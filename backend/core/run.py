"""Run module for managing Pokemon game runs.

This module provides the Run class which represents a complete Pokemon game run,
including the player's party, box, battles, encounters, and run status.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Generator

from models.pokemon import list_pokemon_by_run
from models.run import Run as DbRun
from apis.exceptions import RunNotFoundError, InvalidGameError
from definitions import Battle, Encounter, Pokemon, EncounterStatus
from games import get_game
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

    def to_db_run(self, gen: int, locke_name: str, game_name: str, is_randomize: bool, duplicate_clause: bool, extra_info: dict) -> DbRun:
        db_run = DbRun(
            run_id=self.id,
            created_date=self.creation_date,
            name=self.run_name,
            locke=locke_name,
            game=game_name,
            gen=gen,
            randomized=is_randomize,
            party=[pokemon.metadata.id for pokemon in self.party.pokemons],
            box=[pokemon.metadata.id for pokemon in self.box.pokemons],
            battles=[],  # Empty array as battles are added during run progress
            encounters=list(self._convert_encounters_to_persist()),
            locke_extra_info=extra_info,
            restarts=self.restarts,
            duplicate_clause=duplicate_clause,
            finished=self.finished,
            starter=self.starter.metadata.id if self.starter else None
        )
        return db_run

    def get_run_pokemons(self) -> Dict[str, Pokemon]:
        return {pokemon.metadata.id: pokemon for pokemon in self.box.pokemons}

    def _convert_encounters_to_persist(self) -> Generator[Dict[str, Optional[str]], None, None]:
        for encounter in self.encounters:
            if encounter.status == EncounterStatus.UNMET:
                continue

            encounter_dict = {
                'route': encounter.route,
                'status': encounter.status,
                'pokemon': encounter.pokemon,
            }
            if encounter.status == EncounterStatus.CAUGHT:
                encounter_dict['pokemon'] = encounter.pokemon.metadata.id
            yield encounter_dict


def _get_run_encounters(db_run, all_pokemons, game):
    """Helper function to build the encounters list for a run.

    Args:
        db_run: The database run object
        all_pokemons: Dictionary mapping pokemon IDs to Pokemon objects
        game: The game instance containing routes and encounters

    Returns:
        List of Encounter objects, one for each route in the game.
        Each encounter has a status (UNMET, MET, KILLED, RAN, or CAUGHT) and
        optionally a pokemon if one was caught.
    """
    # Create a dictionary of existing encounters for quick lookup
    existing_encounters = {
        e['route']: (e['status'], e.get('pokemon'))
        for e in db_run.encounters
    }

    # Create encounters for all routes in the game
    encounters = []
    for route in game.routes:
        if route in existing_encounters:
            # Route has been encountered
            status, pokemon_id = existing_encounters[route]
            pokemon = all_pokemons.get(pokemon_id) or pokemon_id or None
            encounters.append(Encounter(route=route, status=status, pokemon=pokemon))
        else:
            # Route hasn't been encountered yet
            encounters.append(Encounter(route=route, status=EncounterStatus.UNMET, pokemon=None))

    return encounters


def convert_db_run_to_core_run(db_run: DbRun, run_id: str) -> Run:
    if not db_run:
        raise RunNotFoundError(run_id)
    try:
        game = get_game(db_run.game)
    except Exception:
        raise InvalidGameError(db_run.game)

    all_pokemons = {p.metadata.id: p for p in list_pokemon_by_run(run_id)}
    # Build party and box
    party_pokemons = [all_pokemons[pid] for pid in db_run.party if pid in all_pokemons]
    box_pokemons = [all_pokemons[pid] for pid in db_run.box if pid in all_pokemons]
    party = Party(pokemons=party_pokemons)
    box = Box(pokemons=box_pokemons)
    # Battles and encounters
    battles = [Battle(**b) for b in db_run.battles]
    encounters = _get_run_encounters(db_run, all_pokemons, game)
    # Starter
    starter = all_pokemons.get(db_run.starter) if db_run.starter else None
    # Build core Run
    core_run = Run(
        id=db_run.run_id,
        run_name=db_run.name,
        creation_date=db_run.created_date,
        party=party,
        box=box,
        battles=battles,
        encounters=encounters,
        starter=starter,
        restarts=db_run.restarts,
        finished=db_run.finished
    )
    return core_run
