from core.lockes.genlocke.gen_locke import GenLocke
from core.lockes.lockes_factory_no_gen import *
from typing import List

# Dictionary mapping locke names to their instances
LOCKE_INSTANCES = {locke_name: locke_inst for locke_name, locke_inst in LOCKE_INSTANCES.items()}
LOCKE_INSTANCES[GenLocke.name] = GenLocke()


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
