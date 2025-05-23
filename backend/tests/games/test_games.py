import unittest
from games import get_game, get_games_from_gen, GAMES
from games.gen1 import BLUE, RED, YELLOW
from games.gen2 import GOLD, SILVER, CRYSTAL


class TestGames(unittest.TestCase):
    def test_get_game(self):
        # Test getting each game by name
        self.assertEqual(get_game("Blue"), BLUE)
        self.assertEqual(get_game("Red"), RED)
        self.assertEqual(get_game("Yellow"), YELLOW)
        self.assertEqual(get_game("Gold"), GOLD)
        self.assertEqual(get_game("Silver"), SILVER)
        self.assertEqual(get_game("Crystal"), CRYSTAL)

        # Test that invalid game name raises StopIteration
        with self.assertRaises(StopIteration):
            get_game("Invalid Game")

    def test_get_games_from_gen(self):
        # Test getting games from gen 1
        gen1_games = get_games_from_gen(1)
        self.assertEqual(len(gen1_games), 6)  # All games are gen 1 or 2
        self.assertIn(BLUE, gen1_games)
        self.assertIn(RED, gen1_games)
        self.assertIn(YELLOW, gen1_games)
        self.assertIn(GOLD, gen1_games)
        self.assertIn(SILVER, gen1_games)
        self.assertIn(CRYSTAL, gen1_games)

        # Test getting games from gen 2
        gen2_games = get_games_from_gen(2)
        self.assertEqual(len(gen2_games), 3)  # Only gen 2 games
        self.assertIn(GOLD, gen2_games)
        self.assertIn(SILVER, gen2_games)
        self.assertIn(CRYSTAL, gen2_games)

        # Test getting games from gen 3 (should be empty)
        gen3_games = get_games_from_gen(3)
        self.assertEqual(len(gen3_games), 0)

    def test_games_list(self):
        # Test that GAMES list contains all games
        self.assertEqual(len(GAMES), 6)
        self.assertIn(BLUE, GAMES)
        self.assertIn(RED, GAMES)
        self.assertIn(YELLOW, GAMES)
        self.assertIn(GOLD, GAMES)
        self.assertIn(SILVER, GAMES)
        self.assertIn(CRYSTAL, GAMES)


if __name__ == '__main__':
    unittest.main() 