"""
Pokemon abilities definitions and related functionality.

Abilities are special traits that provide various effects in battle. Each Pokemon can have one or two abilities,
with some abilities being hidden abilities that are harder to obtain.
"""
from typing import List, Optional
from pokemendel_core.utils.enum_list import EnumList


class Abilities(EnumList):
    """All Pokemon abilities from Generations 1, 2, and 3."""
    
    # Generation 1 Abilities (introduced in Gen 3)
    STENCH = "Stench"
    NEUTRALIZING_GAS = "Neutralizing Gas"
    DRIZZLE = "Drizzle"
    SPEED_BOOST = "Speed Boost"
    BATTLE_ARMOR = "Battle Armor"
    STURDY = "Sturdy"
    DAMP = "Damp"
    LIMBER = "Limber"
    SAND_VEIL = "Sand Veil"
    STATIC = "Static"
    VOLT_ABSORB = "Volt Absorb"
    WATER_ABSORB = "Water Absorb"
    OBLIVIOUS = "Oblivious"
    CLOUD_NINE = "Cloud Nine"
    COMPOUND_EYES = "Compound Eyes"
    COMPETITIVE = "Competitive"
    INSOMNIA = "Insomnia"
    COLOR_CHANGE = "Color Change"
    IMMUNITY = "Immunity"
    WIND_RIDER = "Wind Rider"
    FLASH_FIRE = "Flash Fire"
    SHIELD_DUST = "Shield Dust"
    OWN_TEMPO = "Own Tempo"
    SUCTION_CUPS = "Suction Cups"
    INTIMIDATE = "Intimidate"
    SHADOW_TAG = "Shadow Tag"
    ROUGH_SKIN = "Rough Skin"
    WONDER_GUARD = "Wonder Guard"
    LEVITATE = "Levitate"
    EFFECT_SPORE = "Effect Spore"
    SYNCHRONIZE = "Synchronize"
    CLEAR_BODY = "Clear Body"
    NATURAL_CURE = "Natural Cure"
    LIGHTNING_ROD = "Lightning Rod"
    SERENE_GRACE = "Serene Grace"
    SWIFT_SWIM = "Swift Swim"
    CHLOROPHYLL = "Chlorophyll"
    ILLUMINATE = "Illuminate"
    TRACE = "Trace"
    HUGE_POWER = "Huge Power"
    POISON_POINT = "Poison Point"
    INNER_FOCUS = "Inner Focus"
    MAGMA_ARMOR = "Magma Armor"
    WATER_VEIL = "Water Veil"
    MAGNET_PULL = "Magnet Pull"
    SOUNDPROOF = "Soundproof"
    RAIN_DISH = "Rain Dish"
    SAND_STREAM = "Sand Stream"
    PRESSURE = "Pressure"
    THICK_FAT = "Thick Fat"
    EARLY_BIRD = "Early Bird"
    FLAME_BODY = "Flame Body"
    RUN_AWAY = "Run Away"
    KEEN_EYE = "Keen Eye"
    HYPER_CUTTER = "Hyper Cutter"
    PICKUP = "Pickup"
    TRUANT = "Truant"
    HUSTLE = "Hustle"
    CUTE_CHARM = "Cute Charm"
    PLUS = "Plus"
    MINUS = "Minus"
    FORECAST = "Forecast"
    STICKY_HOLD = "Sticky Hold"
    SHED_SKIN = "Shed Skin"
    GUTS = "Guts"
    MARVEL_SCALE = "Marvel Scale"
    LIQUID_OOZE = "Liquid Ooze"
    OVERGROW = "Overgrow"
    BLAZE = "Blaze"
    TORRENT = "Torrent"
    SWARM = "Swarm"
    ROCK_HEAD = "Rock Head"
    DROUGHT = "Drought"
    ARENA_TRAP = "Arena Trap"
    VITAL_SPIRIT = "Vital Spirit"
    WHITE_SMOKE = "White Smoke"
    PURE_POWER = "Pure Power"
    SHELL_ARMOR = "Shell Armor"
    AIR_LOCK = "Air Lock"
    
    # Generation 2 Abilities (introduced in Gen 3)
    TANGLED_FEET = "Tangled Feet"
    MOTOR_DRIVE = "Motor Drive"
    RIVALRY = "Rivalry"
    STEADFAST = "Steadfast"
    SNOW_CLOAK = "Snow Cloak"
    GLUTTONY = "Gluttony"
    ANGER_POINT = "Anger Point"
    UNBURDEN = "Unburden"
    HEATPROOF = "Heatproof"
    SIMPLE = "Simple"
    DRY_SKIN = "Dry Skin"
    DOWNLOAD = "Download"
    IRON_FIST = "Iron Fist"
    POISON_HEAL = "Poison Heal"
    ADAPTABILITY = "Adaptability"
    SKILL_LINK = "Skill Link"
    HYDRATION = "Hydration"
    SOLAR_POWER = "Solar Power"
    QUICK_FEET = "Quick Feet"
    NORMALIZE = "Normalize"
    SNIPER = "Sniper"
    MAGIC_GUARD = "Magic Guard"
    NO_GUARD = "No Guard"
    STALL = "Stall"
    TECHNICIAN = "Technician"
    LEAF_GUARD = "Leaf Guard"
    KLUTZ = "Klutz"
    MOLD_BREAKER = "Mold Breaker"
    SUPER_LUCK = "Super Luck"
    AFTERMATH = "Aftermath"
    ANTICIPATION = "Anticipation"
    FOREWARN = "Forewarn"
    UNAWARE = "Unaware"
    TINTED_LENS = "Tinted Lens"
    FILTER = "Filter"
    SLOW_START = "Slow Start"
    SCRAPPY = "Scrappy"
    STORM_DRAIN = "Storm Drain"
    ICE_BODY = "Ice Body"
    SOLID_ROCK = "Solid Rock"
    SNOW_WARNING = "Snow Warning"
    HONEY_GATHER = "Honey Gather"
    FRISK = "Frisk"
    RECKLESS = "Reckless"
    MULTITYPE = "Multitype"
    FLOWER_GIFT = "Flower Gift"
    BAD_DREAMS = "Bad Dreams"
    
    # Generation 3 Abilities
    PICKPOCKET = "Pickpocket"
    SHEER_FORCE = "Sheer Force"
    CONTRARY = "Contrary"
    UNNERVE = "Unnerve"
    DEFIANT = "Defiant"
    DEFEATIST = "Defeatist"
    CURSED_BODY = "Cursed Body"
    HEALER = "Healer"
    FRIEND_GUARD = "Friend Guard"
    WEAK_ARMOR = "Weak Armor"
    HEAVY_METAL = "Heavy Metal"
    LIGHT_METAL = "Light Metal"
    MULTISCALE = "Multiscale"
    TOXIC_BOOST = "Toxic Boost"
    FLARE_BOOST = "Flare Boost"
    HARVEST = "Harvest"
    TELEPATHY = "Telepathy"
    MOODY = "Moody"
    OVERCOAT = "Overcoat"
    POISON_TOUCH = "Poison Touch"
    REGENERATOR = "Regenerator"
    BIG_PECKS = "Big Pecks"
    SAND_RUSH = "Sand Rush"
    WONDER_SKIN = "Wonder Skin"
    ANALYTIC = "Analytic"
    ILLUSION = "Illusion"
    IMPOSTER = "Imposter"
    INFILTRATOR = "Infiltrator"
    MUMMY = "Mummy"
    MOXIE = "Moxie"
    JUSTIFIED = "Justified"
    RATTLED = "Rattled"
    MAGIC_BOUNCE = "Magic Bounce"
    SAP_SIPPER = "Sap Sipper"
    PRANKSTER = "Prankster"
    SAND_FORCE = "Powers up Ground, Rock, and Steel moves in sandstorms."
    IRON_BARBS = "Damages opponents on contact."
    ZEN_MODE = "Changes form when HP is below 50%."
    VICTORY_STAR = "Victory Star"
    TURBOBLAZE = "Turboblaze"
    TERAVOLT = "Teravolt"


class InvalidAbilityError(ValueError):
    """Raised when an invalid ability string is provided."""
    pass


def from_str(ability_str: str) -> str:
    """Convert a string to an ability value.
    
    Args:
        ability_str: String representation of the ability
        
    Returns:
        Ability string value
        
    Raises:
        InvalidAbilityError: If the string doesn't match any ability
    """
    if not isinstance(ability_str, str):
        raise InvalidAbilityError(f"Ability must be a string, got {type(ability_str).__name__}")
    
    valid_abilities = Abilities.list_all()
    if ability_str not in valid_abilities:
        raise InvalidAbilityError(f"Invalid ability '{ability_str}'. Valid abilities: {valid_abilities}")
    
    return ability_str


def get_ability_description(ability: str) -> str:
    """Get a description of what an ability does.
    
    Args:
        ability: The ability name
        
    Returns:
        Description of the ability's effect
    """
    descriptions = {
        # Generation 1 abilities
        Abilities.STENCH: "May cause the target to flinch when hit by a move.",
        Abilities.NEUTRALIZING_GAS: "Neutralizes abilities of all Pokémon in battle.",
        Abilities.DRIZZLE: "Summons rain when the Pokémon enters battle.",
        Abilities.SPEED_BOOST: "Speed increases by one stage each turn.",
        Abilities.BATTLE_ARMOR: "Prevents critical hits.",
        Abilities.STURDY: "Cannot be knocked out by a single hit if at full HP.",
        Abilities.DAMP: "Prevents self-destruct and explosion moves.",
        Abilities.LIMBER: "Cannot be paralyzed.",
        Abilities.SAND_VEIL: "Evasion increases in sandstorms.",
        Abilities.STATIC: "May paralyze opponents on contact.",
        Abilities.VOLT_ABSORB: "Heals HP when hit by Electric-type moves.",
        Abilities.WATER_ABSORB: "Heals HP when hit by Water-type moves.",
        Abilities.OBLIVIOUS: "Cannot be infatuated or taunted.",
        Abilities.CLOUD_NINE: "Negates weather effects.",
        Abilities.COMPOUND_EYES: "Increases accuracy of moves.",
        Abilities.COMPETITIVE: "aises the ability-bearer's Special Attack by two stages when hit by a stat-lowering move.",
        Abilities.INSOMNIA: "Cannot fall asleep.",
        Abilities.COLOR_CHANGE: "Changes type to match the last move used against it.",
        Abilities.IMMUNITY: "Cannot be poisoned.",
        Abilities.FLASH_FIRE: "Powers up Fire-type moves when hit by one.",
        Abilities.SHIELD_DUST: "Prevents additional effects of moves.",
        Abilities.OWN_TEMPO: "Cannot be confused.",
        Abilities.SUCTION_CUPS: "Cannot be forced to switch out.",
        Abilities.INTIMIDATE: "Lowers opponent's Attack when entering battle.",
        Abilities.SHADOW_TAG: "Prevents opponents from switching out.",
        Abilities.ROUGH_SKIN: "Damages opponents on contact.",
        Abilities.WONDER_GUARD: "Only super effective moves can hit.",
        Abilities.LEVITATE: "Immune to Ground-type moves.",
        Abilities.EFFECT_SPORE: "May poison, paralyze, or put to sleep on contact.",
        Abilities.SYNCHRONIZE: "Passes status conditions to the opponent.",
        Abilities.CLEAR_BODY: "Cannot have stats lowered.",
        Abilities.NATURAL_CURE: "Status conditions are cured when switching out.",
        Abilities.LIGHTNING_ROD: "Draws in Electric-type moves and raises Special Attack.",
        Abilities.SERENE_GRACE: "Doubles the chance of additional effects.",
        Abilities.SWIFT_SWIM: "Speed doubles in rain.",
        Abilities.CHLOROPHYLL: "Speed doubles in harsh sunlight.",
        Abilities.ILLUMINATE: "Increases encounter rate with wild Pokémon.",
        Abilities.TRACE: "Copies the opponent's ability.",
        Abilities.HUGE_POWER: "Doubles Attack stat.",
        Abilities.POISON_POINT: "May poison opponents on contact.",
        Abilities.INNER_FOCUS: "Cannot flinch.",
        Abilities.MAGMA_ARMOR: "Cannot be frozen.",
        Abilities.WATER_VEIL: "Cannot be burned.",
        Abilities.MAGNET_PULL: "Prevents Steel-type Pokémon from switching out.",
        Abilities.SOUNDPROOF: "Immune to sound-based moves.",
        Abilities.RAIN_DISH: "Recovers HP in rain.",
        Abilities.SAND_STREAM: "Summons sandstorm when entering battle.",
        Abilities.PRESSURE: "Increases PP usage of opponent's moves.",
        Abilities.THICK_FAT: "Reduces damage from Fire and Ice moves.",
        Abilities.EARLY_BIRD: "Sleep duration is halved.",
        Abilities.FLAME_BODY: "May burn opponents on contact.",
        Abilities.RUN_AWAY: "Can always escape from wild battles.",
        Abilities.KEEN_EYE: "Cannot have accuracy lowered.",
        Abilities.HYPER_CUTTER: "Cannot have Attack lowered.",
        Abilities.PICKUP: "May pick up items after battle.",
        Abilities.TRUANT: "Attacks every other turn.",
        Abilities.HUSTLE: "Increases Attack but lowers accuracy.",
        Abilities.CUTE_CHARM: "May infatuate opponents on contact.",
        Abilities.PLUS: "Powers up moves when Plus or Minus is active.",
        Abilities.MINUS: "Powers up moves when Plus or Minus is active.",
        Abilities.FORECAST: "Changes form based on weather.",
        Abilities.STICKY_HOLD: "Cannot lose held items.",
        Abilities.SHED_SKIN: "May cure status conditions each turn.",
        Abilities.GUTS: "Increases Attack when statused.",
        Abilities.MARVEL_SCALE: "Increases Defense when statused.",
        Abilities.LIQUID_OOZE: "Damages opponents that use draining moves.",
        Abilities.OVERGROW: "Powers up Grass-type moves when HP is low.",
        Abilities.BLAZE: "Powers up Fire-type moves when HP is low.",
        Abilities.TORRENT: "Powers up Water-type moves when HP is low.",
        Abilities.SWARM: "Powers up Bug-type moves when HP is low.",
        Abilities.ROCK_HEAD: "Prevents recoil damage.",
        Abilities.DROUGHT: "Summons harsh sunlight when entering battle.",
        Abilities.ARENA_TRAP: "Prevents opponents from switching out.",
        Abilities.VITAL_SPIRIT: "Cannot fall asleep.",
        Abilities.WHITE_SMOKE: "Cannot have stats lowered.",
        Abilities.PURE_POWER: "Doubles Attack stat.",
        Abilities.SHELL_ARMOR: "Prevents critical hits.",
        Abilities.AIR_LOCK: "Negates weather effects.",
        
        # Generation 2 abilities
        Abilities.TANGLED_FEET: "Increases evasion when confused.",
        Abilities.MOTOR_DRIVE: "Raises Speed when hit by Electric moves.",
        Abilities.RIVALRY: "Powers up moves against same gender, weakens against opposite.",
        Abilities.STEADFAST: "Raises Speed when flinching.",
        Abilities.SNOW_CLOAK: "Increases evasion in hail.",
        Abilities.GLUTTONY: "Uses berries at higher HP thresholds.",
        Abilities.ANGER_POINT: "Maximizes Attack when hit by a critical hit.",
        Abilities.UNBURDEN: "Doubles Speed when held item is consumed.",
        Abilities.HEATPROOF: "Reduces damage from Fire moves and prevents burns.",
        Abilities.SIMPLE: "Doubles stat changes.",
        Abilities.DRY_SKIN: "Heals in rain, damaged by sun, absorbs Water moves.",
        Abilities.DOWNLOAD: "Raises Attack or Special Attack based on opponent's Defense.",
        Abilities.IRON_FIST: "Powers up punching moves.",
        Abilities.POISON_HEAL: "Recovers HP when poisoned.",
        Abilities.ADAPTABILITY: "Increases STAB bonus.",
        Abilities.SKILL_LINK: "Multi-hit moves always hit maximum times.",
        Abilities.HYDRATION: "Cures status conditions in rain.",
        Abilities.SOLAR_POWER: "Increases Special Attack in sun but damages each turn.",
        Abilities.QUICK_FEET: "Increases Speed when statused.",
        Abilities.NORMALIZE: "All moves become Normal-type.",
        Abilities.SNIPER: "Critical hits deal more damage.",
        Abilities.MAGIC_GUARD: "Only takes damage from attacks.",
        Abilities.NO_GUARD: "All moves hit and can be hit.",
        Abilities.STALL: "Moves last.",
        Abilities.TECHNICIAN: "Powers up weak moves.",
        Abilities.LEAF_GUARD: "Prevents status conditions in harsh sunlight.",
        Abilities.KLUTZ: "Cannot use held items.",
        Abilities.MOLD_BREAKER: "Ignores abilities that affect moves.",
        Abilities.SUPER_LUCK: "Increases critical hit ratio.",
        Abilities.AFTERMATH: "Damages opponent when knocked out by contact.",
        Abilities.ANTICIPATION: "Senses dangerous moves.",
        Abilities.FOREWARN: "Reveals opponent's most powerful move.",
        Abilities.UNAWARE: "Ignores opponent's stat changes.",
        Abilities.TINTED_LENS: "Powers up not very effective moves.",
        Abilities.FILTER: "Reduces damage from super effective moves.",
        Abilities.SLOW_START: "Halves Attack and Speed for 5 turns.",
        Abilities.SCRAPPY: "Can hit Ghost-types with Normal and Fighting moves.",
        Abilities.STORM_DRAIN: "Draws in Water moves and raises Special Attack.",
        Abilities.ICE_BODY: "Recovers HP in hail.",
        Abilities.SOLID_ROCK: "Reduces damage from super effective moves.",
        Abilities.SNOW_WARNING: "Summons hail when entering battle.",
        Abilities.HONEY_GATHER: "May pick up Honey after battle.",
        Abilities.FRISK: "Reveals opponent's held item.",
        Abilities.RECKLESS: "Powers up recoil moves.",
        Abilities.MULTITYPE: "Changes type based on held plate.",
        Abilities.FLOWER_GIFT: "Raises Attack and Special Defense in harsh sunlight.",
        Abilities.BAD_DREAMS: "Damages sleeping opponents each turn.",
        
        # Generation 3 abilities
        Abilities.WIND_RIDER: "Gives immunity to wind moves, and causes the Pokémon's Attack to increase by one stage when hit by one.",
        Abilities.PICKPOCKET: "Steals opponent's item when hit by contact move.",
        Abilities.SHEER_FORCE: "Removes additional effects for more power.",
        Abilities.CONTRARY: "Stat changes are reversed.",
        Abilities.UNNERVE: "Prevents opponents from eating berries.",
        Abilities.DEFIANT: "Raises Attack when stats are lowered.",
        Abilities.DEFEATIST: "Halves Attack and Special Attack when HP is below 50%.",
        Abilities.CURSED_BODY: "May disable opponent's move when hit.",
        Abilities.HEALER: "May cure ally's status condition.",
        Abilities.FRIEND_GUARD: "Reduces damage to allies.",
        Abilities.WEAK_ARMOR: "Raises Speed and lowers Defense when hit.",
        Abilities.HEAVY_METAL: "Doubles weight.",
        Abilities.LIGHT_METAL: "Halves weight.",
        Abilities.MULTISCALE: "Reduces damage when at full HP.",
        Abilities.TOXIC_BOOST: "Increases Attack when poisoned.",
        Abilities.FLARE_BOOST: "Increases Special Attack when burned.",
        Abilities.HARVEST: "May restore berries.",
        Abilities.TELEPATHY: "Avoids damage from allies' moves.",
        Abilities.MOODY: "Raises one stat and lowers another each turn.",
        Abilities.OVERCOAT: "Immune to powder moves and weather damage.",
        Abilities.POISON_TOUCH: "May poison opponents on contact.",
        Abilities.REGENERATOR: "Recovers HP when switching out.",
        Abilities.BIG_PECKS: "Cannot have Defense lowered.",
        Abilities.SAND_RUSH: "Doubles Speed in sandstorms.",
        Abilities.WONDER_SKIN: "Reduces accuracy of status moves.",
        Abilities.ANALYTIC: "Powers up moves when moving last.",
        Abilities.ILLUSION: "Takes the appearance of the last Pokémon in the party.",
        Abilities.IMPOSTER: "Transforms into the opponent.",
        Abilities.INFILTRATOR: "Ignores Light Screen, Reflect, and Safeguard.",
        Abilities.MUMMY: "Changes opponent's ability to Mummy on contact.",
        Abilities.MOXIE: "Raises Attack when knocking out a Pokémon.",
        Abilities.JUSTIFIED: "Raises Attack when hit by Dark moves.",
        Abilities.RATTLED: "Raises Speed when hit by Bug, Ghost, or Dark moves.",
        Abilities.MAGIC_BOUNCE: "Reflects status moves back at the user.",
        Abilities.SAP_SIPPER: "Immune to Grass moves and raises Attack when hit by them.",
        Abilities.PRANKSTER: "Gives priority to status moves.",
        Abilities.SAND_FORCE: "Powers up Ground, Rock, and Steel moves in sandstorms.",
        Abilities.IRON_BARBS: "Damages opponents on contact.",
        Abilities.ZEN_MODE: "Changes form when HP is below 50%.",
        Abilities.VICTORY_STAR: "Increases accuracy of all Pokémon in battle.",
        Abilities.TURBOBLAZE: "Ignores abilities that affect moves.",
        Abilities.TERAVOLT: "Ignores abilities that affect moves.",
    }
    
    return descriptions.get(ability, "No description available.")


def get_abilities_by_generation(gen: int) -> List[str]:
    """Get all abilities introduced in a specific generation.
    
    Args:
        gen: The generation number (1, 2, or 3)
        
    Returns:
        List of abilities introduced in that generation
    """
    gen_1_abilities = [
        Abilities.STENCH, Abilities.NEUTRALIZING_GAS, Abilities.DRIZZLE, Abilities.SPEED_BOOST, Abilities.BATTLE_ARMOR,
        Abilities.STURDY, Abilities.DAMP, Abilities.LIMBER, Abilities.SAND_VEIL,
        Abilities.STATIC, Abilities.VOLT_ABSORB, Abilities.WATER_ABSORB, Abilities.OBLIVIOUS,
        Abilities.CLOUD_NINE, Abilities.COMPOUND_EYES, Abilities.COMPETITIVE, Abilities.INSOMNIA, Abilities.COLOR_CHANGE,
        Abilities.IMMUNITY, Abilities.FLASH_FIRE, Abilities.SHIELD_DUST, Abilities.OWN_TEMPO,
        Abilities.SUCTION_CUPS, Abilities.INTIMIDATE, Abilities.SHADOW_TAG, Abilities.ROUGH_SKIN,
        Abilities.WONDER_GUARD, Abilities.LEVITATE, Abilities.EFFECT_SPORE, Abilities.SYNCHRONIZE,
        Abilities.CLEAR_BODY, Abilities.NATURAL_CURE, Abilities.LIGHTNING_ROD, Abilities.SERENE_GRACE,
        Abilities.SWIFT_SWIM, Abilities.CHLOROPHYLL, Abilities.ILLUMINATE, Abilities.TRACE,
        Abilities.HUGE_POWER, Abilities.POISON_POINT, Abilities.INNER_FOCUS, Abilities.MAGMA_ARMOR,
        Abilities.WATER_VEIL, Abilities.MAGNET_PULL, Abilities.SOUNDPROOF, Abilities.RAIN_DISH,
        Abilities.SAND_STREAM, Abilities.PRESSURE, Abilities.THICK_FAT, Abilities.EARLY_BIRD,
        Abilities.FLAME_BODY, Abilities.RUN_AWAY, Abilities.KEEN_EYE, Abilities.HYPER_CUTTER,
        Abilities.PICKUP, Abilities.TRUANT, Abilities.HUSTLE, Abilities.CUTE_CHARM,
        Abilities.PLUS, Abilities.MINUS, Abilities.FORECAST, Abilities.STICKY_HOLD,
        Abilities.SHED_SKIN, Abilities.GUTS, Abilities.MARVEL_SCALE, Abilities.LIQUID_OOZE,
        Abilities.OVERGROW, Abilities.BLAZE, Abilities.TORRENT, Abilities.SWARM,
        Abilities.ROCK_HEAD, Abilities.DROUGHT, Abilities.ARENA_TRAP, Abilities.VITAL_SPIRIT,
        Abilities.WHITE_SMOKE, Abilities.PURE_POWER, Abilities.SHELL_ARMOR, Abilities.AIR_LOCK,
    ]
    
    gen_2_abilities = [
        Abilities.TANGLED_FEET, Abilities.MOTOR_DRIVE, Abilities.RIVALRY, Abilities.STEADFAST,
        Abilities.SNOW_CLOAK, Abilities.GLUTTONY, Abilities.ANGER_POINT, Abilities.UNBURDEN,
        Abilities.HEATPROOF, Abilities.SIMPLE, Abilities.DRY_SKIN, Abilities.DOWNLOAD,
        Abilities.IRON_FIST, Abilities.POISON_HEAL, Abilities.ADAPTABILITY, Abilities.SKILL_LINK,
        Abilities.HYDRATION, Abilities.SOLAR_POWER, Abilities.QUICK_FEET, Abilities.NORMALIZE,
        Abilities.SNIPER, Abilities.MAGIC_GUARD, Abilities.NO_GUARD, Abilities.STALL,
        Abilities.TECHNICIAN, Abilities.LEAF_GUARD, Abilities.KLUTZ, Abilities.MOLD_BREAKER,
        Abilities.SUPER_LUCK, Abilities.AFTERMATH, Abilities.ANTICIPATION, Abilities.FOREWARN,
        Abilities.UNAWARE, Abilities.TINTED_LENS, Abilities.FILTER, Abilities.SLOW_START,
        Abilities.SCRAPPY, Abilities.STORM_DRAIN, Abilities.ICE_BODY, Abilities.SOLID_ROCK,
        Abilities.SNOW_WARNING, Abilities.HONEY_GATHER, Abilities.FRISK, Abilities.RECKLESS,
        Abilities.MULTITYPE, Abilities.FLOWER_GIFT, Abilities.BAD_DREAMS,
    ]
    
    gen_3_abilities = [
        Abilities.PICKPOCKET, Abilities.SHEER_FORCE, Abilities.CONTRARY, Abilities.UNNERVE,
        Abilities.DEFIANT, Abilities.DEFEATIST, Abilities.CURSED_BODY, Abilities.HEALER,
        Abilities.FRIEND_GUARD, Abilities.WEAK_ARMOR, Abilities.HEAVY_METAL, Abilities.LIGHT_METAL,
        Abilities.MULTISCALE, Abilities.TOXIC_BOOST, Abilities.FLARE_BOOST, Abilities.HARVEST,
        Abilities.TELEPATHY, Abilities.MOODY, Abilities.OVERCOAT, Abilities.POISON_TOUCH,
        Abilities.REGENERATOR, Abilities.BIG_PECKS, Abilities.SAND_RUSH, Abilities.WONDER_SKIN,
        Abilities.ANALYTIC, Abilities.ILLUSION, Abilities.IMPOSTER, Abilities.INFILTRATOR,
        Abilities.MUMMY, Abilities.MOXIE, Abilities.JUSTIFIED, Abilities.RATTLED,
        Abilities.MAGIC_BOUNCE, Abilities.SAP_SIPPER, Abilities.PRANKSTER, Abilities.SAND_FORCE,
        Abilities.IRON_BARBS, Abilities.ZEN_MODE, Abilities.VICTORY_STAR, Abilities.TURBOBLAZE,
        Abilities.TERAVOLT,
    ]
    
    if gen == 1:
        return gen_1_abilities
    elif gen == 2:
        return gen_2_abilities
    elif gen == 3:
        return gen_3_abilities
    else:
        raise ValueError(f"Invalid generation {gen}. Must be 1, 2, or 3.")


def get_weather_abilities() -> List[str]:
    """Get all abilities that affect weather.
    
    Returns:
        List of weather-affecting abilities
    """
    return [
        Abilities.DRIZZLE,
        Abilities.DROUGHT,
        Abilities.SAND_STREAM,
        Abilities.SNOW_WARNING,
    ]


def get_contact_abilities() -> List[str]:
    """Get all abilities that activate on contact.
    
    Returns:
        List of contact-activated abilities
    """
    return [
        Abilities.STATIC,
        Abilities.POISON_POINT,
        Abilities.FLAME_BODY,
        Abilities.EFFECT_SPORE,
        Abilities.ROUGH_SKIN,
        Abilities.IRON_BARBS,
        Abilities.CUTE_CHARM,
        Abilities.POISON_TOUCH,
        Abilities.MUMMY,
        Abilities.PICKPOCKET,
    ]


def get_immunity_abilities() -> List[str]:
    """Get all abilities that provide immunities.
    
    Returns:
        List of immunity-providing abilities
    """
    return [
        Abilities.VOLT_ABSORB,
        Abilities.WATER_ABSORB,
        Abilities.FLASH_FIRE,
        Abilities.LEVITATE,
        Abilities.SOUNDPROOF,
        Abilities.STORM_DRAIN,
        Abilities.SAP_SIPPER,
        Abilities.LIGHTNING_ROD,
    ]
