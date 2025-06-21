"""Flask application for the Locke Manager API."""

from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
from dotenv import load_dotenv
from apis.main import list_runs_api
from apis.resources import get_pokemon_info, get_gym_leader_info, get_type_info
from apis.run_creation import start_run_creation, continue_run_creation
from apis.run_admin import get_run_api, save_run, load_run, finish_run
from apis.run import get_starter_options, choose_starter, get_run_potential_pokemons, get_run_potential_encounters
from core.lockes import list_all_lockes
from functools import wraps

load_dotenv()

app = Flask(__name__)
CORS(app)

def locke_route(path, *args, **kwargs):
    """Decorator for Locke-related routes that handles error handling.
    
    Args:
        path: The route path to be appended to /locke_manager/
        *args: Additional arguments for the route decorator
        **kwargs: Additional keyword arguments for the route decorator
    """
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            try:
                result = f(*args, **kwargs)
                return result
            except Exception as e:
                status = getattr(e, "status_code", 500)
                print(f"ERROR: {e}")
                return jsonify({
                    "status": "error",
                    "message": str(e)
                }), status
        return app.route(f"/locke_manager/{path}", *args, **kwargs)(wrapped)
    return decorator

@locke_route('runs', methods=['GET'])
def get_runs():
    """Get all runs from the database.
    
    Returns:
        List of runs in the ListRuns response format.
    """
    print("Listing runs")
    runs = list_runs_api()
    print("Found %s runs" % len(runs))
    return jsonify([run.__dict__ for run in runs])

@locke_route('lockes', methods=['GET'])
def get_lockes():
    """Get all available locke types.
    
    Returns:
        List of locke names.
    """
    print("Listing lockes")
    lockes = list_all_lockes()
    print("Found %s lockes: %s" % (len(lockes), lockes))
    return jsonify(lockes)

@locke_route('resources/pokemon/<pokemon_name>', methods=['GET'])
def get_pokemon_resource(pokemon_name):
    """Get Pokemon image by name.
    
    Args:
        pokemon_name: The name of the Pokemon to look up
        
    Returns:
        The Pokemon image file or error message if not found
    """
    image_path = get_pokemon_info(pokemon_name)
    if image_path is None:
        return jsonify({
            "status": "error",
            "message": f"Pokemon '{pokemon_name}' not found"
        }), 404
    
    return send_file(
        image_path,
        mimetype='image/jpeg',
        as_attachment=False
    )

@locke_route('resources/game/<game_name>/gyms/<gym_name>', methods=['GET'])
def get_gym_leader_resource(game_name, gym_name):
    """Get gym leader image by game and gym name.
    
    Args:
        game_name: The name of the game (e.g., 'red', 'blue', 'gold', etc.)
        gym_name: The name of the gym leader
        
    Returns:
        The gym leader image file or error message if not found
    """
    image_path = get_gym_leader_info(game_name, gym_name)
    if image_path is None:
        return jsonify({
            "status": "error",
            "message": f"Gym leader '{gym_name}' from game '{game_name}' not found"
        }), 404
    
    return send_file(
        image_path,
        mimetype='image/jpeg',
        as_attachment=False
    )

@locke_route('resources/types/<type_name>', methods=['GET'])
def get_type_resource(type_name):
    """Get Pokemon type image by name.
    
    Args:
        type_name: The name of the Pokemon type (e.g., 'fire', 'water', etc.)
        
    Returns:
        The type image file or error message if not found
    """
    image_path = get_type_info(type_name)
    if image_path is None:
        return jsonify({
            "status": "error",
            "message": f"Type '{type_name}' not found"
        }), 404
    
    return send_file(
        image_path,
        mimetype='image/jpeg',
        as_attachment=False
    )

@locke_route('run', methods=['PUT'])
def create_new_run_api():
    """Create a new run with the specified parameters.
    
    Request body should contain:
        - run_name: Name of the run
        - locke_type: Type of locke challenge
        - duplicate_clause: Whether duplicate Pokemon are allowed
        - is_randomized: Whether the game is randomized
            
    Returns:
        List of available games that meet the locke's minimum generation requirement
            
    Status codes:
        - 200: Success
        - 400: Invalid request (e.g. invalid locke type)
        - 409: Run already exists
        - 500: Server error
    """
    print("Creating new run")
    data = request.get_json()
    if not data:
        return jsonify("No data provided"), 400
    # Validate required fields
    required_fields = ['run_name', 'locke_type', 'duplicate_clause', 'is_randomized']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify(f"Missing required fields: {', '.join(missing_fields)}"), 400
    print("Start run creation for run %s" % data['run_name'])
    # Call the service layer (let exceptions propagate)
    game_names = start_run_creation(
        run_name=data['run_name'],
        locke_type=data['locke_type'],
        duplicate_clause=data['duplicate_clause'],
        is_randomized=data['is_randomized']
    )
    print("Run creation for run %s had started. Next step is choose from games %s" % (data['run_name'], game_names))
    return jsonify(game_names), 200

@locke_route('run', methods=['POST'])
def continue_run_creation_api():
    """Update an existing run with new information.
    
    Request body:
        run_name: Name of the run to update (required)
        key: The key to update (optional)
        val: The value to set (optional)
        
    Returns:
        A JSON object containing:
            - next_key: The next key to update (if not finished)
            - potential_values: List of potential values for the next key (if not finished)
            - finished: Whether the run creation is complete
            
    Status codes:
        200: Success
        400: Invalid request (missing run_name)
        404: Run not found
        500: Server error
    """
    data = request.get_json()
    # Validate required fields
    if not data or 'run_name' not in data:
        return jsonify({
            'error': 'Missing required field: run_name'
        }), 400
    # Get optional fields with defaults
    key = data.get('key')
    val = data.get('val')
    print("Continue run creation for run %s with key %s and value %s" % (data['run_name'], key, val))
    # Call the service function (let exceptions propagate)
    response = continue_run_creation(
        run_name=data['run_name'],
        key=key,
        val=val
    )
    if response['finished']:
        print("Finished creating run %s with id %s" % (data['run_name'], response['id']))
    else:
        print("Creating run %s in progress. Next key to be filled: %s" % (data['run_name'], response['next_key']))
    return jsonify(response), 200

@locke_route('run/<run_id>', methods=['GET'])
def get_run(run_id):
    """Get a run by its ID.
    
    Args:
        run_id: The ID of the run to fetch
        
    Returns:
        The run data as JSON
        
    Status codes:
        200: Success
        404: Run not found
        500: Server error
    """
    run_data = get_run_api(run_id)
    return jsonify(run_data.to_dict())


@locke_route('run/<run_id>/save', methods=['POST'])
def save_run_api(run_id):
    """Save run by its ID.

    Args:
        run_id: The ID of the run to fetch

    Returns:
        The run data as JSON

    Status codes:
        200: Success
        404: Run not found
        500: Server error
    """
    save_run(run_id)
    return jsonify({'status': 'success'})


@locke_route('run/<run_id>/load', methods=['POST'])
def load_run_api(run_id):
    """Load run by its ID.

    Args:
        run_id: The ID of the run to fetch

    Returns:
        The run data as JSON

    Status codes:
        200: Success
        404: Run not found
        500: Server error
    """
    run_data = load_run(run_id)
    return jsonify(run_data.to_dict())


@locke_route('run/<run_id>/finish', methods=['POST'])
def finish_run_api(run_id):
    """Finish run.

    Args:
        run_id: The ID of the run to fetch

    Returns:
        The run data as JSON

    Status codes:
        200: Success
        404: Run not found
        500: Server error
    """
    run_data = finish_run(run_id)
    return jsonify(run_data.to_dict())


@locke_route('run/<run_id>/starter_options', methods=['GET'])
def get_starter_options_api(run_id):
    starter_options = get_starter_options(run_id)
    return jsonify(starter_options)


@locke_route('run/<run_id>/starter', methods=['PUT'])
def choose_starter_api(run_id):
    data = request.get_json()
    # Validate required fields
    if not data or 'pokemon_name' not in data:
        return jsonify({
            'error': 'Missing required field: pokemon_name'
        }), 400
    choose_starter(run_id, data['pokemon_name'])
    return jsonify({'status': 'success'})


@locke_route('run/<run_id>/potential_pokemons', methods=['GET'])
def get_run_potential_pokemons_api(run_id):
    potential_pokemons = get_run_potential_pokemons(run_id)
    return jsonify(potential_pokemons)


@locke_route('run/<run_id>/encounters', methods=['GET'])
def get_run_potential_encounters_api(run_id):
    route = request.args.get('route')
    potential_encounters = get_run_potential_encounters(run_id, route)
    return jsonify(potential_encounters)


if __name__ == '__main__':
    app.run(debug=True, port=5222)
