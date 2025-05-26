"""Tests for the BaseLocke class.

This module contains tests for the BaseLocke class, verifying its functionality
as a base class for all Locke challenges.
"""

import unittest
from core.lockes.base.base_locke import BaseLocke
from definitions.runs.steps_names import StepsNames
from definitions.runs.steps_info import StepInfo

class TestBaseLocke(unittest.TestCase):
    """Test cases for the BaseLocke class."""

    def setUp(self):
        """Set up test fixtures."""
        self.base_locke = BaseLocke()

    def test_name(self):
        """Test that name is properly set."""
        self.assertEqual(BaseLocke.name, "BaseLocke")

    def test_min_gen(self):
        """Test that min_gen is properly set."""
        self.assertEqual(BaseLocke.min_gen, 1)

    def test_rules(self):
        """Test that rules are properly set."""
        rules = BaseLocke.rules
        self.assertIsInstance(rules, list)
        self.assertTrue(all(isinstance(rule, str) for rule in rules))
        self.assertEqual(len(rules), 3)
        self.assertEqual(rules[0], "Name each pokemon")
        self.assertEqual(rules[1], "Catch 1st encounter")
        self.assertEqual(rules[2], "Fainted pokemon considered dead")

    def test_steps(self):
        """Test that steps returns only optional steps with empty prerequisites."""
        steps = self.base_locke.steps
        self.assertIsInstance(steps, list)
        self.assertEqual(len(steps), 3)
        for step in steps:
            self.assertIn(step.step_name, [StepsNames.ADD_TO_PARTY, StepsNames.REMOVE_FROM_PARTY, StepsNames.SWITCH_PARTY_POKEMONS])
            self.assertEqual(step.prerequisites, [])

    def test_mandatory_steps(self):
        """Test that _mandatory_steps returns an empty list by default."""
        self.assertEqual(self.base_locke._mandatory_steps, [])

    def test_steps_mapper(self):
        """Test that steps_mapper contains all step implementations."""
        mapper = BaseLocke.steps_mapper
        self.assertIsInstance(mapper, dict)
        self.assertEqual(len(mapper), 3)
        self.assertIn(StepsNames.ADD_TO_PARTY, mapper)
        self.assertIn(StepsNames.REMOVE_FROM_PARTY, mapper)
        self.assertIn(StepsNames.SWITCH_PARTY_POKEMONS, mapper)

if __name__ == '__main__':
    unittest.main() 