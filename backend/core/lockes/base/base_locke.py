"""Base class for all Locke challenges that inherits from the abstract Locke class.
This class implements the abstract _mandatory_steps property and provides a base for all Locke challenges.
"""

from core.locke import Locke, Pokemon
from definitions.runs.steps_info import StepInfo
from definitions.runs.steps_names import StepsNames
from definitions.runs.steps_interface import StepInterface
from core.steps import (
    AddToPartyStep,
    RemoveFromPartyStep,
    ReplacePartyPokemon,
    NicknamePokemonStep,
    ChooseGenderStep,
    EvolvePokemonStep,
    KillPokemonStep,
)
from core.run import Run
from pokemendel_core.utils.class_property import classproperty
from typing import List, Dict, ClassVar

class BaseLocke(Locke):
    """Base class for all Locke challenges.
    This class implements the abstract _mandatory_steps property and provides a base for all Locke challenges.
    """
    # Default rules that apply to all Locke challenges
    _DEFAULT_RULES: ClassVar[List[str]] = [
        "Name each pokemon",
        "Catch 1st encounter",
        "Fainted pokemon considered dead"
    ]

    @classproperty
    def name(cls) -> str:
        """Get the name of the Locke challenge.
        Returns:
            str: The name of the Locke challenge, derived from the class name
        """
        return cls.__name__

    @classproperty
    def min_gen(cls) -> int:
        """Get the minimum generation of Pokemon games supported by this Locke.
        Returns:
            int: The minimum generation number (1-9)
        """
        return 1

    @classproperty
    def rules(cls) -> List[str]:
        """Get the list of rules for this Locke challenge.
        This method combines the default rules with any additional rules defined by the subclass.
        Subclasses can override this method to add their own rules while still including the defaults.
        Returns:
            List[str]: A list of rules that must be followed
        """
        return cls._DEFAULT_RULES.copy()

    def steps(self, gen: int) -> List[StepInfo]:
        """Get all steps for this Locke challenge, including mandatory and optional steps.
        The steps include:
        - Mandatory steps that must be completed in order (can be empty)
        - Optional steps (add to party, remove from party, switch party pokemon) that can be done after any mandatory step
        Returns:
            List[StepInfo]: A list of all steps with their prerequisites
        """
        mandatory_steps = self._mandatory_steps(gen)
        prerequisites = [step_info.step_name for step_info in mandatory_steps]
        optional_steps = [
            StepInfo(StepsNames.ADD_TO_PARTY, prerequisites=prerequisites),
            StepInfo(StepsNames.REMOVE_FROM_PARTY, prerequisites=prerequisites),
            StepInfo(StepsNames.SWITCH_PARTY_POKEMONS, prerequisites=prerequisites),
            StepInfo(StepsNames.EVOLVE, prerequisites=prerequisites),
            StepInfo(StepsNames.KILL, prerequisites=prerequisites),
        ]
        return mandatory_steps + optional_steps

    def _mandatory_steps(self, gen: int) -> List[StepInfo]:
        """Get the mandatory steps that must be completed in order.
        This implementation returns an empty list, allowing subclasses to override it.
        Returns:
            List[StepInfo]: A list of steps that must be completed in order
        """
        mandatory_steps = [StepInfo(StepsNames.NICKNAME, prerequisites=[])]
        if gen >= 2:
            mandatory_steps.append(StepInfo(StepsNames.GENDER, prerequisites=[StepsNames.NICKNAME]))
        return mandatory_steps

    @classproperty
    def steps_mapper(cls) -> Dict[StepsNames, StepInterface]:
        """Get a mapping of step names to their implementations.
        Returns:
            Dict[StepsNames, StepInterface]: A dictionary mapping step names to their implementations
        """
        return {
            StepsNames.ADD_TO_PARTY: AddToPartyStep(),
            StepsNames.REMOVE_FROM_PARTY: RemoveFromPartyStep(),
            StepsNames.SWITCH_PARTY_POKEMONS: ReplacePartyPokemon(),
            StepsNames.NICKNAME: NicknamePokemonStep(),
            StepsNames.GENDER: ChooseGenderStep(),
            StepsNames.EVOLVE: EvolvePokemonStep(),
            StepsNames.KILL: KillPokemonStep(),
        }

    def catch_pokemon(self, pokemon: Pokemon, run: Run):
        run.box.add_pokemon(pokemon)
        if not run.party.is_party_full():
            run.party.add_pokemon(pokemon)
