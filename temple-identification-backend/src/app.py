from flask import Flask, request, jsonify, session
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from PIL import Image
import io
import tensorflow as tf
import numpy as np
import json
import logging
import difflib
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId  # Import ObjectId

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

logging.basicConfig(level=logging.DEBUG)

client = MongoClient(os.getenv('MONGO_URI'))
db = client.temple_db

# Load the JSON file
json_file_path = os.path.join(os.path.dirname(__file__), 'data', 'dieties.json')
with open(json_file_path, 'r') as f:
    temples_data = json.load(f)

@app.route('/api/temples', methods=['GET'])
def get_temples():
    try:
        temples = list(db.temples.find({}))
        for temple in temples:
            temple['_id'] = str(temple['_id'])
        logging.debug(f"Fetched temples: {temples}")
        return jsonify(temples), 200
    except Exception as e:
        logging.error("Error fetching temples", exc_info=True)
        return jsonify({"error": str(e)}), 500



# Load the trained model
model = tf.keras.models.load_model('temple_model.h5')

# Load class indices
with open('class_indices.json', 'r') as f:
    class_indices = json.load(f)

def preprocess_image(image, target_size):
    image = Image.open(io.BytesIO(image))
    image = image.convert("RGB")
    image.thumbnail(target_size, Image.LANCZOS)
    new_image = Image.new("RGB", target_size)
    new_image.paste(
        image, ((target_size[0] - image.size[0]) // 2, (target_size[1] - image.size[1]) // 2)
    )
    image_array = np.array(new_image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.route('/')
def home():
    return "Temple Identification Backend is running!"

@app.route('/api/temples/upload', methods=['POST'])
def upload_image():
    try:
        logging.info("Received image upload request.")
        image_data = request.files['image'].read()
        image_array = preprocess_image(image_data, target_size=(150, 150))

        # Predict the temple
        prediction = model.predict(image_array)
        predicted_class = np.argmax(prediction, axis=1)[0]
        temple_name = list(class_indices.keys())[predicted_class]

        logging.info(f"Image processed and temple identified as: {temple_name}")

        # Find the temple with a similar name from the JSON data
        matching_temple = next((temple for temple in temples_data if temple['name'].lower() == temple_name.lower()), None)

        if matching_temple:
            logging.info(f"Temple details found for: {temple_name}")
            return jsonify({
                "name": matching_temple["name"],
                "state": matching_temple.get("state", "Unknown"),
                "info": matching_temple.get("info", ""),
                "story": matching_temple.get("story", ""),
                "architecture": matching_temple.get("architecture", ""),
                "image_url": matching_temple.get("image_url", ""),
            }), 200
        else:
            logging.warning(f"Temple details not found for: {temple_name}")
            return jsonify({"name": temple_name, "message": "Temple not found in database"}), 200
    except Exception as e:
        logging.error("Error during image upload", exc_info=True)
        return jsonify({"error": str(e)}), 500




@app.route('/api/temples/search/<name>', methods=['GET'])
def get_temple_details(name):
    results = [temple for temple in temples_data if name.lower() in temple["name"].lower()]
    if results:
        return jsonify(results), 200
    else:
        return jsonify({"message": "Temple not found"}), 404

@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = db.users.find_one({"username": username})

        if user and check_password_hash(user['password'], password):
            session['user'] = username
            session['is_admin'] = user.get('is_admin', False)  # Set is_admin flag in session
            return jsonify({"message": "Login successful", "status": "success"}), 200
        else:
            return jsonify({"message": "Invalid credentials", "status": "fail"}), 401
    except Exception as e:
        logging.error("Error during login", exc_info=True)
        return jsonify({"error": str(e)}), 500


@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({"message": "Logout successful"}), 200

@app.route('/api/temples/update', methods=['POST'])
def update_temple():
    if not session.get('is_admin'):
        return jsonify({"message": "Unauthorized"}), 403

    data = request.json
    temple_id = data.get('id')
    update_data = {
        "name": data.get('name'),
        "description": data.get('description'),
        "info": data.get('info'),
        "story": data.get('story'),
        "architecture": data.get('architecture')
    }
    db.temples.update_one({"_id": ObjectId(temple_id)}, {"$set": update_data})
    return jsonify({"message": "Temple updated successfully"}), 200

@app.route('/api/temples/add', methods=['POST'])
def add_temple():
    data = request.json
    db.temples.insert_one(data)
    return jsonify({"message": "Temple added successfully"}), 200

@app.route('/api/temples/delete', methods=['POST'])
def delete_temple():
    temple_ids = request.json.get('ids', [])
    db.temples.delete_many({"_id": {"$in": [ObjectId(id) for id in temple_ids]}})
    return jsonify({"message": "Temples deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
