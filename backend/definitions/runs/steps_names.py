from pokemendel_core.utils.enum_list import EnumList


class StepsNames(EnumList):
    # party
    ADD_TO_PARTY = "Add to Party"
    REMOVE_FROM_PARTY = "Remove from Party"
    SWITCH_PARTY_POKEMONS = "Replace Pokemon with Party"

    # pokemon actions
    EVOLVE = "Evolve Pokemon"
    KILL = "Kill Pokemon"

    # pokemon attributes
    NICKNAME = "Nickname Pokemon"
    GENDER = "Gender"

    # starlocke
    STARLOCKE_CHOOSE_TYPE = "Choose Type"

    # wedlocke
    WEDLOCKE_PAIR = "Pair Pokemon"

    # chesslocke
    CHESSLOCKE_SET_ROLE = "Set Role"
