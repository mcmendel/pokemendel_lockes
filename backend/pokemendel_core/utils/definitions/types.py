from ..enum_list import EnumList
from typing import List

class Types(EnumList):
    NORMAL = "Normal"
    FIRE = "Fire"
    WATER = "Water"
    ELECTRIC = "Electric"
    GRASS = "Grass"
    ICE = "Ice"
    FIGHTING = "Fighting"
    POISON = "Poison"
    GROUND = "Ground"
    FLYING = "Flying"
    PSYCHIC = "Psychic"
    BUG = "Bug"
    ROCK = "Rock"
    GHOST = "Ghost"
    DRAGON = "Dragon"
    DARK = "Dark"
    STEEL = "Steel"
    FAIRY = "Fairy"


_GENERATION_TYPES = {
    1: [Types.NORMAL, Types.FIRE, Types.WATER, Types.ELECTRIC, Types.GRASS, Types.ICE, Types.FIGHTING, Types.POISON, Types.GROUND, Types.FLYING, Types.PSYCHIC, Types.BUG, Types.ROCK, Types.GHOST, Types.DRAGON],
    2: [Types.DARK, Types.STEEL],
    6: [Types.FAIRY],
}


def get_generation_types(gen: int) -> List[str]:
    """Get all Pokemon types available up to and including the specified generation.
    
    Args:
        gen (int): The target generation number (1-9)
        
    Returns:
        List[str]: A list of all Pokemon type names available in the specified generation
        
    Raises:
        ValueError: If the generation number is not between 1 and 9
    """
    if not 1 <= gen <= 9:
        raise ValueError("Generation must be between 1 and 9")
        
    all_generation_types = []
    for cur_gen in range(1, gen + 1):
        all_generation_types.extend(_GENERATION_TYPES.get(cur_gen, []))

    return all_generation_types
