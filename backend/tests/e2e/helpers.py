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
    assert len(potential_encounters) == expected_num_pokemons
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


def save_run(client, run_id):
    response = client.post('/locke_manager/run/' + run_id + '/save')
    assert response.status_code == 200
    saved_run = get_run(client, run_id)


def assert_run(run_response, id, party_size, box_size, won_gyms, won_elites, num_encounters, starter, num_restarts=0, finished=False):
    run = run_response['run']
    assert run['id'] == id
    assert run['run_name'] == 'TestRun'
    assert len(run['party']) == party_size
    assert len(run['box']) == box_size
    assert len(run['gyms']) == won_gyms
    assert len(run['elite4']) == won_elites
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
