import pytest
from definitions.runs.inputs_options import InputOptions
from definitions.runs.steps_info import StepInfo
from definitions.runs.steps_names import StepsNames


class TestInputOptions:
    def test_input_options_values(self):
        """Test that InputOptions has the correct values."""
        assert InputOptions.FREE_TEXT == "Free text"
        assert InputOptions.ONE_OF == "One of"
        assert InputOptions.NOTHING == "Nothing"

    def test_input_options_equality(self):
        """Test that InputOptions values can be compared correctly."""
        assert InputOptions.FREE_TEXT == InputOptions.FREE_TEXT
        assert InputOptions.FREE_TEXT != InputOptions.ONE_OF
        assert InputOptions.FREE_TEXT != InputOptions.NOTHING

    def test_input_options_string_representation(self):
        """Test the string representation of InputOptions values."""
        assert str(InputOptions.FREE_TEXT) == "Free text"
        assert str(InputOptions.ONE_OF) == "One of"
        assert str(InputOptions.NOTHING) == "Nothing"


class TestStepInfo:
    def test_step_info_creation(self):
        """Test creating a StepInfo with default prerequisites."""
        step = StepInfo("Test Step")
        assert step.step_name == "Test Step"
        assert step.prerequisites == []

    def test_step_info_with_prerequisites(self):
        """Test creating a StepInfo with specific prerequisites."""
        prerequisites = ["Step 1", "Step 2"]
        step = StepInfo("Test Step", prerequisites)
        assert step.step_name == "Test Step"
        assert step.prerequisites == prerequisites

    def test_step_info_equality(self):
        """Test that StepInfo instances can be compared correctly."""
        step1 = StepInfo("Test Step", ["Step 1"])
        step2 = StepInfo("Test Step", ["Step 1"])
        step3 = StepInfo("Different Step", ["Step 1"])
        step4 = StepInfo("Test Step", ["Step 2"])

        assert step1 == step2
        assert step1 != step3
        assert step1 != step4

    def test_step_info_string_representation(self):
        """Test the string representation of StepInfo."""
        step = StepInfo("Test Step", ["Step 1", "Step 2"])
        expected = "StepInfo(step_name='Test Step', prerequisites=['Step 1', 'Step 2'])"
        assert str(step) == expected


class TestStepsNames:
    def test_steps_names_values(self):
        """Test that StepsNames has the correct values."""
        # Party steps
        assert StepsNames.ADD_TO_PARTY == "Add to Party"
        assert StepsNames.REMOVE_FROM_PARTY == "Remove from Party"
        assert StepsNames.SWITCH_PARTY_POKEMONS == "Replace Pokemon with Party"

        # Pokemon actions
        assert StepsNames.EVOLVE == "Evolve Pokemon"
        assert StepsNames.KILL == "Kill Pokemon"

        # Pokemon attributes
        assert StepsNames.NICKNAME == "Nickname Pokemon"

        # Starlocke
        assert StepsNames.STARLOCKE_CHOOSE_TYPE == "Choose Type"

    def test_steps_names_equality(self):
        """Test that StepsNames values can be compared correctly."""
        assert StepsNames.ADD_TO_PARTY == StepsNames.ADD_TO_PARTY
        assert StepsNames.ADD_TO_PARTY != StepsNames.REMOVE_FROM_PARTY
        assert StepsNames.EVOLVE != StepsNames.KILL

    def test_steps_names_string_representation(self):
        """Test the string representation of StepsNames values."""
        assert str(StepsNames.ADD_TO_PARTY) == "Add to Party"
        assert str(StepsNames.EVOLVE) == "Evolve Pokemon"
        assert str(StepsNames.NICKNAME) == "Nickname Pokemon" 