from pokemendel_core.data.gen1 import PokemonGen1
from pokemendel_core.data import fetch_pokemon
from pokemendel_core.data import list_gen_pokemons, Pokemon as CorePokemon
from pokemendel_core.utils.evolutions import iterate_gen_evolution_lines
from pokemendel_core.utils.definitions.types import get_generation_types
from models.pokemon import generate_locke_pokemon
from core.lockes.base.run_creator import RunCreator, RunCreationProgress
from core.lockes.base.base_locke import BaseLocke
from core.run import Run
from games import get_game
from typing import Dict, Set
from collections import defaultdict

_STARTER = "star_starter"
_TEAM1 = "star_team1"
_TEAM2 = "star_team2"
_TEAM3 = "star_team3"
_TEAM4 = "star_team4"
_TEAM5 = "star_team5"


class StarRunCreator(RunCreator):
    def finish_creation(self, locke: BaseLocke) -> Run:
        created_run = super().finish_creation(locke)
        pokemon_to_base = self._map_pokemons_to_base(created_run.gen)
        pokemon_to_type = {
            self.run_creation.extra_info[cur_type]: cur_type for cur_type
            in get_generation_types(created_run.gen)
        }
        created_pokemons = {
            self.run_creation.extra_info[_STARTER],
            self.run_creation.extra_info[_TEAM1],
            self.run_creation.extra_info[_TEAM2],
            self.run_creation.extra_info[_TEAM3],
            self.run_creation.extra_info[_TEAM4],
            self.run_creation.extra_info[_TEAM5],
        }
        starter_core_pokemon = fetch_pokemon(pokemon_to_base[self.run_creation.extra_info[_STARTER]], created_run.gen)

        starter_run_pokemon = generate_locke_pokemon(
            run_id=created_run.id,
            pokemon_name=starter_core_pokemon.name,
            gen=created_run.gen,
            extra_metadata={
                'starlocke_type': pokemon_to_type[self.run_creation.extra_info[_STARTER]]
            }
        )
        created_run.starter = starter_run_pokemon
        locke.catch_pokemon(starter_run_pokemon, created_run)
        for team_member in [
            self.run_creation.extra_info[_TEAM1],
            self.run_creation.extra_info[_TEAM2],
            self.run_creation.extra_info[_TEAM3],
            self.run_creation.extra_info[_TEAM4],
            self.run_creation.extra_info[_TEAM5],
        ]:
            team_core_pokemon = fetch_pokemon(pokemon_to_base[team_member], created_run.gen)
            team_run_pokemon = generate_locke_pokemon(
                run_id=created_run.id,
                pokemon_name=team_core_pokemon.name,
                gen=created_run.gen,
                extra_metadata={
                'starlocke_type': pokemon_to_type[team_member]
            }
            )
            locke.catch_pokemon(team_run_pokemon, created_run)

        for star_type in get_generation_types(created_run.gen):
            chosen_pokemon_name = self.run_creation.extra_info[star_type]
            base_pokemon_name = pokemon_to_base[chosen_pokemon_name]
            if chosen_pokemon_name in created_pokemons:
                continue
            core_pokemon = fetch_pokemon(base_pokemon_name, created_run.gen)
            run_pokemon = generate_locke_pokemon(
                run_id=created_run.id,
                pokemon_name=core_pokemon.name,
                gen=created_run.gen,
                extra_metadata={
                    'starlocke_type': star_type,
                }
            )
            locke.catch_pokemon(run_pokemon, created_run)

        return created_run

    # def _populate_run_optional_pokemons(self, run_id: str, locke: BaseLocke):
    #     pass
        # game = get_game(self.run_creation.game)
        # print("Storing all Eevee evolutions in pokemon options")
        # eevee_pokemon = fetch_pokemon(name=PokemonGen1.EEVEE, gen=game.gen)
        # current_index = 0
        # self._save_pokemon_option(
        #     run_id=run_id,
        #     pokemon_name=eevee_pokemon.name,
        #     base_pokemon=eevee_pokemon.name,
        #     index=current_index,
        #     caught=True
        # )
        # for eevee_evolution in eevee_pokemon.evolves_to:
        #     current_index += 1
        #     self._save_pokemon_option(
        #         run_id=run_id,
        #         pokemon_name=eevee_evolution.name,
        #         base_pokemon=eevee_pokemon.name,
        #         index=current_index,
        #         caught=True
        #     )

    def _get_creation_missing_extra_info(self) -> RunCreationProgress:
        game = get_game(self.run_creation.game)
        pokemon_to_base = self._map_pokemons_to_base(game.gen)
        found_bases = {
            pokemon_to_base[self.run_creation.extra_info[cur_type]]
            for cur_type in get_generation_types(game.gen)
            if cur_type in self.run_creation.extra_info
        }

        types_mapper = self._map_relevant_types(game.gen, found_bases)
        sorted_types = sorted(types_mapper.keys(), key=lambda x: len(types_mapper[x]))

        for pokemon_type in sorted_types:
            if pokemon_type not in self.run_creation.extra_info:
                return RunCreationProgress(
                    self.run_creation,
                    has_all_info=False,
                    missing_key=pokemon_type,
                    missing_key_options=list(types_mapper[pokemon_type]),
                )

        chosen_pokemons = [
            self.run_creation.extra_info[cur_type]
            for cur_type in get_generation_types(game.gen)
        ]
        for selected_team_member in [
            _STARTER, _TEAM1, _TEAM2, _TEAM3, _TEAM4, _TEAM5
        ]:
            if selected_team_member not in self.run_creation.extra_info:
                return RunCreationProgress(
                    self.run_creation,
                    has_all_info=False,
                    missing_key=selected_team_member,
                    missing_key_options=chosen_pokemons,
                )
            chosen_pokemons = [team_pokemon for team_pokemon in chosen_pokemons if team_pokemon != selected_team_member]
        return RunCreationProgress(run_creation=self.run_creation, has_all_info=True)

    def _map_relevant_types(self, gen: int, found_bases: Set[str]) -> Dict[str, Set[str]]:
        types_pokemons = defaultdict(set)

        for evolution_line in iterate_gen_evolution_lines(gen, reversed=True):
            if evolution_line[-1] in found_bases:
                continue
            for evolution_pokemon_name in evolution_line:
                evolution_pokemon = fetch_pokemon(evolution_pokemon_name, gen)
                if evolution_pokemon.evolves_to:
                    continue
                for evolution_type in evolution_pokemon.types:
                    if evolution_type in self.run_creation.extra_info:
                        continue
                    types_pokemons[evolution_type].add(evolution_pokemon.name)
        return types_pokemons

    def _map_pokemons_to_base(self, gen: int) -> Dict[str, str]:
        pokemon_to_base_map = {}
        for evolution_line in iterate_gen_evolution_lines(gen, reversed=True):
            for evolution_pokemon_name in evolution_line:
                evolution_pokemon = fetch_pokemon(evolution_pokemon_name, gen)
                if evolution_pokemon.evolves_to:
                    continue
                pokemon_to_base_map[evolution_pokemon_name] = evolution_line[-1]

        return pokemon_to_base_map
