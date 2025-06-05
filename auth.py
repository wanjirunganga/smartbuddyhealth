import os  # Module for interacting with the operating system
import json  # Module for working with JSON data
import hashlib  # Module for hashing passwords

DATA_DIR = "data"  # Directory where user data will be stored

def hash_password(password):
    # Hash the password using SHA-256 for secure storage
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Register a new user. Return True if success, False if user exists."""
    # Create the file path for the user's authentication data
    filepath = os.path.join(DATA_DIR, f"{username}_auth.json")
    
    # Check if the user already exists
    if os.path.exists(filepath):
        return False  # User already exists, registration fails
    
    # Create a dictionary to store username and hashed password
    data = {
        "username": username,
        "password": hash_password(password)  # Store the hashed password
    }
    
    # Write the user data to a JSON file
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    
    # Also create an empty profile file to start with
    profile_path = os.path.join(DATA_DIR, f"{username}_profile.json")
    if not os.path.exists(profile_path):
        # Create an empty profile with default values
        with open(profile_path, "w") as pf:
            json.dump({"name": "", "age": "", "gender": ""}, pf, indent=4)
    
    return True  # Registration successful

def authenticate_user(username, password):
    """Authenticate user, return True if credentials match, else False."""
    # Create the file path for the user's authentication data
    filepath = os.path.join(DATA_DIR, f"{username}_auth.json")
    
    # Check if the user file exists
    if not os.path.exists(filepath):
        return False  # User does not exist, authentication fails
    
    # Read the user data from the JSON file
    with open(filepath, "r") as f:
        data = json.load(f)
    
    # Hash the provided password to compare with stored hash
    hashed = hash_password(password)
    
    # Check if the hashed password matches the stored password
    return data.get("password") == hashed  # Return True if match, else False
