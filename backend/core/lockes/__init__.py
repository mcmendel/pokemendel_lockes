"""Locke module initialization.

This module provides the core functionality for different types of Pokemon game runs.
"""

from core.lockes.run_creation_factory import get_run_creator_class
from core.lockes.base.base_locke import BaseLocke
from core.lockes.mono.mono_locke import MonoLocke
from core.lockes.unique.unique_locke import UniqueLocke
from typing import List

# Dictionary mapping locke names to their instances
LOCKE_INSTANCES = {
    BaseLocke.name: BaseLocke(),
    MonoLocke.name: MonoLocke(),
    UniqueLocke.name: UniqueLocke(),
    # TODO: Add more locke instances as they are implemented
    # Example:
    # Nuzlocke.name: Nuzlocke(),
    # Soulocke.name: Soulocke(),
}


def list_all_lockes() -> List[str]:
    """Get a list of all available locke names.
    
    Returns:
        List[str]: A list of locke names.
        
    Example:
        >>> lockes = list_all_lockes()
        >>> print(lockes)
        ['BaseLocke']
    """
    return list(LOCKE_INSTANCES.keys())


__all__ = ['get_run_creator_class', 'LOCKE_INSTANCES', 'list_all_lockes']
