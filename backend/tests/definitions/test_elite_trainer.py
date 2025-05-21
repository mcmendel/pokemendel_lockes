import unittest
from definitions.trainers.elite_trainer import EliteTrainer
from definitions.trainers.trainer_pokemon import TrainerPokemon
from pokemendel_core.utils.definitions.types import Types


class TestEliteTrainer(unittest.TestCase):
    def test_elite_trainer_attributes(self):
        # Create a list of TrainerPokemon instances
        pokemons = [
            TrainerPokemon(pokemon_name="Pikachu", level=25),
            TrainerPokemon(pokemon_name="Charizard", level=30)
        ]
        
        # Create an EliteTrainer instance
        elite_trainer = EliteTrainer(leader="Ash", type=Types.ELECTRIC, pokemons=pokemons)
        
        # Verify that the attributes are set correctly
        self.assertEqual(elite_trainer.leader, "Ash")
        self.assertEqual(elite_trainer.type, Types.ELECTRIC)
        self.assertEqual(elite_trainer.pokemons, pokemons)


if __name__ == '__main__':
    unittest.main() 