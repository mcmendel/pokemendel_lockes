from pokemendel_core.data.gen1 import PokemonGen1
from pokemendel_core.data import fetch_pokemon
from core.lockes.starter.utils import get_gen_starters
from models.pokemon import generate_locke_pokemon
from core.lockes.base.run_creator import RunCreator
from core.lockes.base.base_locke import BaseLocke
from core.run import Run
from games import get_game


class StarterRunCreator(RunCreator):
    def finish_creation(self, locke: BaseLocke) -> Run:
        created_run = super().finish_creation(locke)
        game = get_game(self.run_creation.game)
        for gen in range(1, game.gen + 1):
            print(f"Populate starters for gen {gen}")
            gen_starters = get_gen_starters(gen)
            for cur_gen_starter in gen_starters:
                core_starter_pokemon = fetch_pokemon(cur_gen_starter, created_run.gen)
                run_starter_pokemon = generate_locke_pokemon(
                    run_id=created_run.id,
                    pokemon_name=core_starter_pokemon.name,
                    gen=created_run.gen,
                )
                if not created_run.starter:
                    created_run.starter = run_starter_pokemon
                locke.catch_pokemon(run_starter_pokemon, created_run)
        return created_run

    def _populate_run_optional_pokemons(self, run_id: str, locke: BaseLocke):
        game = get_game(self.run_creation.game)
        print("Storing all starters evolutions in pokemon options")
        current_index = 0
        for gen in range(1, game.gen + 1):
            print(f"Populate starters for gen {gen}")
            gen_starters = get_gen_starters(gen)
            for cur_gen_starter in gen_starters:
                self._save_pokemon_option(
                    run_id=run_id,
                    pokemon_name=cur_gen_starter,
                    base_pokemon=cur_gen_starter,
                    index=current_index,
                    caught=True
                )
                starter_pokemon = fetch_pokemon(cur_gen_starter, game.gen)
                current_index += 1
                mid_evolution_name = starter_pokemon.evolves_to[0].name
                self._save_pokemon_option(
                    run_id=run_id,
                    pokemon_name=mid_evolution_name,
                    base_pokemon=mid_evolution_name,
                    index=current_index,
                    caught=True
                )
                mid_evolution = fetch_pokemon(mid_evolution_name, game.gen)
                current_index += 1
                final_evolution_name = mid_evolution.evolves_to[0].name
                self._save_pokemon_option(
                    run_id=run_id,
                    pokemon_name=final_evolution_name,
                    base_pokemon=final_evolution_name,
                    index=current_index,
                    caught=True
                )
                current_index += 1
