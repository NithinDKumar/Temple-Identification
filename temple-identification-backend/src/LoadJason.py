from pymongo import MongoClient
import json

client = MongoClient('Enter Your Mongo client here')
db = client.temple_db

def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def load_data_into_db():
    # Load dieties data
    dieties_data = load_json_data('data/dieties.json')
    for deity, temples in dieties_data.items():
        for temple in temples:
            db.temples.update_one({'name': temple['name']}, {'$set': temple}, upsert=True)

    # Load hindu temples data
    hindu_temples_data = load_json_data('data/hindu_temples.json')
    for state, temples in hindu_temples_data.items():
        for temple in temples:
            db.temples.update_one({'name': temple['name']}, {'$set': temple}, upsert=True)

    # Load states data
    states_data = load_json_data('data/states.json')
    for state, temples in states_data.items():
        for temple in temples:
            db.temples.update_one({'name': temple['name']}, {'$set': temple}, upsert=True)

if __name__ == '__main__':
    load_data_into_db()
    print('Data loaded successfully!')
