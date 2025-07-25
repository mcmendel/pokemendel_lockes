"""Factory module for run creation classes.

This module provides a factory function to get the appropriate run creation class
based on the locke name. It maps locke names to their corresponding run creation
classes, defaulting to the base RunCreator if no specific implementation exists.
"""

from typing import Type
from core.lockes.base.run_creator import RunCreator
from core.lockes.mono.mono_locke import MonoLocke
from core.lockes.mono.run_creator import MonoRunCreator
from core.lockes.category.run_creator import CategoryRunCreator
from core.lockes.category.category_locke import CategoryLocke


def get_run_creator_class(locke_name: str) -> Type[RunCreator]:
    """Get the appropriate run creation class for a given locke name.
    
    Args:
        locke_name: The name of the locke (e.g., 'nuzlocke', 'soulocke', etc.)
        
    Returns:
        The RunCreator class appropriate for the given locke name.
        Currently, this always returns the base RunCreator class.
        
    Example:
        >>> creator_class = get_run_creator_class('nuzlocke')
        >>> creator = creator_class('my_run')
    """
    # TODO: Add specific implementations for different locke types
    # For now, all lockes use the base implementation
    if locke_name == MonoLocke.name:
        return MonoRunCreator
    if locke_name == CategoryLocke.name:
        return CategoryRunCreator
    return RunCreator 
