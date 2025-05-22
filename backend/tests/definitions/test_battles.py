import unittest
from definitions.runs.battles import Battle


class TestBattle(unittest.TestCase):
    def test_battle_creation(self):
        """Test that a Battle can be created with valid data."""
        battle = Battle(rival="Gary", won=True)
        self.assertEqual(battle.rival, "Gary")
        self.assertTrue(battle.won)

    def test_battle_with_different_rival(self):
        """Test that a Battle can be created with a different rival."""
        battle = Battle(rival="Blue", won=False)
        self.assertEqual(battle.rival, "Blue")
        self.assertFalse(battle.won)

    def test_battle_equality(self):
        """Test that Battle instances can be compared correctly."""
        battle1 = Battle(rival="Gary", won=True)
        battle2 = Battle(rival="Gary", won=True)
        battle3 = Battle(rival="Blue", won=True)
        
        self.assertEqual(battle1, battle2)
        self.assertNotEqual(battle1, battle3)

    def test_battle_string_representation(self):
        """Test that Battle has a proper string representation."""
        battle = Battle(rival="Gary", won=True)
        expected_str = "Battle(rival='Gary', won=True)"
        self.assertEqual(str(battle), expected_str)


if __name__ == '__main__':
    unittest.main() 