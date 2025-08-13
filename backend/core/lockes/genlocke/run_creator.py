from core.lockes.base.run_creator import RunCreator, RunCreationProgress, List
from core.lockes.lockes_factory import list_all_lockes, GenLocke, LOCKE_INSTANCES
from core.lockes.run_creation_factory import get_run_creator_class
from games import Game, get_games_from_gen, get_game
from pokemendel_core.utils.definitions.regions import Regions


_SELECTED_LOCKE = "_selected_locke"
_GAME_PREFIX = "_game_"

_GEN_TO_REGION = {
    1: Regions.KANTO,
    2: Regions.JOHTO,
    3: Regions.HOENN,
}

_REGION_TO_GEN = {region: gen for gen, region in _GEN_TO_REGION.items()}


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
        creation_progress = self._internal_run_creator.get_progress(locke.min_gen)
        return creation_progress

    def _get_games_from_gen(self, locke_min_gen: int) -> List[Game]:
        locke_name = self.run_creation.extra_info[_SELECTED_LOCKE]
        locke = LOCKE_INSTANCES[locke_name]
        return [
            game for game in get_games_from_gen(locke.min_gen)
            if game.region == _GEN_TO_REGION[locke_min_gen]
        ]

    def _init_internal_run_creation(self):
        if not self._internal_run_creator and self.run_creation and _SELECTED_LOCKE in self.run_creation.extra_info:
            creator_cls = get_run_creator_class(self.run_creation.extra_info[_SELECTED_LOCKE])
            self._internal_run_creator = creator_cls(self.run_creation)
