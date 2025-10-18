"""
Definitions for Pokemon regions.
"""
from ..enum_list import EnumList


class Regions(EnumList):
    """Class containing Pokemon region definitions.
    
    Inherits from EnumList to provide list_all functionality.
    """
    
    # Region Constants
    KANTO = "Kanto"
    JOHTO = "Johto"
    HOENN = "Hoenn"
