import unittest
from definitions.trainer_pokemon import TrainerPokemon


class TestTrainerPokemon(unittest.TestCase):
    def test_trainer_pokemon_attributes(self):
        # Create a TrainerPokemon instance
        trainer_pokemon = TrainerPokemon(pokemon_name="Pikachu", level=25)
        
        # Verify that the attributes are set correctly
        self.assertEqual(trainer_pokemon.pokemon_name, "Pikachu")
        self.assertEqual(trainer_pokemon.level, 25)


if __name__ == '__main__':
    unittest.main() 