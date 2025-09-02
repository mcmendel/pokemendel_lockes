from core.lockes.base.run_creator import RunCreator, RunCreationProgress, List, BaseLocke, InfoKeys
from core.lockes.lockes_factory import list_all_lockes, GenLocke, LOCKE_INSTANCES
from core.lockes.genlocke.utils import (
    SELECTED_LOCKE as _SELECTED_LOCKE,
    get_generation_potential_games,
)
from core.lockes.run_creation_factory import get_run_creator_class
from core.run import Run, convert_db_run_to_core_run, Party, Box
from models.run import fetch_run
from games import Game, get_game

_GAME_PREFIX = "_game_"


class GenRunCreator(RunCreator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._internal_run_creator = None
        self._init_internal_run_creation()
    def _get_unfinished_progress(self, locke_min_gen: int) -> RunCreationProgress:
        if _SELECTED_LOCKE not in self.run_creation.extra_info:
            return RunCreationProgress(
                self.run_creation,
                has_all_info=False,
                missing_key=_SELECTED_LOCKE,
                missing_key_options=[locke for locke in list_all_lockes() if locke != GenLocke.name]
            )
        self._init_internal_run_creation()
        locke = LOCKE_INSTANCES[self.run_creation.extra_info[_SELECTED_LOCKE]]
        if self.run_creation.game is None:
            return RunCreationProgress(run_creation=self.run_creation, missing_key=InfoKeys.GAME, missing_key_options=[
                game.name for game in self._get_games_from_gen(locke_min_gen)
            ])
        creation_progress = self._internal_run_creator.get_progress(locke.min_gen)
        return creation_progress

    def _get_games_from_gen(self, locke_min_gen: int) -> List[Game]:
        locke_name = self.run_creation.extra_info[_SELECTED_LOCKE]
        return get_generation_potential_games(locke_min_gen, locke_name)

    def _init_internal_run_creation(self):
        if not self._internal_run_creator and self.run_creation and _SELECTED_LOCKE in self.run_creation.extra_info:
            creator_cls = get_run_creator_class(self.run_creation.extra_info[_SELECTED_LOCKE])
            self._internal_run_creator = creator_cls(self.run_creation)

    def finish_creation(self, locke: BaseLocke) -> Run:
        self._init_internal_run_creation()
        locke = LOCKE_INSTANCES[self.run_creation.extra_info[_SELECTED_LOCKE]]
        return self._internal_run_creator.finish_creation(locke)

    def finish_creation_existing_run(self, run_id: str, new_game: str) -> Run:
        self.run_creation.game = new_game
        self._internal_run_creator = None
        self._init_internal_run_creation()
        locke = LOCKE_INSTANCES[self.run_creation.extra_info[_SELECTED_LOCKE]]
        game = get_game(new_game)
        self._internal_run_creator._populate_run_optional_pokemons(run_id=run_id, locke=locke)
        db_run = fetch_run(run_id)
        run = convert_db_run_to_core_run(db_run, run_id)
        return Run(
            id=run_id,
            run_name=run.run_name,
            creation_date=run.creation_date,
            party=Party(pokemons=[]),
            box=Box(pokemons=[]),
            gen=game.gen,
        )
