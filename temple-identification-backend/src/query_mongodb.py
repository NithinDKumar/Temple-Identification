import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to MongoDB
client = MongoClient(os.getenv('MONGO_URI'))
db = client.temple_db
temples_collection = db.temples

def get_temple_details(temple_name):
    temples = temples_collection.find({"name": {"$regex": temple_name, "$options": "i"}})
    if temples:
        return [temple for temple in temples]
    else:
        return "Temple not found"

if __name__ == "__main__":
    temple_name = input("Enter the name of the temple: ")
    temple_details = get_temple_details(temple_name)
    for temple in temple_details:
        print(temple)
