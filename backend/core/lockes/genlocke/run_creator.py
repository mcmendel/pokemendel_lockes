from core.lockes.base.run_creator import RunCreator, RunCreationProgress
from core.lockes.lockes_factory import list_all_lockes, GenLocke


_SELECTED_LOCKE = "_selected_locke"


class GenRunCreator(RunCreator):
    def _get_unfinished_progress(self, locke_min_gen: int) -> RunCreationProgress:
        if _SELECTED_LOCKE not in self.run_creation.extra_info:
            return RunCreationProgress(
                self.run_creation,
                has_all_info=False,
                missing_key=_SELECTED_LOCKE,
                missing_key_options=[locke for locke in list_all_lockes() if locke != GenLocke.name]
            )
        return super()._get_unfinished_progress(locke_min_gen)
