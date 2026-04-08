from pokemendel_core.data.gen3 import PokemonGen3
from pokemendel_core.data import fetch_pokemon
from models.pokemon import generate_locke_pokemon
from core.lockes.base.run_creator import RunCreator
from core.lockes.base.base_locke import BaseLocke
from core.run import Run
from games import get_game


class CastformRunCreator(RunCreator):
    def finish_creation(self, locke: BaseLocke) -> Run:
        created_run = super().finish_creation(locke)
        for castform_pokemon_name in [PokemonGen3.CASTFORM, PokemonGen3.CASTFORM_SUNNY, PokemonGen3.CASTFORM_RAINY, PokemonGen3.CASTFORM_SNOWY]:
            castform_core_pokemon = fetch_pokemon(castform_pokemon_name, created_run.gen)
            castform_run_pokemon = generate_locke_pokemon(
                run_id=created_run.id,
                pokemon_name=castform_core_pokemon.name,
                gen=created_run.gen,
            )
            if not created_run.starter:
                created_run.starter = castform_run_pokemon
            locke.catch_pokemon(castform_run_pokemon, created_run)

        return created_run

    def _populate_run_optional_pokemons(self, run_id: str, locke: BaseLocke):
        game = get_game(self.run_creation.game)
        print("Storing Castform in pokemon options")
        for castform_name in [PokemonGen3.CASTFORM, PokemonGen3.CASTFORM_SUNNY, PokemonGen3.CASTFORM_RAINY, PokemonGen3.CASTFORM_SNOWY]:
            castform_pokemon = fetch_pokemon(name=castform_name, gen=game.gen)
            self._save_pokemon_option(
                run_id=run_id,
                pokemon_name=castform_pokemon.name,
                base_pokemon=castform_pokemon.name,
                index=0,
                caught=True
            )
