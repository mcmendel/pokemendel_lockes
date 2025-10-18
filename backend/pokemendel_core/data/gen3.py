"""Generation 3 Pokemon data module."""

from ..models.pokemon import Pokemon
from ..models.evolution.evolution import Evolution
from ..models.evolution.evolution_type import EvolutionType
from ..models.evolution.items import Item
from ..utils.definitions.types import Types
from ..utils.definitions.colors import Colors
from ..utils.definitions.categories import Categories
from ..utils.definitions.stats import Stats
from ..utils.definitions.genders import Genders
from ..utils.definitions.abilities import Abilities
from .utils.names import PokemonNames as PokemonGen3
from .utils.evolutions import update_evolution
from .gen2 import NAME_TO_POKEMON as NAME_TO_POKEMON_GEN2
from dataclasses import replace
from copy import deepcopy

_GEN2_ABILITIES = {
    PokemonGen3.BULBASAUR: [Abilities.OVERGROW],
    PokemonGen3.IVYSAUR: [Abilities.OVERGROW],
    PokemonGen3.VENUSAUR: [Abilities.OVERGROW],
    PokemonGen3.CHARMANDER: [Abilities.BLAZE],
    PokemonGen3.CHARMELEON: [Abilities.BLAZE],
    PokemonGen3.CHARIZARD: [Abilities.BLAZE],
    PokemonGen3.SQUIRTLE: [Abilities.TORRENT],
    PokemonGen3.WARTORTLE: [Abilities.TORRENT],
    PokemonGen3.BLASTOISE: [Abilities.TORRENT],
    PokemonGen3.CATERPIE: [Abilities.SHIELD_DUST],
    PokemonGen3.METAPOD: [Abilities.SHED_SKIN],
    PokemonGen3.BUTTERFREE: [Abilities.COMPOUND_EYES],
    PokemonGen3.WEEDLE: [Abilities.SHIELD_DUST],
    PokemonGen3.KAKUNA: [Abilities.SHED_SKIN],
    PokemonGen3.BEEDRILL: [Abilities.SWARM],
    PokemonGen3.PIDGEY: [Abilities.KEEN_EYE, Abilities.TANGLED_FEET],
    PokemonGen3.PIDGEOTTO: [Abilities.KEEN_EYE, Abilities.TANGLED_FEET],
    PokemonGen3.PIDGEOT: [Abilities.KEEN_EYE, Abilities.TANGLED_FEET],
    PokemonGen3.RATTATA: [Abilities.RUN_AWAY, Abilities.GUTS],
    PokemonGen3.RATICATE: [Abilities.RUN_AWAY, Abilities.GUTS],
    PokemonGen3.SPEAROW: [Abilities.KEEN_EYE],
    PokemonGen3.FEAROW: [Abilities.KEEN_EYE],
    PokemonGen3.EKANS: [Abilities.INTIMIDATE, Abilities.SHED_SKIN],
    PokemonGen3.ARBOK: [Abilities.INTIMIDATE, Abilities.SHED_SKIN],
    PokemonGen3.PIKACHU: [Abilities.STATIC],
    PokemonGen3.RAICHU: [Abilities.STATIC],
    PokemonGen3.SANDSHREW: [Abilities.SAND_VEIL],
    PokemonGen3.SANDSLASH: [Abilities.SAND_VEIL],
    PokemonGen3.NIDORAN_F: [Abilities.POISON_POINT, Abilities.RIVALRY],
    PokemonGen3.NIDORINA: [Abilities.POISON_POINT, Abilities.RIVALRY],
    PokemonGen3.NIDOQUEEN: [Abilities.POISON_POINT, Abilities.RIVALRY],
    PokemonGen3.NIDORAN_M: [Abilities.POISON_POINT, Abilities.RIVALRY],
    PokemonGen3.NIDORINO: [Abilities.POISON_POINT, Abilities.RIVALRY],
    PokemonGen3.NIDOKING: [Abilities.POISON_POINT, Abilities.RIVALRY],
    PokemonGen3.CLEFAIRY: [Abilities.CUTE_CHARM, Abilities.MAGIC_GUARD],
    PokemonGen3.CLEFABLE: [Abilities.CUTE_CHARM, Abilities.MAGIC_GUARD],
    PokemonGen3.VULPIX: [Abilities.FLASH_FIRE],
    PokemonGen3.NINETALES: [Abilities.FLASH_FIRE],
    PokemonGen3.JIGGLYPUFF: [Abilities.CUTE_CHARM],
    PokemonGen3.WIGGLYTUFF: [Abilities.CUTE_CHARM],
    PokemonGen3.ZUBAT: [Abilities.INNER_FOCUS],
    PokemonGen3.GOLBAT: [Abilities.INNER_FOCUS],
    PokemonGen3.ODDISH: [Abilities.CHLOROPHYLL],
    PokemonGen3.GLOOM: [Abilities.CHLOROPHYLL],
    PokemonGen3.VILEPLUME: [Abilities.CHLOROPHYLL],
    PokemonGen3.PARAS: [Abilities.EFFECT_SPORE, Abilities.DRY_SKIN],
    PokemonGen3.PARASECT: [Abilities.EFFECT_SPORE, Abilities.DRY_SKIN],
    PokemonGen3.VENONAT: [Abilities.COMPOUND_EYES, Abilities.TINTED_LENS],
    PokemonGen3.VENOMOTH: [Abilities.SHIELD_DUST, Abilities.TINTED_LENS],
    PokemonGen3.DIGLETT: [Abilities.SAND_VEIL, Abilities.ARENA_TRAP],
    PokemonGen3.DUGTRIO: [Abilities.SAND_VEIL, Abilities.ARENA_TRAP],
    PokemonGen3.MEOWTH: [Abilities.PICKUP, Abilities.TECHNICIAN],
    PokemonGen3.PERSIAN: [Abilities.LIMBER, Abilities.TECHNICIAN],
    PokemonGen3.PSYDUCK: [Abilities.DAMP, Abilities.CLOUD_NINE],
    PokemonGen3.GOLDUCK: [Abilities.DAMP, Abilities.CLOUD_NINE],
    PokemonGen3.MANKEY: [Abilities.VITAL_SPIRIT, Abilities.ANGER_POINT],
    PokemonGen3.PRIMEAPE: [Abilities.VITAL_SPIRIT, Abilities.ANGER_POINT],
    PokemonGen3.GROWLITHE: [Abilities.INTIMIDATE, Abilities.FLASH_FIRE],
    PokemonGen3.ARCANINE: [Abilities.INTIMIDATE, Abilities.FLASH_FIRE],
    PokemonGen3.POLIWAG: [Abilities.WATER_ABSORB, Abilities.DAMP],
    PokemonGen3.POLIWHIRL: [Abilities.WATER_ABSORB, Abilities.DAMP],
    PokemonGen3.POLIWRATH: [Abilities.WATER_ABSORB, Abilities.DAMP],
    PokemonGen3.ABRA: [Abilities.SYNCHRONIZE, Abilities.INNER_FOCUS],
    PokemonGen3.KADABRA: [Abilities.SYNCHRONIZE, Abilities.INNER_FOCUS],
    PokemonGen3.ALAKAZAM: [Abilities.SYNCHRONIZE, Abilities.INNER_FOCUS],
    PokemonGen3.MACHOP: [Abilities.GUTS, Abilities.NO_GUARD],
    PokemonGen3.MACHOKE: [Abilities.GUTS, Abilities.NO_GUARD],
    PokemonGen3.MACHAMP: [Abilities.GUTS, Abilities.NO_GUARD],
    PokemonGen3.BELLSPROUT: [Abilities.CHLOROPHYLL],
    PokemonGen3.WEEPINBELL: [Abilities.CHLOROPHYLL],
    PokemonGen3.VICTREEBEL: [Abilities.CHLOROPHYLL],
    PokemonGen3.TENTACOOL: [Abilities.CLEAR_BODY, Abilities.LIQUID_OOZE],
    PokemonGen3.TENTACRUEL: [Abilities.CLEAR_BODY, Abilities.LIQUID_OOZE],
    PokemonGen3.GEODUDE: [Abilities.ROCK_HEAD, Abilities.STURDY],
    PokemonGen3.GRAVELER: [Abilities.ROCK_HEAD, Abilities.STURDY],
    PokemonGen3.GOLEM: [Abilities.ROCK_HEAD, Abilities.STURDY],
    PokemonGen3.PONYTA: [Abilities.RUN_AWAY, Abilities.FLASH_FIRE],
    PokemonGen3.RAPIDASH: [Abilities.RUN_AWAY, Abilities.FLASH_FIRE],
    PokemonGen3.SLOWPOKE: [Abilities.OBLIVIOUS, Abilities.OWN_TEMPO],
    PokemonGen3.SLOWBRO: [Abilities.OBLIVIOUS, Abilities.OWN_TEMPO],
    PokemonGen3.MAGNEMITE: [Abilities.MAGNET_PULL, Abilities.STURDY],
    PokemonGen3.MAGNETON: [Abilities.MAGNET_PULL, Abilities.STURDY],
    PokemonGen3.FARFETCHD: [Abilities.KEEN_EYE, Abilities.INNER_FOCUS],
    PokemonGen3.DODUO: [Abilities.RUN_AWAY, Abilities.EARLY_BIRD],
    PokemonGen3.DODRIO: [Abilities.RUN_AWAY, Abilities.EARLY_BIRD],
    PokemonGen3.SEEL: [Abilities.THICK_FAT, Abilities.HYDRATION],
    PokemonGen3.DEWGONG: [Abilities.THICK_FAT, Abilities.HYDRATION],
    PokemonGen3.GRIMER: [Abilities.STENCH, Abilities.STICKY_HOLD],
    PokemonGen3.MUK: [Abilities.STENCH, Abilities.STICKY_HOLD],
    PokemonGen3.SHELLDER: [Abilities.SHELL_ARMOR, Abilities.SKILL_LINK],
    PokemonGen3.CLOYSTER: [Abilities.SHELL_ARMOR, Abilities.SKILL_LINK],
    PokemonGen3.GASTLY: [Abilities.LEVITATE],
    PokemonGen3.HAUNTER: [Abilities.LEVITATE],
    PokemonGen3.GENGAR: [Abilities.LEVITATE],
    PokemonGen3.ONIX: [Abilities.ROCK_HEAD, Abilities.STURDY],
    PokemonGen3.DROWZEE: [Abilities.INSOMNIA, Abilities.FOREWARN],
    PokemonGen3.HYPNO: [Abilities.INSOMNIA, Abilities.FOREWARN],
    PokemonGen3.KRABBY: [Abilities.HYPER_CUTTER, Abilities.SHELL_ARMOR],
    PokemonGen3.KINGLER: [Abilities.HYPER_CUTTER, Abilities.SHELL_ARMOR],
    PokemonGen3.VOLTORB: [Abilities.SOUNDPROOF, Abilities.STATIC],
    PokemonGen3.ELECTRODE: [Abilities.SOUNDPROOF, Abilities.STATIC],
    PokemonGen3.EXEGGCUTE: [Abilities.CHLOROPHYLL],
    PokemonGen3.EXEGGUTOR: [Abilities.CHLOROPHYLL],
    PokemonGen3.CUBONE: [Abilities.ROCK_HEAD, Abilities.LIGHTNING_ROD],
    PokemonGen3.MAROWAK: [Abilities.ROCK_HEAD, Abilities.LIGHTNING_ROD],
    PokemonGen3.HITMONLEE: [Abilities.LIMBER, Abilities.RECKLESS],
    PokemonGen3.HITMONCHAN: [Abilities.KEEN_EYE, Abilities.IRON_FIST],
    PokemonGen3.LICKITUNG: [Abilities.OWN_TEMPO, Abilities.OBLIVIOUS],
    PokemonGen3.KOFFING: [Abilities.LEVITATE],
    PokemonGen3.WEEZING: [Abilities.LEVITATE],
    PokemonGen3.RHYHORN: [Abilities.LIGHTNING_ROD, Abilities.ROCK_HEAD],
    PokemonGen3.RHYDON: [Abilities.LIGHTNING_ROD, Abilities.ROCK_HEAD],
    PokemonGen3.CHANSEY: [Abilities.NATURAL_CURE, Abilities.SERENE_GRACE],
    PokemonGen3.TANGELA: [Abilities.CHLOROPHYLL, Abilities.LEAF_GUARD],
    PokemonGen3.KANGASKHAN: [Abilities.EARLY_BIRD, Abilities.SCRAPPY],
    PokemonGen3.HORSEA: [Abilities.SWIFT_SWIM, Abilities.SNIPER],
    PokemonGen3.SEADRA: [Abilities.POISON_POINT, Abilities.SNIPER],
    PokemonGen3.GOLDEEN: [Abilities.SWIFT_SWIM, Abilities.WATER_VEIL],
    PokemonGen3.SEAKING: [Abilities.SWIFT_SWIM, Abilities.WATER_VEIL],
    PokemonGen3.STARYU: [Abilities.ILLUMINATE, Abilities.NATURAL_CURE],
    PokemonGen3.STARMIE: [Abilities.ILLUMINATE, Abilities.NATURAL_CURE],
    PokemonGen3.MR_MIME: [Abilities.SOUNDPROOF, Abilities.FILTER],
    PokemonGen3.SCYTHER: [Abilities.SWARM, Abilities.TECHNICIAN],
    PokemonGen3.JYNX: [Abilities.OBLIVIOUS, Abilities.FOREWARN],
    PokemonGen3.ELECTABUZZ: [Abilities.STATIC],
    PokemonGen3.MAGMAR: [Abilities.FLAME_BODY],
    PokemonGen3.PINSIR: [Abilities.HYPER_CUTTER, Abilities.MOLD_BREAKER],
    PokemonGen3.TAUROS: [Abilities.INTIMIDATE, Abilities.ANGER_POINT],
    PokemonGen3.MAGIKARP: [Abilities.SWIFT_SWIM],
    PokemonGen3.GYARADOS: [Abilities.INTIMIDATE],
    PokemonGen3.LAPRAS: [Abilities.WATER_ABSORB, Abilities.SHELL_ARMOR],
    PokemonGen3.DITTO: [Abilities.LIMBER],
    PokemonGen3.EEVEE: [Abilities.RUN_AWAY, Abilities.ADAPTABILITY],
    PokemonGen3.VAPOREON: [Abilities.WATER_ABSORB],
    PokemonGen3.JOLTEON: [Abilities.VOLT_ABSORB],
    PokemonGen3.FLAREON: [Abilities.FLASH_FIRE],
    PokemonGen3.PORYGON: [Abilities.TRACE, Abilities.DOWNLOAD],
    PokemonGen3.OMANYTE: [Abilities.SWIFT_SWIM, Abilities.SHELL_ARMOR],
    PokemonGen3.OMASTAR: [Abilities.SWIFT_SWIM, Abilities.SHELL_ARMOR],
    PokemonGen3.KABUTO: [Abilities.SWIFT_SWIM, Abilities.BATTLE_ARMOR],
    PokemonGen3.KABUTOPS: [Abilities.SWIFT_SWIM, Abilities.BATTLE_ARMOR],
    PokemonGen3.AERODACTYL: [Abilities.ROCK_HEAD, Abilities.PRESSURE],
    PokemonGen3.SNORLAX: [Abilities.IMMUNITY, Abilities.THICK_FAT],
    PokemonGen3.ARTICUNO: [Abilities.PRESSURE],
    PokemonGen3.ZAPDOS: [Abilities.PRESSURE],
    PokemonGen3.MOLTRES: [Abilities.PRESSURE],
    PokemonGen3.DRATINI: [Abilities.SHED_SKIN],
    PokemonGen3.DRAGONAIR: [Abilities.SHED_SKIN],
    PokemonGen3.DRAGONITE: [Abilities.INNER_FOCUS],
    PokemonGen3.MEWTWO: [Abilities.PRESSURE],
    PokemonGen3.MEW: [Abilities.SYNCHRONIZE],
    PokemonGen3.CHIKORITA: [Abilities.OVERGROW],
    PokemonGen3.BAYLEEF: [Abilities.OVERGROW],
    PokemonGen3.MEGANIUM: [Abilities.OVERGROW],
    PokemonGen3.CYNDAQUIL: [Abilities.BLAZE],
    PokemonGen3.QUILAVA: [Abilities.BLAZE],
    PokemonGen3.TYPHLOSION: [Abilities.BLAZE],
    PokemonGen3.TOTODILE: [Abilities.TORRENT],
    PokemonGen3.CROCONAW: [Abilities.TORRENT],
    PokemonGen3.FERALIGATR: [Abilities.TORRENT],
    PokemonGen3.SENTRET: [Abilities.RUN_AWAY, Abilities.KEEN_EYE],
    PokemonGen3.FURRET: [Abilities.RUN_AWAY, Abilities.KEEN_EYE],
    PokemonGen3.HOOTHOOT: [Abilities.INSOMNIA, Abilities.KEEN_EYE],
    PokemonGen3.NOCTOWL: [Abilities.INSOMNIA, Abilities.KEEN_EYE],
    PokemonGen3.LEDYBA: [Abilities.SWARM, Abilities.EARLY_BIRD],
    PokemonGen3.LEDIAN: [Abilities.SWARM, Abilities.EARLY_BIRD],
    PokemonGen3.SPINARAK: [Abilities.SWARM, Abilities.INSOMNIA],
    PokemonGen3.ARIADOS: [Abilities.SWARM, Abilities.INSOMNIA],
    PokemonGen3.CROBAT: [Abilities.INNER_FOCUS],
    PokemonGen3.CHINCHOU: [Abilities.VOLT_ABSORB, Abilities.ILLUMINATE],
    PokemonGen3.LANTURN: [Abilities.VOLT_ABSORB, Abilities.ILLUMINATE],
    PokemonGen3.PICHU: [Abilities.STATIC],
    PokemonGen3.CLEFFA: [Abilities.CUTE_CHARM, Abilities.MAGIC_GUARD],
    PokemonGen3.IGGLYBUFF: [Abilities.CUTE_CHARM],
    PokemonGen3.TOGEPI: [Abilities.HUSTLE, Abilities.SERENE_GRACE],
    PokemonGen3.TOGETIC: [Abilities.HUSTLE, Abilities.SERENE_GRACE],
    PokemonGen3.NATU: [Abilities.SYNCHRONIZE, Abilities.EARLY_BIRD],
    PokemonGen3.XATU: [Abilities.SYNCHRONIZE, Abilities.EARLY_BIRD],
    PokemonGen3.MAREEP: [Abilities.STATIC],
    PokemonGen3.FLAAFFY: [Abilities.STATIC],
    PokemonGen3.AMPHAROS: [Abilities.STATIC],
    PokemonGen3.BELLOSSOM: [Abilities.CHLOROPHYLL],
    PokemonGen3.MARILL: [Abilities.THICK_FAT, Abilities.HUGE_POWER],
    PokemonGen3.AZUMARILL: [Abilities.THICK_FAT, Abilities.HUGE_POWER],
    PokemonGen3.SUDOWOODO: [Abilities.STURDY, Abilities.ROCK_HEAD],
    PokemonGen3.POLITOED: [Abilities.WATER_ABSORB, Abilities.DAMP],
    PokemonGen3.HOPPIP: [Abilities.CHLOROPHYLL, Abilities.LEAF_GUARD],
    PokemonGen3.SKIPLOOM: [Abilities.CHLOROPHYLL, Abilities.LEAF_GUARD],
    PokemonGen3.JUMPLUFF: [Abilities.CHLOROPHYLL, Abilities.LEAF_GUARD],
    PokemonGen3.AIPOM: [Abilities.RUN_AWAY, Abilities.PICKUP],
    PokemonGen3.SUNKERN: [Abilities.CHLOROPHYLL, Abilities.SOLAR_POWER],
    PokemonGen3.SUNFLORA: [Abilities.CHLOROPHYLL, Abilities.SOLAR_POWER],
    PokemonGen3.YANMA: [Abilities.SPEED_BOOST, Abilities.COMPOUND_EYES],
    PokemonGen3.WOOPER: [Abilities.DAMP, Abilities.WATER_ABSORB],
    PokemonGen3.QUAGSIRE: [Abilities.DAMP, Abilities.WATER_ABSORB],
    PokemonGen3.ESPEON: [Abilities.SYNCHRONIZE],
    PokemonGen3.UMBREON: [Abilities.SYNCHRONIZE],
    PokemonGen3.MURKROW: [Abilities.INSOMNIA, Abilities.SUPER_LUCK],
    PokemonGen3.SLOWKING: [Abilities.OBLIVIOUS, Abilities.OWN_TEMPO],
    PokemonGen3.MISDREAVUS: [Abilities.LEVITATE],
    PokemonGen3.UNOWN: [Abilities.LEVITATE],
    PokemonGen3.WOBBUFFET: [Abilities.SHADOW_TAG],
    PokemonGen3.GIRAFARIG: [Abilities.INNER_FOCUS, Abilities.EARLY_BIRD],
    PokemonGen3.PINECO: [Abilities.STURDY],
    PokemonGen3.FORRETRESS: [Abilities.STURDY],
    PokemonGen3.DUNSPARCE: [Abilities.SERENE_GRACE, Abilities.RUN_AWAY],
    PokemonGen3.GLIGAR: [Abilities.HYPER_CUTTER, Abilities.SAND_VEIL],
    PokemonGen3.STEELIX: [Abilities.ROCK_HEAD, Abilities.STURDY],
    PokemonGen3.SNUBBULL: [Abilities.INTIMIDATE, Abilities.RUN_AWAY],
    PokemonGen3.GRANBULL: [Abilities.INTIMIDATE, Abilities.QUICK_FEET],
    PokemonGen3.QWILFISH: [Abilities.POISON_POINT, Abilities.SWIFT_SWIM],
    PokemonGen3.SCIZOR: [Abilities.SWARM, Abilities.TECHNICIAN],
    PokemonGen3.SHUCKLE: [Abilities.STURDY, Abilities.GLUTTONY],
    PokemonGen3.HERACROSS: [Abilities.SWARM, Abilities.GUTS],
    PokemonGen3.SNEASEL: [Abilities.INNER_FOCUS, Abilities.KEEN_EYE],
    PokemonGen3.TEDDIURSA: [Abilities.PICKUP, Abilities.QUICK_FEET],
    PokemonGen3.URSARING: [Abilities.GUTS, Abilities.QUICK_FEET],
    PokemonGen3.SLUGMA: [Abilities.MAGMA_ARMOR, Abilities.FLAME_BODY],
    PokemonGen3.MAGCARGO: [Abilities.MAGMA_ARMOR, Abilities.FLAME_BODY],
    PokemonGen3.SWINUB: [Abilities.OBLIVIOUS, Abilities.SNOW_CLOAK],
    PokemonGen3.PILOSWINE: [Abilities.OBLIVIOUS, Abilities.SNOW_CLOAK],
    PokemonGen3.CORSOLA: [Abilities.HUSTLE, Abilities.NATURAL_CURE],
    PokemonGen3.REMORAID: [Abilities.HUSTLE, Abilities.SNIPER],
    PokemonGen3.OCTILLERY: [Abilities.SUCTION_CUPS, Abilities.SNIPER],
    PokemonGen3.DELIBIRD: [Abilities.VITAL_SPIRIT, Abilities.HUSTLE],
    PokemonGen3.MANTINE: [Abilities.SWIFT_SWIM, Abilities.WATER_ABSORB],
    PokemonGen3.SKARMORY: [Abilities.KEEN_EYE, Abilities.STURDY],
    PokemonGen3.HOUNDOUR: [Abilities.EARLY_BIRD, Abilities.FLASH_FIRE],
    PokemonGen3.HOUNDOOM: [Abilities.EARLY_BIRD, Abilities.FLASH_FIRE],
    PokemonGen3.KINGDRA: [Abilities.SWIFT_SWIM, Abilities.SNIPER],
    PokemonGen3.PHANPY: [Abilities.PICKUP],
    PokemonGen3.DONPHAN: [Abilities.STURDY],
    PokemonGen3.PORYGON2: [Abilities.TRACE, Abilities.DOWNLOAD],
    PokemonGen3.STANTLER: [Abilities.INTIMIDATE, Abilities.FRISK],
    PokemonGen3.SMEARGLE: [Abilities.OWN_TEMPO, Abilities.TECHNICIAN],
    PokemonGen3.TYROGUE: [Abilities.GUTS, Abilities.STEADFAST],
    PokemonGen3.HITMONTOP: [Abilities.INTIMIDATE, Abilities.TECHNICIAN],
    PokemonGen3.SMOOCHUM: [Abilities.OBLIVIOUS, Abilities.FOREWARN],
    PokemonGen3.ELEKID: [Abilities.STATIC],
    PokemonGen3.MAGBY: [Abilities.FLAME_BODY],
    PokemonGen3.MILTANK: [Abilities.THICK_FAT, Abilities.SCRAPPY],
    PokemonGen3.BLISSEY: [Abilities.NATURAL_CURE, Abilities.SERENE_GRACE],
    PokemonGen3.RAIKOU: [Abilities.PRESSURE],
    PokemonGen3.ENTEI: [Abilities.PRESSURE],
    PokemonGen3.SUICUNE: [Abilities.PRESSURE],
    PokemonGen3.LARVITAR: [Abilities.GUTS],
    PokemonGen3.PUPITAR: [Abilities.SHED_SKIN],
    PokemonGen3.TYRANITAR: [Abilities.SAND_STREAM],
    PokemonGen3.LUGIA: [Abilities.PRESSURE],
    PokemonGen3.HO_OH: [Abilities.PRESSURE],
    PokemonGen3.CELEBI: [Abilities.NATURAL_CURE],
}

NAME_TO_POKEMON = {
    pokemon_name: replace(deepcopy(pokemon), gen=3, supported_abilities=_GEN2_ABILITIES[pokemon_name])
    for pokemon_name, pokemon in NAME_TO_POKEMON_GEN2.items()
}

# update_evolution(NAME_TO_POKEMON, PokemonGen3., PokemonGen3.,)
update_evolution(NAME_TO_POKEMON, PokemonGen3.PIKACHU, PokemonGen3.RAICHU, Evolution(name="", level=26, evolution_type=EvolutionType.STONE, item=Item.THUNDER_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.NIDORINA, PokemonGen3.NIDOQUEEN, Evolution(name="", level=53, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.NIDORINO, PokemonGen3.NIDOKING, Evolution(name=PokemonGen3.NIDOKING, level=19, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.CLEFAIRY, PokemonGen3.CLEFABLE, Evolution(name="", level=45, item=Item.MOON_STONE, evolution_type=EvolutionType.STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.VULPIX, PokemonGen3.NINETALES, Evolution(name="", level=29, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.JIGGLYPUFF, PokemonGen3.WIGGLYTUFF, Evolution(name="", level=44, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.GLOOM, PokemonGen3.VILEPLUME, Evolution(name="", level=24, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.GLOOM, PokemonGen3.BELLOSSOM, Evolution(name="", level=44, evolution_type=EvolutionType.STONE, item=Item.SUN_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.GROWLITHE, PokemonGen3.ARCANINE, Evolution(name="", level=49, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.POLIWHIRL, PokemonGen3.POLIWRATH, Evolution(name="", level=35, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.POLIWHIRL, PokemonGen3.POLITOED, Evolution(name="", evolution_type=EvolutionType.TRADE, should_hold=True, item=Item.KINGS_ROCK),)
update_evolution(NAME_TO_POKEMON, PokemonGen3.WEEPINBELL, PokemonGen3.VICTREEBEL, Evolution(name="", level=42, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.SLOWPOKE, PokemonGen3.SLOWKING, Evolution(name="", evolution_type=EvolutionType.TRADE, item=Item.KINGS_ROCK, level=34, should_hold=True))
update_evolution(NAME_TO_POKEMON, PokemonGen3.SHELLDER, PokemonGen3.CLOYSTER, Evolution(name="", level=49, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.ONIX, PokemonGen3.STEELIX, Evolution(name="", evolution_type=EvolutionType.TRADE, level=49, item=Item.METAL_COAT, should_hold=True))
update_evolution(NAME_TO_POKEMON, PokemonGen3.EXEGGCUTE, PokemonGen3.EXEGGUTOR, Evolution(name="", level=19, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.CHANSEY, PokemonGen3.BLISSEY, Evolution(name="", evolution_type=EvolutionType.FRIENDSHIP, level=28))
update_evolution(NAME_TO_POKEMON, PokemonGen3.STARYU, PokemonGen3.STARMIE, Evolution(name="", level=28, item=Item.WATER_STONE, evolution_type=EvolutionType.STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen3.SCYTHER, PokemonGen3.SCIZOR, Evolution(name="", level=26, evolution_type=EvolutionType.TRADE, item=Item.MOON_STONE, should_hold=True))
update_evolution(NAME_TO_POKEMON, PokemonGen3.PICHU, PokemonGen3.PIKACHU, Evolution(name='', evolution_type=EvolutionType.FRIENDSHIP, level=11))
update_evolution(NAME_TO_POKEMON, PokemonGen3.CLEFFA, PokemonGen3.CLEFAIRY, Evolution(name='', evolution_type=EvolutionType.FRIENDSHIP, level=13))
update_evolution(NAME_TO_POKEMON, PokemonGen3.IGGLYBUFF, PokemonGen3.JIGGLYPUFF, Evolution(name='', evolution_type=EvolutionType.FRIENDSHIP, level=14))
update_evolution(NAME_TO_POKEMON, PokemonGen3.SUNKERN, PokemonGen3.SUNFLORA, Evolution(name='', evolution_type=EvolutionType.STONE, item=Item.SUN_STONE, level=13))


# update_evolution(NAME_TO_POKEMON, PokemonGen3., PokemonGen3.,)
_GEN3_POKEMONS = {
    PokemonGen3.TREECKO: Pokemon(
        name=PokemonGen3.TREECKO,
        gen=3,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.GROVYLE)
        ],
        colors=[Colors.GREEN, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=35,
            special_attack=65,
            special_defence=55,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.DRAGON,
        ],
        num_legs=2,
        supported_abilities=[Abilities.OVERGROW],
    ),
    PokemonGen3.GROVYLE: Pokemon(
        name=PokemonGen3.GROVYLE,
        gen=3,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.SCEPTILE),
        ],
        colors=[Colors.GREEN, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=45,
            special_attack=85,
            special_defence=65,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.DRAGON,
        ],
        num_legs=2,
        supported_abilities=[Abilities.OVERGROW],
    ),
    PokemonGen3.SCEPTILE: Pokemon(
        name=PokemonGen3.SCEPTILE,
        gen=3,
        types=[Types.GRASS],
        evolves_to=[],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=65,
            special_attack=105,
            special_defence=85,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.DRAGON,
        ],
        num_legs=2,
        supported_abilities=[Abilities.OVERGROW],
    ),
    PokemonGen3.TORCHIC: Pokemon(
        name=PokemonGen3.TORCHIC,
        gen=3,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen3.COMBUSKEN),
        ],
        colors=[Colors.ORANGE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=40,
            special_attack=70,
            special_defence=50,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.FOOD,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.BLAZE,
        ],
    ),
    PokemonGen3.COMBUSKEN: Pokemon(
        name=PokemonGen3.COMBUSKEN,
        gen=3,
        types=[Types.FIRE, Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen3.BLAZIKEN),
        ],
        colors=[Colors.ORANGE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=60,
            special_attack=85,
            special_defence=60,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.FOOD,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.BLAZE,
        ],
    ),
    PokemonGen3.BLAZIKEN: Pokemon(
        name=PokemonGen3.BLAZIKEN,
        gen=3,
        types=[Types.FIRE, Types.FIGHTING],
        evolves_to=[],
        colors=[Colors.RED, Colors.YELLOW, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=120,
            defence=70,
            special_attack=110,
            special_defence=70,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.FOOD,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.BLAZE,
        ],
    ),
    PokemonGen3.MUDKIP: Pokemon(
        name=PokemonGen3.MUDKIP,
        gen=3,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.MARSHTOMP),
        ],
        colors=[Colors.BLUE, Colors.ORANGE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=50,
            special_attack=50,
            special_defence=50,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FROG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.TORRENT,
        ],
    ),
    PokemonGen3.MARSHTOMP: Pokemon(
        name=PokemonGen3.MARSHTOMP,
        gen=3,
        types=[Types.WATER, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.SWAMPERT),
        ],
        colors=[Colors.BLUE, Colors.ORANGE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=70,
            special_attack=60,
            special_defence=70,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FROG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.TORRENT,
        ],
    ),
    PokemonGen3.SWAMPERT: Pokemon(
        name=PokemonGen3.SWAMPERT,
        gen=3,
        types=[Types.WATER, Types.GROUND],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.ORANGE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=110,
            defence=90,
            special_attack=85,
            special_defence=90,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FROG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.TORRENT,
        ],
    ),
    PokemonGen3.POOCHYENA: Pokemon(
        name=PokemonGen3.POOCHYENA,
        gen=3,
        types=[Types.DARK],
        evolves_to=[
            Evolution(name=PokemonGen3.MIGHTYENA),
        ],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=35,
            special_attack=30,
            special_defence=30,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.RUN_AWAY,
            Abilities.QUICK_FEET,
        ],
    ),
    PokemonGen3.MIGHTYENA: Pokemon(
        name=PokemonGen3.MIGHTYENA,
        gen=3,
        types=[Types.DARK],
        evolves_to=[],
        colors=[
            Colors.GRAY, Colors.BLACK
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=70,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.INTIMIDATE,
            Abilities.QUICK_FEET,
        ],
    ),
    PokemonGen3.ZIGZAGOON: Pokemon(
        name=PokemonGen3.ZIGZAGOON,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.LINOONE),
        ],
        colors=[
            Colors.BROWN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=41,
            special_attack=30,
            special_defence=41,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.PICKUP,
            Abilities.GLUTTONY,
        ],
    ),
    PokemonGen3.LINOONE: Pokemon(
        name=PokemonGen3.LINOONE,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[
            Colors.BROWN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=61,
            special_attack=50,
            special_defence=61,
        ),
        categories=[
            Categories.MAMMAL
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.PICKUP,
            Abilities.GLUTTONY,
        ],
    ),
    PokemonGen3.WURMPLE: Pokemon(
        name=PokemonGen3.WURMPLE,
        gen=3,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen3.CASCOON, evolution_type=EvolutionType.RANDOM),
            Evolution(name=PokemonGen3.SILCOON, evolution_type=EvolutionType.RANDOM),
        ],
        colors=[
            Colors.RED, Colors.YELLOW, Colors.WHITE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=35,
            special_attack=20,
            special_defence=30,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=10,
        supported_abilities=[
            Abilities.SHIELD_DUST,
        ],
    ),
    PokemonGen3.SILCOON: Pokemon(
        name=PokemonGen3.SILCOON,
        gen=3,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen3.BEAUTIFLY),
        ],
        colors=[
            Colors.WHITE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=35,
            defence=55,
            special_attack=25,
            special_defence=25,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.SHED_SKIN,
        ],
    ),
    PokemonGen3.BEAUTIFLY: Pokemon(
        name=PokemonGen3.BEAUTIFLY,
        gen=3,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[],
        colors=[
            Colors.WHITE, Colors.BLACK, Colors.YELLOW, Colors.RED, Colors.BLUE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=50,
            special_attack=100,
            special_defence=50,
        ),
        categories=[
            Categories.BUG,
            Categories.WING,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SWARM,
        ],
    ),
    PokemonGen3.CASCOON: Pokemon(
        name=PokemonGen3.CASCOON,
        gen=3,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen3.DUSTOX),
        ],
        colors=[
            Colors.PURPLE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=35,
            defence=55,
            special_attack=25,
            special_defence=25,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.SHED_SKIN,
        ],
    ),
    PokemonGen3.DUSTOX: Pokemon(
        name=PokemonGen3.DUSTOX,
        gen=3,
        types=[Types.BUG, Types.POISON],
        evolves_to=[],
        colors=[
            Colors.PURPLE, Colors.GREEN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=70,
            special_attack=50,
            special_defence=90,
        ),
        categories=[
            Categories.BUG,
            Categories.WING,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.SHIELD_DUST,
        ],
    ),
    PokemonGen3.LOTAD: Pokemon(
        name=PokemonGen3.LOTAD,
        gen=3,
        types=[Types.WATER, Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.LOMBRE),
        ],
        colors=[
            Colors.BLUE, Colors.GREEN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=30,
            special_attack=40,
            special_defence=50,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=6,
        supported_abilities=[
            Abilities.SWIFT_SWIM,
            Abilities.RAIN_DISH,
        ],
    ),
    PokemonGen3.LOMBRE: Pokemon(
        name=PokemonGen3.LOMBRE,
        gen=3,
        types=[Types.WATER, Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.LUDICOLO, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE, level=37),
        ],
        colors=[
            Colors.GREEN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=50,
            special_attack=60,
            special_defence=70,
        ),
        categories=[
            Categories.PLANT,
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SWIFT_SWIM,
            Abilities.RAIN_DISH,
        ],
    ),
    PokemonGen3.LUDICOLO: Pokemon(
        name=PokemonGen3.LUDICOLO,
        gen=3,
        types=[Types.WATER, Types.GRASS],
        evolves_to=[],
        colors=[
            Colors.GREEN, Colors.YELLOW
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=70,
            special_attack=90,
            special_defence=100,
        ),
        categories=[
            Categories.PLANT,
            Categories.HUMAN,
            Categories.MAMMAL,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SWIFT_SWIM,
            Abilities.RAIN_DISH,
        ],
    ),
    PokemonGen3.SEEDOT: Pokemon(
        name=PokemonGen3.SEEDOT,
        gen=3,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.NUZLEAF),
        ],
        colors=[
            Colors.BROWN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=50,
            special_attack=30,
            special_defence=30,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.CHLOROPHYLL,
            Abilities.EARLY_BIRD,
        ],
    ),
    PokemonGen3.NUZLEAF: Pokemon(
        name=PokemonGen3.NUZLEAF,
        gen=3,
        types=[Types.GRASS, Types.DARK],
        evolves_to=[
            Evolution(name=PokemonGen3.SHIFTRY, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE, level=49),
        ],
        colors=[
            Colors.BROWN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=40,
            special_attack=60,
            special_defence=40,
        ),
        categories=[
            Categories.PLANT,
            Categories.FANTASY,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.CHLOROPHYLL,
            Abilities.EARLY_BIRD,
        ],
    ),
    PokemonGen3.SHIFTRY: Pokemon(
        name=PokemonGen3.SHIFTRY,
        gen=3,
        types=[Types.GRASS, Types.DARK],
        evolves_to=[],
        colors=[
            Colors.BROWN, Colors.WHITE, Colors.GREEN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=60,
            special_attack=90,
            special_defence=60,
        ),
        categories=[
            Categories.PLANT,
            Categories.FANTASY,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.CHLOROPHYLL,
            Abilities.WIND_RIDER,
        ],
    ),
    PokemonGen3.TAILLOW: Pokemon(
        name=PokemonGen3.TAILLOW,
        gen=3,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.SWELLOW),
        ],
        colors=[
            Colors.BLUE, Colors.WHITE, Colors.RED
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=30,
            special_attack=30,
            special_defence=30,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.FOOD,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.GUTS,
        ],
    ),
    PokemonGen3.SWELLOW: Pokemon(
        name=PokemonGen3.SWELLOW,
        gen=3,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[],
        colors=[
            Colors.BLUE, Colors.RED, Colors.WHITE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=60,
            special_attack=75,
            special_defence=50,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.FOOD,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.GUTS,
        ],
    ),
    PokemonGen3.WINGULL: Pokemon(
        name=PokemonGen3.WINGULL,
        gen=3,
        types=[Types.WATER, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.PELIPPER),
        ],
        colors=[
            Colors.WHITE, Colors.BLUE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=30,
            special_attack=55,
            special_defence=30,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.KEEN_EYE,
            Abilities.HYDRATION,
        ],
    ),
    PokemonGen3.PELIPPER: Pokemon(
        name=PokemonGen3.PELIPPER,
        gen=3,
        types=[Types.WATER, Types.FLYING],
        evolves_to=[],
        colors=[
            Colors.BLUE, Colors.WHITE, Colors.YELLOW
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=100,
            special_attack=95,
            special_defence=70,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.KEEN_EYE,
            Abilities.DRIZZLE,
        ],
    ),
    PokemonGen3.RALTS: Pokemon(
        name=PokemonGen3.RALTS,
        gen=3,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.KIRLIA),
        ],
        colors=[
            Colors.WHITE, Colors.GREEN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=25,
            defence=25,
            special_attack=45,
            special_defence=35,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FANTASY,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SYNCHRONIZE,
            Abilities.TRACE,
        ],
    ),
    PokemonGen3.KIRLIA: Pokemon(
        name=PokemonGen3.KIRLIA,
        gen=3,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.GARDEVOIR),
        ],
        colors=[
            Colors.WHITE, Colors.GREEN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=35,
            defence=35,
            special_attack=65,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FANTASY,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SYNCHRONIZE,
            Abilities.TRACE,
        ],
    ),
    PokemonGen3.GARDEVOIR: Pokemon(
        name=PokemonGen3.GARDEVOIR,
        gen=3,
        types=[Types.PSYCHIC],
        evolves_to=[],
        colors=[
            Colors.WHITE, Colors.GREEN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=65,
            special_attack=125,
            special_defence=115,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FANTASY,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SYNCHRONIZE,
            Abilities.TRACE,
        ],
    ),
    PokemonGen3.SURSKIT: Pokemon(
        name=PokemonGen3.SURSKIT,
        gen=3,
        types=[Types.BUG, Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.MASQUERAIN),
        ],
        colors=[
            Colors.BLUE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=32,
            special_attack=50,
            special_defence=52,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.SWIFT_SWIM,
        ],
    ),
    PokemonGen3.MASQUERAIN: Pokemon(
        name=PokemonGen3.MASQUERAIN,
        gen=3,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[],
        colors=[
            Colors.BLUE, Colors.PINK
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=62,
            special_attack=100,
            special_defence=82,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.INTIMIDATE,
        ],
    ),
    PokemonGen3.SHROOMISH: Pokemon(
        name=PokemonGen3.SHROOMISH,
        gen=3,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.BRELOOM),
        ],
        colors=[
            Colors.GREEN, Colors.BROWN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=60,
            special_attack=40,
            special_defence=60,
        ),
        categories=[
            Categories.PLANT,
            Categories.FOOD,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.EFFECT_SPORE,
            Abilities.POISON_POINT,
        ],
    ),
    PokemonGen3.BRELOOM: Pokemon(
        name=PokemonGen3.BRELOOM,
        gen=3,
        types=[Types.GRASS, Types.FIGHTING],
        evolves_to=[],
        colors=[
            Colors.GREEN, Colors.BROWN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=130,
            defence=80,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
            Categories.FOOD,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.EFFECT_SPORE,
            Abilities.POISON_POINT,
        ],
    ),
    PokemonGen3.SLAKOTH: Pokemon(
        name=PokemonGen3.SLAKOTH,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.VIGOROTH),
        ],
        colors=[
            Colors.BROWN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=60,
            special_attack=35,
            special_defence=35,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.SLOTH,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.TRUANT,
        ],
    ),
    PokemonGen3.VIGOROTH: Pokemon(
        name=PokemonGen3.VIGOROTH,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.SLAKING),
        ],
        colors=[
            Colors.WHITE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=80,
            special_attack=55,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.SLOTH,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.VITAL_SPIRIT,
        ],
    ),
    PokemonGen3.SLAKING: Pokemon(
        name=PokemonGen3.SLAKING,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=160,
            defence=100,
            special_attack=95,
            special_defence=65,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.SLOTH,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.TRUANT,
        ],
    ),
    PokemonGen3.NINCADA: Pokemon(
        name=PokemonGen3.NINCADA,
        gen=3,
        types=[Types.BUG, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.NINJASK),
            Evolution(name=PokemonGen3.SHEDINJA, special_information="Empty spot in party"),
        ],
        colors=[
            Colors.BROWN, Colors.WHITE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=90,
            special_attack=30,
            special_defence=30,
        ),
        categories=[
            Categories.BUG,
            Categories.WING,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.COMPOUND_EYES,
        ],
    ),
    PokemonGen3.NINJASK: Pokemon(
        name=PokemonGen3.NINJASK,
        gen=3,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[],
        colors=[
            Colors.WHITE, Colors.BLACK, Colors.YELLOW
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=45,
            special_attack=50,
            special_defence=50,
        ),
        categories=[
            Categories.BUG,
            Categories.WING,
        ],
        num_legs=6,
        supported_abilities=[
            Abilities.SPEED_BOOST,
        ],
    ),
    PokemonGen3.SHEDINJA: Pokemon(
        name=PokemonGen3.SHEDINJA,
        gen=3,
        types=[Types.BUG, Types.GHOST],
        evolves_to=[],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=45,
            special_attack=30,
            special_defence=30,
        ),
        categories=[
            Categories.BUG,
            Categories.WING,
            Categories.FANTASY,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.WONDER_GUARD,
        ],
    ),
    PokemonGen3.WHISMUR: Pokemon(
        name=PokemonGen3.WHISMUR,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.LOUDRED),
        ],
        colors=[
            Colors.PINK
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=51,
            defence=23,
            special_attack=51,
            special_defence=23,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SOUNDPROOF,
        ],
    ),
    PokemonGen3.LOUDRED: Pokemon(
        name=PokemonGen3.LOUDRED,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.EXPLOUD),
        ],
        colors=[
            Colors.PURPLE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=71,
            defence=43,
            special_attack=71,
            special_defence=43,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SOUNDPROOF,
        ],
    ),
    PokemonGen3.EXPLOUD: Pokemon(
        name=PokemonGen3.EXPLOUD,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[
            Colors.PURPLE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=91,
            defence=63,
            special_attack=91,
            special_defence=73,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SOUNDPROOF,
        ],
    ),
    PokemonGen3.MAKUHITA: Pokemon(
        name=PokemonGen3.MAKUHITA,
        gen=3,
        types=[
            Types.FIGHTING,
        ],
        evolves_to=[
            Evolution(name=PokemonGen3.HARIYAMA),
        ],
        colors=[Colors.YELLOW, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=30,
            special_attack=20,
            special_defence=30,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.THICK_FAT,
            Abilities.GUTS,
        ],
    ),
    PokemonGen3.HARIYAMA: Pokemon(
        name=PokemonGen3.HARIYAMA,
        gen=3,
        types=[Types.FIGHTING],
        evolves_to=[],
        colors=[
            Colors.BLACK, Colors.YELLOW, Colors.WHITE, Colors.BROWN,
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=120,
            defence=60,
            special_attack=40,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.THICK_FAT,
            Abilities.GUTS,
        ],
    ),
    PokemonGen3.AZURILL: Pokemon(
        name=PokemonGen3.AZURILL,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.MARILL, evolution_type=EvolutionType.FRIENDSHIP, level=15),
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=20,
            defence=40,
            special_attack=20,
            special_defence=40,
        ),
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.THICK_FAT,
            Abilities.HUGE_POWER,
        ],
    ),
    PokemonGen3.NOSEPASS: Pokemon(
        name=PokemonGen3.NOSEPASS,
        gen=3,
        types=[Types.ROCK],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=135,
            special_attack=45,
            special_defence=90,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.ITEM,
            Categories.FANTASY,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.STURDY,
            Abilities.MAGNET_PULL,
        ],
    ),
    PokemonGen3.SKITTY: Pokemon(
        name=PokemonGen3.SKITTY,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.DELCATTY, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE, level=27),
        ],
        colors=[
            Colors.PINK, Colors.WHITE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=45,
            special_attack=35,
            special_defence=35,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.CUTE_CHARM,
            Abilities.NORMALIZE,
        ],
    ),
    PokemonGen3.DELCATTY: Pokemon(
        name=PokemonGen3.DELCATTY,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[
            Colors.PURPLE, Colors.WHITE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=65,
            special_attack=55,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.CUTE_CHARM,
            Abilities.NORMALIZE,
        ],
    ),
    PokemonGen3.SABLEYE: Pokemon(
        name=PokemonGen3.SABLEYE,
        gen=3,
        types=[Types.DARK, Types.GHOST],
        evolves_to=[],
        colors=[
            Colors.PURPLE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=75,
            special_attack=65,
            special_defence=65,
        ),
        categories=[
            Categories.FANTASY,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.KEEN_EYE,
            Abilities.STALL,
        ],
    ),
    PokemonGen3.MAWILE: Pokemon(
        name=PokemonGen3.MAWILE,
        gen=3,
        types=[Types.STEEL],
        evolves_to=[],
        colors=[
            Colors.GRAY, Colors.YELLOW
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=85,
            special_attack=55,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
            Categories.FANTASY,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.HYPER_CUTTER,
            Abilities.INTIMIDATE,
        ],
    ),
    PokemonGen3.ARON: Pokemon(
        name=PokemonGen3.ARON,
        gen=3,
        types=[Types.STEEL, Types.ROCK],
        evolves_to=[
            Evolution(name=PokemonGen3.LAIRON),
        ],
        colors=[
            Colors.GRAY
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=100,
            special_attack=40,
            special_defence=40,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WEAPON,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.STURDY,
            Abilities.ROCK_HEAD,
        ],
    ),
    PokemonGen3.LAIRON: Pokemon(
        name=PokemonGen3.LAIRON,
        gen=3,
        types=[Types.STEEL, Types.ROCK],
        evolves_to=[
            Evolution(name=PokemonGen3.AGGRON),
        ],
        colors=[
            Colors.GRAY
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=140,
            special_attack=50,
            special_defence=50,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WEAPON,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.STURDY,
            Abilities.ROCK_HEAD,
        ],
    ),
    PokemonGen3.AGGRON: Pokemon(
        name=PokemonGen3.AGGRON,
        gen=3,
        types=[Types.STEEL, Types.ROCK],
        evolves_to=[],
        colors=[
            Colors.GRAY
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=110,
            defence=180,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WEAPON,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.STURDY,
            Abilities.ROCK_HEAD,
        ],
    ),
    PokemonGen3.MEDITITE: Pokemon(
        name=PokemonGen3.MEDITITE,
        gen=3,
        types=[Types.FIGHTING, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.MEDICHAM),
        ],
        colors=[
            Colors.BLUE, Colors.WHITE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=55,
            special_attack=40,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.PURE_POWER,
        ],
    ),
    PokemonGen3.MEDICHAM: Pokemon(
        name=PokemonGen3.MEDICHAM,
        gen=3,
        types=[Types.FIGHTING, Types.PSYCHIC],
        evolves_to=[],
        colors=[
            Colors.PINK, Colors.WHITE
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=75,
            special_attack=60,
            special_defence=75,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.PURE_POWER,
        ],
    ),
    PokemonGen3.ELECTRIKE: Pokemon(
        name=PokemonGen3.ELECTRIKE,
        gen=3,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen3.MANECTRIC),
        ],
        colors=[
            Colors.YELLOW, Colors.GREEN
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=40,
            special_attack=65,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.STATIC,
            Abilities.LIGHTNING_ROD,
        ],
    ),
    PokemonGen3.MANECTRIC: Pokemon(
        name=PokemonGen3.MANECTRIC,
        gen=3,
        types=[Types.ELECTRIC],
        evolves_to=[],
        colors=[
            Colors.BLUE, Colors.YELLOW
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=60,
            special_attack=105,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.STATIC,
            Abilities.LIGHTNING_ROD,
        ],
    ),
    PokemonGen3.PLUSLE: Pokemon(
        name=PokemonGen3.PLUSLE,
        gen=3,
        types=[Types.ELECTRIC],
        evolves_to=[],
        colors=[Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=40,
            special_attack=85,
            special_defence=75,
        ),
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.PLUS,
        ],
    ),
    PokemonGen3.MINUN: Pokemon(
        name=PokemonGen3.MINUN,
        gen=3,
        types=[Types.ELECTRIC],
        evolves_to=[],
        colors=[Colors.YELLOW, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=50,
            special_attack=75,
            special_defence=85,
        ),
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.MINUS,
        ],
    ),
    PokemonGen3.VOLBEAT: Pokemon(
        name=PokemonGen3.VOLBEAT,
        gen=3,
        types=[Types.BUG],
        evolves_to=[],
        colors=[Colors.RED, Colors.BLUE, Colors.BLACK],
        supported_genders=[Genders.MALE],
        stats=Stats(
            attack=73,
            defence=75,
            special_attack=47,
            special_defence=85,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.ILLUMINATE,
            Abilities.SWARM,
        ],
    ),
    PokemonGen3.ILLUMISE: Pokemon(
        name=PokemonGen3.ILLUMISE,
        gen=3,
        types=[Types.BUG],
        evolves_to=[],
        colors=[Colors.BLACK, Colors.BLUE, Colors.PURPLE],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=47,
            defence=75,
            special_attack=73,
            special_defence=85,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.OBLIVIOUS,
            Abilities.TINTED_LENS,
        ],
    ),
    PokemonGen3.ROSELIA: Pokemon(
        name=PokemonGen3.ROSELIA,
        gen=3,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.RED, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=45,
            special_attack=100,
            special_defence=80,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.NATURAL_CURE,
            Abilities.POISON_POINT,
        ],
    ),
    PokemonGen3.GULPIN: Pokemon(
        name=PokemonGen3.GULPIN,
        gen=3,
        types=[Types.POISON],
        evolves_to=[
             Evolution(name=PokemonGen3.SWALOT),
        ],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=43,
            defence=53,
            special_attack=43,
            special_defence=53,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.LIQUID_OOZE,
            Abilities.STICKY_HOLD,
        ],
    ),
    PokemonGen3.SWALOT: Pokemon(
        name=PokemonGen3.SWALOT,
        gen=3,
        types=[Types.POISON],
        evolves_to=[],
        colors=[Colors.PURPLE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=73,
            defence=83,
            special_attack=73,
            special_defence=83,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.LIQUID_OOZE,
            Abilities.STICKY_HOLD,
        ],
    ),
    PokemonGen3.CARVANHA: Pokemon(
        name=PokemonGen3.CARVANHA,
        gen=3,
        types=[Types.WATER, Types.DARK],
        evolves_to=[
            Evolution(name=PokemonGen3.SHARPEDO),
        ],
        colors=[Colors.YELLOW, Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=20,
            special_attack=65,
            special_defence=20,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.ROUGH_SKIN,
        ],
    ),
    PokemonGen3.SHARPEDO: Pokemon(
        name=PokemonGen3.SHARPEDO,
        gen=3,
        types=[Types.WATER, Types.DARK],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=120,
            defence=40,
            special_attack=95,
            special_defence=40,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.ROUGH_SKIN,
        ],
    ),
    PokemonGen3.WAILMER: Pokemon(
        name=PokemonGen3.WAILMER,
        gen=3,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.WAILORD),
        ],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=35,
            special_attack=70,
            special_defence=35,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.WATER_VEIL,
            Abilities.OBLIVIOUS,
        ],
    ),
    PokemonGen3.WAILORD: Pokemon(
        name=PokemonGen3.WAILORD,
        gen=3,
        types=[Types.WATER],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=45,
            special_attack=90,
            special_defence=45,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.WATER_VEIL,
            Abilities.OBLIVIOUS,
        ],
    ),
    PokemonGen3.NUMEL: Pokemon(
        name=PokemonGen3.NUMEL,
        gen=3,
        types=[Types.FIRE, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.CAMERUPT),
        ],
        colors=[Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=40,
            special_attack=65,
            special_defence=45,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HORSE,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.OBLIVIOUS,
            Abilities.SIMPLE,
        ],
    ),
    PokemonGen3.CAMERUPT: Pokemon(
        name=PokemonGen3.CAMERUPT,
        gen=3,
        types=[Types.FIRE, Types.GROUND],
        evolves_to=[],
        colors=[Colors.ORANGE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=70,
            special_attack=105,
            special_defence=75,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HORSE,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.MAGMA_ARMOR,
            Abilities.SOLID_ROCK,
        ],
    ),
    PokemonGen3.TORKOAL: Pokemon(
        name=PokemonGen3.TORKOAL,
        gen=3,
        types=[Types.FIRE],
        evolves_to=[],
        colors=[Colors.ORANGE, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=140,
            special_attack=85,
            special_defence=70,
        ),
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.TURTLE,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.WHITE_SMOKE,
            Abilities.DROUGHT,
        ],
    ),
    PokemonGen3.SPOINK: Pokemon(
        name=PokemonGen3.SPOINK,
        gen=3,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.GRUMPIG),
        ],
        colors=[Colors.GRAY, Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=25,
            defence=35,
            special_attack=70,
            special_defence=80,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.PIG,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.THICK_FAT,
            Abilities.OWN_TEMPO,
        ],
    ),
    PokemonGen3.GRUMPIG: Pokemon(
        name=PokemonGen3.GRUMPIG,
        gen=3,
        types=[Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=65,
            special_attack=90,
            special_defence=110,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.PIG,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.THICK_FAT,
            Abilities.OWN_TEMPO,
        ],
    ),
    PokemonGen3.SPINDA: Pokemon(
        name=PokemonGen3.SPINDA,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.RED, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=60,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.BEAR,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.OWN_TEMPO,
            Abilities.TANGLED_FEET,
        ],
    ),
    PokemonGen3.TRAPINCH: Pokemon(
        name=PokemonGen3.TRAPINCH,
        gen=3,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.VIBRAVA),
        ],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=45,
            special_attack=45,
            special_defence=45,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.HYPER_CUTTER,
            Abilities.ARENA_TRAP,
        ],
    ),
    PokemonGen3.VIBRAVA: Pokemon(
        name=PokemonGen3.VIBRAVA,
        gen=3,
        types=[Types.GROUND, Types.DRAGON],
        evolves_to=[
            Evolution(name=PokemonGen3.FLYGON),
        ],
        colors=[Colors.GREEN, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=50,
            special_attack=50,
            special_defence=50,
        ),
        categories=[
            Categories.BUG,
            Categories.WING,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.LEVITATE,
        ],
    ),
    PokemonGen3.FLYGON: Pokemon(
        name=PokemonGen3.FLYGON,
        gen=3,
        types=[Types.GROUND, Types.DRAGON],
        evolves_to=[],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=80,
            special_attack=80,
            special_defence=80,
        ),
        categories=[
            Categories.BUG,
            Categories.WING,
            Categories.DRAGON,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.LEVITATE,
        ],
    ),
    PokemonGen3.CACNEA: Pokemon(
        name=PokemonGen3.CACNEA,
        gen=3,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.CACTURNE),
        ],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=40,
            special_attack=85,
            special_defence=40,
        ),
        categories=[
            Categories.PLANT,
            Categories.FOOD,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SAND_VEIL,
        ],
    ),
    PokemonGen3.CACTURNE: Pokemon(
        name=PokemonGen3.CACTURNE,
        gen=3,
        types=[Types.GRASS, Types.DARK],
        evolves_to=[],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=115,
            defence=60,
            special_attack=115,
            special_defence=60,
        ),
        categories=[
            Categories.PLANT,
            Categories.FOOD,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SAND_VEIL,
        ],
    ),
    PokemonGen3.SWABLU: Pokemon(
        name=PokemonGen3.SWABLU,
        gen=3,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.ALTARIA),
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=60,
            special_attack=40,
            special_defence=75,
        ),
        categories=[
            Categories.BIRD,
            Categories.WING,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.NATURAL_CURE,
        ],
    ),
    PokemonGen3.ALTARIA: Pokemon(
        name=PokemonGen3.ALTARIA,
        gen=3,
        types=[Types.DRAGON, Types.FLYING],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=90,
            special_attack=70,
            special_defence=105,
        ),
        categories=[
            Categories.BIRD,
            Categories.WING,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.NATURAL_CURE,
        ],
    ),
    PokemonGen3.ZANGOOSE: Pokemon(
        name=PokemonGen3.ZANGOOSE,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=115,
            defence=60,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.IMMUNITY,
        ],
    ),
    PokemonGen3.SEVIPER: Pokemon(
        name=PokemonGen3.SEVIPER,
        gen=3,
        types=[Types.POISON],
        evolves_to=[],
        colors=[Colors.BLACK, Colors.PURPLE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=60,
            special_attack=100,
            special_defence=60,
        ),
        categories=[
            Categories.REPTILE,
            Categories.SNAKE,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.SHED_SKIN,
        ],
    ),
    PokemonGen3.LUNATONE: Pokemon(
        name=PokemonGen3.LUNATONE,
        gen=3,
        types=[Types.ROCK, Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.BROWN],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=55,
            defence=65,
            special_attack=95,
            special_defence=85,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.LEVITATE,
        ],
    ),
    PokemonGen3.SOLROCK: Pokemon(
        name=PokemonGen3.SOLROCK,
        gen=3,
        types=[Types.ROCK, Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.BROWN, Colors.ORANGE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=95,
            defence=85,
            special_attack=55,
            special_defence=65,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.LEVITATE,
        ],
    ),
    PokemonGen3.BARBOACH: Pokemon(
        name=PokemonGen3.BARBOACH,
        gen=3,
        types=[Types.WATER, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.WHISCASH),
        ],
        colors=[Colors.GRAY, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=48,
            defence=43,
            special_attack=46,
            special_defence=41,
        ),
        categories=[
            Categories.WATERMON,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.OBLIVIOUS,
            Abilities.ANTICIPATION,
        ],
    ),
    PokemonGen3.WHISCASH: Pokemon(
        name=PokemonGen3.WHISCASH,
        gen=3,
        types=[Types.WATER, Types.GROUND],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=78,
            defence=73,
            special_attack=76,
            special_defence=71,
        ),
        categories=[
            Categories.WATERMON,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.OBLIVIOUS,
            Abilities.ANTICIPATION,
        ],
    ),
    PokemonGen3.CORPHISH: Pokemon(
        name=PokemonGen3.CORPHISH,
        gen=3,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.CRAWDAUNT),
        ],
        colors=[Colors.RED, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=65,
            special_attack=50,
            special_defence=35,
        ),
        categories=[
            Categories.WATERMON,
            Categories.CRAB,
            Categories.FOOD,
        ],
        num_legs=6,
        supported_abilities=[
            Abilities.HYPER_CUTTER,
            Abilities.SHELL_ARMOR,
        ],
    ),
    PokemonGen3.CRAWDAUNT: Pokemon(
        name=PokemonGen3.CRAWDAUNT,
        gen=3,
        types=[Types.WATER, Types.DARK],
        evolves_to=[],
        colors=[Colors.RED, Colors.WHITE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=120,
            defence=85,
            special_attack=90,
            special_defence=55,
        ),
        categories=[
            Categories.WATERMON,
            Categories.CRAB,
            Categories.FOOD,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.HYPER_CUTTER,
            Abilities.SHELL_ARMOR,
        ],
    ),
    PokemonGen3.BALTOY: Pokemon(
        name=PokemonGen3.BALTOY,
        gen=3,
        types=[Types.GROUND, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.CLAYDOL),
        ],
        colors=[Colors.BROWN],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=40,
            defence=55,
            special_attack=40,
            special_defence=70,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.ITEM,
        ],
        num_legs=1,
        supported_abilities=[
            Abilities.LEVITATE,
        ],
    ),
    PokemonGen3.CLAYDOL: Pokemon(
        name=PokemonGen3.CLAYDOL,
        gen=3,
        types=[Types.GROUND, Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.BROWN],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=70,
            defence=105,
            special_attack=70,
            special_defence=120,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.LEVITATE,
        ],
    ),
    PokemonGen3.LILEEP: Pokemon(
        name=PokemonGen3.LILEEP,
        gen=3,
        types=[Types.ROCK, Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.CRADILY),
        ],
        colors=[Colors.PURPLE, Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=41,
            defence=77,
            special_attack=61,
            special_defence=87,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.SUCTION_CUPS,
        ],
    ),
    PokemonGen3.CRADILY: Pokemon(
        name=PokemonGen3.CRADILY,
        gen=3,
        types=[Types.ROCK, Types.GRASS],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=81,
            defence=97,
            special_attack=81,
            special_defence=107,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.SUCTION_CUPS,
        ],
    ),
    PokemonGen3.ANORITH: Pokemon(
        name=PokemonGen3.ANORITH,
        gen=3,
        types=[Types.ROCK, Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen3.ARMALDO),
        ],
        colors=[Colors.GRAY, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=50,
            special_attack=40,
            special_defence=50,
        ),
        categories=[
            Categories.CRAB,
            Categories.WATERMON,
            Categories.PREHISTORIC,
        ],
        num_legs=8,
        supported_abilities=[
            Abilities.BATTLE_ARMOR,
        ],
    ),
    PokemonGen3.ARMALDO: Pokemon(
        name=PokemonGen3.ARMALDO,
        gen=3,
        types=[Types.ROCK, Types.BUG],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=125,
            defence=100,
            special_attack=70,
            special_defence=80,
        ),
        categories=[
            Categories.MOUSE,
            Categories.RODENT,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.BATTLE_ARMOR,
        ],
    ),
    PokemonGen3.FEEBAS: Pokemon(
        name=PokemonGen3.FEEBAS,
        gen=3,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.MILTOIC, evolution_type=EvolutionType.TRADE, item=Item.PRISM_SCALE, should_hold=True, level=20),
        ],
        colors=[Colors.BROWN, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=15,
            defence=20,
            special_attack=20,
            special_defence=10,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.FOOD,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.SWIFT_SWIM,
            Abilities.OBLIVIOUS,
        ],
    ),
    PokemonGen3.MILTOIC: Pokemon(
        name=PokemonGen3.MILTOIC,
        gen=3,
        types=[Types.WATER],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.PINK, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=79,
            special_attack=100,
            special_defence=125,
        ),
        categories=[
            Categories.REPTILE,
            Categories.FANTASY,
            Categories.SNAKE,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.MARVEL_SCALE,
            Abilities.COMPETITIVE,
        ],
    ),
    PokemonGen3.CASTFORM: Pokemon(
        name=PokemonGen3.CASTFORM,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=70,
            special_attack=70,
            special_defence=70,
        ),
        categories=[
            Categories.ITEM,
            Categories.FANTASY,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.FORECAST,
        ],
    ),
    PokemonGen3.KECLEON: Pokemon(
        name=PokemonGen3.KECLEON,
        gen=3,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=70,
            special_attack=60,
            special_defence=120,
        ),
        categories=[
            Categories.REPTILE,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.COLOR_CHANGE,
        ],
    ),
    PokemonGen3.SHUPPET: Pokemon(
        name=PokemonGen3.SHUPPET,
        gen=3,
        types=[Types.GHOST],
        evolves_to=[
            Evolution(name=PokemonGen3.BANETTE),
        ],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=35,
            special_attack=63,
            special_defence=33,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.INSOMNIA,
            Abilities.FRISK,
        ],
    ),
    PokemonGen3.BANETTE: Pokemon(
        name=PokemonGen3.BANETTE,
        gen=3,
        types=[Types.GHOST],
        evolves_to=[],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=115,
            defence=65,
            special_attack=83,
            special_defence=63,
        ),
        categories=[
            Categories.FANTASY,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.INSOMNIA,
            Abilities.FRISK,
        ],
    ),
    PokemonGen3.DUSKULL: Pokemon(
        name=PokemonGen3.DUSKULL,
        gen=3,
        types=[Types.GHOST],
        evolves_to=[
            Evolution(name=PokemonGen3.DUSCLOPS),
        ],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=90,
            special_attack=30,
            special_defence=90,
        ),
        categories=[
            Categories.FANTASY,
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.LEVITATE,
        ],
    ),
    PokemonGen3.DUSCLOPS: Pokemon(
        name=PokemonGen3.DUSCLOPS,
        gen=3,
        types=[Types.GHOST],
        evolves_to=[],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=130,
            special_attack=60,
            special_defence=130,
        ),
        categories=[
            Categories.FANTASY,
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.PRESSURE,
        ],
    ),
    PokemonGen3.TROPIUS: Pokemon(
        name=PokemonGen3.TROPIUS,
        gen=3,
        types=[Types.GRASS, Types.FLYING],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=68,
            defence=83,
            special_attack=72,
            special_defence=87,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.WING,
            Categories.PLANT,
            Categories.REPTILE,
            Categories.FOOD,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.CHLOROPHYLL,
            Abilities.SOLAR_POWER,
        ],
    ),
    PokemonGen3.CHIMECHO: Pokemon(
        name=PokemonGen3.CHIMECHO,
        gen=3,
        types=[Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=80,
            special_attack=95,
            special_defence=90,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.LEVITATE,
        ],
    ),
    PokemonGen3.ABSOL: Pokemon(
        name=PokemonGen3.ABSOL,
        gen=3,
        types=[Types.DARK],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=130,
            defence=60,
            special_attack=75,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FANTASY,
            Categories.DOG,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.PRESSURE,
            Abilities.SUPER_LUCK,
        ],
    ),
    PokemonGen3.WYNAUT: Pokemon(
        name=PokemonGen3.WYNAUT,
        gen=3,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.WOBBUFFET),
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=23,
            defence=48,
            special_attack=23,
            special_defence=48,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SHADOW_TAG,
        ],
    ),
    PokemonGen3.SNORUNT: Pokemon(
        name=PokemonGen3.SNORUNT,
        gen=3,
        types=[Types.ICE],
        evolves_to=[
            Evolution(name=PokemonGen3.GLALIE),
        ],
        colors=[Colors.YELLOW, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=50,
            special_attack=50,
            special_defence=50,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.INNER_FOCUS,
            Abilities.ICE_BODY,
        ],
    ),
    PokemonGen3.GLALIE: Pokemon(
        name=PokemonGen3.GLALIE,
        gen=3,
        types=[Types.ICE],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=80,
            special_attack=80,
            special_defence=80,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.INNER_FOCUS,
            Abilities.ICE_BODY,
        ],
    ),
    PokemonGen3.SPHEAL: Pokemon(
        name=PokemonGen3.SPHEAL,
        gen=3,
        types=[Types.ICE, Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.SEALEO),
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=50,
            special_attack=55,
            special_defence=50,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.DOG,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.THICK_FAT,
            Abilities.ICE_BODY,
        ],
    ),
    PokemonGen3.SEALEO: Pokemon(
        name=PokemonGen3.SEALEO,
        gen=3,
        types=[Types.ICE, Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.WALREIN),
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=70,
            special_attack=75,
            special_defence=70,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.DOG,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.THICK_FAT,
            Abilities.ICE_BODY,
        ],
    ),
    PokemonGen3.WALREIN: Pokemon(
        name=PokemonGen3.WALREIN,
        gen=3,
        types=[Types.ICE, Types.WATER],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=90,
            special_attack=95,
            special_defence=90,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.DOG,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.THICK_FAT,
            Abilities.ICE_BODY,
        ],
    ),
    PokemonGen3.CLAMPERL: Pokemon(
        name=PokemonGen3.CLAMPERL,
        gen=3,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.GOREBYSS, evolution_type=EvolutionType.TRADE, item=Item.DEEP_SEA_SCALE, should_hold=True, level=8),
            Evolution(name=PokemonGen3.HUNTAIL, evolution_type=EvolutionType.TRADE, item=Item.DEEP_SEA_TOOTH, should_hold=True, level=8),
        ],
        colors=[Colors.BLUE, Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=64,
            defence=85,
            special_attack=74,
            special_defence=55,
        ),
        categories=[
            Categories.ITEM,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.SHELL_ARMOR,
        ],
    ),
    PokemonGen3.HUNTAIL: Pokemon(
        name=PokemonGen3.HUNTAIL,
        gen=3,
        types=[Types.WATER],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=104,
            defence=105,
            special_attack=94,
            special_defence=75,
        ),
        categories=[
            Categories.WATERMON,
            Categories.SNAKE,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.SWIFT_SWIM,
        ],
    ),
    PokemonGen3.GOREBYSS: Pokemon(
        name=PokemonGen3.GOREBYSS,
        gen=3,
        types=[Types.WATER],
        evolves_to=[],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=84,
            defence=105,
            special_attack=114,
            special_defence=75,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.SWIFT_SWIM,
        ],
    ),
    PokemonGen3.RELICANTH: Pokemon(
        name=PokemonGen3.RELICANTH,
        gen=3,
        types=[Types.WATER, Types.ROCK],
        evolves_to=[],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=130,
            special_attack=45,
            special_defence=65,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.FISH,
            Categories.WATERMON,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.SWIFT_SWIM,
            Abilities.ROCK_HEAD,
        ],
    ),
    PokemonGen3.LUVDISC: Pokemon(
        name=PokemonGen3.LUVDISC,
        gen=3,
        types=[Types.WATER],
        evolves_to=[],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=55,
            special_attack=40,
            special_defence=65,
        ),
        categories=[
            Categories.FOOD,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.SWIFT_SWIM,
        ],
    ),
    PokemonGen3.BAGON: Pokemon(
        name=PokemonGen3.BAGON,
        gen=3,
        types=[Types.DRAGON],
        evolves_to=[
            Evolution(name=PokemonGen3.SHELGON),
        ],
        colors=[Colors.BLUE, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=60,
            special_attack=40,
            special_defence=30,
        ),
        categories=[
            Categories.DRAGON,
            Categories.FANTASY,
            Categories.PREHISTORIC,
            Categories.REPTILE,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.ROCK_HEAD,
        ],
    ),
    PokemonGen3.SHELGON: Pokemon(
        name=PokemonGen3.SHELGON,
        gen=3,
        types=[Types.DRAGON],
        evolves_to=[
            Evolution(name=PokemonGen3.SALAMENCE),
        ],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=100,
            special_attack=60,
            special_defence=50,
        ),
        categories=[
            Categories.FANTASY,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.ROCK_HEAD,
        ],
    ),
    PokemonGen3.SALAMENCE: Pokemon(
        name=PokemonGen3.SALAMENCE,
        gen=3,
        types=[Types.DRAGON, Types.FLYING],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=135,
            defence=80,
            special_attack=110,
            special_defence=80,
        ),
        categories=[
            Categories.DRAGON,
            Categories.FANTASY,
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WING,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.INTIMIDATE,
        ],
    ),
    PokemonGen3.BELDUM: Pokemon(
        name=PokemonGen3.BELDUM,
        gen=3,
        types=[Types.STEEL, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.METANG),
        ],
        colors=[Colors.BLUE, Colors.GRAY],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=55,
            defence=80,
            special_attack=35,
            special_defence=60,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.CLEAR_BODY,
        ],
    ),
    PokemonGen3.METANG: Pokemon(
        name=PokemonGen3.METANG,
        gen=3,
        types=[Types.STEEL, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.METAGROSS),
        ],
        colors=[Colors.BLUE, Colors.GRAY],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=75,
            defence=100,
            special_attack=55,
            special_defence=80,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.CLEAR_BODY,
        ],
    ),
    PokemonGen3.METAGROSS: Pokemon(
        name=PokemonGen3.METAGROSS,
        gen=3,
        types=[Types.STEEL, Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.GRAY],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=135,
            defence=130,
            special_attack=95,
            special_defence=90,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=4,
        supported_abilities=[
            Abilities.CLEAR_BODY,
        ],
    ),
    PokemonGen3.REGIROCK: Pokemon(
        name=PokemonGen3.REGIROCK,
        gen=3,
        types=[Types.ROCK],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.BROWN],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=100,
            defence=200,
            special_attack=50,
            special_defence=100,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.CLEAR_BODY,
        ],
    ),
    PokemonGen3.REGICE: Pokemon(
        name=PokemonGen3.REGICE,
        gen=3,
        types=[Types.ICE],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=50,
            defence=100,
            special_attack=100,
            special_defence=200,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.CLEAR_BODY,
        ],
    ),
    PokemonGen3.REGISTEEL: Pokemon(
        name=PokemonGen3.REGISTEEL,
        gen=3,
        types=[Types.STEEL],
        evolves_to=[],
        colors=[Colors.GRAY],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=75,
            defence=150,
            special_attack=75,
            special_defence=150,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.CLEAR_BODY,
        ],
    ),
    PokemonGen3.LATIAS: Pokemon(
        name=PokemonGen3.LATIAS,
        gen=3,
        types=[Types.DRAGON, Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.PINK, Colors.WHITE],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=90,
            special_attack=110,
            special_defence=130,
        ),
        categories=[
            Categories.ITEM,
            Categories.WING,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.LEVITATE,
        ],
    ),
    PokemonGen3.LATIOS: Pokemon(
        name=PokemonGen3.LATIOS,
        gen=3,
        types=[Types.DRAGON, Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE],
        stats=Stats(
            attack=90,
            defence=80,
            special_attack=130,
            special_defence=110,
        ),
        categories=[
            Categories.ITEM,
            Categories.WING,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.LEVITATE,
        ],
    ),
    PokemonGen3.KYOGRE: Pokemon(
        name=PokemonGen3.KYOGRE,
        gen=3,
        types=[Types.WATER],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=100,
            defence=90,
            special_attack=150,
            special_defence=140,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.DRIZZLE,
        ],
    ),
    PokemonGen3.GROUDON: Pokemon(
        name=PokemonGen3.GROUDON,
        gen=3,
        types=[Types.GROUND],
        evolves_to=[],
        colors=[Colors.RED, Colors.BROWN],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=150,
            defence=140,
            special_attack=100,
            special_defence=90,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.FANTASY,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.DROUGHT,
        ],
    ),
    PokemonGen3.RAYQUAZA: Pokemon(
        name=PokemonGen3.RAYQUAZA,
        gen=3,
        types=[Types.DRAGON, Types.FLYING],
        evolves_to=[],
        colors=[Colors.GREEN],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=150,
            defence=90,
            special_attack=150,
            special_defence=90,
        ),
        categories=[
            Categories.REPTILE,
            Categories.FANTASY,
            Categories.SNAKE,
            Categories.DRAGON,
        ],
        num_legs=0,
        supported_abilities=[
            Abilities.AIR_LOCK,
        ],
    ),
    PokemonGen3.JIRACHI: Pokemon(
        name=PokemonGen3.JIRACHI,
        gen=3,
        types=[Types.STEEL, Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.YELLOW, Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=100,
            defence=100,
            special_attack=100,
            special_defence=100,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
            Categories.FANTASY,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.SERENE_GRACE,
        ],
    ),
    PokemonGen3.DEOXYS: Pokemon(
        name=PokemonGen3.DEOXYS,
        gen=3,
        types=[Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.RED, Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=150,
             defence=50,
            special_attack=150,
            special_defence=50,
        ),
        categories=[
            Categories.ITEM,
            Categories.FANTASY,
        ],
        num_legs=2,
        supported_abilities=[
            Abilities.PRESSURE,
        ],
    ),
}

NAME_TO_POKEMON.update(_GEN3_POKEMONS)
