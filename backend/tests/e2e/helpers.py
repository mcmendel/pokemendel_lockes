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

def choose_starter(client, run_id: str, pokemon_name: str):
    response = client.put("/locke_manager/run/" + run_id + "/starter", json={
        'pokemon_name': pokemon_name
    })
    assert response.status_code == 200


def save_run(client, run_id):
    response = client.post('/locke_manager/run/' + run_id + '/save')
    assert response.status_code == 200
    saved_run = get_run(client, run_id)


def assert_run(run, id, party_size, box_size, won_battles, num_encounters, starter, num_restarts=0, finished=False):
    assert run['id'] == id
    assert run['run_name'] == 'TestRun'
    assert len(run['party']['pokemons']) == party_size
    assert len(run['box']['pokemons']) == box_size
    assert len(run['battles']) == won_battles
    assert len([encounter for encounter in run['encounters'] if encounter['pokemon']]) == num_encounters
    if starter:
        assert run['starter']['name'] == starter
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
