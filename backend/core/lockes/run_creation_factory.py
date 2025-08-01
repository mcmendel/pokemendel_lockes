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
from core.lockes.leg.run_creator import LegRunCreator
from core.lockes.leg.leg_locke import LegLocke
from core.lockes.eevee.eevee_locke import EeveeLocke
from core.lockes.eevee.run_creator import EeveeRunCreator
from core.lockes.star.run_creator import StarRunCreator
from core.lockes.star.star_locke import StarLocke
from core.lockes.color.color_locke import ColorLocke
from core.lockes.color.run_creator import ColorRunCreator


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
    if locke_name == LegLocke.name:
        return LegRunCreator
    if locke_name == EeveeLocke.name:
        return EeveeRunCreator
    if locke_name == StarLocke.name:
        return StarRunCreator
    if locke_name == ColorLocke.name:
        return ColorRunCreator
    return RunCreator 
