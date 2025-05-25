"""Tests for the StepInterface and ExecutionReturnValue classes."""

import unittest
from definitions.runs.steps_interface import StepInterface, ExecutionReturnValue
from unittest.mock import MagicMock
from core.run_manager import RunManager
from definitions import Pokemon


class TestStepInterface(unittest.TestCase):
    """Test cases for the StepInterface abstract class."""

    def test_step_options_abstract(self):
        """Test that step_options is an abstract method."""
        with self.assertRaises(TypeError):
            StepInterface()

    def test_is_step_relevant_abstract(self):
        """Test that is_step_relevant is an abstract method."""
        class ConcreteStep(StepInterface):
            def step_options(self, run: RunManager, pokemon: Pokemon):
                return None, []

            def execute_step(self, run: RunManager, pokemon: Pokemon, value: str):
                return ExecutionReturnValue([])

        with self.assertRaises(TypeError):
            ConcreteStep()

    def test_execute_step_abstract(self):
        """Test that execute_step is an abstract method."""
        class ConcreteStep(StepInterface):
            def step_options(self, run: RunManager, pokemon: Pokemon):
                return None, []

            def is_step_relevant(self, run: RunManager, pokemon: Pokemon):
                return True

        with self.assertRaises(TypeError):
            ConcreteStep()


class TestExecutionReturnValue(unittest.TestCase):
    """Test cases for the ExecutionReturnValue dataclass."""

    def test_init(self):
        """Test initialization of ExecutionReturnValue."""
        pokemons = ["Pikachu", "Charizard"]
        return_value = ExecutionReturnValue(pokemons_to_update=pokemons)
        self.assertEqual(return_value.pokemons_to_update, pokemons)

    def test_empty_list(self):
        """Test initialization with empty list."""
        return_value = ExecutionReturnValue(pokemons_to_update=[])
        self.assertEqual(return_value.pokemons_to_update, [])


if __name__ == '__main__':
    unittest.main() 