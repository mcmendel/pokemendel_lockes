from pokemendel_core.data import fetch_pokemon
from models.run_pokemons_options import list_runs_options
from models.run import update_run
from models.pokemon import save_pokemon
from dataclasses import dataclass, asdict
from definitions.pokemons.pokemon import Pokemon, PokemonMetadata, PokemonStatus
from core.locke import Locke
from core.run import Run
from games import Game
from typing import List
from uuid import uuid4

@dataclass
class RunManager:
    run: Run
    locke: Locke
    game: Game
    duplicate_clause: bool
    randomized: bool

    def get_starter_options(self) -> List[str]:
        print("Getting starter options")
        assert not self.run.starter, "Can't ask for starters if run's starter already applied"
        run_options = list_runs_options(self.run.id)
        base_options = {option.base_pokemon for option in run_options}
        if self.randomized:
            print("Getting all %s base pokemons as starters for randomized run" % len(base_options))
            return list(base_options)
        print("Returning game starters for randomized run")
        relevant_game_starters = [
            game_starter.name for game_starter in self.game.starters
            if game_starter.name in base_options
        ]
        if relevant_game_starters:
            print("Return relevant game starters %s" % relevant_game_starters)
            return relevant_game_starters

        print("No game starter is relevant, return all %s options" % len(base_options))
        return list(base_options)
    
    def choose_starter(self, pokemon_name: str):
        print("Run %s choosing %s as starter" % (self.run.id, pokemon_name))
        run_options = {pokemon.pokemon_name for pokemon in list_runs_options(self.run.id)}
        assert pokemon_name in run_options, f"Pokemon {pokemon_name} is not valid"
        starter_pokemon = self._generate_locke_pokemon(pokemon_name=pokemon_name)
        save_pokemon(starter_pokemon, self.run.id)
        self.run.starter = starter_pokemon
        self.locke.catch_pokemon(starter_pokemon, self.run)
        db_run = self.run.to_db_run(self.game.gen, self.locke.name, self.game.name, self.randomized, self.duplicate_clause, self.locke.extra_info)
        update_run(db_run)

    def _generate_locke_pokemon(self, pokemon_name: str) -> Pokemon:
        core_pokemon = fetch_pokemon(pokemon_name, self.game.gen)
        pokemon_core_attributes = asdict(core_pokemon)
        return Pokemon(**pokemon_core_attributes, metadata=PokemonMetadata(id=uuid4().hex),  status=PokemonStatus.ALIVE)

