from pokemendel_core.data.gen1 import PokemonGen1
from pokemendel_core.data.gen2 import PokemonGen2
from pokemendel_core.utils.definitions.types import Types, get_generation_types
from tests.e2e.gen1_helpers import (
    GAME_NAME as GEN1_GAME_NAME,
    NUM_POKEMONS as GEN1_NUM_POKEMONS,
    NUM_ENCOUNTERS as GEN1_NUM_ENCOUNTERS,
    STARTERS as GEN1_STARTERS,
)
from tests.e2e.gen2_helpers import (
    GAME_NAME as GEN2_GAME_NAME,
    NUM_POKEMONS as GEN2_NUM_POKEMONS,
    NUM_ENCOUNTERS as GEN2_NUM_ENCOUNTERS,
    STARTERS as GEN2_STARTERS,
)
from tests.e2e.helpers import (
    client_fixture,
    list_runs,
    list_lockes,
    start_locke_creation,
    continue_locke_creation_not_finished,
    continue_locke_creation_finished,
    get_run,
    save_run,
    load_run,
    get_starter_options,
    get_run_supported_pokemons,
    get_run_potential_encounters,
    choose_starter,
    encounter_pokemon,
    update_encounter,
    get_next_actions,
    get_action_options,
    execute_action,
    win_battle,
    finish_run,
    assert_run,
    assert_saved_run,
    assert_run_potential_pokemons,
    assert_pokemon,
)
from typing import List, Tuple, Dict
import pytest


TEST_LOCKE = "StarLocke"


def test_base_gen1(client_fixture):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture, GEN1_GAME_NAME, [
            [Types.DRAGON, Types.GHOST],
            [Types.ICE, Types.FIGHTING],
            [Types.BUG, Types.ELECTRIC, Types.GRASS, Types.ROCK, Types.FIRE, Types.GROUND, Types.PSYCHIC],
            [Types.POISON, Types.FLYING],
            [Types.NORMAL, Types.WATER],
        ],
        {
            Types.DRAGON: (PokemonGen1.DRAGONITE, PokemonGen1.DRATINI),
            Types.GHOST: (PokemonGen1.GENGAR, PokemonGen1.GASTLY),
            Types.ICE: (PokemonGen1.DEWGONG, PokemonGen1.SEEL),
            Types.FIGHTING: (PokemonGen1.HITMONLEE, PokemonGen1.HITMONLEE),
            Types.BUG: (PokemonGen1.BUTTERFREE, PokemonGen1.CATERPIE),
            Types.ELECTRIC: (PokemonGen1.RAICHU, PokemonGen1.PIKACHU),
            Types.GRASS: (PokemonGen1.PARASECT, PokemonGen1.PARAS),
            Types.ROCK: (PokemonGen1.ONIX, PokemonGen1.ONIX),
            Types.FIRE: (PokemonGen1.CHARIZARD, PokemonGen1.CHARMANDER),
            Types.GROUND: (PokemonGen1.MAROWAK, PokemonGen1.CUBONE),
            Types.PSYCHIC: (PokemonGen1.MR_MIME, PokemonGen1.MR_MIME),
            Types.POISON: (PokemonGen1.WEEZING, PokemonGen1.KOFFING),
            Types.FLYING: (PokemonGen1.ZAPDOS, PokemonGen1.ZAPDOS),
            Types.NORMAL: (PokemonGen1.WIGGLYTUFF, PokemonGen1.JIGGLYPUFF),
            Types.WATER: (PokemonGen1.BLASTOISE, PokemonGen1.SQUIRTLE),
        }
    )
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['pokemons']) == len(get_generation_types(1))
    star_types = {
        pokemon['metadata']['starlocke_type']
        for pokemon in run_response['pokemons'].values()
    }
    assert star_types == set(get_generation_types(1))
    print("TEST Finished")


def test_base_gen2(client_fixture):
    """Test that the list_runs endpoint works with e2e_ prefixed collections."""
    # ==== CREATE RUN ====
    run_id = _create_run(client_fixture, GEN2_GAME_NAME, [
            [Types.DRAGON, Types.GHOST],
            [Types.DARK, Types.STEEL],
            [Types.ICE, Types.FIGHTING],
            [Types.BUG, Types.ELECTRIC, Types.GRASS, Types.ROCK, Types.FIRE, Types.GROUND],
            [Types.POISON, Types.FLYING, Types.PSYCHIC],
            [Types.NORMAL, Types.WATER],
        ],
        {
            Types.DRAGON: (PokemonGen2.DRAGONITE, PokemonGen2.DRATINI),
            Types.GHOST: (PokemonGen2.GENGAR, PokemonGen2.GASTLY),
            Types.ICE: (PokemonGen2.DEWGONG, PokemonGen1.SEEL),
            Types.FIGHTING: (PokemonGen2.HITMONLEE, PokemonGen2.TYROGUE),
            Types.BUG: (PokemonGen2.BUTTERFREE, PokemonGen2.CATERPIE),
            Types.ELECTRIC: (PokemonGen2.RAICHU, PokemonGen2.PICHU),
            Types.GRASS: (PokemonGen2.PARASECT, PokemonGen2.PARAS),
            Types.STEEL: (PokemonGen2.STEELIX, PokemonGen2.ONIX),
            Types.FIRE: (PokemonGen2.CHARIZARD, PokemonGen2.CHARMANDER),
            Types.GROUND: (PokemonGen2.MAROWAK, PokemonGen2.CUBONE),
            Types.PSYCHIC: (PokemonGen2.MR_MIME, PokemonGen2.MR_MIME),
            Types.POISON: (PokemonGen2.WEEZING, PokemonGen2.KOFFING),
            Types.FLYING: (PokemonGen2.ZAPDOS, PokemonGen2.ZAPDOS),
            Types.NORMAL: (PokemonGen2.WIGGLYTUFF, PokemonGen2.IGGLYBUFF),
            Types.WATER: (PokemonGen2.BLASTOISE, PokemonGen2.SQUIRTLE),
            Types.ROCK: (PokemonGen2.SUDOWOODO, PokemonGen2.SUDOWOODO),
            Types.DARK: (PokemonGen2.HOUNDOOM, PokemonGen2.HOUNDOUR),
        }
    )
    run_response = get_run(client_fixture, run_id)
    assert len(run_response['pokemons']) == len(get_generation_types(2))
    star_types = {
        pokemon['metadata']['starlocke_type']
        for pokemon in run_response['pokemons'].values()
    }
    assert star_types == set(get_generation_types(2))
    print("TEST Finished")


def _create_run(client_fixture, game_name, expected_types: List[List[str]], type_pokemon_map: Dict[str, Tuple[str, str]]):
    list_runs(client_fixture, None)
    list_lockes(client_fixture, TEST_LOCKE)
    start_locke_creation(client_fixture, TEST_LOCKE, game_name, True, False)
    continue_locke_creation_not_finished(client_fixture, None, None, 'GAME', game_name)
    continue_locke_creation_not_finished(client_fixture, 'GAME', game_name, None, None)
    chosen_pokemons = set()

    for next_type_groups in expected_types:
        while next_type_groups:
            next_key, next_options = continue_locke_creation_not_finished(client_fixture, None, None, None, None)
            assert next_key in next_type_groups, f"Next type {next_key} is not in expected {next_type_groups}"
            next_type_groups.remove(next_key)
            type_pokemon, type_base_pokemon = type_pokemon_map[next_key]
            continue_locke_creation_not_finished(client_fixture, next_key, type_pokemon, None, None)
            chosen_pokemons.add(type_pokemon)

    random_starter = chosen_pokemons.pop()
    continue_locke_creation_not_finished(client_fixture, None, None, "star_starter", random_starter)
    first_team_member = chosen_pokemons.pop()
    continue_locke_creation_not_finished(client_fixture, "star_starter", random_starter, "star_team1", first_team_member)
    second_team_member = chosen_pokemons.pop()
    continue_locke_creation_not_finished(client_fixture, "star_team1", first_team_member, "star_team2", second_team_member)
    third_team_member = chosen_pokemons.pop()
    continue_locke_creation_not_finished(client_fixture, "star_team2", second_team_member, "star_team3", third_team_member )
    fourth_team_member = chosen_pokemons.pop()
    continue_locke_creation_not_finished(client_fixture, "star_team3", third_team_member, "star_team4", fourth_team_member)
    fifth_team_member = chosen_pokemons.pop()
    continue_locke_creation_not_finished(client_fixture, "star_team4", fourth_team_member, "star_team5", fifth_team_member)

    run_id = continue_locke_creation_finished(client_fixture, "star_team5", fifth_team_member)
    return run_id


if __name__ == '__main__':
    pytest.main([__file__])

