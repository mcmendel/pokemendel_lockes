from core.lockes.base.run_creator import RunCreationProgress, RunCreator
from .utils import LEG_TYPE_KEY, NumLegs


class LegRunCreator(RunCreator):

    def _get_creation_missing_extra_info(self) -> RunCreationProgress:
        """Get any additional information needed for run creation.
        
        This method should be overridden by concrete implementations to handle
        their specific requirements.
        
        Returns:
            RunCreationProgress indicating what additional information is needed
        """
        if LEG_TYPE_KEY in self.run_creation.extra_info:
            return RunCreationProgress(run_creation=self.run_creation, has_all_info=True)
        return RunCreationProgress(run_creation=self.run_creation, has_all_info=False, missing_key=LEG_TYPE_KEY, missing_key_options=NumLegs.list_all())
