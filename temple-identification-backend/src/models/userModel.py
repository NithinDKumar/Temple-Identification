# src/models/userModel.py

from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client.temple_db

class User:
    @staticmethod
    def create_user(username, password, is_admin=False):
        password_hash = generate_password_hash(password)
        user = {"username": username, "password": password_hash, "is_admin": is_admin}
        db.users.insert_one(user)

    @staticmethod
    def find_user(username):
        return db.users.find_one({"username": username})

    @staticmethod
    def check_password(user, password):
        return check_password_hash(user['password'], password)
