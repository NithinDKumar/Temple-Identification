# test_mongodb.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client.temple_db
    # Test connection
    client.server_info()
    print("Connected to MongoDB successfully.")
    
    # Test a query
    temple_name = "Golden Temple"
    temples = db.temples.find({"name": {"$regex": temple_name, "$options": "i"}})
    temples_list = list(temples)
    
    if len(temples_list) > 0:
        print(f"Temples found in database: {temples_list}")
    else:
        print(f"Temple '{temple_name}' not found in database.")
except Exception as e:
    print(f"Error: {e}")
