"""Generation 2 Pokemon data module."""

from ..models.pokemon import Pokemon
from ..models.evolution.evolution import Evolution
from ..models.evolution.evolution_type import EvolutionType
from ..models.evolution.items import Item
from ..utils.definitions.types import Types
from ..utils.definitions.colors import Colors
from ..utils.definitions.categories import Categories
from ..utils.definitions.stats import Stats
from ..utils.definitions.genders import Genders
from .utils.names import PokemonNames as PokemonGen2
from .gen1 import NAME_TO_POKEMON as NAME_TO_POKEMON_GEN1
from dataclasses import replace
from copy import deepcopy

_GEN1_STATS = {
    PokemonGen2.BULBASAUR: Stats(
            attack=49,
            defence=49,
            special_attack=65,
            special_defence=65,
    ),
    PokemonGen2.IVYSAUR: Stats(
            attack=62,
            defence=63,
            special_attack=80,
            special_defence=80,
    ),
    PokemonGen2.VENUSAUR: Stats(
            attack=82,
            defence=83,
            special_attack=100,
            special_defence=100,
    ),
    PokemonGen2.CHARMANDER: Stats(
            attack=39,
            defence=52,
            special_attack=43,
            special_defence=60,
    ),
    PokemonGen2.CHARMELEON: Stats(
            attack=58,
            defence=64,
            special_attack=58,
            special_defence=80,
    ),
    PokemonGen2.CHARIZARD: Stats(
            attack=84,
            defence=78,
            special_attack=78,
            special_defence=109,
    ),
    PokemonGen2.SQUIRTLE: Stats(
            attack=59,
            defence=63,
            special_attack=58,
            special_defence=67,
    ),
    PokemonGen2.WARTORTLE: Stats(
            attack=83,
            defence=80,
            special_attack=80,
            special_defence=100,
    ),
    PokemonGen2.BLASTOISE: Stats(
            attack=100,
            defence=110,
            special_attack=95,
            special_defence=80,
    ),
    PokemonGen2.CATERPIE: Stats(
            attack=30,
            defence=35,
            special_attack=45,
            special_defence=20,
    ),
    PokemonGen2.METAPOD: Stats(
            attack=70,
            defence=60,
            special_attack=65,
            special_defence=55,
    ),
    PokemonGen2.BUTTERFREE: Stats(
            attack=80,
            defence=55,
            special_attack=65,
            special_defence=75,
    ),
    PokemonGen2.WEEDLE: Stats(
            attack=75,
            defence=35,
            special_attack=55,
            special_defence=25,
    ),
    PokemonGen2.KAKUNA: Stats(
            attack=80,
            defence=55,
            special_attack=65,
            special_defence=75,
    ),
    PokemonGen2.BEEDRILL: Stats(
            attack=100,
            defence=65,
            special_attack=60,
            special_defence=70,
    ),
    PokemonGen2.PIDGEY: Stats(
            attack=45,
            defence=40,
            special_attack=35,
            special_defence=35,
    ),
    PokemonGen2.PIDGEOTTO: Stats(
            attack=60,
            defence=55,
            special_attack=50,
            special_defence=50,
    ),
    PokemonGen2.PIDGEOT: Stats(
            attack=83,
            defence=80,
            special_attack=75,
            special_defence=70,
    ),
    PokemonGen2.RATTATA: Stats(
            attack=55,
            defence=35,
            special_attack=30,
            special_defence=40,
    ),
    PokemonGen2.RATICATE: Stats(
            attack=75,
            defence=55,
            special_attack=40,
            special_defence=50,
    ),
    PokemonGen2.SPEAROW: Stats(
            attack=65,
            defence=60,
            special_attack=60,
            special_defence=70,
    ),
    PokemonGen2.FEAROW: Stats(
            attack=85,
            defence=65,
            special_attack=60,
            special_defence=70,
    ),
    PokemonGen2.EKANS: Stats(
            attack=60,
            defence=60,
            special_attack=40,
            special_defence=40,
    ),
    PokemonGen2.ARBOK: Stats(
            attack=85,
            defence=60,
            special_attack=60,
            special_defence=70,
    ),
    PokemonGen2.PIKACHU: Stats(
            attack=50,
            defence=40,
            special_attack=40,
            special_defence=40,
    ),
    PokemonGen2.RAICHU: Stats(
            attack=90,
            defence=55,
            special_attack=65,
            special_defence=85,
    ),
    PokemonGen2.SANDSHREW: Stats(
            attack=50,
            defence=95,
            special_attack=40,
            special_defence=50,
    ),
    PokemonGen2.SANDSLASH: Stats(
            attack=75,
            defence=100,
            special_attack=60,
            special_defence=70,
    ),
    PokemonGen2.NIDORAN_F: Stats(
            attack=50,
            defence=25,
            special_attack=25,
            special_defence=35,
    ),
    PokemonGen2.NIDORINA: Stats(
            attack=70,
            defence=55,
            special_attack=55,
            special_defence=45,
    ),
    PokemonGen2.NIDOQUEEN: Stats(
            attack=90,
            defence=85,
            special_attack=75,
            special_defence=85,
    ),
    PokemonGen2.NIDORAN_M: Stats(
            attack=50,
            defence=25,
            special_attack=25,
            special_defence=35,
    ),
    PokemonGen2.NIDORINO: Stats(
            attack=70,
            defence=55,
            special_attack=55,
            special_defence=45,
    ),
    PokemonGen2.NIDOKING: Stats(
            attack=90,
            defence=85,
            special_attack=75,
            special_defence=85,
    ),
    PokemonGen2.CLEFAIRY: Stats(
            attack=70,
            defence=45,
            special_attack=48,
            special_defence=60,
    ),
    PokemonGen2.CLEFABLE: Stats(
            attack=95,
            defence=75,
            special_attack=80,
            special_defence=100,
    ),
    PokemonGen2.VULPIX: Stats(
            attack=38,
            defence=41,
            special_attack=40,
            special_defence=50,
    ),
    PokemonGen2.NINETALES: Stats(
            attack=73,
            defence=76,
            special_attack=75,
            special_defence=81,
    ),
    PokemonGen2.JIGGLYPUFF: Stats(
            attack=115,
            defence=45,
            special_attack=20,
            special_defence=20,
    ),
    PokemonGen2.WIGGLYTUFF: Stats(
            attack=100,
            defence=50,
            special_attack=50,
            special_defence=75,
    ),
    PokemonGen2.ZUBAT: Stats(
            attack=40,
            defence=30,
            special_attack=50,
            special_defence=55,
    ),
    PokemonGen2.GOLBAT: Stats(
            attack=75,
            defence=80,
            special_attack=70,
            special_defence=90,
    ),
    PokemonGen2.ODDISH: Stats(
            attack=45,
            defence=50,
            special_attack=55,
            special_defence=75,
    ),
    PokemonGen2.GLOOM: Stats(
            attack=65,
            defence=70,
            special_attack=85,
            special_defence=75,
    ),
    PokemonGen2.VILEPLUME: Stats(
            attack=75,
            defence=80,
            special_attack=85,
            special_defence=90,
    ),
    PokemonGen2.PARAS: Stats(
            attack=40,
            defence=30,
            special_attack=50,
            special_defence=55,
    ),
    PokemonGen2.PARASECT: Stats(
            attack=60,
            defence=55,
            special_attack=50,
            special_defence=40,
    ),
    PokemonGen2.VENONAT: Stats(
            attack=65,
            defence=55,
            special_attack=50,
            special_defence=40,
    ),
    PokemonGen2.VENOMOTH: Stats(
            attack=65,
            defence=55,
            special_attack=50,
            special_defence=40,
    ),
    PokemonGen2.DIGLETT: Stats(
            attack=35,
            defence=100,
            special_attack=50,
            special_defence=50,
    ),
    PokemonGen2.DUGTRIO: Stats(
            attack=85,
            defence=90,
            special_attack=80,
            special_defence=70,
    ),
    PokemonGen2.MEOWTH: Stats(
            attack=45,
            defence=50,
            special_attack=43,
            special_defence=38,
    ),
    PokemonGen2.PERSIAN: Stats(
            attack=65,
            defence=60,
            special_attack=60,
            special_defence=70,
    ),
    PokemonGen2.PSYDUCK: Stats(
            attack=85,
            defence=73,
            special_attack=70,
            special_defence=70,
    ),
    PokemonGen2.GOLDUCK: Stats(
            attack=85,
            defence=73,
            special_attack=70,
            special_defence=70,
    ),
    PokemonGen2.MANKEY: Stats(
            attack=40,
            defence=35,
            special_attack=30,
            special_defence=20,
    ),
    PokemonGen2.PRIMEAPE: Stats(
            attack=65,
            defence=50,
            special_attack=52,
            special_defence=50,
    ),
    PokemonGen2.GROWLITHE: Stats(
            attack=65,
            defence=50,
            special_attack=52,
            special_defence=50,
    ),
    PokemonGen2.ARCANINE: Stats(
            attack=90,
            defence=70,
            special_attack=80,
            special_defence=70,
    ),
    PokemonGen2.POLIWAG: Stats(
            attack=40,
            defence=40,
            special_attack=35,
            special_defence=50,
    ),
    PokemonGen2.POLIWHIRL: Stats(
            attack=65,
            defence=65,
            special_attack=60,
            special_defence=50,
    ),
    PokemonGen2.POLIWRATH: Stats(
            attack=65,
            defence=65,
            special_attack=60,
            special_defence=50,
    ),
    PokemonGen2.ABRA: Stats(
            attack=25,
            defence=20,
            special_attack=15,
            special_defence=90,
    ),
    PokemonGen2.KADABRA: Stats(
            attack=50,
            defence=45,
            special_attack=75,
            special_defence=85,
    ),
    PokemonGen2.ALAKAZAM: Stats(
            attack=55,
            defence=50,
            special_attack=45,
            special_defence=135,
    ),
    PokemonGen2.MACHOP: Stats(
            attack=70,
            defence=80,
            special_attack=50,
            special_defence=35,
    ),
    PokemonGen2.MACHOKE: Stats(
            attack=80,
            defence=100,
            special_attack=30,
            special_defence=50,
    ),
    PokemonGen2.MACHAMP: Stats(
            attack=90,
            defence=130,
            special_attack=45,
            special_defence=55,
    ),
    PokemonGen2.BELLSPROUT: Stats(
            attack=50,
            defence=75,
            special_attack=35,
            special_defence=70,
    ),
    PokemonGen2.WEEPINBELL: Stats(
            attack=60,
            defence=90,
            special_attack=50,
            special_defence=85,
    ),
    PokemonGen2.VICTREEBEL: Stats(
            attack=80,
            defence=105,
            special_attack=65,
            special_defence=100,
    ),
    PokemonGen2.TENTACOOL: Stats(
            attack=40,
            defence=35,
            special_attack=30,
            special_defence=50,
    ),
    PokemonGen2.TENTACRUEL: Stats(
            attack=80,
            defence=70,
            special_attack=65,
            special_defence=80,
    ),
    PokemonGen2.GEODUDE: Stats(
            attack=55,
            defence=85,
            special_attack=45,
            special_defence=50,
    ),
    PokemonGen2.GRAVELER: Stats(
            attack=80,
            defence=105,
            special_attack=65,
            special_defence=100,
    ),
    PokemonGen2.GOLEM: Stats(
            attack=80,
            defence=105,
            special_attack=65,
            special_defence=100,
    ),
    PokemonGen2.PONYTA: Stats(
            attack=85,
            defence=55,
            special_attack=65,
            special_defence=60,
    ),
    PokemonGen2.RAPIDASH: Stats(
            attack=85,
            defence=55,
            special_attack=65,
            special_defence=60,
    ),
    PokemonGen2.SLOWPOKE: Stats(
            attack=30,
            defence=40,
            special_attack=50,
            special_defence=50,
    ),
    PokemonGen2.SLOWBRO: Stats(
            attack=95,
            defence=75,
            special_attack=80,
            special_defence=100,
    ),
    PokemonGen2.MAGNEMITE: Stats(
            attack=25,
            defence=35,
            special_attack=70,
            special_defence=95,
    ),
    PokemonGen2.MAGNETON: Stats(
            attack=50,
            defence=60,
            special_attack=95,
            special_defence=120,
    ),
    PokemonGen2.FARFETCHD: Stats(
            attack=35,
            defence=85,
            special_attack=45,
            special_defence=35,
    ),
    PokemonGen2.DODUO: Stats(
            attack=35,
            defence=85,
            special_attack=45,
            special_defence=35,
    ),
    PokemonGen2.DODRIO: Stats(
            attack=60,
            defence=110,
            special_attack=60,
            special_defence=60,
    ),
    PokemonGen2.SEEL: Stats(
            attack=65,
            defence=50,
            special_attack=35,
            special_defence=60,
    ),
    PokemonGen2.DEWGONG: Stats(
            attack=90,
            defence=65,
            special_attack=65,
            special_defence=55,
    ),
    PokemonGen2.GRIMER: Stats(
            attack=80,
            defence=105,
            special_attack=65,
            special_defence=100,
    ),
    PokemonGen2.MUK: Stats(
            attack=105,
            defence=105,
            special_attack=75,
            special_defence=65,
    ),
    PokemonGen2.SHELLDER: Stats(
            attack=30,
            defence=105,
            special_attack=95,
            special_defence=55,
    ),
    PokemonGen2.CLOYSTER: Stats(
            attack=50,
            defence=95,
            special_attack=180,
            special_defence=85,
    ),
    PokemonGen2.GASTLY: Stats(
            attack=30,
            defence=35,
            special_attack=30,
            special_defence=100,
    ),
    PokemonGen2.HAUNTER: Stats(
            attack=45,
            defence=50,
            special_attack=45,
            special_defence=100,
    ),
    PokemonGen2.GENGAR: Stats(
            attack=60,
            defence=110,
            special_attack=80,
            special_defence=100,
    ),
    PokemonGen2.ONIX: Stats(
            attack=35,
            defence=45,
            special_attack=160,
            special_defence=30,
    ),
    PokemonGen2.DROWZEE: Stats(
            attack=40,
            defence=30,
            special_attack=50,
            special_defence=55,
    ),
    PokemonGen2.HYPNO: Stats(
            attack=85,
            defence=40,
            special_attack=80,
            special_defence=100,
    ),
    PokemonGen2.KRABBY: Stats(
            attack=55,
            defence=115,
            special_attack=45,
            special_defence=70,
    ),
    PokemonGen2.KINGLER: Stats(
            attack=55,
            defence=115,
            special_attack=45,
            special_defence=70,
    ),
    PokemonGen2.VOLTORB: Stats(
            attack=60,
            defence=50,
            special_attack=70,
            special_defence=80,
    ),
    PokemonGen2.ELECTRODE: Stats(
            attack=60,
            defence=50,
            special_attack=70,
            special_defence=80,
    ),
    PokemonGen2.EXEGGCUTE: Stats(
            attack=60,
            defence=50,
            special_attack=70,
            special_defence=80,
    ),
    PokemonGen2.EXEGGUTOR: Stats(
            attack=95,
            defence=55,
            special_attack=85,
            special_defence=45,
    ),
    PokemonGen2.CUBONE: Stats(
            attack=50,
            defence=50,
            special_attack=95,
            special_defence=35,
    ),
    PokemonGen2.MAROWAK: Stats(
            attack=80,
            defence=80,
            special_attack=50,
            special_defence=40,
    ),
    PokemonGen2.HITMONLEE: Stats(
            attack=100,
            defence=53,
            special_attack=110,
            special_defence=87,
    ),
    PokemonGen2.HITMONCHAN: Stats(
            attack=100,
            defence=53,
            special_attack=110,
            special_defence=87,
    ),
    PokemonGen2.LICKITUNG: Stats(
            attack=90,
            defence=55,
            special_attack=25,
            special_defence=35,
    ),
    PokemonGen2.KOFFING: Stats(
            attack=60,
            defence=60,
            special_attack=60,
            special_defence=60,
    ),
    PokemonGen2.WEEZING: Stats(
            attack=60,
            defence=60,
            special_attack=60,
            special_defence=60,
    ),
    PokemonGen2.RHYHORN: Stats(
            attack=80,
            defence=80,
            special_attack=40,
            special_defence=40,
    ),
    PokemonGen2.RHYDON: Stats(
            attack=105,
            defence=75,
            special_attack=85,
            special_defence=40,
    ),
    PokemonGen2.CHANSEY: Stats(
            attack=100,
            defence=53,
            special_attack=110,
            special_defence=87,
    ),
    PokemonGen2.TANGELA: Stats(
            attack=65,
            defence=55,
            special_attack=115,
            special_defence=60,
    ),
    PokemonGen2.KANGASKHAN: Stats(
            attack=105,
            defence=95,
            special_attack=85,
            special_defence=95,
    ),
    PokemonGen2.HORSEA: Stats(
            attack=30,
            defence=40,
            special_attack=70,
            special_defence=20,
    ),
    PokemonGen2.SEADRA: Stats(
            attack=55,
            defence=65,
            special_attack=95,
            special_defence=85,
    ),
    PokemonGen2.GOLDEEN: Stats(
            attack=55,
            defence=65,
            special_attack=95,
            special_defence=85,
    ),
    PokemonGen2.SEAKING: Stats(
            attack=85,
            defence=95,
            special_attack=55,
            special_defence=45,
    ),
    PokemonGen2.STARYU: Stats(
            attack=50,
            defence=50,
            special_attack=95,
            special_defence=85,
    ),
    PokemonGen2.STARMIE: Stats(
            attack=50,
            defence=50,
            special_attack=95,
            special_defence=85,
    ),
    PokemonGen2.MR_MIME: Stats(
            attack=80,
            defence=80,
            special_attack=50,
            special_defence=40,
    ),
    PokemonGen2.SCYTHER: Stats(
            attack=70,
            defence=100,
            special_attack=55,
            special_defence=80,
    ),
    PokemonGen2.JYNX: Stats(
            attack=95,
            defence=95,
            special_attack=90,
            special_defence=90,
    ),
    PokemonGen2.ELECTABUZZ: Stats(
            attack=95,
            defence=95,
            special_attack=90,
            special_defence=90,
    ),
    PokemonGen2.MAGMAR: Stats(
            attack=95,
            defence=95,
            special_attack=90,
            special_defence=90,
    ),
    PokemonGen2.PINSIR: Stats(
            attack=100,
            defence=125,
            special_attack=100,
            special_defence=50,
    ),
    PokemonGen2.TAUROS: Stats(
            attack=130,
            defence=85,
            special_attack=80,
            special_defence=60,
    ),
    PokemonGen2.MAGIKARP: Stats(
            attack=80,
            defence=100,
            special_attack=20,
            special_defence=50,
    ),
    PokemonGen2.GYARADOS: Stats(
            attack=85,
            defence=90,
            special_attack=100,
            special_defence=120,
    ),
    PokemonGen2.LAPRAS: Stats(
            attack=130,
            defence=85,
            special_attack=80,
            special_defence=60,
    ),
    PokemonGen2.DITTO: Stats(
            attack=45,
            defence=50,
            special_attack=45,
            special_defence=50,
    ),
    PokemonGen2.EEVEE: Stats(
            attack=55,
            defence=50,
            special_attack=40,
            special_defence=55,
    ),
    PokemonGen2.VAPOREON: Stats(
            attack=65,
            defence=60,
            special_attack=110,
            special_defence=95,
    ),
    PokemonGen2.JOLTEON: Stats(
            attack=65,
            defence=60,
            special_attack=110,
            special_defence=95,
    ),
    PokemonGen2.FLAREON: Stats(
            attack=65,
            defence=60,
            special_attack=110,
            special_defence=95,
    ),
    PokemonGen2.PORYGON: Stats(
            attack=60,
            defence=70,
            special_attack=85,
            special_defence=75,
    ),
    PokemonGen2.OMANYTE: Stats(
            attack=35,
            defence=40,
            special_attack=100,
            special_defence=90,
    ),
    PokemonGen2.OMASTAR: Stats(
            attack=55,
            defence=105,
            special_attack=100,
            special_defence=50,
    ),
    PokemonGen2.KABUTO: Stats(
            attack=55,
            defence=105,
            special_attack=100,
            special_defence=50,
    ),
    PokemonGen2.KABUTOPS: Stats(
            attack=55,
            defence=105,
            special_attack=100,
            special_defence=50,
    ),
    PokemonGen2.AERODACTYL: Stats(
            attack=80,
            defence=105,
            special_attack=60,
            special_defence=70,
    ),
    PokemonGen2.SNORLAX: Stats(
            attack=160,
            defence=110,
            special_attack=65,
            special_defence=110,
    ),
    PokemonGen2.ARTICUNO: Stats(
            attack=90,
            defence=85,
            special_attack=100,
            special_defence=95,
    ),
    PokemonGen2.ZAPDOS: Stats(
            attack=90,
            defence=85,
            special_attack=100,
            special_defence=95,
    ),
    PokemonGen2.MOLTRES: Stats(
            attack=90,
            defence=85,
            special_attack=100,
            special_defence=95,
    ),
    PokemonGen2.DRATINI: Stats(
            attack=61,
            defence=84,
            special_attack=65,
            special_defence=70,
    ),
    PokemonGen2.DRAGONAIR: Stats(
            attack=61,
            defence=84,
            special_attack=65,
            special_defence=70,
    ),
    PokemonGen2.DRAGONITE: Stats(
            attack=106,
            defence=90,
            special_attack=130,
            special_defence=90,
    ),
    PokemonGen2.MEWTWO: Stats(
            attack=106,
            defence=90,
            special_attack=130,
            special_defence=90,
    ),
    PokemonGen2.MEW: Stats(
            attack=100,
            defence=100,
            special_attack=100,
            special_defence=100,
    ),
}

_GEN1_GENDERS = {
    PokemonGen2.NIDORAN_F: [Genders.FEMALE],
    PokemonGen2.NIDORINA: [Genders.FEMALE],
    PokemonGen2.NIDOQUEEN: [Genders.FEMALE],
    PokemonGen2.NIDORAN_M: [Genders.MALE],
    PokemonGen2.NIDORINO: [Genders.MALE],
    PokemonGen2.NIDOKING: [Genders.MALE],
    PokemonGen2.MAGNEMITE: [Genders.GENDERLESS],
    PokemonGen2.MAGNETON: [Genders.GENDERLESS],
    PokemonGen2.VOLTORB: [Genders.GENDERLESS],
    PokemonGen2.ELECTRODE: [Genders.GENDERLESS],
    PokemonGen2.HITMONLEE: [Genders.MALE],
    PokemonGen2.HITMONCHAN: [Genders.MALE],
    PokemonGen2.CHANSEY: [Genders.FEMALE],
    PokemonGen2.KANGASKHAN: [Genders.FEMALE],
    PokemonGen2.STARYU: [Genders.GENDERLESS],
    PokemonGen2.STARMIE: [Genders.GENDERLESS],
    PokemonGen2.JYNX: [Genders.FEMALE],
    PokemonGen2.TAUROS: [Genders.MALE],
    PokemonGen2.DITTO: [Genders.GENDERLESS],
    PokemonGen2.PORYGON: [Genders.GENDERLESS],
    PokemonGen2.ARTICUNO: [Genders.GENDERLESS],
    PokemonGen2.MOLTRES: [Genders.GENDERLESS],
    PokemonGen2.ZAPDOS: [Genders.GENDERLESS],
    PokemonGen2.MEWTWO: [Genders.GENDERLESS],
    PokemonGen2.MEW: [Genders.GENDERLESS],
}

NAME_TO_POKEMON = {
    pokemon_name: replace(
        deepcopy(pokemon),
        gen=2,
        stats=_GEN1_STATS[pokemon_name],
        supported_genders=_GEN1_GENDERS.get(pokemon_name, [Genders.MALE, Genders.FEMALE])
    )
    for pokemon_name, pokemon in NAME_TO_POKEMON_GEN1.items()
}

# update gen1 pokemons with changes
NAME_TO_POKEMON[PokemonGen2.GOLBAT].evolves_to = [Evolution(name=PokemonGen2.CROBAT, evolution_type=EvolutionType.FRIENDSHIP,)]
NAME_TO_POKEMON[PokemonGen2.GLOOM].evolves_to.append(Evolution(name=PokemonGen2.BELLOSSOM, level=44, evolution_type=EvolutionType.STONE, item=Item.SUN_STONE))
NAME_TO_POKEMON[PokemonGen2.POLIWHIRL].evolves_to = [
    Evolution(name=PokemonGen2.POLIWRATH, level=35, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE),
    Evolution(name=PokemonGen2.POLITOED, evolution_type=EvolutionType.TRADE, should_hold=True, item=Item.KINGS_ROCK),
]
NAME_TO_POKEMON[PokemonGen2.GLOOM].evolves_to.append(Evolution(name=PokemonGen2.BELLOSSOM, level=44, evolution_type=EvolutionType.STONE, item=Item.SUN_STONE))
NAME_TO_POKEMON[PokemonGen2.MAGNEMITE].types.append(Types.STEEL)
NAME_TO_POKEMON[PokemonGen2.MAGNETON].types.append(Types.STEEL)
NAME_TO_POKEMON[PokemonGen2.ONIX].evolves_to = [Evolution(name=PokemonGen2.STEELIX, evolution_type=EvolutionType.TRADE, item=Item.METAL_COAT, should_hold=True)]
NAME_TO_POKEMON[PokemonGen2.CHANSEY].evolves_to = [
    Evolution(name=PokemonGen2.BLISSEY, evolution_type=EvolutionType.FRIENDSHIP, level=47)
]
NAME_TO_POKEMON[PokemonGen2.SEADRA].evolves_to = [
            Evolution(name=PokemonGen2.KINGDRA, evolution_type=EvolutionType.TRADE, item=Item.DRAGON_SCALE, should_hold=True)
        ]
NAME_TO_POKEMON[PokemonGen2.STARYU].evolves_to = [
    Evolution(name=PokemonGen2.STARMIE, level=31, item=Item.WATER_STONE, evolution_type=EvolutionType.STONE)
]
NAME_TO_POKEMON[PokemonGen2.SCYTHER].evolves_to = [
    Evolution(name=PokemonGen2.SCIZOR, evolution_type=EvolutionType.TRADE, item=Item.MOON_STONE, should_hold=True)
]
NAME_TO_POKEMON[PokemonGen2.EEVEE].evolves_to.extend([
    Evolution(name=PokemonGen2.UMBREON, evolution_type=EvolutionType.FRIENDSHIP, special_information="Nighttime"),
    Evolution(name=PokemonGen2.ESPEON, evolution_type=EvolutionType.FRIENDSHIP, special_information="Daytime"),
])
NAME_TO_POKEMON[PokemonGen2.PORYGON].evolves_to = [
    Evolution(name=PokemonGen2.PORYGON2, evolution_type=EvolutionType.TRADE, item=Item.UPGRADE, should_hold=True)
]
NAME_TO_POKEMON[PokemonGen2.SLOWPOKE].evolves_to = [
    Evolution(name=PokemonGen2.SLOWBRO),
    Evolution(name=PokemonGen2.SLOWKING, evolution_type=EvolutionType.TRADE, item=Item.KINGS_ROCK, should_hold=True)
]


_GEN2_POKEMONS = {
    PokemonGen2.CHIKORITA: Pokemon(
        name=PokemonGen2.CHIKORITA,
        gen=2,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen2.BAYLEEF)
        ],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=49,
            defence=65,
            special_attack=49,
            special_defence=65,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.PLANT,
        ],
        num_legs=4,
    ),
    PokemonGen2.BAYLEEF: Pokemon(
        name=PokemonGen2.BAYLEEF,
        gen=2,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen2.MEGANIUM)
        ],
        colors=[Colors.GREEN, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=62,
            defence=80,
            special_attack=63,
            special_defence=80,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.PLANT,
        ],
        num_legs=4,
    ),
    PokemonGen2.MEGANIUM: Pokemon(
        name=PokemonGen2.MEGANIUM,
        gen=2,
        types=[Types.GRASS],
        colors=[Colors.GREEN, Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=82,
            defence=100,
            special_attack=83,
            special_defence=100,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.PLANT,
        ],
        num_legs=4,
    ),
    PokemonGen2.CYNDAQUIL: Pokemon(
        name=PokemonGen2.CYNDAQUIL,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name="Quilava")
        ],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=52,
            defence=43,
            special_attack=60,
            special_defence=50,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen2.QUILAVA: Pokemon(
        name=PokemonGen2.QUILAVA,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name="Typhlosion")
        ],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=64,
            defence=58,
            special_attack=80,
            special_defence=65,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen2.TYPHLOSION: Pokemon(
        name=PokemonGen2.TYPHLOSION,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=84,
            defence=78,
            special_attack=109,
            special_defence=85,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen2.TOTODILE: Pokemon(
        name=PokemonGen2.TOTODILE,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name="Croconaw")
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=64,
            special_attack=44,
            special_defence=48,
        ),
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
        ],
        num_legs=2,
    ),
    PokemonGen2.CROCONAW: Pokemon(
        name=PokemonGen2.CROCONAW,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name="Feraligatr")
        ],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=80,
            special_attack=59,
            special_defence=63,
        ),
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
        ],
        num_legs=2,
    ),
    PokemonGen2.FERALIGATR: Pokemon(
        name=PokemonGen2.FERALIGATR,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=105,
            defence=100,
            special_attack=79,
            special_defence=83,
        ),
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
        ],
        num_legs=2,
    ),
    PokemonGen2.SENTRET: Pokemon(
        name=PokemonGen2.SENTRET,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.FURRET)
        ],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=49,
            defence=34,
            special_attack=35,
            special_defence=45,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen2.FURRET: Pokemon(
        name=PokemonGen2.FURRET,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.BROWN, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=76,
            defence=64,
            special_attack=45,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen2.HOOTHOOT: Pokemon(
        name=PokemonGen2.HOOTHOOT,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.NOCTOWL)
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=30,
            special_attack=36,
            special_defence=56,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen2.NOCTOWL: Pokemon(
        name=PokemonGen2.NOCTOWL,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=50,
            special_attack=86,
            special_defence=96,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen2.LEDYBA: Pokemon(
        name=PokemonGen2.LEDYBA,
        gen=2,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.LEDIAN)
        ],
        colors=[Colors.WHITE, Colors.RED, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=20,
            defence=30,
            special_attack=40,
            special_defence=80,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
        ],
        num_legs=6,
    ),
    PokemonGen2.LEDIAN: Pokemon(
        name=PokemonGen2.LEDIAN,
        gen=2,
        types=[Types.BUG, Types.FLYING],
        colors=[Colors.WHITE, Colors.RED, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=35,
            defence=50,
            special_attack=55,
            special_defence=110,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
        ],
        num_legs=2,
    ),
    PokemonGen2.SPINARAK: Pokemon(
        name=PokemonGen2.SPINARAK,
        gen=2,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.ARIADOS)
        ],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=40,
            special_attack=40,
            special_defence=40,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=6,
    ),
    PokemonGen2.ARIADOS: Pokemon(
        name=PokemonGen2.ARIADOS,
        gen=2,
        types=[Types.BUG, Types.POISON],
        colors=[Colors.RED, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=70,
            special_attack=60,
            special_defence=70,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=4,
    ),
    PokemonGen2.CROBAT: Pokemon(
        name=PokemonGen2.CROBAT,
        gen=2,
        types=[Types.POISON, Types.FLYING],
        colors=[Colors.PURPLE, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=80,
            special_attack=70,
            special_defence=80,
        ),
        categories=[
            Categories.WING,
            Categories.MAMMAL,
        ],
        num_legs=2,
    ),
    PokemonGen2.CHINCHOU: Pokemon(
        name=PokemonGen2.CHINCHOU,
        gen=2,
        types=[Types.WATER, Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen2.LANTURN)
        ],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=38,
            defence=38,
            special_attack=56,
            special_defence=56,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
    ),
    PokemonGen2.LANTURN: Pokemon(
        name=PokemonGen2.LANTURN,
        gen=2,
        types=[Types.WATER, Types.ELECTRIC],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=58,
            defence=58,
            special_attack=76,
            special_defence=76,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
    ),
    PokemonGen2.PICHU: Pokemon(
        name=PokemonGen2.PICHU,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[Evolution(name='Pikachu', evolution_type=EvolutionType.FRIENDSHIP, level=11)],
        colors=[Colors.YELLOW, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=15,
            special_attack=35,
            special_defence=35,
        ),
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
    ),
    PokemonGen2.CLEFFA: Pokemon(
        name=PokemonGen2.CLEFFA,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name='Clefairy', evolution_type=EvolutionType.FRIENDSHIP, level=13)
        ],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=25,
            defence=28,
            special_attack=45,
            special_defence=55,
        ),
        categories=[
            Categories.FANTASY,
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        ),
    PokemonGen2.IGGLYBUFF: Pokemon(
        name=PokemonGen2.IGGLYBUFF,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name='Jigglypuff', evolution_type=EvolutionType.FRIENDSHIP, level=14)
        ],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=15,
            special_attack=40,
            special_defence=20,
        ),
        categories=[
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=2,
    ),
    PokemonGen2.TOGEPI: Pokemon(
        name=PokemonGen2.TOGEPI,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name='Togetic', evolution_type=EvolutionType.FRIENDSHIP)
        ],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=20,
            defence=65,
            special_attack=40,
            special_defence=65,
        ),
        categories=[
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=2,
    ),
    PokemonGen2.TOGETIC: Pokemon(
        name=PokemonGen2.TOGETIC,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=85,
            special_attack=80,
            special_defence=105,
        ),
        categories=[
            Categories.ITEM,
            Categories.FOOD,
            Categories.WING,
        ],
        num_legs=2,
    ),
    PokemonGen2.NATU: Pokemon(
        name=PokemonGen2.NATU,
        gen=2,
        types=[Types.PSYCHIC, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.XATU)
        ],
        colors=[Colors.GREEN, Colors.YELLOW, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=45,
            special_attack=70,
            special_defence=45,
        ),
        categories=[
            Categories.BIRD,
            Categories.WING,
        ],
        num_legs=2,
    ),
    PokemonGen2.XATU: Pokemon(
        name=PokemonGen2.XATU,
        gen=2,
        types=[Types.PSYCHIC, Types.FLYING],
        colors=[Colors.GREEN, Colors.WHITE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],stats=Stats(
            attack=75,
            defence=70,
            special_attack=95,
            special_defence=70,
        ),
        categories=[
            Categories.BIRD,
            Categories.WING,
        ],
        num_legs=2,
    ),
    PokemonGen2.MAREEP: Pokemon(
        name=PokemonGen2.MAREEP,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen2.FLAAFFY)
        ],
        colors=[Colors.WHITE, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=40,
            special_attack=65,
            special_defence=45,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.CATTLE,
        ],
        num_legs=4,
    ),
    PokemonGen2.FLAAFFY: Pokemon(
        name=PokemonGen2.FLAAFFY,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen2.AMPHAROS)
        ],
        colors=[Colors.WHITE, Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=55,
            special_attack=80,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.CATTLE,
        ],
        num_legs=2,
    ),
    PokemonGen2.AMPHAROS: Pokemon(
        name=PokemonGen2.AMPHAROS,
        gen=2,
        types=[Types.ELECTRIC],
        colors=[Colors.WHITE, Colors.BLACK, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=85,
            special_attack=115,
            special_defence=90,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.CATTLE,
        ],
        num_legs=2,
    ),
    PokemonGen2.BELLOSSOM: Pokemon(
        name=PokemonGen2.BELLOSSOM,
        gen=2,
        types=[Types.GRASS],
        colors=[Colors.YELLOW, Colors.GREEN, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=95,
            special_attack=90,
            special_defence=100,
        ),
        categories=[
            Categories.PLANT,
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen2.MARILL: Pokemon(
        name=PokemonGen2.MARILL,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.AZUMARILL)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=20,
            defence=50,
            special_attack=20,
            special_defence=50,
        ),
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
    ),
    PokemonGen2.AZUMARILL: Pokemon(
        name=PokemonGen2.AZUMARILL,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=80,
            special_attack=60,
            special_defence=80,
        ),
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
    ),
    PokemonGen2.SUDOWOODO: Pokemon(
        name=PokemonGen2.SUDOWOODO,
        gen=2,
        types=[Types.ROCK],
        colors=[Colors.BROWN, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=115,
            special_attack=30,
            special_defence=65,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen2.POLITOED: Pokemon(
        name=PokemonGen2.POLITOED,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.GREEN, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=75,
            special_attack=90,
            special_defence=100,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
            Categories.FROG,
            Categories.REPTILE,
        ],
        num_legs=2,
    ),
    PokemonGen2.HOPPIP: Pokemon(
        name=PokemonGen2.HOPPIP,
        gen=2,
        types=[Types.GRASS, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.SKIPLOOM)
        ],
        colors=[Colors.PINK, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=35,
            defence=40,
            special_attack=35,
            special_defence=55,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen2.SKIPLOOM: Pokemon(
        name=PokemonGen2.SKIPLOOM,
        gen=2,
        types=[Types.GRASS, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.JUMPLUFF)
        ],
        colors=[Colors.GREEN, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=50,
            special_attack=45,
            special_defence=65,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen2.JUMPLUFF: Pokemon(
        name=PokemonGen2.JUMPLUFF,
        gen=2,
        types=[Types.GRASS, Types.FLYING],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=75,
            special_attack=55,
            special_defence=95,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen2.AIPOM: Pokemon(
        name=PokemonGen2.AIPOM,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PURPLE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=55,
            special_attack=40,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
    ),
    PokemonGen2.SUNKERN: Pokemon(
        name=PokemonGen2.SUNKERN,
        gen=2,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen2.SUNFLORA, evolution_type=EvolutionType.STONE, item=Item.SUN_STONE, level=13)
        ],
        colors=[Colors.YELLOW, Colors.BROWN, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=30,
            special_attack=30,
            special_defence=30,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=0,
    ),
    PokemonGen2.SUNFLORA: Pokemon(
        name=PokemonGen2.SUNFLORA,
        gen=2,
        types=[Types.GRASS],
        colors=[Colors.GREEN, Colors.YELLOW, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=55,
            special_attack=105,
            special_defence=85,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen2.YANMA: Pokemon(
        name=PokemonGen2.YANMA,
        gen=2,
        types=[Types.BUG, Types.FLYING],
        colors=[Colors.RED, Colors.WHITE, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=45,
            special_attack=75,
            special_defence=45,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
            Categories.WATERMON,
            Categories.DRAGON,
        ],
        num_legs=6,
    ),
    PokemonGen2.WOOPER: Pokemon(
        name=PokemonGen2.WOOPER,
        gen=2,
        types=[Types.WATER, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.QUAGSIRE)
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=45,
            special_attack=25,
            special_defence=25,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FROG,
        ],
        num_legs=2,
    ),
    PokemonGen2.QUAGSIRE: Pokemon(
        name=PokemonGen2.QUAGSIRE,
        gen=2,
        types=[Types.WATER, Types.GROUND],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=85,
            special_attack=65,
            special_defence=65,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FROG,
        ],
        num_legs=2,
    ),
    PokemonGen2.ESPEON: Pokemon(
        name=PokemonGen2.ESPEON,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=60,
            special_attack=130,
            special_defence=95,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen2.UMBREON: Pokemon(
        name=PokemonGen2.UMBREON,
        gen=2,
        types=[Types.DARK],
        colors=[Colors.BLACK, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=110,
            special_attack=60,
            special_defence=130,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen2.MURKROW: Pokemon(
        name=PokemonGen2.MURKROW,
        gen=2,
        types=[Types.DARK, Types.FLYING],
        colors=[Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=42,
            special_attack=85,
            special_defence=42,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.FANTASY,
        ],
        num_legs=2,
    ),
    PokemonGen2.SLOWKING: Pokemon(
        name=PokemonGen2.SLOWKING,
        gen=2,
        types=[Types.WATER, Types.PSYCHIC],
        colors=[Colors.PINK, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=80,
            special_attack=100,
            special_defence=110,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.SLOTH,
        ],
        num_legs=2,
    ),
    PokemonGen2.MISDREAVUS: Pokemon(
        name=PokemonGen2.MISDREAVUS,
        gen=2,
        types=[Types.GHOST],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=60,
            special_attack=85,
            special_defence=85,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=0,
    ),
    PokemonGen2.UNOWN: Pokemon(
        name=PokemonGen2.UNOWN,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.BLACK, Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=72,
            defence=48,
            special_attack=72,
            special_defence=48,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen2.WOBBUFFET: Pokemon(
        name=PokemonGen2.WOBBUFFET,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=33,
            defence=58,
            special_attack=33,
            special_defence=58,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
    ),
    PokemonGen2.GIRAFARIG: Pokemon(
        name=PokemonGen2.GIRAFARIG,
        gen=2,
        types=[Types.NORMAL, Types.PSYCHIC],
        colors=[Colors.YELLOW, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=65,
            special_attack=90,
            special_defence=65,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen2.PINECO: Pokemon(
        name=PokemonGen2.PINECO,
        gen=2,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen2.FORRETRESS)
        ],
        colors=[Colors.BLUE, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=90,
            special_attack=35,
            special_defence=35,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=0,
    ),
    PokemonGen2.FORRETRESS: Pokemon(
        name=PokemonGen2.FORRETRESS,
        gen=2,
        types=[Types.BUG, Types.STEEL],
        colors=[Colors.GRAY, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=140,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=0,
    ),
    PokemonGen2.DUNSPARCE: Pokemon(
        name=PokemonGen2.DUNSPARCE,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.YELLOW, Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=70,
            special_attack=65,
            special_defence=65,
        ),
        categories=[
            Categories.REPTILE,
            Categories.SNAKE,
        ],
        num_legs=0,
    ),
    PokemonGen2.GLIGAR: Pokemon(
        name=PokemonGen2.GLIGAR,
        gen=2,
        types=[Types.GROUND, Types.FLYING],
        colors=[Colors.PINK, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=105,
            special_attack=35,
            special_defence=65,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=2,
    ),
    PokemonGen2.STEELIX: Pokemon(
        name=PokemonGen2.STEELIX,
        gen=2,
        types=[Types.STEEL, Types.GROUND],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=200,
            special_attack=55,
            special_defence=65,
        ),
        categories=[
            Categories.REPTILE,
            Categories.SNAKE,
        ],
        num_legs=0,
    ),
    PokemonGen2.SNUBBULL: Pokemon(
        name=PokemonGen2.SNUBBULL,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.GRANBULL)
        ],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=50,
            special_attack=40,
            special_defence=40,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=2,
    ),
    PokemonGen2.GRANBULL: Pokemon(
        name=PokemonGen2.GRANBULL,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=120,
            defence=75,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=2,
    ),
    PokemonGen2.QWILFISH: Pokemon(
        name=PokemonGen2.QWILFISH,
        gen=2,
        types=[Types.WATER, Types.POISON],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        colors=[Colors.BLUE, Colors.YELLOW],
        stats=Stats(
            attack=95,
            defence=85,
            special_attack=55,
            special_defence=55,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
    ),
    PokemonGen2.SCIZOR: Pokemon(
        name=PokemonGen2.SCIZOR,
        gen=2,
        types=[Types.BUG, Types.STEEL],
        colors=[Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=130,
            defence=100,
            special_attack=55,
            special_defence=80,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen2.SHUCKLE: Pokemon(
        name=PokemonGen2.SHUCKLE,
        gen=2,
        types=[Types.BUG, Types.ROCK],
        colors=[Colors.RED, Colors.YELLOW, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=10,
            defence=230,
            special_attack=10,
            special_defence=230,
        ),
        categories=[
            Categories.REPTILE,
            Categories.FOOD,
            Categories.TURTLE,
        ],
        num_legs=4,
    ),
    PokemonGen2.HERACROSS: Pokemon(
        name=PokemonGen2.HERACROSS,
        gen=2,
        types=[Types.BUG, Types.FIGHTING],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=125,
            defence=75,
            special_attack=40,
            special_defence=95,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
        ],
        num_legs=2,
    ),
    PokemonGen2.SNEASEL: Pokemon(
        name=PokemonGen2.SNEASEL,
        gen=2,
        types=[Types.DARK, Types.ICE],
        colors=[Colors.PURPLE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=55,
            special_attack=35,
            special_defence=75,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=2,
    ),
    PokemonGen2.TEDDIURSA: Pokemon(
        name=PokemonGen2.TEDDIURSA,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.URSARING)
        ],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=50,
            special_attack=50,
            special_defence=50,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.BEAR,
        ],
        num_legs=2,
    ),
    PokemonGen2.URSARING: Pokemon(
        name=PokemonGen2.URSARING,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=130,
            defence=75,
            special_attack=75,
            special_defence=75,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.BEAR,
        ],
        num_legs=2,
    ),
    PokemonGen2.SLUGMA: Pokemon(
        name=PokemonGen2.SLUGMA,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.RED],
        evolves_to=[
            Evolution(name=PokemonGen2.MAGCARGO)
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=40,
            special_attack=70,
            special_defence=40,
        ),
        categories=[
            Categories.FOOD,
            Categories.BUG,
        ],
        num_legs=0,
    ),
    PokemonGen2.MAGCARGO: Pokemon(
        name=PokemonGen2.MAGCARGO,
        gen=2,
        types=[Types.FIRE, Types.ROCK],
        colors=[Colors.RED, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=120,
            special_attack=90,
            special_defence=80,
        ),
        categories=[
            Categories.FOOD,
            Categories.BUG,
        ],
        num_legs=0,
    ),
    PokemonGen2.SWINUB: Pokemon(
        name=PokemonGen2.SWINUB,
        gen=2,
        types=[Types.ICE, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.PILOSWINE)
        ],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=40,
            special_attack=30,
            special_defence=30,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.PIG,
        ],
        num_legs=4,
    ),
    PokemonGen2.PILOSWINE: Pokemon(
        name=PokemonGen2.PILOSWINE,
        gen=2,
        types=[Types.ICE, Types.GROUND],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=80,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.PIG,
            Categories.PREHISTORIC,
        ],
        num_legs=4,
    ),
    PokemonGen2.CORSOLA: Pokemon(
        name=PokemonGen2.CORSOLA,
        gen=2,
        types=[Types.WATER, Types.ROCK],
        colors=[Colors.PINK, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=95,
            special_attack=65,
            special_defence=95,
        ),
        categories=[
            Categories.ITEM,
            Categories.WATERMON,
        ],
        num_legs=4,
    ),
    PokemonGen2.REMORAID: Pokemon(
        name=PokemonGen2.REMORAID,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.OCTILLERY)
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=35,
            special_attack=65,
            special_defence=35,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
    ),
    PokemonGen2.OCTILLERY: Pokemon(
        name=PokemonGen2.OCTILLERY,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=105,
            defence=75,
            special_attack=105,
            special_defence=75,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen2.DELIBIRD: Pokemon(
        name=PokemonGen2.DELIBIRD,
        gen=2,
        types=[Types.ICE, Types.FLYING],
        colors=[Colors.RED, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=45,
            special_attack=65,
            special_defence=45,
        ),
        categories=[
            Categories.BIRD,
            Categories.FANTASY,
        ],
        num_legs=2,
    ),
    PokemonGen2.MANTINE: Pokemon(
        name=PokemonGen2.MANTINE,
        gen=2,
        types=[Types.WATER, Types.FLYING],
        colors=[Colors.PURPLE, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=70,
            special_attack=80,
            special_defence=140,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.WING,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen2.SKARMORY: Pokemon(
        name=PokemonGen2.SKARMORY,
        gen=2,
        types=[Types.STEEL, Types.FLYING],
        colors=[Colors.GRAY, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=140,
            special_attack=40,
            special_defence=70,
        ),
        categories=[
            Categories.WING,
            Categories.ITEM,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen2.HOUNDOUR: Pokemon(
        name=PokemonGen2.HOUNDOUR,
        gen=2,
        types=[Types.DARK, Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen2.HOUNDOOM)
        ],
        colors=[Colors.BLACK, Colors.RED, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=30,
            special_attack=80,
            special_defence=50,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen2.HOUNDOOM: Pokemon(
        name=PokemonGen2.HOUNDOOM,
        gen=2,
        types=[Types.DARK, Types.FIRE],
        colors=[Colors.BLACK, Colors.RED, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=50,
            special_attack=110,
            special_defence=80,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen2.KINGDRA: Pokemon(
        name=PokemonGen2.KINGDRA,
        gen=2,
        types=[Types.WATER, Types.DRAGON],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=95,
            special_attack=95,
            special_defence=95,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.DRAGON,
        ],
        num_legs=0,
    ),
    PokemonGen2.PHANPY: Pokemon(
        name=PokemonGen2.PHANPY,
        gen=2,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.DONPHAN)
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=60,
            special_attack=40,
            special_defence=40,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen2.DONPHAN: Pokemon(
        name=PokemonGen2.DONPHAN,
        gen=2,
        types=[Types.GROUND],
        colors=[Colors.GRAY, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=120,
            defence=120,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen2.PORYGON2: Pokemon(
        name=PokemonGen2.PORYGON2,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK, Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=80,
            defence=90,
            special_attack=105,
            special_defence=95,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen2.STANTLER: Pokemon(
        name=PokemonGen2.STANTLER,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=62,
            special_attack=85,
            special_defence=65,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
        ],
        num_legs=4,
    ),
    PokemonGen2.SMEARGLE: Pokemon(
        name=PokemonGen2.SMEARGLE,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.WHITE, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=20,
            defence=35,
            special_attack=20,
            special_defence=45,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=2,
    ),
    PokemonGen2.TYROGUE: Pokemon(
        name=PokemonGen2.TYROGUE,
        gen=2,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name='Hitmontop', evolution_type=EvolutionType.RANDOM, special_information="Attack = Defense", level=20),
            Evolution(name='Hitmonchan', evolution_type=EvolutionType.RANDOM, special_information="Attack < Defense", level=20),
            Evolution(name='Hitmonlee', evolution_type=EvolutionType.RANDOM, special_information="Attack > Defense", level=20),
        ],
        colors=[Colors.PURPLE, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=35,
            defence=35,
            special_attack=35,
            special_defence=35,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen2.HITMONTOP: Pokemon(
        name=PokemonGen2.HITMONTOP,
        gen=2,
        types=[Types.FIGHTING],
        colors=[Colors.BROWN, Colors.BLUE],
        supported_genders=[Genders.MALE],
        stats=Stats(
            attack=95,
            defence=95,
            special_attack=35,
            special_defence=110,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen2.SMOOCHUM: Pokemon(
        name=PokemonGen2.SMOOCHUM,
        gen=2,
        types=[Types.ICE, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen2.JYNX)
        ],
        colors=[Colors.PURPLE, Colors.YELLOW],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=15,
            special_attack=85,
            special_defence=65,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FANTASY,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen2.ELEKID: Pokemon(
        name=PokemonGen2.ELEKID,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen2.ELECTABUZZ)
        ],
        colors=[Colors.YELLOW, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=63,
            defence=37,
            special_attack=65,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
            Categories.ITEM,
        ],
        num_legs=2,
    ),
    PokemonGen2.MAGBY: Pokemon(
        name=PokemonGen2.MAGBY,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen2.MAGMAR)
        ],
        colors=[Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=37,
            special_attack=70,
            special_defence=55,
        ),
        categories=[
            Categories.BIRD,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.DUCK,
        ],
        num_legs=2,
    ),
    PokemonGen2.MILTANK: Pokemon(
        name=PokemonGen2.MILTANK,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK, Colors.WHITE],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=105,
            special_attack=40,
            special_defence=70,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.CATTLE,
            Categories.COW,
        ],
        num_legs=4,
    ),
    PokemonGen2.BLISSEY: Pokemon(
        name=PokemonGen2.BLISSEY,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK, Colors.WHITE],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=10,
            defence=10,
            special_attack=75,
            special_defence=135,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen2.RAIKOU: Pokemon(
        name=PokemonGen2.RAIKOU,
        gen=2,
        types=[Types.ELECTRIC],
        colors=[Colors.YELLOW, Colors.BLACK,Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=85,
            defence=75,
            special_attack=115,
            special_defence=100,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
    ),
    PokemonGen2.ENTEI: Pokemon(
        name=PokemonGen2.ENTEI,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.BROWN, Colors.GRAY, Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=115,
            defence=85,
            special_attack=90,
            special_defence=75,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
    ),
    PokemonGen2.SUICUNE: Pokemon(
        name=PokemonGen2.SUICUNE,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.WHITE, Colors.PURPLE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=75,
            defence=115,
            special_attack=90,
            special_defence=115,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
    ),
    PokemonGen2.LARVITAR: Pokemon(
        name=PokemonGen2.LARVITAR,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.PUPITAR)
        ],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=64,
            defence=50,
            special_attack=45,
            special_defence=50,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.FANTASY,
        ],
        num_legs=2,
    ),
    PokemonGen2.PUPITAR: Pokemon(
        name=PokemonGen2.PUPITAR,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.TYRANITAR)
        ],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=84,
            defence=70,
            special_attack=65,
            special_defence=70,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.FANTASY,
        ],
        num_legs=0,
    ),
    PokemonGen2.TYRANITAR: Pokemon(
        name=PokemonGen2.TYRANITAR,
        gen=2,
        types=[Types.ROCK, Types.DARK],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=134,
            defence=110,
            special_attack=95,
            special_defence=100,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.FANTASY,
        ],
        num_legs=2,
    ),
    PokemonGen2.LUGIA: Pokemon(
        name=PokemonGen2.LUGIA,
        gen=2,
        types=[Types.PSYCHIC, Types.FLYING],
        colors=[Colors.WHITE, Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=90,
            defence=130,
            special_attack=90,
            special_defence=154,
        ),
        categories=[
            Categories.WING,
            Categories.DRAGON,
        ],
        num_legs=2,
    ),
    PokemonGen2.HO_OH: Pokemon(
        name=PokemonGen2.HO_OH,
        gen=2,
        types=[Types.FIRE, Types.FLYING],
        colors=[Colors.RED, Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=130,
            defence=90,
            special_attack=110,
            special_defence=154,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen2.CELEBI: Pokemon(
        name=PokemonGen2.CELEBI,
        gen=2,
        types=[Types.PSYCHIC, Types.GRASS],
        colors=[Colors.GREEN],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=100,
            defence=100,
            special_attack=100,
            special_defence=100,
        ),
        categories=[
            Categories.WING,
            Categories.FANTASY,
        ],
        num_legs=2,
    ),
}


NAME_TO_POKEMON.update(_GEN2_POKEMONS)
