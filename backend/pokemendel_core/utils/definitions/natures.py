"""
Pokemon natures definitions and related functionality.

Natures are personality traits that affect a Pokemon's stats. Each nature increases one stat by 10%
and decreases another stat by 10%, or has no effect (neutral natures).
"""
from typing import Optional, Tuple
from pokemendel_core.utils.enum_list import EnumList


class Natures(EnumList):
    """All 25 Pokemon natures with their stat effects."""
    
    # Neutral natures (no stat changes)
    HARDY = "Hardy"
    DOCILE = "Docile"
    SERIOUS = "Serious"
    BASHFUL = "Bashful"
    QUIRKY = "Quirky"
    
    # Attack-increasing natures
    LONELY = "Lonely"      # +Attack, -Defense
    BRAVE = "Brave"        # +Attack, -Speed
    ADAMANT = "Adamant"    # +Attack, -Sp.Atk
    NAUGHTY = "Naughty"    # +Attack, -Sp.Def
    
    # Defense-increasing natures
    BOLD = "Bold"          # +Defense, -Attack
    RELAXED = "Relaxed"    # +Defense, -Speed
    IMPISH = "Impish"      # +Defense, -Sp.Atk
    LAX = "Lax"            # +Defense, -Sp.Def
    
    # Speed-increasing natures
    TIMID = "Timid"        # +Speed, -Attack
    HASTY = "Hasty"        # +Speed, -Defense
    JOLLY = "Jolly"        # +Speed, -Sp.Atk
    NAIVE = "Naive"        # +Speed, -Sp.Def
    
    # Special Attack-increasing natures
    MODEST = "Modest"      # +Sp.Atk, -Attack
    MILD = "Mild"          # +Sp.Atk, -Defense
    QUIET = "Quiet"        # +Sp.Atk, -Speed
    RASH = "Rash"          # +Sp.Atk, -Sp.Def
    
    # Special Defense-increasing natures
    CALM = "Calm"          # +Sp.Def, -Attack
    GENTLE = "Gentle"      # +Sp.Def, -Defense
    SASSY = "Sassy"        # +Sp.Def, -Speed
    CAREFUL = "Careful"    # +Sp.Def, -Sp.Atk


class InvalidNatureError(ValueError):
    """Raised when an invalid nature string is provided."""
    pass


def get_nature_effects(nature: str) -> Tuple[Optional[str], Optional[str]]:
    """Get the stat effects of a nature.
    
    Args:
        nature: The nature to get effects for
        
    Returns:
        Tuple of (increased_stat, decreased_stat) where each can be None for neutral natures
    """
    effects = {
        # Neutral natures
        Natures.HARDY: (None, None),
        Natures.DOCILE: (None, None),
        Natures.SERIOUS: (None, None),
        Natures.BASHFUL: (None, None),
        Natures.QUIRKY: (None, None),
        
        # Attack-increasing natures
        Natures.LONELY: ("Attack", "Defense"),
        Natures.BRAVE: ("Attack", "Speed"),
        Natures.ADAMANT: ("Attack", "Sp.Atk"),
        Natures.NAUGHTY: ("Attack", "Sp.Def"),
        
        # Defense-increasing natures
        Natures.BOLD: ("Defense", "Attack"),
        Natures.RELAXED: ("Defense", "Speed"),
        Natures.IMPISH: ("Defense", "Sp.Atk"),
        Natures.LAX: ("Defense", "Sp.Def"),
        
        # Speed-increasing natures
        Natures.TIMID: ("Speed", "Attack"),
        Natures.HASTY: ("Speed", "Defense"),
        Natures.JOLLY: ("Speed", "Sp.Atk"),
        Natures.NAIVE: ("Speed", "Sp.Def"),
        
        # Special Attack-increasing natures
        Natures.MODEST: ("Sp.Atk", "Attack"),
        Natures.MILD: ("Sp.Atk", "Defense"),
        Natures.QUIET: ("Sp.Atk", "Speed"),
        Natures.RASH: ("Sp.Atk", "Sp.Def"),
        
        # Special Defense-increasing natures
        Natures.CALM: ("Sp.Def", "Attack"),
        Natures.GENTLE: ("Sp.Def", "Defense"),
        Natures.SASSY: ("Sp.Def", "Speed"),
        Natures.CAREFUL: ("Sp.Def", "Sp.Atk"),
    }
    
    return effects[nature]


def from_str(nature_str: str) -> str:
    """Convert a string to a nature value.
    
    Args:
        nature_str: String representation of the nature
        
    Returns:
        Nature string value
        
    Raises:
        InvalidNatureError: If the string doesn't match any nature
    """
    if not isinstance(nature_str, str):
        raise InvalidNatureError(f"Nature must be a string, got {type(nature_str).__name__}")
    
    valid_natures = Natures.list_all()
    if nature_str not in valid_natures:
        raise InvalidNatureError(f"Invalid nature '{nature_str}'. Valid natures: {valid_natures}")
    
    return nature_str


def get_neutral_natures() -> list[str]:
    """Get all neutral natures (those that don't affect stats).
    
    Returns:
        List of neutral natures
    """
    return [
        Natures.HARDY,
        Natures.DOCILE,
        Natures.SERIOUS,
        Natures.BASHFUL,
        Natures.QUIRKY,
    ]


def get_attack_natures() -> list[str]:
    """Get all natures that increase Attack.
    
    Returns:
        List of Attack-increasing natures
    """
    return [
        Natures.LONELY,
        Natures.BRAVE,
        Natures.ADAMANT,
        Natures.NAUGHTY,
    ]


def get_defense_natures() -> list[str]:
    """Get all natures that increase Defense.
    
    Returns:
        List of Defense-increasing natures
    """
    return [
        Natures.BOLD,
        Natures.RELAXED,
        Natures.IMPISH,
        Natures.LAX,
    ]


def get_speed_natures() -> list[str]:
    """Get all natures that increase Speed.
    
    Returns:
        List of Speed-increasing natures
    """
    return [
        Natures.TIMID,
        Natures.HASTY,
        Natures.JOLLY,
        Natures.NAIVE,
    ]


def get_sp_atk_natures() -> list[str]:
    """Get all natures that increase Special Attack.
    
    Returns:
        List of Special Attack-increasing natures
    """
    return [
        Natures.MODEST,
        Natures.MILD,
        Natures.QUIET,
        Natures.RASH,
    ]


def get_sp_def_natures() -> list[str]:
    """Get all natures that increase Special Defense.
    
    Returns:
        List of Special Defense-increasing natures
    """
    return [
        Natures.CALM,
        Natures.GENTLE,
        Natures.SASSY,
        Natures.CAREFUL,
    ]
