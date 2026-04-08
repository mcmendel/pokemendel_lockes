from pokemendel_core.data.gen3 import PokemonGen3
from pokemendel_core.data import fetch_pokemon
from models.pokemon import generate_locke_pokemon
from core.lockes.base.run_creator import RunCreator
from core.lockes.base.base_locke import BaseLocke
from core.run import Run
from games import get_game


class DeoxysRunCreator(RunCreator):
    def finish_creation(self, locke: BaseLocke) -> Run:
        created_run = super().finish_creation(locke)
        for deoxys_pokemon_name in [PokemonGen3.DEOXYS, PokemonGen3.DEOXYS_ATTACK, PokemonGen3.DEOXYS_DEFENSE, PokemonGen3.DEOXYS_SPEED]:
            deoxys_core_pokemon = fetch_pokemon(deoxys_pokemon_name, created_run.gen)
            deoxys_run_pokemon = generate_locke_pokemon(
                run_id=created_run.id,
                pokemon_name=deoxys_core_pokemon.name,
                gen=created_run.gen,
            )
            if not created_run.starter:
                created_run.starter = deoxys_run_pokemon
            locke.catch_pokemon(deoxys_run_pokemon, created_run)

        return created_run

    def _populate_run_optional_pokemons(self, run_id: str, locke: BaseLocke):
        game = get_game(self.run_creation.game)
        print("Storing Deoxys in pokemon options")
        for deoxys_name in [PokemonGen3.DEOXYS, PokemonGen3.DEOXYS_ATTACK, PokemonGen3.DEOXYS_DEFENSE, PokemonGen3.DEOXYS_SPEED]:
            deoxys_pokemon = fetch_pokemon(name=deoxys_name, gen=game.gen)
            self._save_pokemon_option(
                run_id=run_id,
                pokemon_name=deoxys_pokemon.name,
                base_pokemon=deoxys_pokemon.name,
                index=0,
                caught=True
            )
