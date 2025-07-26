from pokemendel_core.utils.definitions.categories import Categories
from core.lockes.base.run_creator import RunCreationProgress, RunCreator
from .utils import CATEGORY_TYPE_KEY


class CategoryRunCreator(RunCreator):

    def _get_creation_missing_extra_info(self) -> RunCreationProgress:
        """Get any additional information needed for run creation.
        
        This method should be overridden by concrete implementations to handle
        their specific requirements.
        
        Returns:
            RunCreationProgress indicating what additional information is needed
        """
        if CATEGORY_TYPE_KEY in self.run_creation.extra_info:
            return RunCreationProgress(run_creation=self.run_creation, has_all_info=True)
        return RunCreationProgress(run_creation=self.run_creation, has_all_info=False, missing_key=CATEGORY_TYPE_KEY, missing_key_options=Categories.list_all())
