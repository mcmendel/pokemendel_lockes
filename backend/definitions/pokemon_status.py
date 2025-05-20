from pokemendel_core.utils.enum_list import EnumList

class PokemonStatus(EnumList):
    """Represents the possible states a Pokémon can be in during a Locke run."""
    ALIVE = "alive"      # Pokémon is active and can be used
    DEAD = "dead"        # Pokémon has been defeated and cannot be used