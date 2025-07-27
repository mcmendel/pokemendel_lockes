from pokemendel_core.utils.enum_list import EnumList

LEG_TYPE_KEY = "num_legs"


class NumLegs(EnumList):
    ZERO = "no legs"
    ONE = "1"
    TWO = "2"
    FOUR = "4"
    OTHER = "a lot"
