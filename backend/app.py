from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/api/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Backend is running!"})

if __name__ == '__main__':
    app.run(debug=True, port=5222) 