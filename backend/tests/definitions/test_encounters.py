import unittest
from definitions.runs.encounters import Encounter, EncounterStatus
from definitions import Pokemon, PokemonMetadata
from pokemendel_core.utils.definitions.types import Types


class TestEncounterStatus(unittest.TestCase):
    def test_status_values(self):
        """Test that all status values are correctly defined."""
        self.assertEqual(EncounterStatus.UNMET, "Unmet")
        self.assertEqual(EncounterStatus.MET, "Met")
        self.assertEqual(EncounterStatus.KILLED, "Killed")
        self.assertEqual(EncounterStatus.RAN, "Ran")
        self.assertEqual(EncounterStatus.CAUGHT, "Caught")

    def test_status_equality(self):
        """Test that status values can be compared correctly."""
        self.assertEqual(EncounterStatus.UNMET, EncounterStatus.UNMET)
        self.assertNotEqual(EncounterStatus.UNMET, EncounterStatus.MET)

    def test_status_string_representation(self):
        """Test that status values have correct string representations."""
        self.assertEqual(str(EncounterStatus.UNMET), "Unmet")
        self.assertEqual(str(EncounterStatus.CAUGHT), "Caught")


class TestEncounter(unittest.TestCase):
    def setUp(self):
        """Set up common test data."""
        self.route = "Route 1"
        self.pokemon = Pokemon(
            name="Pikachu",
            gen=1,
            types=[Types.ELECTRIC],
            metadata=PokemonMetadata(id="025", nickname="Sparky")
        )

    def test_encounter_creation(self):
        """Test that an Encounter can be created with valid data."""
        encounter = Encounter(route=self.route, status=EncounterStatus.UNMET)
        self.assertEqual(encounter.route, self.route)
        self.assertEqual(encounter.status, EncounterStatus.UNMET)
        self.assertIsNone(encounter.pokemon)

    def test_encounter_with_pokemon(self):
        """Test that an Encounter can be created with a Pokemon."""
        encounter = Encounter(
            route=self.route,
            status=EncounterStatus.CAUGHT,
            pokemon=self.pokemon
        )
        self.assertEqual(encounter.route, self.route)
        self.assertEqual(encounter.status, EncounterStatus.CAUGHT)
        self.assertEqual(encounter.pokemon, self.pokemon)

    def test_is_caught(self):
        """Test the is_caught method."""
        # Test caught encounter
        caught_encounter = Encounter(
            route=self.route,
            status=EncounterStatus.CAUGHT,
            pokemon=self.pokemon
        )
        self.assertTrue(caught_encounter.is_caught())

        # Test non-caught encounter with pokemon
        met_encounter = Encounter(
            route=self.route,
            status=EncounterStatus.MET,
            pokemon=self.pokemon
        )
        self.assertFalse(met_encounter.is_caught())

        # Test caught encounter without pokemon
        invalid_caught = Encounter(
            route=self.route,
            status=EncounterStatus.CAUGHT
        )
        self.assertFalse(invalid_caught.is_caught())

    def test_encounter_equality(self):
        """Test that Encounter instances can be compared correctly."""
        encounter1 = Encounter(route=self.route, status=EncounterStatus.UNMET)
        encounter2 = Encounter(route=self.route, status=EncounterStatus.UNMET)
        encounter3 = Encounter(route="Route 2", status=EncounterStatus.UNMET)
        
        self.assertEqual(encounter1, encounter2)
        self.assertNotEqual(encounter1, encounter3)

    def test_encounter_string_representation(self):
        """Test that Encounter has a proper string representation."""
        encounter = Encounter(route=self.route, status=EncounterStatus.UNMET)
        expected_str = f"Encounter(route='{self.route}', status='Unmet', pokemon=None)"
        self.assertEqual(str(encounter), expected_str)


if __name__ == '__main__':
    unittest.main() 