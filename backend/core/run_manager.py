from pokemendel_core.data import fetch_pokemon
from models.run_pokemons_options import list_runs_options, mark_caught_pokemon
from models.run import update_run
from models.pokemon import save_pokemon
from dataclasses import dataclass, asdict
from definitions.pokemons.pokemon import Pokemon, PokemonMetadata, PokemonStatus
from core.locke import Locke
from core.run import Run, EncounterStatus, Battle
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
        self.run.starter = starter_pokemon
        self.locke.catch_pokemon(starter_pokemon, self.run)
        self.update_run()
        self._update_caught_pokemon(starter_pokemon)

    def encounter_pokemon(self, route: str, pokemon_name: str):
        route_encounters = [encounter for encounter in self.run.encounters if encounter.route == route]
        assert len(route_encounters) == 1
        route_encounter = route_encounters[0]
        assert not route_encounter.pokemon, f"Route {route} already has pokemon {route_encounter.pokemon}"
        assert route_encounter.status == EncounterStatus.UNMET, f"Empty route {route} should have status {EncounterStatus.UNMET}, but instead has status {route_encounter.status}"
        assert route in self.game.routes, f"Route {route} does not exist in game {self.game.name}"
        route_encounter.pokemon = pokemon_name
        route_encounter.status = EncounterStatus.MET
        self.update_run()

    def update_encounter(self, route: str, encounter_status: str):
        assert encounter_status in [EncounterStatus.CAUGHT, EncounterStatus.RAN, EncounterStatus.RAN], f"Encounter status {encounter_status} is invalid"
        route_encounters = [encounter for encounter in self.run.encounters if encounter.route == route]
        assert len(route_encounters) == 1
        route_encounter = route_encounters[0]
        assert route_encounter.pokemon, f"Route {route} already does not have pokemon for status update"
        assert route_encounter.status == EncounterStatus.MET, f"Route {route} should have status {EncounterStatus.MET}, but instead has status {route_encounter.status}"
        assert route in self.game.routes, f"Route {route} does not exist in game {self.game.name}"
        route_encounter.status = encounter_status

        if encounter_status == EncounterStatus.CAUGHT:
            assert isinstance(route_encounter.pokemon, str), f"Uncaught pokemon in route {route_encounter.route} should have been string"
            caught_pokemon = self._catch_pokemon(route_encounter.pokemon)
            route_encounter.pokemon = caught_pokemon

        self.update_run()

    def _generate_locke_pokemon(self, pokemon_name: str) -> Pokemon:
        core_pokemon = fetch_pokemon(pokemon_name, self.game.gen)
        pokemon_core_attributes = asdict(core_pokemon)
        locke_pokemon = Pokemon(**pokemon_core_attributes, metadata=PokemonMetadata(id=uuid4().hex),  status=PokemonStatus.ALIVE)
        save_pokemon(locke_pokemon, self.run.id)
        return locke_pokemon

    def _update_caught_pokemon(self, pokemon: Pokemon):
        mark_caught_pokemon(self.run.id, pokemon.name)

    def update_run(self):
        print("Saving run %s" % self.run.id)
        db_run = self.run.to_db_run(self.game.gen, self.locke.name, self.game.name, self.randomized, self.duplicate_clause, self.locke.extra_info)
        update_run(db_run)

    def win_battle(self, leader: str):
        print("Winning battle %s in run %s" % (leader, self.run.id))
        try:
            run_battle = next(battle for battle in self.run.battles if battle.rival == leader)
            run_battle.won = True
        except StopIteration:
            self.run.battles.append(Battle(leader, True))

        self.update_run()

    def _catch_pokemon(self, pokemon_name: str) -> Pokemon:
        new_pokemon = self._generate_locke_pokemon(pokemon_name)
        self.locke.catch_pokemon(new_pokemon, self.run)
        self._update_caught_pokemon(new_pokemon)
        return new_pokemon

