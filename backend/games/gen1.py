from definitions import Game, GymTrainer, TrainerPokemon, EliteTrainer
from pokemendel_core.utils.definitions import Regions, Types
from pokemendel_core.data import fetch_pokemon
from dataclasses import dataclass


@dataclass
class _BaseGame(Game):
    def __init__(self, **kwargs):
        assert 'name' in kwargs
        for override_field, default_value in [
            ('gen', 1),
            ('region', Regions.KANTO),
            ('gyms', [GymTrainer(
            leader="Brock",
            type=Types.ROCK,
            pokemons=[
                TrainerPokemon("Geodude", 12),
                TrainerPokemon("Onix", 14),
            ],
            location="Pewter City",
            badge="Boulder Badge"
        ),
        GymTrainer(
            leader="Misty",
            type=Types.WATER,
            pokemons=[
                TrainerPokemon("Staryu", 18),
                TrainerPokemon("Starmie", 21),
            ],
            location="Cerulean City",
            badge="Cascade Badge"
        ),
        GymTrainer(
            leader="Lt. Surge",
            type=Types.ELECTRIC,
            pokemons=[
                TrainerPokemon("Voltorb", 21),
                TrainerPokemon("Pikachu", 18),
                TrainerPokemon("Raichu", 24),
            ],
            location="Vermillion City",
            badge="Thunder Badge"
        ),
        GymTrainer(
            leader="Erika",
            type=Types.GRASS,
            pokemons=[
                TrainerPokemon("Victreebel", 29),
                TrainerPokemon("Tangela", 24),
                TrainerPokemon("Vileplume", 29),
            ],
            location="Celadon City",
            badge="Rainbow Badge"
        ),
        GymTrainer(
            leader="Koga",
            type=Types.POISON,
            pokemons=[
                TrainerPokemon("Koffing", 37),
                TrainerPokemon("Muk", 39),
                TrainerPokemon("Koffing", 37),
                TrainerPokemon("Weezing", 43),
            ],
            location="Fuchsia City",
            badge="Soul Badge"
        ),
        GymTrainer(
            leader="Sabrina",
            type=Types.PSYCHIC,
            pokemons=[
                TrainerPokemon("Kadabra", 38),
                TrainerPokemon("Mr. Mime", 37),
                TrainerPokemon("Venomoth", 38),
                TrainerPokemon("Alakazam", 43),
            ],
            location="Saffron City",
            badge="Marsh Badge"
        ),
        GymTrainer(
            leader="Blaine",
            type=Types.FIRE,
            pokemons=[
                TrainerPokemon("Growlithe", 42),
                TrainerPokemon("Ponyta", 40),
                TrainerPokemon("Rapidash", 42),
                TrainerPokemon("Arcanine", 47),
            ],
            location="Cinnabar Island",
            badge="Volcano Badge"
        ),
        GymTrainer(
            leader="Giovanni",
            type=Types.GROUND,
            pokemons=[
                TrainerPokemon("Rhyhorn", 45),
                TrainerPokemon("Dugtrio", 42),
                TrainerPokemon("Nidoqueen", 44),
                TrainerPokemon("Nidoking", 45),
                TrainerPokemon("Rhydon", 50),
            ],
            location="Viridian City",
            badge="Earth Badge"
        )]),
            ('elite4', [
        EliteTrainer(
            leader="Lorelei", type=Types.ICE, pokemons=[
                TrainerPokemon("Dewgong", 54),
                TrainerPokemon("Cloyster", 53),
                TrainerPokemon("Slowbro", 54),
                TrainerPokemon("Jynx", 56),
                TrainerPokemon("Lapras", 56),
            ]
        ),
        EliteTrainer(
            leader="Bruno", type=Types.FIGHTING, pokemons=[
                TrainerPokemon("Onix", 53),
                TrainerPokemon("Hitmonchan", 55),
                TrainerPokemon("Hitmonlee", 55),
                TrainerPokemon("Onix", 56),
                TrainerPokemon("Machamp", 58),
            ]
        ),
        EliteTrainer(
            leader="Agatha", type=Types.POISON, pokemons=[
                TrainerPokemon("Gengar", 56),
                TrainerPokemon("Golbat", 56),
                TrainerPokemon("Haunter", 55),
                TrainerPokemon("Arbok", 58),
                TrainerPokemon("Gengar", 60),
            ]
        ),
        EliteTrainer(
            leader="Lance", type=Types.DRAGON, pokemons=[
                TrainerPokemon("Gyarados", 58),
                TrainerPokemon("Dragonair", 56),
                TrainerPokemon("Dragonair", 56),
                TrainerPokemon("Aerodactyl", 60),
                TrainerPokemon("Dragonite", 62),
            ]
        ),
    ]),
            ('routes', [
        "Pallet Town",
        "Viridian City",
        "Viridian Forest",
        "Pewter City",
        "Mt. Moon",
        "Cerulean City",
        "Vermillion City",
        "Diglet's Cave",
        "Rock Tunnel",
        "Lavender Town",
        "Pokemon Tower",
        "Celadon City",
        "Saffron City",
        "Fuchsia City",
        "Safari Zone",
        "Seaform Island",
        "Cinnabar Island",
        "Pokemon Mansion",
        "Power Plant",
        "Victory Road",
        "Route 1",
        "Route 2",
        "Route 3",
        "Route 4",
        "Route 5",
        "Route 6",
        "Route 7",
        "Route 8",
        "Route 9",
        "Route 10",
        "Route 11",
        "Route 12",
        "Route 13",
        "Route 14",
        "Route 15",
        "Route 16",
        "Route 17",
        "Route 18",
        "Route 19",
        "Route 20",
        "Route 21",
        "Route 22",
        "Route 23",
        "Route 24",
        "Route 25",
    ]),
            ('starters', [
        fetch_pokemon("Bulbasaur", 1),
        fetch_pokemon("Charmander", 1),
        fetch_pokemon("Squirtle", 1),
    ]),
            ('important_battles', [
        "Route 22 - Rival (9)",
        "Pewter City - GymTrainer (14)",
        "Nugget Bridge - Rival (18)",
        "SS Anne - Rival (20)",
        "Cerulean City - GymTrainer (21)",
        "Vermillion City - GymTrainer (24)",
        "Pokemon Tower - Rival (25)",
        "Game Corner - Boss (29)",
        "Celadon City - GymTrainer (29)",
        "Silph Co - Rival (40)",
        "Silph Co - Boss (41)",
        "Saffron City - GymTrainer (43)",
        "Fuchia City - GymTrainer (43)",
        "Cinnabar Island - GymTrainer (47)",
        "Viridian City - GymTrainer (50)",
        "Route 22 - Rival (53)",
    ]),
        ]:
            kwargs[override_field] = kwargs.get(override_field, default_value)
        super().__init__(**kwargs)


BLUE = _BaseGame(
    name="Blue",
    encounters={
        "Pallet Town": {"Poliwag", "Tentacool", "Goldeen", "Magikarp", "Tangela"},
        "Viridian City": {"Poliwag", "Tentacool", "Goldeen", "Magikarp"},
        "Viridian Forest": {"Caterpie", "Metapod", "Weedle", "Kakuna", "Pikachu"},
        "Pewter City": {"Aerodactyl"},
        "Mt. Moon": {"Zubat", "Clefairy", "Paras", "Geodude", "Omanyte", "Kabuto"},
        "Cerulean City": {"Jynx"},
        "Vermillion City": {"Shellder", "Krabby", "Poliwag", "Goldeen", "Magikarp", "Farfetchd"},
        "Diglet's Cave": {"Diglett", "Dugtrio"},
        "Rock Tunnel": {"Zubat", "Geodude", "Onix", "Machop"},
        "Pokemon Tower": {"Gastly", "Cubone", "Haunter"},
        "Celadon City": {"Poliwhirl", "Slowpoke", "Poliwag", "Goldeen", "Magikarp", "Eevee", "Nidorino", "Clefairy", "Abra", "Pinsir", "Porygon", "Dratini"},
        "Saffron City": {"Hitmonlee", "Hitmonchan", "Lapras"},
        "Fuchsia City": {"Krabby", "Goldeen", "Seaking", "Magikarp", "Poliwag"},
        "Safari Zone": {"Nidoran Male", "Exeggcute", "Venonat", "Rhyhorn", "Nidorina", "Nidorino", "Parasect", "Pinsir", "Chansey", "Psyduck", "Slowpoke", "Krabby", "Dratini", "Poliwag", "Goldeen", "Magikarp", "Nidoran Female", "Paras", "Doduo", "Kangaskhan", "Venomoth", "Tauros", "Venonat"},
        "Seaform Island": {"Seel", "Krabby", "Staryu", "Psyduck", "Zubat", "Golbat", "Slowpoke", "Slowbro", "Shellder", "Dewgong", "Kingler", "Golduck", "Horsea", "Poliwag", "Goldeen", "Magikarp", "Articuno"},
        "Cinnabar Island": {"Aerodactyl", "Omanyte", "Kabuto", "Seel", "Electrode", "Tangela"},
        "Pokemon Mansion": {"Ponyta", "Grimer", "Muk", "Koffing", "Weezing", "Vulpix", "Magmar"},
        "Power Plant": {"Pikachu", "Magnemite", "Voltorb", "Raichu", "Magneton", "Zapdos"},
        "Victory Road": {"Onix", "Machop", "Zubat", "Geodude", "Golbat", "Graveler", "Machoke", "Marowak", "Moltres", "Venomoth"},
        "Route 1": {"Pidgey", "Rattata"},
        "Route 2": {"Pidgey", "Rattata", "Caterpie"},
        "Route 3": {"Pidgey", "Spearow", "Jigglypuff"},
        "Route 4": {"Rattata", "Spearow", "Sandshrew", "Magikarp"},
        "Route 5": {"Pidgey", "Meowth", "Bellsprout", "Nidoran Female"},
        "Route 6": {"Pidgey", "Meowth", "Bellsprout", "Shellder", "Krabby", "Poliwag", "Goldeen", "Magikarp"},
        "Route 7": {"Pidgey", "Meowth", "Bellsprout", "Vulpix"},
        "Route 8": {"Pidgey", "Meowth", "Sandshrew", "Vulpix"},
        "Route 9": {"Rattata", "Spearow", "Sandshrew"},
        "Route 10": {"Spearow", "Sandshrew", "Voltorb", "Poliwhirl", "Slowpoke", "Poliwag", "Goldeen", "Magikarp"},
        "Route 11": {"Spearow", "Sandshrew", "Drowzee", "Shellder", "Krabby", "Poliwag", "Goldeen", "Magikarp", "Nidorina"},
        "Route 12": {"Pidgey", "Bellsprout", "Weepinbell", "Venonat", "Tentacool", "Krabby", "Goldeen", "Magikarp", "Poliwag", "Snorlax"},
        "Route 13": {"Pidgey", "Bellsprout", "Weepinbell", "Ditto", "Venonat", "Tentacool", "Krabby", "Goldeen", "Magikarp", "Poliwag"},
        "Route 14": {"Venonat", "Bellsprout", "Pidgeotto", "Weepinbell", "Pidgey", "Ditto"},
        "Route 15": {"Bellsprout", "Pidgeotto", "Weepinbell", "Pidgey", "Venonat", "Ditto"},
        "Route 16": {"Rattata", "Spearow", "Doduo", "Raticate", "Snorlax"},
        "Route 17": {"Raticate", "Spearow", "Doduo", "Fearow", "Tentacool", "Krabby", "Goldeen", "Magikarp", "Poliwag"},
        "Route 18": {"Spearow", "Doduo", "Raticate", "Fearow", "Tentacool", "Krabby", "Goldeen", "Magikarp", "Poliwag", "Lickitung"},
        "Route 19": {"Tentacool", "Shellder", "Horsea", "Goldeen", "Staryu", "Poliwag", "Magikarp"},
        "Route 20": {"Tentacool", "Shellder", "Horsea", "Goldeen", "Staryu", "Poliwag", "Magikarp"},
        "Route 21": {"Pidgey", "Rattata", "Pidgeotto", "Raticate", "Tangela", "Tentacool", "Shellder", "Horsea", "Goldeen", "Staryu", "Poliwag", "Magikarp"},
        "Route 22": {"Rattata", "Nidoran Female", "Nidoran Male", "Spearow", "Poliwag", "Goldeen", "Magikarp"},
        "Route 23": {"Fearow", "Sandshrew", "Ditto", "Sandslash", "Spearow", "Slowbro", "Kingler", "Seadra", "Seaking", "Poliwag", "Goldeen", "Magikarp"},
        "Route 24": {"Caterpie", "Bellsprout", "Metapod", "Pidgey", "Abra", "Psyduck", "Krabby", "Goldeen", "Poliwag", "Magikarp"},
        "Route 25": {"Caterpie", "Bellsprout", "Weedle", "Kakuna", "Metapod", "Pidgey", "Abra", "Psyduck", "Krabby", "Poliwag", "Goldeen", "Magikarp"},
    },
)

RED = _BaseGame(
    name="Red",
    encounters={
        "Pallet Town": {"Poliwag", "Tentacool", "Goldeen", "Magikarp"},
        "Viridian City": {"Poliwag", "Tentacool", "Goldeen", "Magikarp"},
        "Viridian Forest": {"Weedle", "Kakuna", "Caterpie", "Metapod", "Pikachu"},
        "Pewter City": {"Aerodactyl"},
        "Mt. Moon": {"Zubat", "Clefairy", "Paras", "Geodude", "Omanyte", "Kabuto"},
        "Cerulean City": {"Jynx"},
        "Vermillion City": {"Shellder", "Krabby", "Poliwag", "Goldeen", "Magikarp", "Farfetchd"},
        "Diglet's Cave": {"Diglett", "Dugtrio"},
        "Rock Tunnel": {"Zubat", "Geodude", "Onix", "Machop"},
        "Pokemon Tower": {"Gastly", "Cubone", "Haunter"},
        "Celadon City": {"Poliwhirl", "Slowpoke", "Poliwag", "Goldeen", "Magikarp", "Nidorina", "Clefairy", "Abra", "Scyther", "Porygon", "Dratini"},
        "Saffron City": {"Hitmonlee", "Hitmonchan", "Lapras"},
        "Fuchsia City": {"Krabby", "Goldeen", "Seaking", "Magikarp", "Poliwag"},
        "Safari Zone": {"Nidoran Male", "Exeggcute", "Venonat", "Rhyhorn", "Nidorina", "Nidorino", "Parasect", "Scyther", "Chansey", "Psyduck", "Slowpoke", "Krabby", "Dratini", "Poliwag", "Krabby", "Magikarp", "Paras", "Doduo", "Nidoran Female", "Kanghaskhan", "Venomoth", "Tauros", },
        "Seaform Island": {"Seel", "Horsea", "Shellder", "Slowpoke", "Zubat", "Golbat", "Psyduck", "Golduck", "Horsea", "Staryu", "Slowpoke", "Seel", "Dewgong", "Seadra", "Slowbro", "Goldeen", "Poliwag", "Magikarp", "Articuno"},
        "Cinnabar Island": {"Aerodactyl", "Omanyte", "Kabuto", "Seel", "Electrode", "Tangela"},
        "Pokemon Mansion": {"Ponyta", "Koffing", "Grimer", "Muk", "Weezing", "Growlithe"},
        "Power Plant": {"Pikachu", "Magnemite", "Voltorb", "Electabuzz", "Magneton", "Zapdos"},
        "Victory Road": {"Onix", "Machop", "Zubat", "Geodude", "Golbat", "Machoke", "Graveler", "Moltres", "Venomoth"},
        "Route 1": {"Pidgey", "Rattata"},
        "Route 2": {"Pidgey", "Rattata", "Weedle"},
        "Route 3": {"Pidgey", "Spearow", "Jigglypuff"},
        "Route 4": {"Rattata", "Spearow", "Ekans", "Magikarp"},
        "Route 5": {"Pidgey", "Oddish", "Mankey", "Nidoran Female"},
        "Route 6": {"Pidgey", "Oddish", "Mankey", "Sheldder", "Krabby", "Poliwag", "Goldeen", "Magikarp"},
        "Route 7": {"Pidgey", "Oddish", "Mankey","Growlithe"},
        "Route 8": {"Pidgey", "Mankey", "Ekans", "Growlithe"},
        "Route 9": {"Rattata", "Spearow", "Ekans"},
        "Route 10": {"Spearow", "Ekans", "Voltorb", "Poliwhirl", "Slowpoke", "Poliwag", "Goldeen", "Magikarp"},
        "Route 11": {"Spearow", "Ekans", "Drowzee", "Shellder", "Krabby", "Poliwag", "Goldeen", "Magikarp", "Nidorina"},
        "Route 12": {"Pidgey", "Oddish", "Gloom", "Venonat", "Tentacool", "Krabby", "Goldeen", "Magikarp", "Poliwag", "Snorlax"},
        "Route 13": {"Pidgey", "Oddish", "Gloom", "Ditto", "Venonat", "Tentacool", "Krabby", "Goldeen", "Maikarp", "Poliwag"},
        "Route 14": {"Oddish", "Pidgeotto", "Gloom", "Pidgey", "Venonat", "Ditto"},
        "Route 15": {"Oddish", "Pidgeotto", "Gloom", "Pidgey", "Venonat", "Ditto"},
        "Route 16": {"Rattata", "Spearow", "Doduo", "Raticate", "Snorlax"},
        "Route 17": {"Raticate", "Spearow", "Doduo", "Fearow", "Tentacool", "Krabby", "Goldeen", "Magikarp", "Poliwag"},
        "Route 18": {"Spearow", "Doduo", "Raticate", "Fearow", "Tentacool", "Krabby", "Goldeen", "Magikarp", "Poliwag", "Lickitung"},
        "Route 19": {"Tentacool", "Shellder", "Horsea", "Goldeen", "Staryu", "Poliwag", "Magikarp"},
        "Route 20": {"Tentacool", "Shellder", "Horsea", "Goldeen", "Staryu", "Poliwag", "Magikarp"},
        "Route 21": {"Pidgey", "Rattata", "Pidgeotto", "Raticate", "Tangela", "Tentacool", "Shellder", "Horsea", "Goldeen", "Staryu", "Poliwag", "Magikarp"},
        "Route 22": {"Rattata", "Nidoran Male", "Nidoran Female", "Spearow", "Poliwag", "Goldeen", "Magikarp"},
        "Route 23": {"Fearow", "Ekans", "Ditto", "Arbok", "Spearow", "Slowbro", "Kingler", "Seadra", "Seaking", "Poliwag", "Goldeen", "Magikarp"},
        "Route 24": {"Weedle", "Oddish", "Kakuna", "Pidgey", "Abra", "Psyduck", "Krabby", "Goldeen", "Poliwag", "Magikarp"},
        "Route 25": {"Weedle", "Oddish", "Caterpie", "Metapod", "Kakunah", "Pidgey", "Abra", "Psyduck", "Krabby", "Poliwag", "Goldeen", "Magikarp"},
    },
)


YELLOW = _BaseGame(
    name="Yellow",
    gyms=[
        GymTrainer(
            leader="Brock",
            type=Types.ROCK,
            pokemons=[
                TrainerPokemon("Geodude", 10),
                TrainerPokemon("Onix", 12),
            ],
            location="Pewter City",
            badge="Boulder Badge"
        ),
        GymTrainer(
            leader="Misty",
            type=Types.WATER,
            pokemons=[
                TrainerPokemon("Staryu", 18),
                TrainerPokemon("Starmie", 21),
            ],
            location="Cerulean City",
            badge="Cascade Badge"
        ),
        GymTrainer(
            leader="Lt. Surge",
            type=Types.ELECTRIC,
            pokemons=[
                TrainerPokemon("Raichu", 28),
            ],
            location="Vermillion City",
            badge="Thunder Badge"
        ),
        GymTrainer(
            leader="Erika",
            type=Types.GRASS,
            pokemons=[
                TrainerPokemon("Tangela", 30),
                TrainerPokemon("Weepinbell", 32),
                TrainerPokemon("Gloom", 32),
            ],
            location="Celadon City",
            badge="Rainbow Badge"
        ),
        GymTrainer(
            leader="Koga",
            type=Types.POISON,
            pokemons=[
                TrainerPokemon("Venonat", 44),
                TrainerPokemon("Venonat", 46),
                TrainerPokemon("Venonat", 48),
                TrainerPokemon("Venomoth", 50),
            ],
            location="Fuchsia City",
            badge="Soul Badge"
        ),
        GymTrainer(
            leader="Sabrina",
            type=Types.PSYCHIC,
            pokemons=[
                TrainerPokemon("Abra", 50),
                TrainerPokemon("Kadabra", 50),
                TrainerPokemon("Alakazam", 50),
            ],
            location="Saffron City",
            badge="Marsh Badge"
        ),
        GymTrainer(
            leader="Blaine",
            type=Types.FIRE,
            pokemons=[
                TrainerPokemon("Ninetales", 48),
                TrainerPokemon("Rapidash", 50),
                TrainerPokemon("Arcanine", 54),
            ],
            location="Cinnabar Island",
            badge="Volcano Badge"
        ),
        GymTrainer(
            leader="Giovanni",
            type=Types.GROUND,
            pokemons=[
                TrainerPokemon("Dugtrio", 50),
                TrainerPokemon("Persian", 53),
                TrainerPokemon("Nidoqueen", 53),
                TrainerPokemon("Nidoking", 55),
                TrainerPokemon("Rhydon", 55),
            ],
            location="Viridian City",
            badge="Earth Badge"
        ),
    ],
    elite4=[
        EliteTrainer(
            leader="Lorelei", type=Types.ICE, pokemons=[
                TrainerPokemon("Dewgong", 54),
                TrainerPokemon("Cloyster", 53),
                TrainerPokemon("Slowbro", 54),
                TrainerPokemon("Jynx", 56),
                TrainerPokemon("Lapras", 56),
            ]
        ),
        EliteTrainer(
            leader="Bruno", type=Types.FIGHTING, pokemons=[
                TrainerPokemon("Onix", 53),
                TrainerPokemon("Hitmonchan", 55),
                TrainerPokemon("Hitmonlee", 55),
                TrainerPokemon("Onix", 56),
                TrainerPokemon("Machamp", 58),
            ]
        ),
        EliteTrainer(
            leader="Agatha", type=Types.POISON, pokemons=[
                TrainerPokemon("Gengar", 56),
                TrainerPokemon("Golbat", 56),
                TrainerPokemon("Haunter", 55),
                TrainerPokemon("Arbok", 58),
                TrainerPokemon("Gengar", 60),
            ]
        ),
        EliteTrainer(
            leader="Lance", type=Types.DRAGON, pokemons=[
                TrainerPokemon("Gyarados", 58),
                TrainerPokemon("Dragonair", 56),
                TrainerPokemon("Dragonair", 56),
                TrainerPokemon("Aerodactyl", 60),
                TrainerPokemon("Dragonite", 62),
            ]
        ),
    ],
    routes=[
        "Pallet Town",
        "Viridian City",
        "Viridian Forest",
        "Pewter City",
        "Mt. Moon",
        "Cerulean City",
        "Vermillion City",
        "Vermillion Harbor",
        "Diglet's Cave",
        "Rock Tunnel",
        "Lavender Town",
        "Pokemon Tower",
        "Celadon City",
        "Saffron City",
        "Fuchsia City",
        "Safari Zone",
        "Seaform Island",
        "Cinnabar Island",
        "Pokemon Mansion",
        "Power Plant",
        "Victory Road",
        "Route 1",
        "Route 2",
        "Route 3",
        "Route 4",
        "Route 5",
        "Route 6",
        "Route 7",
        "Route 8",
        "Route 9",
        "Route 10",
        "Route 11",
        "Route 12",
        "Route 13",
        "Route 14",
        "Route 15",
        "Route 16",
        "Route 17",
        "Route 18",
        "Route 19",
        "Route 20",
        "Route 21",
        "Route 22",
        "Route 23",
        "Route 24",
        "Route 25",
    ],
    starters=[
        fetch_pokemon("Pikachu", 1)
    ],
    important_battles=[
        "Route 22 - Rival (9)",
        "Pewter City - GymTrainer (12)",
        "Mt. Moon - Boss (14)",
        "Nugget Bridge - Rival (18)",
        "SS Anne - Rival (20)",
        "Cerulean City - GymTrainer (21)",
        "Pokemon Tower - Rival (25)",
        "Vermillion City - GymTrainer (28)",
        "Game Corner - Boss (29)",
        "Celadon City - GymTrainer (32)",
        "Silph Co - Rival (40)",
        "Saffron City - GymTrainer (50)",
        "Fuchia City - GymTrainer (50)",
        "Route 22 - Rival (53)",
        "Cinnabar Island - GymTrainer (54)",
        "Viridian City - GymTrainer (55)",
    ],
    encounters={
        "Pallet Town": {"Staryu", "Poliwag", "Tentacool", "Goldeen", "Magikarp"},
        "Viridian City": {"Poliwag", "Goldeen", "Magikarp"},
        "Viridian Forest": {"Caterpie", "Pidgeotto", "Metapod", "Pisgey"},
        "Pewter City": {"Aerodactyl"},
        "Mt. Moon": {"Zubat", "Geodude", "Sandshrew", "Clefairy", "Paras", "Omanyte", "Kabuto"},
        "Cerulean City": {"Bulbasaur"},
        "Vermillion City": {"Tentacool", "Horsea", "Poliwag", "Goldeen", "Magikarp", "Squirtle"},
        "Vermillion Harbor": {"Staryu", "Shellder", "Tentacool", "Poliwag", "Goldeen", "Magikarp"},
        "Diglet's Cave": {"Diglett", "Dugtrio"},
        "Rock Tunnel": {"Zubat", "Geodude", "Machop", "Onix"},
        "Lavender Town": {},
        "Pokemon Tower": {"Gastly", "Haunter", "Cubone"},
        "Celadon City": {"Goldeen", "Poliwag", "Magikarp", "Eevee", "Porygon", "Vulpix", "Wigglytuff", "Abra", "Scyther", "Pinsi"},
        "Saffron City": {"Hitmonlee", "Hitmonchan"},
        "Fuchsia City": {"Magikarp", "Gyarados", "Poliwag", "Gold"},
        "Safari Zone": {"Nidoran Male", "Nidoran Female", "Parasect", "Exeggcute", "Nidorino", "Rhyhorn", "Paras", "Tangela", "Chansey", "Magikarp", "Dratini", "Dragonair", "Poliwag", "Goldeen", "Nidorina", "Cubone", "Tauros", "Marowak", "Kangashkhan", "Pinsir"},
        "Seaform Island": {"Zubat", "Krabby", "Slowpoke", "Golbat", "Seel", "Kingler", "Slowbro", "Dewgong", "Tentacool", "Staryu", "Pokiwag", "Goldeen", "Magikarp", "Articuno"},
        "Cinnabar Island": {"Aerodactyl", "Omanyte", "Kabuto", "Dewgong", "Muk", "Rhydon"},
        "Pokemon Mansion": {"Rattata", "Raticate", "Growlithe", "Grimer", "Muk", "Ditto"},
        "Power Plant": {"Magnemite", "Muk", "Magneton", "Grimer", "Voltorb", "Zapdos"},
        "Victory Road": {"Geodude", "Zubat", "Onix", "Graveler", "Golbat", "Machoke", "Moltres"},
        "Route 1": {"Rattata", "Pidgey"},
        "Route 2": {"Pidgey", "Rattata", "Nidoran Female", "Nidoran Male", "Mr. Mime"},
        "Route 3": {"Spearow", "Rattata", "Sandshrew", "Mankey"},
        "Route 4": {"Spearow", "Rattata", "Sandshrew", "Mankey", "Magikarp"},
        "Route 5": {"Pidgey", "Rattata", "Pidgeotto", "Jigglypuff", "Abra", "Machoke"},
        "Route 6": {"Pidgey", "Rattata", "Pidgeotto", "Jigglypuff", "Abra", "Psyduck", "Golduck", "Goldeen", "Poliwag", "Magikarp"},
        "Route 7": {"Pidgey", "Abra", "Pidgeotto", "Rattata", "Jigglypuff"},
        "Route 8": {"Pidgey", "Kadabra", "Pidgeotto", "Rattata", "Abra", "Jigglypuff"},
        "Route 9": {"Nidram Female", "Nidoran Male", "Raticate", "Fearow", "Nidorina", "Nidorino", "Rattata", "Spearow"},
        "Route 10": {"Magnemite", "Raticate", "Machop", "Rattata", "Nidoran Male", "Nidoran Female", "Krabby", "Kingler", "Horsea", "Poliwag", "Goldeen", "Magikarp"},
        "Route 11": {"Pidgey", "Rattata", "Raticate", "Pidgeotto", "Drowzee", "Tentacool", "Horsea", "Poliwag", "Goldeen", "Magikarp", "Dugtrio"},
        "Route 12": {"Oddish", "Bellsprout", "Golem", "Weepinbell", "Farfetch'd", "Pidgey", "Pidgeotto", "Slowpoke", "Slowbro", "Horsea", "Seadra", "Poliwag", "Goldeen", "Magikarp", "Snorlax"},
        "Route 13": {"Oddish", "Bellsprout", "Golem", "Weepinbell", "Farfetch'd", "Pidgey", "Pidgeotto", "Slowpoke", "Slowbro", "Horsea", "Tentacool", "Seadra", "Poliwag", "Goldeen", "Magikarp"},
        "Route 14": {"Oddish", "Bellsprout", "Gloom", "Weepinbell", "Venomoth", "Pidgeotto", "Venonat"},
        "Route 15": {"Oddish", "Bellsprout", "Gloom","Weepinbell", "Venomoth", "Pidgeotto", "Venonat"},
        "Route 16": {"Rattata", "Spearow", "Doduo", "Raticate", "Fearow", "Snorlax"},
        "Route 17": {"Doduo", "Dodrio", "Fearow", "Ponyta", "Tentacool", "Shellder", "Poliwag", "Goldeen", "Magikarp"},
        "Route 18": {"Rattata", "Spearow", "Doduo", "Raticate", "Fearow", "Tentacool", "Shellder", "Poliwag", "Goldeen", "Magikarp", "Parasect"},
        "Route 19": {"Tentacool", "Staryu", "Tentacruel", "Poliwag", "Goldeen", "Magikarp"},
        "Route 20": {"Tentacool", "Tentacruel", "Staryu", "Poliwag", "Goldeen", "Magikarp"},
        "Route 21": {"Pidgey", "Rattata", "Raticate", "Pidgeotto", "Tentacool", "Staryu", "Tentacruel", "Poliwag", "Goldeen", "Magikarp"},
        "Route 22": {"Nidoran Female", "Nidoran Male", "Rattata", "Spearow", "Mankey", "Poliwag", "Poliwhir", "Goldeen", "Magikarp"},
        "Route 23": {"Nidorina", "Nidorino", "Primeape", "Fearow", "Mankey", "Poliwag", "Poliwhirl", "Goldeen", "Magikarp"},
        "Route 24": {"Oddish", "Bellsprout", "Pidgey", "Pidgeotto", "Venonat", "Goldeen", "Poliwag", "Seaking", "Magikarp", "Charmander"},
        "Route 25": {"Oddish", "Bellsprout", "Pidgey", "Pidgeotto", "Venonat", "Krabby", "Kingler", "Poliwag", "Goldeen", "Magikarp"}

    },
)
