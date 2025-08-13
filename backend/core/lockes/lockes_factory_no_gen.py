from core.lockes.base.base_locke import BaseLocke
from core.lockes.mono.mono_locke import MonoLocke
from core.lockes.unique.unique_locke import UniqueLocke
from core.lockes.category.category_locke import CategoryLocke
from core.lockes.leg.leg_locke import LegLocke
from core.lockes.eevee.eevee_locke import EeveeLocke
from core.lockes.wed.wed_locke import WedLocke
from core.lockes.chess.chess_locke import ChessLocke
from core.lockes.star.star_locke import StarLocke
from core.lockes.wrap.wrap_locke import WrapLocke
from core.lockes.color.color_locke import ColorLocke
from core.lockes.castform.castform_locke import CastformLocke
from core.lockes.deoxys.deoxys_locke import DeoxysLocke
from typing import List

# Dictionary mapping locke names to their instances
LOCKE_INSTANCES = {
    BaseLocke.name: BaseLocke(),
    MonoLocke.name: MonoLocke(),
    UniqueLocke.name: UniqueLocke(),
    CategoryLocke.name: CategoryLocke(),
    LegLocke.name: LegLocke(),
    EeveeLocke.name: EeveeLocke(),
    WedLocke.name: WedLocke(),
    ChessLocke.name: ChessLocke(),
    StarLocke.name: StarLocke(),
    WrapLocke.name: WrapLocke(),
    ColorLocke.name: ColorLocke(),
    CastformLocke.name: CastformLocke(),
    DeoxysLocke.name: DeoxysLocke(),
}
