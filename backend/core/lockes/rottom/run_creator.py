from pokemendel_core.data.gen4 import PokemonGen4
from pokemendel_core.data import fetch_pokemon
from models.pokemon import generate_locke_pokemon
from core.lockes.base.run_creator import RunCreator
from core.lockes.base.base_locke import BaseLocke
from core.run import Run
from games import get_game


class RottomRunCreator(RunCreator):
    def finish_creation(self, locke: BaseLocke) -> Run:
        created_run = super().finish_creation(locke)
        rottom_core_pokemon = fetch_pokemon(PokemonGen4.ROTOM, created_run.gen)
        rottom_run_pokemon = generate_locke_pokemon(
            run_id=created_run.id,
            pokemon_name=rottom_core_pokemon.name,
            gen=created_run.gen,
        )
        created_run.starter = rottom_run_pokemon
        locke.catch_pokemon(rottom_run_pokemon, created_run)
        for rottom_form in ["Heat", "Fan", "Frost", "Wash"]:
            form_run_pokemon = generate_locke_pokemon(
                run_id=created_run.id,
                pokemon_name=rottom_core_pokemon.name,
                gen=created_run.gen,
            )
            locke.catch_pokemon(form_run_pokemon, created_run)

        return created_run

    def _populate_run_optional_pokemons(self, run_id: str, locke: BaseLocke):
        game = get_game(self.run_creation.game)
        print("Storing Rottom in pokemon options")
        rottom_pokemon = fetch_pokemon(name=PokemonGen4.ROTOM, gen=game.gen)
        self._save_pokemon_option(
            run_id=run_id,
            pokemon_name=rottom_pokemon.name,
            base_pokemon=rottom_pokemon.name,
            index=0,
            caught=True
        )
