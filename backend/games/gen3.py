from definitions import Game, GymTrainer, TrainerPokemon, EliteTrainer
from pokemendel_core.utils.definitions import Regions, Types
from pokemendel_core.data import fetch_pokemon
from pokemendel_core.data.gen3 import PokemonGen3
from dataclasses import dataclass


_GENERATION = 3


@dataclass
class _BaseGame(Game):
    def __init__(self, **kwargs):
        assert 'name' in kwargs
        for override_field, default_value in [
            ('gen', _GENERATION),
            ('region', Regions.HOENN),
            ('gyms', [
        GymTrainer(
            leader="Roxanne",
            type=Types.ROCK,
            pokemons=[
                TrainerPokemon(PokemonGen3.GEODUDE, 14),
                TrainerPokemon(PokemonGen3.NOSEPASS, 15),
            ],
            location="Rustboro City",
            badge="Stone Badge"
        ),
        GymTrainer(
            leader="Brawly",
            type=Types.FIGHTING,
            pokemons=[
                TrainerPokemon(PokemonGen3.MACHOP, 17),
                TrainerPokemon(PokemonGen3.MAKUHITA, 18),
            ],
            location="Dewford Town",
            badge="Knuckle Badge"
        ),
        GymTrainer(
            leader="Wattson",
            type=Types.ELECTRIC,
            pokemons=[
                TrainerPokemon(PokemonGen3.MAGNEMITE, 22),
                TrainerPokemon(PokemonGen3.VOLTORB, 20),
                TrainerPokemon(PokemonGen3.MAGNETON, 23),
            ],
            location="Mauville City",
            badge="Dynamo Badge"
        ),
        GymTrainer(
            leader="Flannery",
            type=Types.FIRE,
            pokemons=[
                TrainerPokemon(PokemonGen3.SLUGMA, 26),
                TrainerPokemon(PokemonGen3.SLUGMA, 26),
                TrainerPokemon(PokemonGen3.TORKOAL, 28),
            ],
            location="Lavaridge City",
            badge="Heat Badge"
        ),
        GymTrainer(
            leader="Norman",
            type=Types.NORMAL,
            pokemons=[
                TrainerPokemon(PokemonGen3.SLAKING, 28),
                TrainerPokemon(PokemonGen3.VIGOROTH, 30),
                TrainerPokemon(PokemonGen3.SLAKING, 31),
            ],
            location="Petalburg City",
            badge="Balance Badge"
        ),
        GymTrainer(
            leader="Winona",
            type=Types.FLYING,
            pokemons=[
                TrainerPokemon(PokemonGen3.SWELLOW, 31),
                TrainerPokemon(PokemonGen3.PELIPPER, 30),
                TrainerPokemon(PokemonGen3.SKARMORY, 32),
                TrainerPokemon(PokemonGen3.ALTARIA, 33),
            ],
            location="Fortree Town",
            badge="Feather Badge"
        ),
        GymTrainer(
            leader="Tate & Liza",
            type=Types.PSYCHIC,
            pokemons=[
                TrainerPokemon(PokemonGen3.SOLROCK, 42),
                TrainerPokemon(PokemonGen3.LUNATONE, 42),
            ],
            location="Mossdeep City",
            badge="Mind Badge"
        ),
        GymTrainer(
            leader="Chuck",
            type=Types.FIGHTING,
            pokemons=[
                TrainerPokemon(PokemonGen3.LUVDISC, 40),
                TrainerPokemon(PokemonGen3.WHISCASH, 42),
                TrainerPokemon(PokemonGen3.SEALEO, 40),
                TrainerPokemon(PokemonGen3.SEAKING, 42),
                TrainerPokemon(PokemonGen3.MILTOIC, 43),
            ],
            location="Wallace City",
            badge="Rain Badge"
        ),
    ]),
            ('elite4', [
        EliteTrainer(
            leader="Sydney", type=Types.DARK, pokemons=[
                TrainerPokemon(PokemonGen3.MIGHTYENA, 46),
                TrainerPokemon(PokemonGen3.CACTURNE, 46),
                TrainerPokemon(PokemonGen3.SHIFTRY, 48),
                TrainerPokemon(PokemonGen3.SHARPEDO, 48),
                TrainerPokemon(PokemonGen3.ABSOL, 49),
            ]
        ),
        EliteTrainer(
            leader="Phoebe", type=Types.GHOST, pokemons=[
                TrainerPokemon(PokemonGen3.DUSCLOPS, 48),
                TrainerPokemon(PokemonGen3.BANETTE, 49),
                TrainerPokemon(PokemonGen3.BANETTE, 49),
                TrainerPokemon(PokemonGen3.SABLEYE, 50),
                TrainerPokemon(PokemonGen3.DUSCLOPS, 51),
            ]
        ),
        EliteTrainer(
            leader="Glacia", type=Types.ICE, pokemons=[
                TrainerPokemon(PokemonGen3.GLALIE, 50),
                TrainerPokemon(PokemonGen3.SEALEO, 50),
                TrainerPokemon(PokemonGen3.GLALIE, 52),
                TrainerPokemon(PokemonGen3.SEALEO, 52),
                TrainerPokemon(PokemonGen3.WALREIN, 53),
            ]
        ),
        EliteTrainer(
            leader="Drake", type=Types.DRAGON, pokemons=[
                TrainerPokemon(PokemonGen3.SHELGON, 52),
                TrainerPokemon(PokemonGen3.ALTARIA, 54),
                TrainerPokemon(PokemonGen3.FLYGON, 53),
                TrainerPokemon(PokemonGen3.FLYGON, 53),
                TrainerPokemon(PokemonGen3.SALAMENCE, 55),
            ]
        ),
        EliteTrainer(
            leader="Steven", type=Types.STEEL, pokemons=[
                TrainerPokemon(PokemonGen3.SKARMORY, 57),
                TrainerPokemon(PokemonGen3.CRADILY, 56),
                TrainerPokemon(PokemonGen3.CLAYDOL, 55),
                TrainerPokemon(PokemonGen3.ARMALDO, 56),
                TrainerPokemon(PokemonGen3.AGGRON, 56),
                TrainerPokemon(PokemonGen3.METAGROSS, 58),
            ]
        ),
    ]),
            ('routes', [
        "Route 101",
"Route 102",
"Route 103",
"Route 104",
"Route 105",
"Route 106",
"Route 107",
"Route 108",
"Route 109",
"Route 110",
"Route 111",
"Route 112",
"Route 113",
"Route 114",
"Route 115",
"Route 116",
"Route 117",
"Route 118",
"Route 119",
"Route 120",
"Route 121",
"Route 122",
"Route 123",
"Route 124",
"Route 125",
"Route 126",
"Route 127",
"Route 128",
"Route 129",
"Route 130",
"Route 131",
"Route 132",
"Route 133",
"Route 134",
"Abandoned Ship",
"Altering Cave",
"Artisan Cave",
"Battle Frontier",
"Battle Resort",
"Battle Tower",
"Birth Island",
"Cave of Origin",
"Desert Underpass",
"Dewford Town",
"Ever Grande City",
"Fallarbor Town",
"Faraway Island",
"Fiery Path",
"Fortree City",
"Granite Cave",
"Jagged Pass",
"Lavaridge Town",
"Lilycove City",
"Littleroot Town",
"Marine Cave",
"Mauville City",
"Meteor Falls",
"Mirage Island",
"Mirage Spots",
"Mirage Tower",
"Mossdeep City",
"Mt. Chimney",
"Mt. Pyre",
"New Mauville",
"Oldale Town",
"Pacifidlog Town",
"Petalburg City",
"Petalburg Woods",
"Roaming Hoenn",
"Rustboro City",
"Rusturf Tunnel",
"Safari Zone",
"Scorched Slab",
"Sea Mauville",
"Seafloor Cavern",
"Sealed Chamber",
"Shoal Cave",
"Sky Pillar",
"Slateport City",
"Sootopolis City",
"Southern Island",
"SS Tidal",
"Team Magma/Aqua Hideout",
"Terra Cave",
"Trainer Hill",
"Verdanturf Town",
"Victory Road",
    ]),
            ('starters', [
        fetch_pokemon(PokemonGen3.TREECKO, _GENERATION),
        fetch_pokemon(PokemonGen3.TORCHIC, _GENERATION),
        fetch_pokemon(PokemonGen3.MUDKIP, _GENERATION),
    ]),
            ('important_battles', [
                "Rustboro City - GymTrainer (15)",
                "Dewford Town - GymTrainer (18)",
                "Route 110 - Rival (20)",
                "Mauville City - Wally (16)",
                "Mauville City - GymTrainer (23)",
                "Mt. Chimney - Boss (25)",
                "Lavaridge City - GymTrainer (28)",
                "Petalburg City - GymTrainer (31)",
                "Weather Institute - Boss (28)"
                "Route 119 - Rival (31)",
                "Fortree Town - GymTrainer (33)",
                "Lilycove City - Rival (34)",
                "Team X Hideout - Boss (32)",
                "Mossdeep City - GymTrainer (42)",
                "Route 128 - Boss (43)",
                "Sootopolis City - GymTrainer (43)",
                "Ever Grand City - Wally (45)",
                "EliteTrainer 4  (58)",
            ]),
            ('egg_pokemons', {
                PokemonGen3.ANORITH, PokemonGen3.LILEEP,
            }),
        ]:
            kwargs[override_field] = kwargs.get(override_field, default_value)
        super().__init__(**kwargs)
