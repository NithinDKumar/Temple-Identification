import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client.temple_db

def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

def save_to_mongodb(data, collection_name):
    collection = db[collection_name]
    for item in data:
        if collection.count_documents({"name": item["name"]}) == 0:
            collection.insert_one(item)
            print(f"Inserted: {item['name']}")
        else:
            print(f"Already exists: {item['name']}")

if __name__ == "__main__":
    dieties = load_data('data/dieties.json')
    temples = load_data('data/hindu_temples.json')
    states = load_data('data/states.json')

    save_to_mongodb(dieties, 'temples')
    save_to_mongodb(temples, 'temples')
    save_to_mongodb(states, 'temples')
