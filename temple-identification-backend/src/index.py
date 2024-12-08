# temple-identification-backend/src/index.py

from flask import Flask, jsonify, request
import os
from src.utils import load_json_data, load_all_json_data

app = Flask(__name__)

# Load all JSON data from a directory
data_directory = r'Enter your directory here'
combined_data = load_all_json_data(data_directory)

# Load specific JSON files
dieties_data = load_json_data(os.path.join('data', 'dieties.json'))
hindu_temples_data = load_json_data(os.path.join('data', 'hindu_temples.json'))

@app.route('/')
def index():
    return jsonify(combined_data)

@app.route('/api/temple-details', methods=['GET'])
def get_temple_details():
    temple_name = request.args.get('name')
    deity = request.args.get('deity')

    if deity:
        for deity_name, temples in dieties_data.items():
            if deity_name.lower() == deity.lower():
                for temple in temples:
                    if temple['name'].lower() == temple_name.lower():
                        return jsonify(temple)
    
    if temple_name:
        for state, temples in hindu_temples_data.items():
            for temple in temples:
                if temple['name'].lower() == temple_name.lower():
                    return jsonify(temple)

    return jsonify({"error": "Temple not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
