from core.lockes.base.run_creator import RunCreator, RunCreationProgress, List
from core.lockes.lockes_factory import list_all_lockes, GenLocke, LOCKE_INSTANCES
from core.lockes.run_creation_factory import get_run_creator_class
from games import Game, get_games_from_gen
from pokemendel_core.utils.definitions.regions import Regions


_SELECTED_LOCKE = "_selected_locke"
_GAME_PREFIX = "_game_"

_GEN_TO_REGION = {
    1: Regions.KANTO,
    2: Regions.JOHTO,
    3: Regions.HOENN,
}


class GenRunCreator(RunCreator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._internal_run_creator = None
        if self.run_creation and _SELECTED_LOCKE in self.run_creation.extra_info:
            creator_cls = get_run_creator_class(self.run_creation.extra_info[_SELECTED_LOCKE])
            self._internal_run_creator = creator_cls(self.run_creation)
    def _get_unfinished_progress(self, locke_min_gen: int) -> RunCreationProgress:
        if _SELECTED_LOCKE not in self.run_creation.extra_info:
            return RunCreationProgress(
                self.run_creation,
                has_all_info=False,
                missing_key=_SELECTED_LOCKE,
                missing_key_options=[locke for locke in list_all_lockes() if locke != GenLocke.name]
            )

        for supported_gens in sorted(_GEN_TO_REGION.keys()):
            if f"{_GAME_PREFIX}{supported_gens}" in self.run_creation.extra_info:
                if supported_gens == 1:
                    self.run_creation.game = self.run_creation.extra_info[f"{_GAME_PREFIX}{supported_gens}"]
                continue
            gen_games = self._get_games_from_gen(supported_gens)
            if not gen_games:
                continue
            return RunCreationProgress(
                self.run_creation,
                has_all_info=False,
                missing_key=f"{_GAME_PREFIX}{supported_gens}",
                missing_key_options=[game.name for game in gen_games]
            )
        return self._internal_run_creator.get_progress(locke_min_gen)

    def _get_games_from_gen(self, locke_min_gen: int) -> List[Game]:
        locke_name = self.run_creation.extra_info[_SELECTED_LOCKE]
        locke = LOCKE_INSTANCES[locke_name]
        return [
            game for game in get_games_from_gen(locke.min_gen)
            if game.region == _GEN_TO_REGION[locke_min_gen]
        ]
