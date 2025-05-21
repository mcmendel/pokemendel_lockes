import unittest
from definitions import GymTrainer, TrainerPokemon
from pokemendel_core.utils.definitions.types import Types


class TestGymTrainer(unittest.TestCase):
    def test_gym_trainer_attributes(self):
        # Create a list of TrainerPokemon instances
        pokemons = [
            TrainerPokemon(pokemon_name="Pikachu", level=25),
            TrainerPokemon(pokemon_name="Raichu", level=30)
        ]
        
        # Create a GymTrainer instance
        gym_trainer = GymTrainer(
            name="Lt. Surge",
            type=Types.ELECTRIC,
            pokemons=pokemons,
            badge="Thunder Badge",
            level=3
        )
        
        # Verify that the attributes are set correctly
        self.assertEqual(gym_trainer.name, "Lt. Surge")
        self.assertEqual(gym_trainer.type, Types.ELECTRIC)
        self.assertEqual(gym_trainer.pokemons, pokemons)
        self.assertEqual(gym_trainer.badge, "Thunder Badge")
        self.assertEqual(gym_trainer.level, 3)

    def test_gym_trainer_with_empty_pokemon_list(self):
        # Create a GymTrainer instance with no pokemon
        gym_trainer = GymTrainer(
            name="Brock",
            type=Types.ROCK,
            pokemons=[],
            badge="Boulder Badge",
            level=1
        )
        
        # Verify that the attributes are set correctly
        self.assertEqual(gym_trainer.name, "Brock")
        self.assertEqual(gym_trainer.type, Types.ROCK)
        self.assertEqual(gym_trainer.pokemons, [])
        self.assertEqual(gym_trainer.badge, "Boulder Badge")
        self.assertEqual(gym_trainer.level, 1)


if __name__ == '__main__':
    unittest.main() 