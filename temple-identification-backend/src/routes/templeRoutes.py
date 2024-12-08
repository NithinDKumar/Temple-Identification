from flask import Blueprint, request, jsonify
from src.models.templeModel import Temple
from src.utils import preprocess_image
import numpy as np
import tensorflow as tf
import os
import json
import logging
from src.utils import fetch_image_from_google
temple_routes = Blueprint('temple_routes', __name__)

# Load the trained model
model = tf.keras.models.load_model(os.getenv('MODEL_PATH'))

# Load class indices
with open(os.getenv('CLASS_INDICES_PATH'), 'r') as f:
    class_indices = json.load(f)

@temple_routes.route('/api/temples/search/<temple_name>', methods=['GET'])
def get_temple_details(temple_name):
    try:
        temples = Temple.objects(name__icontains=temple_name)
        if temples:
            return jsonify([temple.to_json() for temple in temples]), 200
        else:
            logging.warning(f"Temple '{temple_name}' not found in the database.")
            return jsonify({"message": "Temple not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching temple details: {str(e)}")
        return jsonify({"error": str(e)}), 500

@temple_routes.route('/api/temples/upload', methods=['POST'])
def upload_temple_image():
    try:
        logging.info("Received image upload request.")
        image_data = request.files['image'].read()
        image_array = preprocess_image(image_data, target_size=(150, 150))

        # Predict the temple
        prediction = model.predict(image_array)
        predicted_class = np.argmax(prediction, axis=1)[0]
        temple_name = list(class_indices.keys())[predicted_class]

        logging.info(f"Image processed and temple identified as: {temple_name}")

        temple = Temple.objects(name=temple_name).first()
        if temple:
            logging.info(f"Temple details found in database for: {temple_name}")
            return jsonify(temple.to_json()), 200
        else:
            # Fetch from Google if not found in database
            image_url = fetch_image_from_google(temple_name)
            new_temple = Temple(
                name=temple_name,
                location="Unknown",
                built_date="Unknown",
                description="No description available",
                images=[image_url] if image_url else []
            )
            new_temple.save()
            logging.warning(f"Temple details not found in database for: {temple_name}. Created a new entry.")
            return jsonify(new_temple.to_json()), 200
    except Exception as e:
        logging.error("Error during image upload", exc_info=True)
        return jsonify({"error": str(e)}), 500