import unittest
from unittest.mock import Mock, patch
from core.steps_interface import StepInterface, ExecutionReturnValue
from definitions import Pokemon, InputOptions
from core.run_manager import RunManager


class TestStepInterface(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        # Create a concrete implementation of StepInterface for testing
        class TestStep(StepInterface):
            def step_options(self, run, pokemon):
                return InputOptions.ONE_OF, ["option1", "option2"]

            def is_step_relevant(self, run, pokemon):
                return True

            def execute_step(self, run, pokemon, value):
                return ExecutionReturnValue(pokemons_to_update=["pokemon1"])

        self.test_step = TestStep()
        self.mock_run = Mock(spec=RunManager)
        self.mock_pokemon = Mock(spec=Pokemon)

    def test_step_options(self):
        """Test that step_options returns the correct tuple of InputOptions and list."""
        options, choices = self.test_step.step_options(self.mock_run, self.mock_pokemon)
        self.assertEqual(options, InputOptions.ONE_OF)
        self.assertEqual(choices, ["option1", "option2"])

    def test_is_step_relevant(self):
        """Test that is_step_relevant returns the correct boolean."""
        self.assertTrue(self.test_step.is_step_relevant(self.mock_run, self.mock_pokemon))

    def test_execute_step(self):
        """Test that execute_step returns an ExecutionReturnValue with the correct pokemons."""
        result = self.test_step.execute_step(self.mock_run, self.mock_pokemon, "option1")
        self.assertIsInstance(result, ExecutionReturnValue)
        self.assertEqual(result.pokemons_to_update, ["pokemon1"])

    def test_step_options_free_text(self):
        """Test step_options with FREE_TEXT input type."""
        class FreeTextStep(StepInterface):
            def step_options(self, run, pokemon):
                return InputOptions.FREE_TEXT, []

            def is_step_relevant(self, run, pokemon):
                return True

            def execute_step(self, run, pokemon, value):
                return ExecutionReturnValue(pokemons_to_update=[])

        step = FreeTextStep()
        options, choices = step.step_options(self.mock_run, self.mock_pokemon)
        self.assertEqual(options, InputOptions.FREE_TEXT)
        self.assertEqual(choices, [])

    def test_step_options_nothing(self):
        """Test step_options with NOTHING input type."""
        class NothingStep(StepInterface):
            def step_options(self, run, pokemon):
                return InputOptions.NOTHING, []

            def is_step_relevant(self, run, pokemon):
                return True

            def execute_step(self, run, pokemon, value):
                return ExecutionReturnValue(pokemons_to_update=[])

        step = NothingStep()
        options, choices = step.step_options(self.mock_run, self.mock_pokemon)
        self.assertEqual(options, InputOptions.NOTHING)
        self.assertEqual(choices, [])


class TestExecutionReturnValue(unittest.TestCase):
    def test_execution_return_value_creation(self):
        """Test that ExecutionReturnValue is created with the correct pokemons list."""
        pokemons = ["pokemon1", "pokemon2"]
        result = ExecutionReturnValue(pokemons_to_update=pokemons)
        self.assertEqual(result.pokemons_to_update, pokemons)

    def test_execution_return_value_empty_list(self):
        """Test that ExecutionReturnValue can be created with an empty list."""
        result = ExecutionReturnValue(pokemons_to_update=[])
        self.assertEqual(result.pokemons_to_update, [])


if __name__ == '__main__':
    unittest.main() 