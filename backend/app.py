from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from apis.main import list_runs_api
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
                return jsonify(result)
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
    return [run.__dict__ for run in runs]

if __name__ == '__main__':
    app.run(debug=True, port=5222) 