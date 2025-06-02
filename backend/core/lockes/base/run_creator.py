"""Base module for run creation functionality.

This module provides the foundation for creating and managing Pokemon game runs.
It defines the RunCreationProgress class which tracks the state of run creation,
including what information has been provided and what is still needed.

The RunCreationProgress class is used by concrete implementations of run creators
to manage the step-by-step process of creating a new run, ensuring all required
information is collected before the run can begin.
"""

from dataclasses import dataclass
from typing import Optional, List, Any
from models.run_creation import RunCreation, update_run_creation
from pokemendel_core.utils.enum_list import EnumList


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

    def get_progress(self) -> RunCreationProgress:
        """Get the current progress of run creation.
        
        Returns:
            RunCreationProgress indicating what information is still needed
        """
        if self.run_creation.finished:
            return RunCreationProgress(run_creation=self.run_creation, has_all_info=True)
        
        if self.run_creation.game is None:
            return RunCreationProgress(run_creation=self.run_creation, missing_key=InfoKeys.GAME)
        
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

    def finish_creation(self) -> None:
        """Mark the run creation as complete."""
        self.run_creation.finished = True
        update_run_creation(self.run_creation)

    def _get_creation_missing_extra_info(self) -> RunCreationProgress:
        """Get any additional information needed for run creation.
        
        This method should be overridden by concrete implementations to handle
        their specific requirements.
        
        Returns:
            RunCreationProgress indicating what additional information is needed
        """
        return RunCreationProgress(run_creation=self.run_creation, has_all_info=True)

