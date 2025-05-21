import unittest
from definitions import Game, GymTrainer, EliteTrainer, Pokemon, PokemonMetadata
from pokemendel_core.utils.definitions.types import Types


class TestGame(unittest.TestCase):
    def setUp(self):
        """Set up common test data."""
        self.name = "Pokemon Red"
        self.gen = 1
        self.region = "Kanto"
        self.gyms = [
            GymTrainer(
                name="Brock",
                type=Types.ROCK,
                pokemons=[],
                badge="Boulder Badge",
                level=1
            )
        ]
        self.elite4 = [
            EliteTrainer(
                leader="Lorelei",
                type=Types.ICE,
                pokemons=[]
            )
        ]
        self.routes = ["Route 1", "Route 2"]
        self.starters = [
            Pokemon(
                name="Bulbasaur",
                gen=1,
                types=[Types.GRASS, Types.POISON],
                metadata=PokemonMetadata(id="001", nickname="Bulby")
            )
        ]

    def test_valid_game_creation(self):
        """Test that a Game can be created with valid data."""
        game = Game(
            name=self.name,
            gen=self.gen,
            region=self.region,
            gyms=self.gyms,
            elite4=self.elite4,
            routes=self.routes,
            starters=self.starters
        )
        
        self.assertEqual(game.name, self.name)
        self.assertEqual(game.gen, self.gen)
        self.assertEqual(game.region, self.region)
        self.assertEqual(game.gyms, self.gyms)
        self.assertEqual(game.elite4, self.elite4)
        self.assertEqual(game.routes, self.routes)
        self.assertEqual(game.starters, self.starters)
        self.assertEqual(game.important_battles, [])
        self.assertEqual(game.encounters, {})

    def test_game_with_important_battles(self):
        """Test that a Game can be created with important battles."""
        important_battles = ["Rival Battle 1", "Rival Battle 2"]
        game = Game(
            name=self.name,
            gen=self.gen,
            region=self.region,
            gyms=self.gyms,
            elite4=self.elite4,
            routes=self.routes,
            starters=self.starters,
            important_battles=important_battles
        )
        
        self.assertEqual(game.important_battles, important_battles)

    def test_game_with_encounters(self):
        """Test that a Game can be created with encounters."""
        encounters = {
            "Route 1": {"Pidgey", "Rattata"},
            "Route 2": {"Caterpie", "Weedle"}
        }
        game = Game(
            name=self.name,
            gen=self.gen,
            region=self.region,
            gyms=self.gyms,
            elite4=self.elite4,
            routes=self.routes,
            starters=self.starters,
            encounters=encounters
        )
        
        self.assertEqual(game.encounters, encounters)

    def test_empty_lists(self):
        """Test that a Game can be created with empty lists."""
        game = Game(
            name=self.name,
            gen=self.gen,
            region=self.region,
            gyms=[],
            elite4=[],
            routes=[],
            starters=[]
        )
        
        self.assertEqual(game.gyms, [])
        self.assertEqual(game.elite4, [])
        self.assertEqual(game.routes, [])
        self.assertEqual(game.starters, [])


if __name__ == '__main__':
    unittest.main() 