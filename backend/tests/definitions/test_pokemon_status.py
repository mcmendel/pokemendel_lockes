import unittest
from definitions.pokemons.pokemon_status import PokemonStatus


class TestPokemonStatus(unittest.TestCase):
    def test_status_values(self):
        """Test that all status values are correctly defined."""
        self.assertEqual(PokemonStatus.ALIVE, "alive")
        self.assertEqual(PokemonStatus.DEAD, "dead")

    def test_status_equality(self):
        """Test that status values can be compared correctly."""
        self.assertEqual(PokemonStatus.ALIVE, PokemonStatus.ALIVE)
        self.assertNotEqual(PokemonStatus.ALIVE, PokemonStatus.DEAD)

    def test_status_string_representation(self):
        """Test that status values have correct string representations."""
        self.assertEqual(str(PokemonStatus.ALIVE), "alive")
        self.assertEqual(str(PokemonStatus.DEAD), "dead")


if __name__ == '__main__':
    unittest.main() 