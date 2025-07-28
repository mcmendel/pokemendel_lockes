from pokemendel_core.data.gen1 import PokemonGen1
from pokemendel_core.data import fetch_pokemon
from models.pokemon import generate_locke_pokemon
from core.lockes.base.run_creator import RunCreator
from core.lockes.base.base_locke import BaseLocke
from core.run import Run
from games import get_game


class EeveeRunCreator(RunCreator):
    def finish_creation(self, locke: BaseLocke) -> Run:
        created_run = super().finish_creation(locke)
        eevee_core_pokemon = fetch_pokemon(PokemonGen1.EEVEE, created_run.gen)
        eevee_run_pokemon = generate_locke_pokemon(
            run_id=created_run.id,
            pokemon_name=eevee_core_pokemon.name,
            gen=created_run.gen,
        )
        created_run.starter = eevee_run_pokemon
        locke.catch_pokemon(eevee_run_pokemon, created_run)
        for eevee_evolution in eevee_run_pokemon.evolves_to:
            evolution_core_pokemon = fetch_pokemon(eevee_evolution['name'], created_run.gen)
            evolution_run_pokemon = generate_locke_pokemon(
                run_id=created_run.id,
                pokemon_name=evolution_core_pokemon.name,
                gen=created_run.gen,
            )
            locke.catch_pokemon(evolution_run_pokemon, created_run)

        return created_run

    def _populate_run_optional_pokemons(self, run_id: str, locke: BaseLocke):
        game = get_game(self.run_creation.game)
        print("Storing all Eevee evolutions in pokemon options")
        eevee_pokemon = fetch_pokemon(name=PokemonGen1.EEVEE, gen=game.gen)
        current_index = 0
        self._save_pokemon_option(
            run_id=run_id,
            pokemon_name=eevee_pokemon.name,
            base_pokemon=eevee_pokemon.name,
            index=current_index,
            caught=True
        )
        for eevee_evolution in eevee_pokemon.evolves_to:
            current_index += 1
            self._save_pokemon_option(
                run_id=run_id,
                pokemon_name=eevee_evolution.name,
                base_pokemon=eevee_pokemon.name,
                index=current_index,
                caught=True
            )
