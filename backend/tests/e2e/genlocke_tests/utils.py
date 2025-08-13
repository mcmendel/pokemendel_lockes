from tests.e2e.helpers import (
    list_runs,
    list_lockes,
    start_locke_creation,
    continue_locke_creation_not_finished,
    continue_locke_creation_finished,
    get_starter_options,
    choose_starter,
    get_run,
    get_next_actions,
    get_action_options,
    execute_action,
    assert_pokemon,
)
from typing import Optional
import pytest


TEST_LOCKE = "GenLocke"


def create_genlocke_run(client, game_name, locke_name, extra_info, specific_pokemons) -> Optional[str]:
    list_runs(client, None)
    list_lockes(client, TEST_LOCKE)
    with pytest.raises(AssertionError, match=f"Failed to continue run creation with game {game_name}"):
        start_locke_creation(client, TEST_LOCKE, game_name, True, False)

    continue_locke_creation_not_finished(client, None, None, '_selected_locke', locke_name)
    continue_locke_creation_not_finished(client, '_selected_locke', locke_name, "GAME", game_name)
    if extra_info:
        continue_locke_creation_not_finished(client, "GAME", game_name, None, None)
        return None
    return continue_locke_creation_finished(client, "GAME", game_name, all_pokemons_caught=specific_pokemons)


def choose_gen_starter(client, run_id, expected_starter_options, starter_pokemon, nickname, gender=None, nature=None, ability=None):
    starter_options = get_starter_options(client, run_id)
    assert set(starter_options) == expected_starter_options
    assert starter_pokemon in starter_options
    choose_starter(client, run_id, starter_pokemon, starter_pokemon)
    run_response = get_run(client, run_id)
    run = run_response['run']
    assert run['starter']
    starter_id = run['starter']

    handle_caught_pokemon(
        client=client,
        run_response=run_response,
        run_id=run_id,
        num_box=1,
        num_party=1,
        pokemon_id=run['starter'],
        pokemon_name=starter_pokemon,
        is_pokemon_in_party=True,
        nickname=nickname,
        gender=gender,
        ability=ability,
        nature=nature,
    )
    return starter_id


def handle_caught_pokemon(
        client, run_response: dict, run_id: str,
        num_box: int, num_party: int,
        pokemon_id: str, pokemon_name: str, is_pokemon_in_party: bool,
        nickname: str, gender: str = None, ability: str = None, nature: str = None
):
    assert len(run_response['run']['box']) == num_box
    assert len(run_response['run']['party']) == num_party
    assert pokemon_id in run_response['run']['box']
    assert bool(pokemon_id in run_response['run']['party']) == is_pokemon_in_party
    assert_pokemon(
        run_response=run_response,
        pokemon_id=pokemon_id,
        pokemon_name=pokemon_name,
    )
    next_actions = get_next_actions(client, run_id, pokemon_id)
    assert next_actions == ["Nickname Pokemon"]

    nickname_options = get_action_options(client, run_id, pokemon_id, "Nickname Pokemon")
    assert nickname_options == {
        "input_options": [],
        "input_type": "Free text"
    }
    execute_action(client, run_id, pokemon_id, "Nickname Pokemon", nickname)
    run_response = get_run(client, run_id)
    assert_pokemon(
        run_response=run_response,
        pokemon_id=pokemon_id,
        pokemon_name=pokemon_name,
        nickname=nickname,
    )

    if gender:
        next_actions = get_next_actions(client, run_id, pokemon_id)
        expected_next_actions = _build_next_actions(True, bool(nature), bool(ability))
        assert next_actions == expected_next_actions, f"{next_actions} VS {expected_next_actions}"
        gender_options = get_action_options(client, run_id, pokemon_id, "Gender")
        assert gender_options["input_type"] == "One of"
        assert gender in gender_options["input_options"]
        execute_action(client, run_id, pokemon_id, "Gender", gender)
        run_response = get_run(client, run_id)
        assert_pokemon(
            run_response=run_response,
            pokemon_id=pokemon_id,
            pokemon_name=pokemon_name,
            nickname=nickname,
            gender=gender,
        )

    if nature:
        next_actions = get_next_actions(client, run_id, pokemon_id)
        expected_next_actions = _build_next_actions(False, bool(nature), bool(ability))
        assert next_actions == expected_next_actions, f"{next_actions} VS {expected_next_actions}"
        nature_options = get_action_options(client, run_id, pokemon_id, "Nature")
        assert nature_options["input_type"] == "One of"
        assert nature in nature_options["input_options"]
        execute_action(client, run_id, pokemon_id, "Nature", nature)
        run_response = get_run(client, run_id)
        assert_pokemon(
            run_response=run_response,
            pokemon_id=pokemon_id,
            pokemon_name=pokemon_name,
            nickname=nickname,
            gender=gender,
            nature=nature
        )

    if ability:
        next_actions = get_next_actions(client, run_id, pokemon_id)
        expected_next_actions = _build_next_actions(False, False, bool(ability))
        assert next_actions == expected_next_actions, f"{next_actions} VS {expected_next_actions}"
        ability_options = get_action_options(client, run_id, pokemon_id, "Ability")
        assert ability_options["input_type"] == "One of"
        assert ability in ability_options["input_options"]
        execute_action(client, run_id, pokemon_id, "Ability", ability)
        run_response = get_run(client, run_id)
        assert_pokemon(
            run_response=run_response,
            pokemon_id=pokemon_id,
            pokemon_name=pokemon_name,
            nickname=nickname,
            gender=gender,
            nature=nature,
            ability=ability,
        )


def _build_next_actions(gender: bool, nature: bool, ability: bool):
    next_actions = []
    if gender:
        next_actions.append("Gender")
    if nature:
        next_actions.append("Nature")
    if ability:
        next_actions.append("Ability")
    return next_actions
