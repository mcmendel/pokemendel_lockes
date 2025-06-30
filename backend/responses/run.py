from definitions.runs.encounters import EncounterStatus
from definitions.pokemons.pokemon import Pokemon
from definitions.game import Game
from core.run import Run as CoreRun, Encounter
from core.locke import Locke
from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import List, Optional, Dict

_POKEMON_ID_TYPE = str


@dataclass
class _BattleResponse:
    leader: str
    won: bool


@dataclass
class _EncounterResponse:
    route: str
    pokemon: Optional[_POKEMON_ID_TYPE]
    status: str = EncounterStatus.UNMET


@dataclass
class _Run:
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
    party: List[_POKEMON_ID_TYPE]
    box: List[_POKEMON_ID_TYPE]
    gyms: List[_BattleResponse]
    rules: List[str]
    main_battles: List[str]
    encounters: List[_EncounterResponse] = field(default_factory=list)
    starter: Optional[_POKEMON_ID_TYPE] = None
    restarts: int = 0
    finished: bool = False


@dataclass
class RunResponse:
    run: _Run
    pokemons: Dict[_POKEMON_ID_TYPE, Pokemon]

    @classmethod
    def from_core_run(cls, run: CoreRun, game: Game, locke: Locke):
        response_run = _Run(
            id=run.id,
            run_name=run.run_name,
            creation_date=run.creation_date,
            rules=locke.rules,
            main_battles=game.important_battles,
            party=[
                pokemon.metadata.id for pokemon in run.party.pokemons
            ],
            box=[
                pokemon.metadata.id for pokemon in run.box.pokemons
            ],
            gyms=cls._convert_gyms(run, game),
            encounters=[
                _EncounterResponse(route=encounter.route, pokemon=cls._convert_encounter_pokemon(encounter) if encounter.pokemon else None, status=encounter.status) for encounter in run.encounters
            ],
            starter=run.starter.metadata.id if run.starter else None,
            restarts=run.restarts,
            finished=run.finished,
        )
        return cls(
            run=response_run,
            pokemons=run.get_run_pokemons(),
        )

    @classmethod
    def _convert_encounter_pokemon(cls, encounter: Encounter):
        if not encounter.pokemon:
            return None
        if isinstance(encounter.pokemon, str):
            return encounter.pokemon
        return encounter.pokemon.metadata.id

    @classmethod
    def _convert_gyms(cls, run: CoreRun, game: Game) -> List[_BattleResponse]:
        won_battles = {battle.rival: battle.won for battle in run.battles}
        if len(won_battles) < len(game.gyms):
            return [
                _BattleResponse(leader=gym.leader, won=won_battles.get(gym.leader, False)) for gym in game.gyms
            ]
        
        return [
            _BattleResponse(leader=gym.leader, won=won_battles.get(gym.leader, False)) for gym in game.elite4
        ]

    def to_dict(self) -> Dict:
        return asdict(self)
