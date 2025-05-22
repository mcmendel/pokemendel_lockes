from definitions import Game, GymTrainer, TrainerPokemon, EliteTrainer
from pokemendel_core.utils.definitions import Regions, Types
from pokemendel_core.data import fetch_pokemon
from dataclasses import dataclass


@dataclass
class _BaseGame(Game):
    def __init__(self, **kwargs):
        assert 'name' in kwargs
        for override_field, default_value in [
            ('gen', 2),
            ('region', Regions.JOHTO),
            ('gyms', [
        GymTrainer(
            leader="Falkner",
            type=Types.FLYING,
            pokemons=[
                TrainerPokemon("Pidgey", 7),
                TrainerPokemon("Pidgeotto", 9),
            ],
            location="Violet City",
            badge="Zephyr Badge"
        ),
        GymTrainer(
            leader="Bugsy",
            type=Types.BUG,
            pokemons=[
                TrainerPokemon("Metapod", 14),
                TrainerPokemon("Kakuna", 14),
                TrainerPokemon("Scyther", 16),
            ],
            location="Azalea Town",
            badge="Hive Badge"
        ),
        GymTrainer(
            leader="Whitney",
            type=Types.NORMAL,
            pokemons=[
                TrainerPokemon("Clefairy", 18),
                TrainerPokemon("Miltank", 20),
            ],
            location="Goldenrod City",
            badge="Plain Badge"
        ),
        GymTrainer(
            leader="Morty",
            type=Types.GHOST,
            pokemons=[
                TrainerPokemon("Gastly", 21),
                TrainerPokemon("Haunter", 21),
                TrainerPokemon("Gengar", 25),
            ],
            location="Ecruteak City",
            badge="Fog Badge"
        ),
        GymTrainer(
            leader="Chuck",
            type=Types.FIGHTING,
            pokemons=[
                TrainerPokemon("Primeape", 27),
                TrainerPokemon("Poliwrath", 30),
            ],
            location="Cianwood City",
            badge="Storm Badge"
        ),
        GymTrainer(
            leader="Jasmine",
            type=Types.STEEL,
            pokemons=[
                TrainerPokemon("Magnemite", 30),
                TrainerPokemon("Magnemite", 30),
                TrainerPokemon("Steelix", 35),
            ],
            location="Olivine City",
            badge="Mineral Badge"
        ),
        GymTrainer(
            leader="Pryce",
            type=Types.ICE,
            pokemons=[
                TrainerPokemon("Seel", 27),
                TrainerPokemon("Dewgong", 29),
                TrainerPokemon("Piloswine", 31),
            ],
            location="Mahogany Town",
            badge="Glacier Badge"
        ),
        GymTrainer(
            leader="Clair",
            type=Types.DRAGON,
            pokemons=[
                TrainerPokemon("Dragonair", 37),
                TrainerPokemon("Dragonair", 37),
                TrainerPokemon("Gyarados", 40),
                TrainerPokemon("Kingdra", 42),
            ],
            location="Blackthorn City",
            badge="Rising Badge"
        ),
    ]),
            ('elite4', [
        EliteTrainer(
            leader="Will", type=Types.PSYCHIC, pokemons=[
                TrainerPokemon("Xatu", 40),
                TrainerPokemon("Jynx", 41),
                TrainerPokemon("Slowbro", 41),
                TrainerPokemon("Exeggutor", 41),
                TrainerPokemon("Xatu", 42),
            ]
        ),
        EliteTrainer(
            leader="Koga", type=Types.POISON, pokemons=[
                TrainerPokemon("Ariados", 40),
                TrainerPokemon("Venomoth", 41),
                TrainerPokemon("Forretress", 43),
                TrainerPokemon("Muk", 42),
                TrainerPokemon("Crobat", 44),
            ]
        ),
        EliteTrainer(
            leader="Bruno", type=Types.FIGHTING, pokemons=[
                TrainerPokemon("Hitmontop", 42),
                TrainerPokemon("Hitmonlee", 42),
                TrainerPokemon("Hitmonchan", 42),
                TrainerPokemon("Onix", 43),
                TrainerPokemon("Machamp", 46),
            ]
        ),
        EliteTrainer(
            leader="Karen", type=Types.DARK, pokemons=[
                TrainerPokemon("Umbreon", 42),
                TrainerPokemon("Vileplume", 42),
                TrainerPokemon("Murkrow", 44),
                TrainerPokemon("Gengar", 45),
                TrainerPokemon("Houndoom", 47),
            ]
        ),
        EliteTrainer(
            leader="Lance", type=Types.DRAGON, pokemons=[
                TrainerPokemon("Gyarados", 44),
                TrainerPokemon("Dragonite", 47),
                TrainerPokemon("Charizard", 46),
                TrainerPokemon("Aerodactyl", 46),
                TrainerPokemon("Dragonite", 47),
                TrainerPokemon("Dragonite", 50),
            ]
        ),
    ]),
            ('routes', [
        "New Bark Town",
        "Cherrygrove City",
        "Violet City",
        "Sprout Tower",
        "Ruins of Alph",
        "Union Cave",
        "Azalea Town",
        "Slowpoke Well",
        "Ilex Forest",
        "Goldenrod City",
        "National Park",
        "Ecruteak City",
        "Burned Tower",
        "Tin Tower",
        "Olivine City",
        "Whirl Islands",
        "Cianwood City",
        "Mt. Mortar",
        "Mahogany Town",
        "Lake of Rage",
        "Ice Path",
        "Blackthorn City",
        "Dragon's Den",
        "Dark Cave",
        "Victory Road",
        "Route 29",
        "Route 30",
        "Route 31",
        "Route 32",
        "Route 33",
        "Route 34",
        "Route 35",
        "Route 36",
        "Route 37",
        "Route 38",
        "Route 39",
        "Route 40",
        "Route 41",
        "Route 42",
        "Route 43",
        "Route 44",
        "Route 45",
        "Route 46",
        "Route 27",
        "Route 26",
    ]),
            ('starters', [
        fetch_pokemon("Chikorita", 2),
        fetch_pokemon("Cyndaquil", 2),
        fetch_pokemon("Totodile", 2),
    ]),
            ('important_battles', [
                "Violet City - GymTrainer (9)",
                "Slowpoke Well - Boss (14)",
                "Azalea Town - GymTrainer (16)",
                "Azalea Town - Rival (16)",
                "Goldenrod City - GymTrainer (20)",
                "Burned Tower - Rival (22)",
                "Ecruteak City - GymTrainer (25)",
                "Mahogany Town - Boss (25)",
                "Cianwood City - GymTrainer (30)",
                "Mahogany Town - GymTrainer (31)",
                "Olivine City - GymTrainer (35)",
                "Goldenrod City - Rival (32)",
                "Goldenrod City - Boss (35)",
                "Blackthorn City - GymTrainer (40)",
                "Victory Road - Rival (38)",
                "EliteTrainer 4  (50)",
            ])
        ]:
            kwargs[override_field] = kwargs.get(override_field, default_value)
        super().__init__(**kwargs)


GOLD = _BaseGame(
    name="Gold",
    encounters={
        "New Bark Town": {"Tentacool", "Tentacruel", "Shellder", "Chinchou", "Lanturn", "Magikarp"},
        "Cherrygrove City": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp"},
        "Violet City": {"Poliwag", "Poliwhirl", "Magikarp", "Togepi", "Onix"},
        "Sprout Tower": {"Rattata", "Gastly"},
        "Ruins of Alph": {"Unown", "Natu", "Smeargle", "Wooper", "Quagsire", "Poliwag", "Poliwhirl", "Magikarp"},
        "Union Cave": {"Sandshrew", "Zubat", "Geodude", "Rattata", "Wooper", "Quagsire", "Goldeen", "Seaking", "Raticate", "Golbat", "Tentacool", "Tentacruel", "Shellder", "Chinchou", "Lanturn", "Lapras"},
        "Azalea Town": {"Caterpie", "Butterfree", "Metapod", "Exeggcute", "Pineco"},
        "Slowpoke Well": {"Zubat", "Slowpoke", "Goldeen", "Seaking", "Magikarp"},
        "Ilex Forest": {"Caterpie", "Metapod", "Zubat", "Oddish", "Zubat", "Paras", "Psyduck", "Golduck", "Poliwag", "Poliwhirl", "Pineco"},
        "Goldenrod City": {"Eevee", "Machop", "Ekans", "Abra", "Dratini"},
        "National Park": {"Caterpie", "Metapod", "Hoothoot", "Sunkern", "Pidgey", "Butterfree", "Beedrill", "Scyther", "Pinsir", "Weedle", "Kakuna", "Paras", "Venonat"},
        "Ecruteak City": {"Poliwag", "Poliwhirl", "Magikarp"},
        "Burned Tower": {"Rattata", "Koffing", "Raticate", "Zubat", "Krabby", "Shuckle", "Magmar"},
        "Tin Tower": {"Rattata", "Gastly", "Ho-Ho"},
        "Olivine City": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Voltorb", "Shellder", "Chinchou", "Lanturn"},
        "Whirl Islands": {"Zubat", "Krabby", "Golbat", "Seel", "Tentacool", "Horsea", "Tentacruel", "Kingler", "Seadra", "Lugia"},
        "Cianwood City": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Shuckle"},
        "Mt. Mortar": {"Machop", "Geodude", "Zubat", "Rattata", "Marill", "Goldeen", "Seaking", "Magikarp", "Machoke", "Graveler", "Golbat", "Raticate", "Tyrogue"},
        "Mahogany Town": {},
        "Lake of Rage": {"Magikarp", "Gyarados", "Caterpie", "Butterfree", "Metapod", "Exeggcute", "Pineco"},
        "Ice Path": {"Zubat", "Golbat", "Swinub", "Jynx", "Golbat"},
        "Blackthorn City": {"Magikarp", "Poliwag", "Poliwhirl", "Rhydon"},
        "Dragon's Den": {"Magikarp", "Dratini", "Dragonair"},
        "Dark Cave": {"Zubat", "Geodude", "Golbat", "Graveler", "Wobbuffet", "Magikarp", "Goldeen", "Seaking", "Krabby", "Shuckle", "Dunsparce"},
        "Victory Road": {"Golbat", "Graveler", "Ursaring", "Onix", "Rhyhorn"},
        "Route 29": {"Pidgey", "Sentret", "Hoothoot", "Rattata", "Spearow", "Aipom", "Heracross"},
        "Route 30": {"Caterpie", "Pidgey", "Rattata", "Hoothoot", "Spinarak", "Metapod", "Poliwag", "Poliwhirl", "Magikarp", "Spearow", "Aipom", "Heracross"},
        "Route 31": {"Caterpie", "Pisgey", "Rattata", "Hoothoot", "Spinarak", "Metapod", "Bellsproute", "Poliwag", "Poliwhirl", "Magikarp", "Spearow", "Aipom", "Heracross"},
        "Route 32": {"Rattata", "Bellsprout", "Wooper", "Zubat", "Mareep", "Hoppip", "Tentacool", "Quagsire", "Tentacruel", "Magikarp", "Quilfish", "Spearow", "Aipom", "Heracross"},
        "Route 33": {"Rattata", "Zubat", "Hoppip", "Spearow", "Aipom", "Heracross"},
        "Route 34": {"Rattata", "Drowzee", "Ditto", "Abra", "Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Pichu", "Cleffa", "Igllybuff", "Tyrogue", "Smoochum", "Elekid", "Magby", "Caterpie", "Butterfree", "Metapod", "Exeggcute", "Pineco"},
        "Route 35": {"Nidoran Female", "Nidoran Male", "Pidgey", "Ditto", "Hoothoot", "Yanma", "Abra", "Drowzee", "Noctowl", "Psyduck", "Golduck", "Poliwag", "Poliwhirl", "Magikarp", "Spearow", "Caterpie", "Butterfree", "Metapod", "Exeggcute", "Pineco"},
        "Route 36": {"Pidgey", "Nidoran Female", "Nidoran Male", "Hoothoot", "Stantler", "Growlithe", "Sudowoodo", "Caterpie", "Butterfree", "Metapod", "Exeggcute", "Pineco"},
        "Route 37": {"Pidgey", "Spinarak", "Stantler", "Pidgeotto", "Growlithe", "Hoothoot", "Caterpie", "Butterfree", "Metapod", "Exeggcute", "Pineco"},
        "Route 38": {"Rattata", "Raticate", "Tauros", "Snubbull", "Miltank", "Magnemite", "Farfetchd", "Caterpie", "Butterfree", "Metapod", "Exeggcute", "Pineco"},
        "Route 39": {"Rattata", "Raticate", "Tauros", "Miltank", "Magnemite", "Farfetchd", "Caterpie", "Butterfree", "Metapod", "Exeggcute", "Pineco"},
        "Route 40": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Shuckle"},
        "Route 41": {"Tentacool", "Tentacruel", "Mantine", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp"},
        "Route 42": {"Spearow", "Zubat", "Mankey", "Mareep", "Flaafy", "Goldeen", "Seaking", "Magikarp", "Aipom", "Heracross"},
        "Route 43": {"Pidgeotto", "Flaafy", "Girafarig", "Venonat", "Mareep", "Noctowl", "Magikarp", "Aipom", "Heracross"},
        "Route 44": {"Weepinbell", "Tangela", "Bellsprout", "Lickitung", "Poliwag", "Poliwhirl", "Magikarp", "Remoraid", "Spearow", "Aipom", "Heracross"},
        "Route 45": {"Geodude", "Graveler", "Gligar", "Teddiursa", "Magikarp", "Dratini", "Dragonair", "Spearow", "Aipom", "Heracross"},
        "Route 46": {"Rattata", "Spearow", "Geodude", "Jigglypuff", "Aipom", "Heracross"},
        "Route 26": {"Raticate", "Sandslash", "Doduo", "Dodrio", "Quagsire", "Ponyta", "Tentacool", "Tentacruel", "Shellder", "Chinchou", "Lanturn", "Magikarp", "Caterpie", "Butterfree", "Metapod", "Exeggcute", "Pineco"},
        "Route 27": {"Raticate", "Doduo", "Quagsire", "Sandslash", "Ponyta", "Tentacool", "Tentacruel", "Shellder", "Chinchou", "Lanturn", "Magikarp" ,"Caterpie", "Butterfree", "Metapod", "Exeggcute", "Pineco"},
    }
)


SILVER = _BaseGame(
    name="Silver",
    encounters={
        "New Bark Town": {"Tentacool", "Tentacruel", "Shellder", "Chinchou", "Lanturn", "Magikarp"},
        "Cherrygrove City": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp"},
        "Violet City": {"Poliwag", "Poliwhirl", "Magikarp", "Togepi", "Onix"},
        "Sprout Tower": {"Rattata", "Gastly"},
        "Ruins of Alph": {"Unown", "Natu", "Smeargle", "Wooper", "Quagsire", "Poliwag", "Poliwhirl", "Magikarp"},
        "Union Cave": {"Sandshrew", "Zubat", "Geodude", "Rattata", "Wooper", "Quagsire", "Goldeen", "Seaking", "Raticate", "Golbat", "Tentacool", "Tentacruel", "Shellder", "Chinchou", "Lanturn", "Lapras"},
        "Azalea Town": {"Weedle", "Beedrill", "Kakuna", "Exeggcute", "Pineco"},
        "Slowpoke Well": {"Zubat", "Slowpoke", "Goldeen", "Seaking", "Magikarp"},
        "Ilex Forest": {"Weedle", "Kakuna", "Zubat", "Oddish", "Paras", "Psyduck", "Golduck", "Poliwag", "Poliwhirl", "Magikarp"},
        "Goldenrod City": {"Eevee", "Machop", "Sandshrew", "Abra", "Dratini"},
        "National Park": {"Weedle", "Beedrill", "Kakuna", "Hoothoot", "Sunkern", "Pidgey", "Butterfree", "Scyther", "Pinsir", "Caterpie", "Metapod", "Paras", "Venonat"},
        "Ecruteak City": {"Poliwag", "Poliwhirl", "Magikarp"},
        "Burned Tower": {"Rattata", "Koffing", "Raticate", "Zubat", "Krabby", "Shuckle", "Magmar"},
        "Tin Tower": {"Rattata", "Gastly", "Ho-Ho"},
        "Olivine City": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Voltorb", "Shellder", "Chinchou", "Lanturn"},
        "Whirl Islands": {"Zubat", "Krabby", "Golbat", "Seel", "Tentacool", "Horsea", "Tentacruel", "Kingler", "Seadra", "Lugia"},
        "Cianwood City": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Shuckle"},
        "Mt. Mortar": {"Machop", "Geodude", "Zubat", "Rattata", "Marill", "Goldeen", "Seaking", "Magikarp", "Machoke", "Graveler", "Golbat", "Raticate", "Tyrogue"},
        "Mahogany Town": {},
        "Lake of Rage": {"Magikarp", "Gyarados", "Weedle", "Kakuna", "Beedrill", "Exeggcute", "Pineco"},
        "Ice Path": {"Golbat", "Swinub", "Zubat", "Jynx", "Delibird"},
        "Blackthorn City": {"Magikarp", "Poliwag", "Poliwhirl", "Rhydon"},
        "Dragon's Den": {"Magikarp", "Dratini", "Dragonair"},
        "Dark Cave": {"Zubat", "Geodude", "Golbat", "Graveler", "Wobbuffet", "Magikarp", "Goldeen", "Seaking", "Krabby", "Shuckle", "Dunsparce"},
        "Victory Road": {"Golbat", "Graveler", "Donphan", "Onix", "Rhyhorn"},
        "Route 29": {"Pidgey", "Sentret", "Hoothoot", "Rattata", "Spearow", "Aipom", "Heracross"},
        "Route 30": {"Weedle", "Pidgey", "Rattata", "Hoothoot", "Ledyba", "Kakuna", "Poliwag", "Poliwhirl", "Magikarp", "Spearow", "Aipom", "Heracross"},
        "Route 31": {"Weedle", "Pidgey", "Rattata", "Hoothoot", "Ledyba", "Kakuna", "Poliwag", "Poliwhirl", "Magikarp", "Spearow", "Aipom", "Heracross"},
        "Route 32": {"Ekans", "Bellsprout", "Wooper", "Rattata", "Zubat", "Mareep", "Hoppip", "Tentacool", "Tentacruel", "Quagsire", "Magikarp", "Qwilfish", "Spearow", "Aipom", "Heracross"},
        "Route 33": {"Ekans", "Rattata", "Zubat", "Hoppip", "Spearow", "Aipom", "Heracross"},
        "Route 34": {"Rattata", "Drowzee", "Ditto", "Abra", "Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Weedle", "Beedrill", "Kakuna", "Exeggcute", "Pineco"},
        "Route 35": {"Nidoran Female", "Nidoran Male", "Pidgey", "Ditto", "Hoothoot", "Yanma", "Abra", "Drowzee", "Noctowl", "Psyduck", "Golduck", "Poliwag", "Poliwhirl", "Magikarp", "Spearow", "Weedle", "Beedrill", "Kakuna", "Exeggcute", "Pineco"},
        "Route 36": {"Pidgey", "Nidoran Female", "Nidoran Male", "Hoothoot", "Stantler", "Growlithe", "Sudowoodo", "Weedle", "Beedrill", "Kakuna", "Exeggcute", "Pineco"},
        "Route 37": {"PIdgey", "Hoothoot", "Ledyba", "Stantler", "Pidgeotto", "Vulpix", "Weedle", "Beedrill", "Kakuna", "Exeggcute", "Pineco"},
        "Route 38": {"Raticate", "Meowth", "Tauros", "Snubbull", "Miltank", "Magnemite", "Farfetchd", "Weedle", "Kakuna", "Beedrill", "Exeggcute", "Pineco"},
        "Route 39": {"Raticate", "Meowth", "Tauros", "Miltank", "Magnemite", "Farfetchd", "Weedle", "Beedrill", "Kakuna", "Exeggcute", "Pineco"},
        "Route 40": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Shuckle"},
        "Route 41": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp"},
        "Route 42": {"Spearow", "Zubat", "Mankey", "Mareep", "Flaafy", "Goldeen", "Seaking", "Magikarp", "Aipom", "Heracross"},
        "Route 43": {"Pidgeotto", "Flaafy", "Girafarig", "Venonat", "Mareep", "Noctowl", "Magikarp", "Aipom", "Heracross"},
        "Route 44": {"Weepinbell", "Tangela", "Bellsprout", "Lickitung", "Poliwag", "Poliwhirl", "Magikarp", "Remoraid", "Spearow", "Aipom", "Heracross"},
        "Route 45": {"Geodude", "Graveler", "Skarmory", "Phanpy", "Gligar", "Donphan", "Magikarp", "Dratini", "Dragonair"},
        "Route 46": {"Rattata", "Spearow", "Geodude", "Jigglypuff", "Aipom", "Heracross"},
        "Route 26": {"Raticate", "Doduo", "Raticate", "Arbok", "Quagsire", "Ponyta", "Tentacool", "Tentacruel", "Shellder", "Chincou", "Lanturn", "Magikarp", "Weedle", "Beedrill", "Kakuna", "Exeggcute", "Pineco"},
        "Route 27": {"Raticate", "Arbok", "Quagsire", "Ponyta", "Dodrio", "Tentacool", "Tentacruel", "Shellder", "Chincou", "Lanutrn", "Magikarp", "Weedle", "Kakuna", "Beedrill", "Exeggcute", "Pineco"},
    },
)


CRYSTAL = _BaseGame(
    name="Crystal",
    gyms=[
        GymTrainer(
            leader="Falkner",
            type=Types.FLYING,
            pokemons=[
                TrainerPokemon("Pidgey", 7),
                TrainerPokemon("Pidgeotto", 9),
            ],
            location="Violet City",
            badge="Zephyr Badge"
        ),
        GymTrainer(
            leader="Bugsy",
            type=Types.BUG,
            pokemons=[
                TrainerPokemon("Metapod", 14),
                TrainerPokemon("Kakuna", 14),
                TrainerPokemon("Scyther", 16)
            ],
            location="Azalea Town",
            badge="Hive Badge"
        ),
        GymTrainer(
            leader="Whitney",
            type=Types.NORMAL,
            pokemons=[
                TrainerPokemon("Clefairy", 18),
                TrainerPokemon("Miltank", 20),
            ],
            location="Goldenrod City",
            badge="Plain Badge"
        ),
        GymTrainer(
            leader="Morty",
            type=Types.GHOST,
            pokemons=[
                TrainerPokemon("Gastly", 21),
                TrainerPokemon("Haunter", 21),
                TrainerPokemon("Haunter", 24),
                TrainerPokemon("Gengar", 25),
            ],
            location="Ecruteak City",
            badge="Fog Badge"
        ),
        GymTrainer(
            leader="Chuck",
            type=Types.FIGHTING,
            pokemons=[
                TrainerPokemon("Primeape", 27),
                TrainerPokemon("Poliwrath", 30),
            ],
            location="Cianwood City",
            badge="Storm Badge"
        ),
        GymTrainer(
            leader="Jasmine",
            type=Types.STEEL,
            pokemons=[
                TrainerPokemon("Magnemite", 30),
                TrainerPokemon("Magnemite", 30),
                TrainerPokemon("Steelix", 35),
            ],
            location="Olivine City",
            badge="Mineral Badge"
        ),
        GymTrainer(
            leader="Pryce",
            type=Types.ICE,
            pokemons=[
                TrainerPokemon("Seel", 27),
                TrainerPokemon("Dewgong", 29),
                TrainerPokemon("Piloswine", 31),
            ],
            location="Maohany Island",
            badge="Glacier Badge"
        ),
        GymTrainer(
            leader="Clair",
            type=Types.DRAGON,
            pokemons=[
                TrainerPokemon("Dragonair", 37),
                TrainerPokemon("Dragonair", 37),
                TrainerPokemon("Dragonair", 37),
                TrainerPokemon("Kingdra", 40),
            ],
            location="Blackthorn City",
            badge="Rising Badge"
        ),
    ],
    elite4=[
        EliteTrainer(
            leader="Will", type=Types.PSYCHIC, pokemons=[
                TrainerPokemon("Xatu", 40),
                TrainerPokemon("Jynx", 41),
                TrainerPokemon("Slowbro", 41),
                TrainerPokemon("Exeggutor", 41),
                TrainerPokemon("Xatu", 42),
            ]
        ),
        EliteTrainer(
            leader="Koga", type=Types.POISON, pokemons=[
                TrainerPokemon("Ariados", 40),
                TrainerPokemon("Venomoth", 41),
                TrainerPokemon("Forretress", 43),
                TrainerPokemon("Muk", 42),
                TrainerPokemon("Crobat", 44),
            ]
        ),
        EliteTrainer(
            leader="Bruno", type=Types.FIGHTING, pokemons=[
                TrainerPokemon("Hitmontop", 42),
                TrainerPokemon("Hitmonlee", 42),
                TrainerPokemon("Hitmonchan", 42),
                TrainerPokemon("Onix", 43),
                TrainerPokemon("Machamp", 46),
            ]
        ),
        EliteTrainer(
            leader="Karen", type=Types.DARK, pokemons=[
                TrainerPokemon("Umbreon", 42),
                TrainerPokemon("Vileplume", 42),
                TrainerPokemon("Murkrow", 44),
                TrainerPokemon("Gengar", 45),
                TrainerPokemon("Houndoom", 47),
            ]
        ),
        EliteTrainer(
            leader="Lance", type=Types.DRAGON, pokemons=[
                TrainerPokemon("Gyarados", 44),
                TrainerPokemon("Dragonite", 47),
                TrainerPokemon("Charizard", 46),
                TrainerPokemon("Aerodactyl", 46),
                TrainerPokemon("Dragonite", 47),
                TrainerPokemon("Dragonite", 50),
            ]
        ),
    ],
    routes=[
        "New Bark Town",
        "Cherrygrove City",
        "Violet City",
        "Sprout Tower",
        "Ruins of Alph",
        "Union Cave",
        "Azalea Town",
        "Slowpoke Well",
        "Ilex Forest",
        "Goldenrod City",
        "National Park",
        "Ecruteak City",
        "Burned Tower",
        "Tin Tower",
        "Olivine City",
        "Whirl Islands",
        "Cianwood City",
        "Mt. Mortar",
        "Mahogany Town",
        "Lake of Rage",
        "Ice Path",
        "Blackthorn City",
        "Dragon's Den",
        "Dark Cave",
        "Victory Road",
        "Route 29",
        "Route 30",
        "Route 31",
        "Route 32",
        "Route 33",
        "Route 34",
        "Route 35",
        "Route 36",
        "Route 37",
        "Route 38",
        "Route 39",
        "Route 40",
        "Route 41",
        "Route 42",
        "Route 43",
        "Route 44",
        "Route 45",
        "Route 46",
        "Route 27",
        "Route 26",
    ],
    encounters={
       "New Bark Town": {"Tentacool", "Tentacruel", "Shellder", "Chinchou", "Lanturn", "Magikarp", "Chikorita", "Cyndaquil", "Totodile"},
        "Cherrygrove City": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp"},
        "Violet City": {"Poliwag", "Poliwhirl", "Magikarp", "Togepi", "Onix"},
        "Sprout Tower": {"Rattata", "Gastly"},
        "Ruins of Alph": {"Unown", "Natu", "Smeargle", "Wooper", "Quagsire", "Poliwag", "Poliwhirl", "Magikarp"},
        "Union Cave": {"Rattata", "Sandshrew", "Geodude", "Zubat", "Wooper", "Onix", "Quagsire", "Goldeen", "Seaking", "Magikarp", "Golbat", "Raticate", "Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Lapras"},
        "Azalea Town": {"Spearow", "Aipom", "Ekans", "Heracross"},
        "Slowpoke Well": {"Zubat", "Slowpoke", "Goldeen", "Seaking", "Magikarp", "Golbat", "Slowbro"},
        "Ilex Forest": {"Caterpie", "Weedle", "Oddish", "Venonat", "Paras", "Pidgey", "Hoothoot", "Metapod", "Kakuna", "Psyduck", "Golduck", "Poliwag", "Poliwhirl", "Magikarp", "Celebi", "Pineco", "Noctowl", "Butterfree", "Beedrill"},
        "Goldenrod City": {"Eevee", "Machop", "Abra", "Cubone", "Wobbuffet"},
        "National Park": {"Hoothoot", "Nidoran Female", "Nidoran Male", "Psyduck", "Ledyba", "Spinarak", "Sunkern", "Pidgey", "Vednonat", "Caterpie", "Weedle", "Butterfree", "Beetdrill", "Scyther", "Pinsir", "Paras", "Venonat"},
        "Ecruteak City": {"Poliwag", "Poliwhirl", "Magikarp"},
        "Burned Tower": {"Rattata", "Koffing", "Zubat", "Raticate", "Krabby", "Shuckle", "Weezing"},
        "Tin Tower": {"Rattata", "Gastly", "Suicone", "HoHo"},
        "Olivine City": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Voltorb", "Shellder", "Chinchou", "Lanturn"},
        "Whirl Islands": {"Krabby", "Zubat", "Seel", "Golbat", "Tentacool", "Horsea", "Tentacruel", "Kingler", "Seadra", "Magikarp", "Lugia"},
        "Cianwood City": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Shuckle"},
        "Mt. Mortar": {"Rattata", "Geodude", "Raticate", "Machop", "Zubat", "Golbat", "Marill", "Goldeen", "Seaking", "Magikarp", "Machoke", "Graveler", "Tyrogue"},
        "Mahogany Town": {},
        "Lake of Rage": {"Magikarp", "Gyarados", "Hoothoot", "Exeggcute", "Venonat", "Pineco"},
        "Ice Path": {"Swinub", "Delibird", "Zubat", "Golbat", "Jynx", "Sneasel"},
        "Blackthorn City": {"Magikarp", "Poliwag", "Poliwhirl", "Dodrio"},
        "Dragon's Den": {"Magikarp", "Dratini", "Dragonair"},
        "Dark Cave": {"Zubat", "Geodude", "Graveler", "Wobbuffet", "Ursaring", "Golbat", "Teddiursa", "Magikarp", "Goldeen", "Seaking", "Krabby", "Shuckle", "Dunsparce"},
        "Victory Road": {"Graveler", "Golbat", "Rhyhorn", "Onix", "Sandslash", "Rhydon"},
        "Route 29": {"Sentret", "Pidgey", "Rattata", "Hoothoot", "Hoppip", "Exeggcute", "Spinarak", "Ledyba", "Pineco"},
        "Route 30": {"Caterpie", "Ledyba", "Spinarak", "Pidgey", "Hoothoot", "Weedle", "Zubat", "Marill", "Hoppip", "Pidgey", "Poliwag", "Poliwhirl", "Magikarp", "Exeggcute", "Pineco"},
        "Route 31": {"Ledyba", "Spinarak", "Caterpie", "Pidgey", "Poliwag", "Weedle", "Zubat", "Gastly", "Hoppip", "Hoothoot", "Bellsprout", "Poliwhirl", "Magikarp", "Exeggcute", "Pineco"},
        "Route 32": {"Ekans", "Rattata", "Wooper", "Pidgey", "Gastly", "Hoothoot", "Zubat", "Bellsprout", "Hoppip", "Tentacool", "Quagsire", "Tentacruel", "Magikarp", "Quilfish", "Exeggcute", "Ekans", "Pineco"},
        "Route 33": {"Rattata", "Spearow", "Zubat", "Ekans", "Geodude", "Hoppip", "Aipom", "Heracross"},
        "Route 34": {"Rattata", "Drowzee", "Snubbull", "Ditto", "Jigglypuff", "Abra", "Pidgey", "Hoothoot", "Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Pichu", "Cleffa", "Igglybuff", "Tyrogue", "Smoochum", "Elekid", "Magby", "Exeggcute", "Ledyba", "Spinarak", "Pineco"},
        "Route 35": {"Pidgey", "Drowzee", "Hoothoot", "Snubull", "Ditto", "Yanma", "Jigglypuff", "Abra", "Psyduck", "Growlithe", "Nidoran Female", "Nidoran Male", "Noctowl", "Golduck", "Poliwag", "Poliwhirl", "Magikarp", "Spearow", "Exeggcute", "Spinarak", "Ledyba", "Pineco"},
        "Route 36": {"Pidgey", "Hoothoot", "Ledyba", "Spinarak", "Gastly", "Growlithe", "Bellsprout", "Sudowoodo", "Exeggcute", "Pineco"},
        "Route 37": {"Pidgey", "Growlithe", "Ledyba", "Spinarak", "Stantlar", "Pidgeotto", "Noctowl", "Ledian", "Ariados", "Exeggcute", "Pineco"},
        "Route 38": {"Rattata", "Raticate", "Meowth", "Tauros", "Miltank", "Magnemite", "Pidgeotto", "Noctowl", "Hoothoot", "Exeggcute", "Ledyba", "Spinarak", "Pineco"},
        "Route 39": {"Rattata", "Meowth", "Raticate", "Tauros", "Miltank", "Magnemite", "Pidgeotto", "Noctowl", "Exeggcute", "Ledyba", "Spinarak", "Hoothoot", "Pineco"},
        "Route 40": {"Tentacool", "Tentacruel", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp", "Shuckle"},
        "Route 41": {"Tentacruel", "Tentacool", "Mantine", "Krabby", "Staryu", "Corsola", "Kingler", "Magikarp"},
        "Route 42": {"Rattata", "Spearow", "Ekans", "Zubat", "Fearow", "Arbok", "Marill", "Raticate", "Golbat", "Goldeen", "Seaking", "Spearow", "Aipom", "Ekans", "Heracross"},
        "Route 43": {"Pidgeotto", "Raticate", "Venonat", "Sentret", "Noctowl", "Venomoth", "Farfetchd", "Furret", "Magikarp", "Hoothoot", "Exeggcute", "Pineco"},
        "Route 44": {"Tangela", "Weepinbell", "Poliwag", "Lickitung", "Bellsprout", "Poliwhirl", "Poliwag", "Magikarp", "Spearow", "Aipom", "Heracross"},
        "Route 45": {"Geodude", "Graveler", "Skarmory", "Phanpy", "Gligar", "Donphan", "Magikarp", "Dratini", "Dragonair"},
        "Route 46": {"Rattata", "Spearow", "Geodude", "Phanpy"},
        "Route 27": {"Arbok", "Doduo", "Quagsire", "Noctowl", "Ponyta", "Dodrio", "Raticate", "Tentacool", "Tentacruel", "Shellder", "Chinchou", "Lanturn", "Magikarp", "Hoothoot", "Ekans", "Exeggcute", "Pineco"},
        "Route 26": {"Raticate", "Sandslash", "Doduo", "Noctowl", "Arbok", "Ponyta", "Tentacool", "Tentacruel", "Shellder", "Chinchou", "Lanturn", "Magikarp", "Hoothoot", "Exeggcute", "Ekans", "Pineco"},
    },
)
