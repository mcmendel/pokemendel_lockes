from definitions import Pokemon
from definitions.runs.steps_interface import ExecutionReturnValue, StepInterface
from definitions.runs.inputs_options import InputOptions
from pokemendel_core.utils.definitions.genders import Genders
from core.run import Run
from typing import Tuple, List, Optional


class PairPokemonStep(StepInterface):
    def is_step_relevant(self, run: Run, pokemon: Pokemon) -> bool:
        return not pokemon.metadata.paired and pokemon.metadata.gender in [Genders.MALE, Genders.FEMALE]

    def step_options(self, run: Run, pokemon: Pokemon) -> Tuple[InputOptions, List[str]]:
        partner_gender = self._get_opposite_gender(pokemon)
        relevant_pokemons = [box_pokemon.metadata.id for box_pokemon in run.box.pokemons if not box_pokemon.metadata.paired and box_pokemon.metadata.gender == partner_gender]
        return InputOptions.ONE_OF, relevant_pokemons

    def execute_step(self, run: Run, pokemon: Pokemon, value: Optional[str]) -> ExecutionReturnValue:
        partner_pokemon = run.box.get_pokemon_by_id(value)
        assert partner_pokemon, "Not existing pokemon was given"
        assert not partner_pokemon.metadata.paired and not pokemon.metadata.paired
        expected_partner_gender = self._get_opposite_gender(pokemon)
        assert partner_pokemon.metadata.gender == expected_partner_gender

        partner_pokemon.metadata.paired = pokemon.metadata.id
        pokemon.metadata.paired = partner_pokemon.metadata.id
        self._add_couple_to_party_if_needed(run, pokemon, partner_pokemon)
        return ExecutionReturnValue(pokemons_to_update=[pokemon.metadata.id, partner_pokemon.metadata.id])

    def _add_couple_to_party_if_needed(self, run: Run, partner1: Pokemon, partner2: Pokemon):
        if not run.party.is_pokemon_in_party(partner1) and not run.party.is_pokemon_in_party(partner2):
            return
        if run.party.is_pokemon_in_party(partner1) and run.party.is_pokemon_in_party(partner2):
            return

        if run.party.is_pokemon_in_party(partner1):
            run.party.add_pokemon(partner2)
        else:
            run.party.add_pokemon(partner1)

    def _get_opposite_gender(self, pokemon: Pokemon) -> str:
        assert pokemon.metadata.gender in [Genders.MALE, Genders.FEMALE], "Can't get opposite gender to non male/female genders"
        opposite_genders = {
            Genders.MALE: Genders.FEMALE,
            Genders.FEMALE: Genders.MALE,
        }
        return opposite_genders[pokemon.metadata.gender]


