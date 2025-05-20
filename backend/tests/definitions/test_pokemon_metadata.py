import unittest
from definitions.pokemon_metadata import PokemonMetadata
from pokemendel_core.utils.definitions.genders import Genders


class TestPokemonMetadata(unittest.TestCase):
    def test_default_initialization(self):
        """Test that a PokemonMetadata instance initializes with default values."""
        with self.assertRaises(ValueError) as context:
            PokemonMetadata(id="001")
        self.assertEqual(str(context.exception), "nickname cannot be empty")

    def test_custom_initialization(self):
        """Test that a PokemonMetadata instance can be initialized with custom values."""
        metadata = PokemonMetadata(
            id="025",
            nickname="Sparky",
            caught_index=5,
            starlocke_type="star",
            gender=Genders.MALE,
            paired_partner="Pikachu"
        )
        self.assertEqual(metadata.id, "025")
        self.assertEqual(metadata.nickname, "Sparky")
        self.assertEqual(metadata.caught_index, 5)
        self.assertEqual(metadata.starlocke_type, "star")
        self.assertEqual(metadata.gender, Genders.MALE)
        self.assertEqual(metadata.paired_partner, "Pikachu")

    def test_partial_initialization(self):
        """Test that a PokemonMetadata instance can be initialized with only some fields."""
        metadata = PokemonMetadata(
            id="025",
            nickname="Sparky",
            gender=Genders.FEMALE
        )
        self.assertEqual(metadata.id, "025")
        self.assertEqual(metadata.nickname, "Sparky")
        self.assertEqual(metadata.gender, Genders.FEMALE)
        self.assertIsNone(metadata.caught_index)
        self.assertIsNone(metadata.starlocke_type)
        self.assertIsNone(metadata.paired_partner)

    def test_empty_nickname_validation(self):
        """Test that an empty nickname raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            PokemonMetadata(id="025", nickname="")
        self.assertEqual(str(context.exception), "nickname cannot be empty")

    def test_whitespace_nickname_validation(self):
        """Test that a nickname containing only whitespace raises a ValueError."""
        with self.assertRaises(ValueError) as context:
            PokemonMetadata(id="025", nickname="   ")
        self.assertEqual(str(context.exception), "nickname cannot be empty")

    def test_zero_caught_index(self):
        """Test that a caught_index of 0 is handled correctly."""
        metadata = PokemonMetadata(id="025", nickname="Pikachu", caught_index=0)
        self.assertEqual(metadata.caught_index, 0)


if __name__ == '__main__':
    unittest.main() 