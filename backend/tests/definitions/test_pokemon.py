import sys
print('PYTHONPATH at test runtime:', sys.path)
import unittest
from definitions.pokemons.pokemon import Pokemon
from definitions.pokemons.pokemon_metadata import PokemonMetadata
from definitions.pokemons.pokemon_status import PokemonStatus
from pokemendel_core.utils.definitions.types import Types


class TestPokemon(unittest.TestCase):
    def setUp(self):
        """Set up common test data."""
        self.metadata = PokemonMetadata(id="001", nickname="Bulby")
        self.name = "Bulbasaur"
        self.gen = 1
        self.types = [Types.GRASS, Types.POISON]

    def test_valid_pokemon_creation(self):
        """Test that a Pokemon can be created with valid data."""
        pokemon = Pokemon(
            name=self.name,
            gen=self.gen,
            types=self.types,
            metadata=self.metadata,
            status=PokemonStatus.ALIVE
        )
        self.assertEqual(pokemon.metadata.id, "001")
        self.assertEqual(pokemon.status, PokemonStatus.ALIVE)
        self.assertEqual(pokemon.metadata.nickname, "Bulby")

    def test_empty_id_validation(self):
        """Test that creating a Pokemon with an empty id in metadata raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Pokemon(
                name=self.name,
                gen=self.gen,
                types=self.types,
                metadata=PokemonMetadata(id="", nickname="Bulby"),
                status=PokemonStatus.ALIVE
            )
        self.assertEqual(str(context.exception), "id cannot be empty")

    def test_whitespace_id_validation(self):
        """Test that creating a Pokemon with a whitespace-only id in metadata raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Pokemon(
                name=self.name,
                gen=self.gen,
                types=self.types,
                metadata=PokemonMetadata(id="   ", nickname="Bulby"),
                status=PokemonStatus.ALIVE
            )
        self.assertEqual(str(context.exception), "id cannot be empty")

    def test_invalid_status_validation(self):
        """Test that creating a Pokemon with an invalid status raises ValueError."""
        with self.assertRaises(ValueError) as context:
            Pokemon(
                name=self.name,
                gen=self.gen,
                types=self.types,
                metadata=self.metadata,
                status="invalid_status"
            )
        self.assertEqual(str(context.exception), "Invalid status: invalid_status")

    def test_default_status(self):
        """Test that status defaults to ALIVE if not specified."""
        pokemon = Pokemon(
            name=self.name,
            gen=self.gen,
            types=self.types,
            metadata=self.metadata
        )
        self.assertEqual(pokemon.status, PokemonStatus.ALIVE)

    def test_metadata_required(self):
        """Test that metadata is required for Pokemon."""
        with self.assertRaises(ValueError) as context:
            Pokemon(
                name=self.name,
                gen=self.gen,
                types=self.types,
                metadata=None
            )
        self.assertEqual(str(context.exception), "metadata cannot be None and must include a valid id")

    def test_pokemon_with_metadata(self):
        """Test that a Pokemon can be created with metadata."""
        metadata = PokemonMetadata(id="025", nickname="Sparky", caught_index=1)
        pokemon = Pokemon(
            name="Pikachu",
            gen=1,
            types=[Types.ELECTRIC],
            metadata=metadata
        )
        self.assertEqual(pokemon.metadata.nickname, "Sparky")
        self.assertEqual(pokemon.metadata.caught_index, 1)


if __name__ == '__main__':
    unittest.main() 