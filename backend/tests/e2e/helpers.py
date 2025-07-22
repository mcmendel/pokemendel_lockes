from app import app
import pytest
from models.db_helper import delete_documents_by_query, insert_document, fetch_documents_by_query


@pytest.fixture
def client_fixture():
    client = app.test_client()
    client.testing = True
    yield client


def list_runs(client, expected_run_name):
    response = client.get('/locke_manager/runs')
    assert response.status_code == 200
    runs = response.get_json()
    if not expected_run_name:
        assert len(runs) == 0
    else:
        assert len(runs) == 1
        assert runs[0]['run_name'] == expected_run_name


def list_lockes(client, test_locke):
    response = client.get('/locke_manager/lockes')
    assert response.status_code == 200
    lockes = response.get_json()
    assert test_locke in lockes


def start_locke_creation(client, test_locke, test_game, duplicate_clause, is_randomized):
    response = client.put('/locke_manager/run', json={
        'run_name': 'TestRun',
        'locke_type': test_locke,
        'duplicate_clause': duplicate_clause,
        'is_randomized': is_randomized,
    })
    assert response.status_code == 200
    potential_games = response.get_json()
    assert test_game in potential_games


def continue_locke_creation_not_finished(client, key, val, expected_next_key, expected_optional_val):
    response = client.post('/locke_manager/run', json={
        'run_name': 'TestRun',
        'key': key,
        'val': val,
    })
    assert response.status_code == 200
    continue_response = response.get_json()
    assert not continue_response['finished']
    assert continue_response['next_key'] == expected_next_key
    assert expected_optional_val in continue_response['potential_values']


def continue_locke_creation_finished(client, key, val):
    response = client.post('/locke_manager/run', json={
        'run_name': 'TestRun',
        'key': key,
        'val': val,
    })
    assert response.status_code == 200
    continue_response = response.get_json()
    assert continue_response['finished']
    assert continue_response['id']
    assert not continue_response['next_key']
    assert not continue_response['potential_values']

    # make sure all run potential pokemons entered correctly
    db_runs = list(fetch_documents_by_query("locke_manager", "runs_pokemons_options", {"run_id": continue_response['id']}))
    assert len(db_runs) >= 1
    pokemon_indices = set()
    for db_run in db_runs:
        pokemon_indices.add(db_run['index'])
        assert not db_run['caught']
    assert len(pokemon_indices) == len(db_runs)

    return continue_response['id']


def get_run(client, run_id):
    response = client.get('/locke_manager/run/' + run_id)
    assert response.status_code == 200
    run = response.get_json()
    return run


def get_starter_options(client, run_id):
    response = client.get('/locke_manager/run/' + run_id + '/starter_options')
    assert response.status_code == 200
    run = response.get_json()
    return run


def get_run_supported_pokemons(client, run_id, expected_num_pokemons):
    response = client.get('/locke_manager/run/' + run_id + '/potential_pokemons')
    assert response.status_code == 200
    supported_pokemons = response.get_json()
    assert len(supported_pokemons) == expected_num_pokemons
    return supported_pokemons


def get_run_potential_encounters(client, run_id, route, expected_num_pokemons):
    url = '/locke_manager/run/' + run_id + '/encounters'
    if route:
        url = f"{url}?route={route}"
    response = client.get(url)
    assert response.status_code == 200
    potential_encounters = response.get_json()
    assert len(potential_encounters) == expected_num_pokemons, f"{expected_num_pokemons} != {len(potential_encounters)}"
    return potential_encounters


def choose_starter(client, run_id: str, pokemon_name: str, pokemon_base: str):
    response = client.put("/locke_manager/run/" + run_id + "/starter", json={
        'pokemon_name': pokemon_name
    })
    assert response.status_code == 200
    db_runs = list(fetch_documents_by_query("locke_manager", "runs_pokemons_options", {"run_id": run_id, "base_pokemon": pokemon_base}))
    assert len(db_runs) >= 1
    for db_run in db_runs:
        assert db_run['caught']


def encounter_pokemon(client, run_id: str, route: str, pokemon_name: str):
    response = client.put("/locke_manager/run/" + run_id + "/encounter/" + route, json={
        'pokemon_name': pokemon_name
    })
    assert response.status_code == 200


def update_encounter(client, run_id: str, route: str, encounter_status: str):
    response = client.post("/locke_manager/run/" + run_id + "/encounter/" + route, json={
        'encounter_status': encounter_status
    })
    assert response.status_code == 200


def get_next_actions(client, run_id: str, pokemon_id: str) -> list:
    response = client.get("/locke_manager/run/" + run_id + "/pokemon/" + pokemon_id + "/actions")
    assert response.status_code == 200
    next_actions = response.get_json()
    return next_actions


def get_action_options(client, run_id: str, pokemon_id: str, action: str) -> list:
    response = client.get("/locke_manager/run/" + run_id + "/pokemon/" + pokemon_id + "/action?action=" + action)
    assert response.status_code == 200
    action_options = response.get_json()
    return action_options


def execute_action(client, run_id: str, pokemon_id: str, action: str, value: str):
    response = client.post("/locke_manager/run/" + run_id + "/pokemon/" + pokemon_id + "/action", json={
        'action': action,
        'value': value,
    })
    assert response.status_code == 200


def save_run(client, run_id):
    response = client.post('/locke_manager/run/' + run_id + '/save')
    assert response.status_code == 200
    saved_run = get_run(client, run_id)
    return saved_run


def load_run(client, run_id):
    response = client.post('/locke_manager/run/' + run_id + '/load')
    assert response.status_code == 200
    loaded_run = get_run(client, run_id)
    return loaded_run


def win_battle(client, run_id, leader):
    response = client.post('/locke_manager/run/' + run_id + '/battle/' + leader)
    assert response.status_code == 200
    run_response = get_run(client, run_id)
    assert next(gym for gym in run_response['run']['gyms'] if gym['leader'] == leader)['won']


def finish_run(client, run_id):
    response = client.post('/locke_manager/run/' + run_id + '/finish')
    assert response.status_code == 200
    run_response = get_run(client, run_id)
    assert run_response['run']['finished']


def assert_run(run_response, id, party_size, box_size, won_gyms, num_encounters, starter, num_restarts=0, finished=False, gen=1):
    run = run_response['run']
    assert run['id'] == id
    assert run['run_name'] == 'TestRun'
    assert run['gen'] == gen
    assert len(run['party']) == party_size
    assert len(run['box']) == box_size
    assert len(run['gyms']) == won_gyms
    assert len([encounter for encounter in run['encounters'] if encounter['pokemon']]) == num_encounters
    if starter:
        assert run['starter'] in run_response['pokemons']
        assert run_response['pokemons'][run['starter']]['name'] == starter
    else:
        assert not run['starter']

    assert run['restarts'] == num_restarts
    assert run['finished'] == finished


def assert_saved_run(run_id, party_size, box_size, won_battles, num_encounters, starter, num_restarts=0, finished=False):
    db_runs = list(fetch_documents_by_query("locke_manager", "runs_save", {"_id": run_id}))
    assert len(db_runs) == 1
    db_run = db_runs[0]
    assert db_run['_id'] == run_id
    assert db_run['name'] == 'TestRun'
    assert len(db_run['party']) == party_size
    assert len(db_run['box']) == box_size
    assert len(db_run['battles']) == won_battles
    assert len(db_run['encounters']) == num_encounters
    if starter:
        assert db_run['starter']['name'] == starter
    else:
        assert not db_run['starter']

    assert db_run['restarts'] == num_restarts
    assert db_run['finished'] == finished


def assert_run_potential_pokemons(run_id: str, expected_num_pokemons: int):
    db_runs = list(fetch_documents_by_query("locke_manager", "runs_pokemons_options", {"run_id": run_id}))
    assert len(db_runs) == expected_num_pokemons
