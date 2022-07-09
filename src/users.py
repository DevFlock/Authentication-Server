from pymongo import MongoClient
import argon2

hasher = argon2.PasswordHasher()

db = MongoClient("mongodb://root:example@mongo:27017/").UsersDB.users
def hash_password(password):
    return hasher.hash(password)

def verify_password(password, hashed):
    try:
        return hasher.verify(hashed, password)
    except argon2.exceptions.VerifyMismatchError:
        return False

def add_user(username, email, password):
    if db.find_one({"username": username}) or db.find_one({'email': email}):
        return False
    hashed = hash_password(password)
    db.insert_one({"username": username, "email": email, "password": hashed})
    return True

def get_user(username):
    return db.find_one({"username": username})

def verify_user(username, password):
    user = get_user(username)
    if not user:
        return False
    return verify_password(password, user['password'])