"""Flask application for the Locke Manager API."""

from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
from dotenv import load_dotenv
from apis.main import list_runs_api
from apis.resources import get_pokemon_info, get_gym_leader_info, get_type_info
from apis.run_creation import start_run_creation
from apis.exceptions import RunCreationError
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
                return jsonify({
                    "status": "error",
                    "message": str(e)
                }), 500
        return app.route(f"/locke_manager/{path}", *args, **kwargs)(wrapped)
    return decorator

@locke_route('runs', methods=['GET'])
def get_runs():
    """Get all runs from the database.
    
    Returns:
        List of runs in the ListRuns response format.
    """
    runs = list_runs_api()
    return jsonify([run.__dict__ for run in runs])

@locke_route('lockes', methods=['GET'])
def get_lockes():
    """Get all available locke types.
    
    Returns:
        List of locke names.
    """
    lockes = list_all_lockes()
    return jsonify(lockes)

@locke_route('resources/pokemon/<pokemon_name>', methods=['GET'])
def get_pokemon(pokemon_name):
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
def get_gym_leader(game_name, gym_name):
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
def get_type(type_name):
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
def create_new_run():
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
    try:
        data = request.get_json()
        if not data:
            return jsonify("No data provided"), 400
            
        # Validate required fields
        required_fields = ['run_name', 'locke_type', 'duplicate_clause', 'is_randomized']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify(f"Missing required fields: {', '.join(missing_fields)}"), 400
            
        # Call the service layer
        game_names = start_run_creation(
            run_name=data['run_name'],
            locke_type=data['locke_type'],
            duplicate_clause=data['duplicate_clause'],
            is_randomized=data['is_randomized']
        )
            
        return jsonify(game_names), 200
        
    except RunCreationError as e:
        return jsonify(str(e)), e.status_code
    except Exception as e:
        return jsonify(str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, port=5222) 