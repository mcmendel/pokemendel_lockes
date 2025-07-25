from games import get_game
from pokemendel_core.utils.definitions.types import get_generation_types
from core.lockes.base.run_creator import RunCreationProgress, RunCreator
from .utils import MONO_TYPE_KEY


class MonoRunCreator(RunCreator):

    def _get_creation_missing_extra_info(self) -> RunCreationProgress:
        """Get any additional information needed for run creation.
        
        This method should be overridden by concrete implementations to handle
        their specific requirements.
        
        Returns:
            RunCreationProgress indicating what additional information is needed
        """
        if MONO_TYPE_KEY in self.run_creation.extra_info:
            return RunCreationProgress(run_creation=self.run_creation, has_all_info=True)
        game = get_game(self.run_creation.game)
        generation_types = get_generation_types(game.gen)
        return RunCreationProgress(run_creation=self.run_creation, has_all_info=False, missing_key=MONO_TYPE_KEY, missing_key_options=generation_types)
