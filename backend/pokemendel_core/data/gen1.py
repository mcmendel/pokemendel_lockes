"""Generation 1 Pokemon data module."""

from ..models.pokemon import Pokemon
from ..models.evolution.evolution import Evolution
from ..models.evolution.evolution_type import EvolutionType
from ..models.evolution.items import Item
from ..utils.definitions.types import Types
from ..utils.definitions.colors import Colors
from ..utils.definitions.categories import Categories
from .utils.names import PokemonNames as PokemonGen1


NAME_TO_POKEMON = {
    PokemonGen1.BULBASAUR: Pokemon(
        name=PokemonGen1.BULBASAUR,
        gen=1,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.IVYSAUR)
        ],
        colors=[Colors.GREEN, Colors.BLUE],
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
            Categories.FROG
        ],
        num_legs=4,
    ),
    PokemonGen1.IVYSAUR: Pokemon(
        name=PokemonGen1.IVYSAUR,
        gen=1,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.VENUSAUR)
        ],
        colors=[Colors.BLUE, Colors.GREEN, Colors.PINK],
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
            Categories.FROG
        ],
        num_legs=4,
    ),
    PokemonGen1.VENUSAUR: Pokemon(
        name=PokemonGen1.VENUSAUR,
        gen=1,
        types=[Types.GRASS, Types.POISON],
        colors=[Colors.BLUE, Colors.GREEN, Colors.PINK],
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
            Categories.FROG
        ],
        num_legs=4,
    ),
    PokemonGen1.CHARMANDER: Pokemon(
        name=PokemonGen1.CHARMANDER,
        gen=1,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen1.CHARMELEON)
        ],
        colors=[Colors.ORANGE],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.DRAGON,
        ],
        num_legs=2,
    ),
    PokemonGen1.CHARMELEON: Pokemon(
        name=PokemonGen1.CHARMELEON,
        gen=1,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen1.CHARIZARD)
        ],
        colors=[Colors.RED],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.DRAGON,
        ],
        num_legs=2,
    ),
    PokemonGen1.CHARIZARD: Pokemon(
        name=PokemonGen1.CHARIZARD,
        gen=1,
        types=[Types.FIRE, Types.FLYING],
        colors=[Colors.ORANGE],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.DRAGON,
            Categories.WING,
        ],
        num_legs=2,
    ),
    PokemonGen1.SQUIRTLE: Pokemon(
        name=PokemonGen1.SQUIRTLE,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.WARTORTLE)
        ],
        colors=[Colors.BLUE, Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.TURTLE,
        ],
        num_legs=2,
    ),
    PokemonGen1.WARTORTLE: Pokemon(
        name=PokemonGen1.WARTORTLE,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.BLASTOISE)
        ],
        colors=[Colors.BLUE, Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.TURTLE,
        ],
        num_legs=2,
    ),
    PokemonGen1.BLASTOISE: Pokemon(
        name=PokemonGen1.BLASTOISE,
        gen=1,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.TURTLE,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen1.CATERPIE: Pokemon(
        name=PokemonGen1.CATERPIE,
        gen=1,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen1.METAPOD)
        ],
        colors=[Colors.GREEN],
        categories=[
            Categories.BUG,
        ],
        num_legs=6,
    ),
    PokemonGen1.METAPOD: Pokemon(
        name=PokemonGen1.METAPOD,
        gen=1,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen1.BUTTERFREE)
        ],
        colors=[Colors.GREEN],
        categories=[
            Categories.BUG,
        ],
        num_legs=0,
    ),
    PokemonGen1.BUTTERFREE: Pokemon(
        name=PokemonGen1.BUTTERFREE,
        gen=1,
        types=[Types.BUG, Types.FLYING],
        colors=[Colors.WHITE, Colors.PURPLE],
        categories=[
            Categories.BUG,
            Categories.WING,
        ],
        num_legs=2,
    ),
    PokemonGen1.WEEDLE: Pokemon(
        name=PokemonGen1.WEEDLE,
        gen=1,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.KAKUNA)
        ],
        colors=[Colors.BROWN],
        categories=[
            Categories.BUG,
            Categories.WEAPON,
        ],
        num_legs=14,
    ),
    PokemonGen1.KAKUNA: Pokemon(
        name=PokemonGen1.KAKUNA,
        gen=1,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.BEEDRILL)
        ],
        colors=[Colors.YELLOW],
        categories=[
            Categories.BUG,
        ],
        num_legs=0,
    ),
    PokemonGen1.BEEDRILL: Pokemon(
        name=PokemonGen1.BEEDRILL,
        gen=1,
        types=[Types.BUG, Types.POISON],
        colors=[Colors.YELLOW, Colors.BLACK],
        categories=[
            Categories.BUG,
            Categories.WEAPON,
            Categories.WING,
        ],
        num_legs=2,
    ),
    PokemonGen1.PIDGEY: Pokemon(
        name=PokemonGen1.PIDGEY,
        gen=1,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen1.PIDGEOTTO)
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.FOOD,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen1.PIDGEOTTO: Pokemon(
        name=PokemonGen1.PIDGEOTTO,
        gen=1,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen1.PIDGEOT)
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.FOOD,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen1.PIDGEOT: Pokemon(
        name=PokemonGen1.PIDGEOT,
        gen=1,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.FOOD,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen1.RATTATA: Pokemon(
        name=PokemonGen1.RATTATA,
        gen=1,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen1.RATICATE)
        ],
        colors=[Colors.PURPLE, Colors.WHITE],
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=4,
    ),
    PokemonGen1.RATICATE: Pokemon(
        name=PokemonGen1.RATICATE,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=4,
    ),
    PokemonGen1.SPEAROW: Pokemon(
        name=PokemonGen1.SPEAROW,
        gen=1,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen1.FEAROW)
        ],
        colors=[Colors.BROWN, Colors.RED, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.FOOD,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen1.FEAROW: Pokemon(
        name=PokemonGen1.FEAROW,
        gen=1,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.BROWN, Colors.RED, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.FOOD,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen1.EKANS: Pokemon(
        name=PokemonGen1.EKANS,
        gen=1,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.ARBOK)
        ],
        colors=[Colors.PURPLE, Colors.WHITE],
        categories=[
            Categories.REPTILE,
            Categories.FOOD,
            Categories.SNAKE,
        ],
        num_legs=0,
    ),
    PokemonGen1.ARBOK: Pokemon(
        name=PokemonGen1.ARBOK,
        gen=1,
        types=[Types.POISON],
        colors=[Colors.PURPLE],
        categories=[
            Categories.REPTILE,
            Categories.FOOD,
            Categories.SNAKE,
        ],
        num_legs=0,
    ),
    PokemonGen1.PIKACHU: Pokemon(
        name=PokemonGen1.PIKACHU,
        gen=1,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen1.RAICHU, level=41, evolution_type=EvolutionType.STONE, item=Item.THUNDER_STONE)
        ],
        colors=[Colors.YELLOW],
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=4,
    ),
    PokemonGen1.RAICHU: Pokemon(
        name=PokemonGen1.RAICHU,
        gen=1,
        types=[Types.ELECTRIC],
        colors=[Colors.YELLOW, Colors.ORANGE],
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
    ),
    PokemonGen1.SANDSHREW: Pokemon(
        name=PokemonGen1.SANDSHREW,
        gen=1,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen1.SANDSLASH)
        ],
        colors=[Colors.YELLOW, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.MOUSE,
            Categories.RODENT,
        ],
        num_legs=2,
    ),
    PokemonGen1.SANDSLASH: Pokemon(
        name=PokemonGen1.SANDSLASH,
        gen=1,
        types=[Types.GROUND],
        colors=[Colors.YELLOW, Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.MOUSE,
            Categories.RODENT,
        ],
        num_legs=2,
    ),
    PokemonGen1.NIDORAN_F: Pokemon(
        name=PokemonGen1.NIDORAN_F,
        gen=1,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.NIDORINA)
        ],
        colors=[Colors.BLUE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
        ],
        num_legs=4,
    ),
    PokemonGen1.NIDORINA: Pokemon(
        name=PokemonGen1.NIDORINA,
        gen=1,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.NIDOQUEEN, level=19, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE)
        ],
        colors=[Colors.BLUE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
        ],
        num_legs=4,
    ),
    PokemonGen1.NIDOQUEEN: Pokemon(
        name=PokemonGen1.NIDOQUEEN,
        gen=1,
        types=[Types.POISON, Types.GROUND],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
        ],
        num_legs=2,
    ),
    PokemonGen1.NIDORAN_M: Pokemon(
        name=PokemonGen1.NIDORAN_M,
        gen=1,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.NIDORINO)
        ],
        colors=[Colors.PURPLE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
        ],
        num_legs=4,
    ),
    PokemonGen1.NIDORINO: Pokemon(
        name=PokemonGen1.NIDORINO,
        gen=1,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.NIDOKING, level=19, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE)
        ],
        colors=[Colors.PURPLE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
        ],
        num_legs=4,
    ),
    PokemonGen1.NIDOKING: Pokemon(
        name=PokemonGen1.NIDOKING,
        gen=1,
        types=[Types.POISON, Types.GROUND],
        colors=[Colors.PURPLE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen1.CLEFAIRY: Pokemon(
        name=PokemonGen1.CLEFAIRY,
        gen=1,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen1.CLEFABLE, level=34, item=Item.MOON_STONE, evolution_type=EvolutionType.STONE)
        ],
        colors=[Colors.PINK],
        categories=[
            Categories.FANTASY,
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.CLEFABLE: Pokemon(
        name=PokemonGen1.CLEFABLE,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.PINK],
        categories=[
            Categories.FANTASY,
            Categories.MAMMAL,
            Categories.HUMAN,
            Categories.WING,
        ],
        num_legs=2,
    ),
    PokemonGen1.VULPIX: Pokemon(
        name=PokemonGen1.VULPIX,
        gen=1,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen1.NINETALES, level=31, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE)
        ],
        colors=[Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen1.NINETALES: Pokemon(
        name=PokemonGen1.NINETALES,
        gen=1,
        types=[Types.FIRE],
        colors=[Colors.YELLOW],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen1.JIGGLYPUFF: Pokemon(
        name=PokemonGen1.JIGGLYPUFF,
        gen=1,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen1.WIGGLYTUFF, level=34, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE)
        ],
        colors=[Colors.PINK],
        categories=[
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=2,
    ),
    PokemonGen1.WIGGLYTUFF: Pokemon(
        name=PokemonGen1.WIGGLYTUFF,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.PINK],
        categories=[
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=2,
    ),
    PokemonGen1.ZUBAT: Pokemon(
        name=PokemonGen1.ZUBAT,
        gen=1,
        types=[Types.POISON, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen1.GOLBAT)
        ],
        colors=[Colors.BLUE],
        categories=[
            Categories.WING,
            Categories.MAMMAL,
        ],
        num_legs=0,
    ),
    PokemonGen1.GOLBAT: Pokemon(
        name=PokemonGen1.GOLBAT,
        gen=1,
        types=[Types.POISON, Types.FLYING],
        colors=[Colors.BLUE],
        categories=[
            Categories.WING,
            Categories.MAMMAL,
        ],
        num_legs=2,
    ),
    PokemonGen1.ODDISH: Pokemon(
        name=PokemonGen1.ODDISH,
        gen=1,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.GLOOM)
        ],
        colors=[Colors.BLUE, Colors.GREEN],
        categories=[
            Categories.PLANT,
            Categories.FOOD,
        ],
        num_legs=2,
    ),
    PokemonGen1.GLOOM: Pokemon(
        name=PokemonGen1.GLOOM,
        gen=1,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.VILEPLUME, level=44, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE)
        ],
        colors=[Colors.BLUE, Colors.RED],
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen1.VILEPLUME: Pokemon(
        name=PokemonGen1.VILEPLUME,
        gen=1,
        types=[Types.GRASS, Types.POISON],
        colors=[Colors.BLUE, Colors.RED],
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen1.PARAS: Pokemon(
        name=PokemonGen1.PARAS,
        gen=1,
        types=[Types.BUG, Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen1.PARASECT)
        ],
        colors=[Colors.ORANGE, Colors.RED, Colors.YELLOW],
        categories=[
            Categories.PLANT,
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=4,
    ),
    PokemonGen1.PARASECT: Pokemon(
        name=PokemonGen1.PARASECT,
        gen=1,
        types=[Types.BUG, Types.GRASS],
        colors=[Colors.ORANGE, Colors.RED],
        categories=[
            Categories.PLANT,
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=4,
    ),
    PokemonGen1.VENONAT: Pokemon(
        name=PokemonGen1.VENONAT,
        gen=1,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.VENOMOTH)
        ],
        colors=[Colors.PURPLE, Colors.RED],
        categories=[
            Categories.BUG,
        ],
        num_legs=2,
    ),
    PokemonGen1.VENOMOTH: Pokemon(
        name=PokemonGen1.VENOMOTH,
        gen=1,
        types=[Types.BUG, Types.POISON],
        colors=[Colors.PURPLE],
        categories=[
            Categories.BUG,
            Categories.WING,
        ],
        num_legs=0,
    ),
    PokemonGen1.DIGLETT: Pokemon(
        name=PokemonGen1.DIGLETT,
        gen=1,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen1.DUGTRIO)
        ],
        colors=[Colors.BROWN],
        categories=[
            Categories.BUG,
            Categories.REPTILE,
        ],
        num_legs=0,
    ),
    PokemonGen1.DUGTRIO: Pokemon(
        name=PokemonGen1.DUGTRIO,
        gen=1,
        types=[Types.GROUND],
        colors=[Colors.BROWN],
        categories=[
            Categories.BUG,
            Categories.REPTILE,
        ],
        num_legs=0,
    ),
    PokemonGen1.MEOWTH: Pokemon(
        name=PokemonGen1.MEOWTH,
        gen=1,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen1.PERSIAN)
        ],
        colors=[Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
    ),
    PokemonGen1.PERSIAN: Pokemon(
        name=PokemonGen1.PERSIAN,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
    ),
    PokemonGen1.PSYDUCK: Pokemon(
        name=PokemonGen1.PSYDUCK,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.GOLDUCK)
        ],
        colors=[Colors.YELLOW],
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.DUCK,
        ],
        num_legs=2,
    ),
    PokemonGen1.GOLDUCK: Pokemon(
        name=PokemonGen1.GOLDUCK,
        gen=1,
        types=[Types.WATER],
        colors=[Colors.BLUE],
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.DUCK,
        ],
        num_legs=2,
    ),
    PokemonGen1.MANKEY: Pokemon(
        name=PokemonGen1.MANKEY,
        gen=1,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen1.PRIMEAPE)
        ],
        colors=[Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
    ),
    PokemonGen1.PRIMEAPE: Pokemon(
        name=PokemonGen1.PRIMEAPE,
        gen=1,
        types=[Types.FIGHTING],
        colors=[Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
    ),
    PokemonGen1.GROWLITHE: Pokemon(
        name=PokemonGen1.GROWLITHE,
        gen=1,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen1.ARCANINE, level=50, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE)
        ],
        colors=[Colors.ORANGE, Colors.BLACK, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen1.ARCANINE: Pokemon(
        name=PokemonGen1.ARCANINE,
        gen=1,
        types=[Types.FIRE],
        colors=[Colors.ORANGE, Colors.BLACK, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen1.POLIWAG: Pokemon(
        name=PokemonGen1.POLIWAG,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.POLIWHIRL)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FROG,
        ],
        num_legs=2,
    ),
    PokemonGen1.POLIWHIRL: Pokemon(
        name=PokemonGen1.POLIWHIRL,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.POLIWRATH, level=43, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FROG,
        ],
        num_legs=2,
    ),
    PokemonGen1.POLIWRATH: Pokemon(
        name=PokemonGen1.POLIWRATH,
        gen=1,
        types=[Types.WATER, Types.FIGHTING],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FROG,
        ],
        num_legs=2,
    ),
    PokemonGen1.ABRA: Pokemon(
        name=PokemonGen1.ABRA,
        gen=1,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen1.KADABRA)
        ],
        colors=[Colors.YELLOW, Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
    ),
    PokemonGen1.KADABRA: Pokemon(
        name=PokemonGen1.KADABRA,
        gen=1,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen1.ALAKAZAM, evolution_type=EvolutionType.TRADE)
        ],
        colors=[Colors.YELLOW, Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
    ),
    PokemonGen1.ALAKAZAM: Pokemon(
        name=PokemonGen1.ALAKAZAM,
        gen=1,
        types=[Types.PSYCHIC],
        colors=[Colors.YELLOW, Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
    ),
    PokemonGen1.MACHOP: Pokemon(
        name=PokemonGen1.MACHOP,
        gen=1,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen1.MACHOKE)
        ],
        colors=[Colors.GRAY],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.MACHOKE: Pokemon(
        name=PokemonGen1.MACHOKE,
        gen=1,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen1.MACHAMP, evolution_type=EvolutionType.TRADE)
        ],
        colors=[Colors.GRAY, Colors.BLUE],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.MACHAMP: Pokemon(
        name=PokemonGen1.MACHAMP,
        gen=1,
        types=[Types.FIGHTING],
        colors=[Colors.BLUE, Colors.GRAY],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.BELLSPROUT: Pokemon(
        name=PokemonGen1.BELLSPROUT,
        gen=1,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.WEEPINBELL)
        ],
        colors=[Colors.YELLOW, Colors.GREEN],
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen1.WEEPINBELL: Pokemon(
        name=PokemonGen1.WEEPINBELL,
        gen=1,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.VICTREEBEL, level=54, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE)
        ],
        colors=[Colors.YELLOW, Colors.GREEN],
        categories=[
            Categories.PLANT,
        ],
        num_legs=0,
    ),
    PokemonGen1.VICTREEBEL: Pokemon(
        name=PokemonGen1.VICTREEBEL,
        gen=1,
        types=[Types.GRASS, Types.POISON],
        colors=[Colors.YELLOW, Colors.GREEN],
        categories=[
            Categories.PLANT,
        ],
        num_legs=0,
    ),
    PokemonGen1.TENTACOOL: Pokemon(
        name=PokemonGen1.TENTACOOL,
        gen=1,
        types=[Types.WATER, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.TENTACRUEL)
        ],
        colors=[Colors.BLUE, Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.TENTACRUEL: Pokemon(
        name=PokemonGen1.TENTACRUEL,
        gen=1,
        types=[Types.WATER, Types.POISON],
        colors=[Colors.BLUE, Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.GEODUDE: Pokemon(
        name=PokemonGen1.GEODUDE,
        gen=1,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen1.GRAVELER)
        ],
        colors=[Colors.GRAY],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.GRAVELER: Pokemon(
        name=PokemonGen1.GRAVELER,
        gen=1,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen1.GOLEM, evolution_type=EvolutionType.TRADE)
        ],
        colors=[Colors.GRAY],
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
    ),
    PokemonGen1.GOLEM: Pokemon(
        name=PokemonGen1.GOLEM,
        gen=1,
        types=[Types.ROCK, Types.GROUND],
        colors=[Colors.GRAY, Colors.GREEN],
        categories=[
            Categories.REPTILE,
            Categories.FOOD,
            Categories.TURTLE,
        ],
        num_legs=2,
    ),
    PokemonGen1.PONYTA: Pokemon(
        name=PokemonGen1.PONYTA,
        gen=1,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen1.RAPIDASH)
        ],
        colors=[Colors.WHITE, Colors.RED],
        categories=[
            Categories.MAMMAL,
            Categories.HORSE,
        ],
        num_legs=4,
    ),
    PokemonGen1.RAPIDASH: Pokemon(
        name=PokemonGen1.RAPIDASH,
        gen=1,
        types=[Types.FIRE],
        colors=[Colors.WHITE, Colors.RED],
        categories=[
            Categories.MAMMAL,
            Categories.HORSE,
        ],
        num_legs=4,
    ),
    PokemonGen1.SLOWPOKE: Pokemon(
        name=PokemonGen1.SLOWPOKE,
        gen=1,
        types=[Types.WATER, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen1.SLOWBRO)
        ],
        colors=[Colors.PINK],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.SLOTH,
        ],
        num_legs=4,
    ),
    PokemonGen1.SLOWBRO: Pokemon(
        name=PokemonGen1.SLOWBRO,
        gen=1,
        types=[Types.WATER, Types.PSYCHIC],
        colors=[Colors.PINK, Colors.GRAY],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.SLOTH,
        ],
        num_legs=2,
    ),
    PokemonGen1.MAGNEMITE: Pokemon(
        name=PokemonGen1.MAGNEMITE,
        gen=1,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen1.MAGNETON)
        ],
        colors=[Colors.GRAY, Colors.BLUE, Colors.RED],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.MAGNETON: Pokemon(
        name=PokemonGen1.MAGNETON,
        gen=1,
        types=[Types.ELECTRIC],
        colors=[Colors.GRAY, Colors.BLUE, Colors.RED],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.FARFETCHD: Pokemon(
        name=PokemonGen1.FARFETCHD,
        gen=1,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.BROWN],
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.DUCK,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen1.DODUO: Pokemon(
        name=PokemonGen1.DODUO,
        gen=1,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen1.DODRIO)
        ],
        colors=[Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen1.DODRIO: Pokemon(
        name=PokemonGen1.DODRIO,
        gen=1,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen1.SEEL: Pokemon(
        name=PokemonGen1.SEEL,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.DEWGONG)
        ],
        colors=[Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.DOG,
        ],
        num_legs=0,
    ),
    PokemonGen1.DEWGONG: Pokemon(
        name=PokemonGen1.DEWGONG,
        gen=1,
        types=[Types.WATER, Types.ICE],
        colors=[Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.DOG,
        ],
        num_legs=0,
    ),
    PokemonGen1.GRIMER: Pokemon(
        name=PokemonGen1.GRIMER,
        gen=1,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.MUK)
        ],
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.MUK: Pokemon(
        name=PokemonGen1.MUK,
        gen=1,
        types=[Types.POISON],
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.SHELLDER: Pokemon(
        name=PokemonGen1.SHELLDER,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.CLOYSTER, level=49, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE)
        ],
        colors=[Colors.PURPLE, Colors.BLACK],
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.CLOYSTER: Pokemon(
        name=PokemonGen1.CLOYSTER,
        gen=1,
        types=[Types.WATER, Types.ICE],
        colors=[Colors.GRAY, Colors.BLUE],
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.GASTLY: Pokemon(
        name=PokemonGen1.GASTLY,
        gen=1,
        types=[Types.GHOST, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.HAUNTER)
        ],
        colors=[Colors.BLACK, Colors.PURPLE],
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
    ),
    PokemonGen1.HAUNTER: Pokemon(
        name=PokemonGen1.HAUNTER,
        gen=1,
        types=[Types.GHOST, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.GENGAR, evolution_type=EvolutionType.TRADE)
        ],
        num_legs=0,
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM
        ],
    ),
    PokemonGen1.GENGAR: Pokemon(
        name=PokemonGen1.GENGAR,
        gen=1,
        types=[Types.GHOST, Types.POISON],
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM
        ],
        num_legs=2,
    ),
    PokemonGen1.ONIX: Pokemon(
        name=PokemonGen1.ONIX,
        gen=1,
        types=[Types.ROCK, Types.GROUND],
        colors=[Colors.GRAY],
        categories=[
            Categories.REPTILE,
            Categories.SNAKE,
        ],
        num_legs=0,
    ),
    PokemonGen1.DROWZEE: Pokemon(
        name=PokemonGen1.DROWZEE,
        gen=1,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen1.HYPNO)
        ],
        colors=[Colors.YELLOW, Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.PIG,
        ],
        num_legs=2,
    ),
    PokemonGen1.HYPNO: Pokemon(
        name=PokemonGen1.HYPNO,
        gen=1,
        types=[Types.PSYCHIC],
        colors=[Colors.YELLOW],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
            Categories.PIG,
        ],
        num_legs=2,
    ),
    PokemonGen1.KRABBY: Pokemon(
        name=PokemonGen1.KRABBY,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.KINGLER)
        ],
        colors=[Colors.ORANGE, Colors.WHITE],
        categories=[
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=4,
    ),
    PokemonGen1.KINGLER: Pokemon(
        name=PokemonGen1.KINGLER,
        gen=1,
        types=[Types.WATER],
        colors=[Colors.WHITE, Colors.ORANGE],
        categories=[
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=4,
    ),
    PokemonGen1.VOLTORB: Pokemon(
        name=PokemonGen1.VOLTORB,
        gen=1,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen1.ELECTRODE)
        ],
        colors=[Colors.RED, Colors.WHITE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.ELECTRODE: Pokemon(
        name=PokemonGen1.ELECTRODE,
        gen=1,
        types=[Types.ELECTRIC],
        colors=[Colors.RED, Colors.WHITE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.EXEGGCUTE: Pokemon(
        name=PokemonGen1.EXEGGCUTE,
        gen=1,
        types=[Types.GRASS, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen1.EXEGGUTOR, level=43, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE)
        ],
        colors=[Colors.PINK],
        categories=[
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.EXEGGUTOR: Pokemon(
        name=PokemonGen1.EXEGGUTOR,
        gen=1,
        types=[Types.GRASS, Types.PSYCHIC],
        colors=[Colors.BROWN, Colors.YELLOW, Colors.GREEN],
        categories=[
            Categories.FOOD,
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen1.CUBONE: Pokemon(
        name=PokemonGen1.CUBONE,
        gen=1,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen1.MAROWAK)
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen1.MAROWAK: Pokemon(
        name=PokemonGen1.MAROWAK,
        gen=1,
        types=[Types.GROUND],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen1.HITMONLEE: Pokemon(
        name=PokemonGen1.HITMONLEE,
        gen=1,
        types=[Types.FIGHTING],
        colors=[Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.HITMONCHAN: Pokemon(
        name=PokemonGen1.HITMONCHAN,
        gen=1,
        types=[Types.FIGHTING],
        colors=[Colors.BROWN, Colors.RED],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.LICKITUNG: Pokemon(
        name=PokemonGen1.LICKITUNG,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.PINK, Colors.YELLOW],
        categories=[
            Categories.FROG,
        ],
        num_legs=2,
    ),
    PokemonGen1.KOFFING: Pokemon(
        name=PokemonGen1.KOFFING,
        gen=1,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen1.WEEZING)
        ],
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.WEEZING: Pokemon(
        name=PokemonGen1.WEEZING,
        gen=1,
        types=[Types.POISON],
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.RHYHORN: Pokemon(
        name=PokemonGen1.RHYHORN,
        gen=1,
        types=[Types.GROUND, Types.ROCK],
        evolves_to=[
            Evolution(name=PokemonGen1.RHYDON)
        ],
        colors=[Colors.GRAY],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
        ],
        num_legs=4,
    ),
    PokemonGen1.RHYDON: Pokemon(
        name=PokemonGen1.RHYDON,
        gen=1,
        types=[Types.GROUND, Types.ROCK],
        colors=[Colors.GRAY, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
        ],
        num_legs=2,
    ),
    PokemonGen1.CHANSEY: Pokemon(
        name=PokemonGen1.CHANSEY,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.PINK, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.TANGELA: Pokemon(
        name=PokemonGen1.TANGELA,
        gen=1,
        types=[Types.GRASS],
        colors=[Colors.GREEN],
        categories=[
            Categories.PLANT,
            Categories.FOOD,
        ],
        num_legs=2,
    ),
    PokemonGen1.KANGASKHAN: Pokemon(
        name=PokemonGen1.KANGASKHAN,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=2,
    ),
    PokemonGen1.HORSEA: Pokemon(
        name=PokemonGen1.HORSEA,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.SEADRA)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.DRAGON,
        ],
        num_legs=0,
    ),
    PokemonGen1.SEADRA: Pokemon(
        name=PokemonGen1.SEADRA,
        gen=1,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.DRAGON,
        ],
        num_legs=0,
    ),
    PokemonGen1.GOLDEEN: Pokemon(
        name=PokemonGen1.GOLDEEN,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.SEAKING)
        ],
        colors=[Colors.WHITE, Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.SEAKING: Pokemon(
        name=PokemonGen1.SEAKING,
        gen=1,
        types=[Types.WATER],
        colors=[Colors.ORANGE, Colors.WHITE, Colors.BLACK],
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.STARYU: Pokemon(
        name=PokemonGen1.STARYU,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.STARMIE, level=50, item=Item.WATER_STONE, evolution_type=EvolutionType.STONE)
        ],
        colors=[Colors.BROWN, Colors.YELLOW, Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.STARMIE: Pokemon(
        name=PokemonGen1.STARMIE,
        gen=1,
        types=[Types.WATER, Types.PSYCHIC],
        colors=[Colors.PURPLE, Colors.YELLOW, Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.MR_MIME: Pokemon(
        name=PokemonGen1.MR_MIME,
        gen=1,
        types=[Types.PSYCHIC],
        colors=[Colors.PINK, Colors.WHITE, Colors.BLUE],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.SCYTHER: Pokemon(
        name=PokemonGen1.SCYTHER,
        gen=1,
        types=[Types.BUG, Types.FLYING],
        colors=[Colors.GREEN, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.BUG,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen1.JYNX: Pokemon(
        name=PokemonGen1.JYNX,
        gen=1,
        types=[Types.ICE, Types.PSYCHIC],
        colors=[Colors.PURPLE, Colors.YELLOW, Colors.RED],
        categories=[
            Categories.MAMMAL,
            Categories.FANTASY,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.ELECTABUZZ: Pokemon(
        name=PokemonGen1.ELECTABUZZ,
        gen=1,
        types=[Types.ELECTRIC],
        colors=[Colors.YELLOW, Colors.BLACK],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.MAGMAR: Pokemon(
        name=PokemonGen1.MAGMAR,
        gen=1,
        types=[Types.FIRE],
        colors=[Colors.RED, Colors.YELLOW],
        categories=[
            Categories.BIRD,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.DUCK,
        ],
        num_legs=2,
    ),
    PokemonGen1.PINSIR: Pokemon(
        name=PokemonGen1.PINSIR,
        gen=1,
        types=[Types.BUG],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.BUG,
        ],
        num_legs=2,
    ),
    PokemonGen1.TAUROS: Pokemon(
        name=PokemonGen1.TAUROS,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.CATTLE,
            Categories.COW,
        ],
        num_legs=4,
    ),
    PokemonGen1.MAGIKARP: Pokemon(
        name=PokemonGen1.MAGIKARP,
        gen=1,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.GYARADOS)
        ],
        colors=[Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
            Categories.FISH,
        ],
        num_legs=0,
    ),
    PokemonGen1.GYARADOS: Pokemon(
        name=PokemonGen1.GYARADOS,
        gen=1,
        types=[Types.WATER, Types.FLYING],
        colors=[Colors.BLUE, Colors.YELLOW],
        categories=[
            Categories.WATERMON,
            Categories.DRAGON,
        ],
        num_legs=0,
    ),
    PokemonGen1.LAPRAS: Pokemon(
        name=PokemonGen1.LAPRAS,
        gen=1,
        types=[Types.WATER, Types.ICE],
        colors=[Colors.BLUE, Colors.GRAY, Colors.WHITE],
        categories=[
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FANTASY,
            Categories.TURTLE,
        ],
        num_legs=0,
    ),
    PokemonGen1.DITTO: Pokemon(
        name=PokemonGen1.DITTO,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.PINK],
        categories=[
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.EEVEE: Pokemon(
        name=PokemonGen1.EEVEE,
        gen=1,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen1.VAPOREON, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE),
            Evolution(name=PokemonGen1.JOLTEON, evolution_type=EvolutionType.STONE, item=Item.THUNDER_STONE),
            Evolution(name=PokemonGen1.FLAREON, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE),
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen1.VAPOREON: Pokemon(
        name=PokemonGen1.VAPOREON,
        gen=1,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
            Categories.WATERMON,
        ],
        num_legs=4,
    ),
    PokemonGen1.JOLTEON: Pokemon(
        name=PokemonGen1.JOLTEON,
        gen=1,
        types=[Types.ELECTRIC],
        colors=[Colors.YELLOW, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen1.FLAREON: Pokemon(
        name=PokemonGen1.FLAREON,
        gen=1,
        types=[Types.FIRE],
        colors=[Colors.RED, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen1.PORYGON: Pokemon(
        name=PokemonGen1.PORYGON,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.BLUE, Colors.PINK],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen1.OMANYTE: Pokemon(
        name=PokemonGen1.OMANYTE,
        gen=1,
        types=[Types.ROCK, Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.OMASTAR)
        ],
        colors=[Colors.BLUE, Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.OMASTAR: Pokemon(
        name=PokemonGen1.OMASTAR,
        gen=1,
        types=[Types.ROCK, Types.WATER],
        colors=[Colors.BLUE, Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.KABUTO: Pokemon(
        name=PokemonGen1.KABUTO,
        gen=1,
        types=[Types.ROCK, Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen1.KABUTOPS)
        ],
        colors=[Colors.BROWN, Colors.BLACK],
        categories=[
            Categories.PREHISTORIC,
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen1.KABUTOPS: Pokemon(
        name=PokemonGen1.KABUTOPS,
        gen=1,
        types=[Types.ROCK, Types.WATER],
        colors=[Colors.BROWN, Colors.BLACK],
        categories=[
            Categories.PREHISTORIC,
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen1.AERODACTYL: Pokemon(
        name=PokemonGen1.AERODACTYL,
        gen=1,
        types=[Types.ROCK, Types.FLYING],
        colors=[Colors.GRAY, Colors.PURPLE],
        categories=[
            Categories.PREHISTORIC,
            Categories.WING,
            Categories.REPTILE,
        ],
        num_legs=2,
    ),
    PokemonGen1.SNORLAX: Pokemon(
        name=PokemonGen1.SNORLAX,
        gen=1,
        types=[Types.NORMAL],
        colors=[Colors.GREEN, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.BEAR,
        ],
        num_legs=2,
    ),
    PokemonGen1.ARTICUNO: Pokemon(
        name=PokemonGen1.ARTICUNO,
        gen=1,
        types=[Types.ICE, Types.FLYING],
        colors=[Colors.BLUE],
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen1.ZAPDOS: Pokemon(
        name=PokemonGen1.ZAPDOS,
        gen=1,
        types=[Types.ELECTRIC, Types.FLYING],
        colors=[Colors.YELLOW],
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen1.MOLTRES: Pokemon(
        name=PokemonGen1.MOLTRES,
        gen=1,
        types=[Types.FIRE, Types.FLYING],
        colors=[Colors.RED, Colors.YELLOW, Colors.ORANGE],
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen1.DRATINI: Pokemon(
        name=PokemonGen1.DRATINI,
        gen=1,
        types=[Types.DRAGON],
        evolves_to=[
            Evolution(name=PokemonGen1.DRAGONAIR)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FANTASY,
            Categories.DRAGON,
            Categories.SNAKE,
        ],
        num_legs=0,
    ),
    PokemonGen1.DRAGONAIR: Pokemon(
        name=PokemonGen1.DRAGONAIR,
        gen=1,
        types=[Types.DRAGON],
        evolves_to=[
            Evolution(name=PokemonGen1.DRAGONITE)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FANTASY,
            Categories.DRAGON,
            Categories.SNAKE,
        ],
        num_legs=0,
    ),
    PokemonGen1.DRAGONITE: Pokemon(
        name=PokemonGen1.DRAGONITE,
        gen=1,
        types=[Types.DRAGON, Types.FLYING],
        colors=[Colors.ORANGE, Colors.GREEN, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.REPTILE,
            Categories.FANTASY,
            Categories.DRAGON,
        ],
        num_legs=2,
    ),
    PokemonGen1.MEWTWO: Pokemon(
        name=PokemonGen1.MEWTWO,
        gen=1,
        types=[Types.PSYCHIC],
        colors=[Colors.GRAY, Colors.PURPLE],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen1.MEW: Pokemon(
        name=PokemonGen1.MEW,
        gen=1,
        types=[Types.PSYCHIC],
        colors=[Colors.PINK],
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
    ),
}
    
    
    
    
