# create_admin.py

from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client.temple_db

# Create admin user
username = "admin"
password = "admin"
password_hash = generate_password_hash(password)
is_admin = True

admin_user = {
    "username": username,
    "password": password_hash,
    "is_admin": is_admin
}

# Insert admin user into the database
db.users.insert_one(admin_user)
print("Admin user created successfully.")
