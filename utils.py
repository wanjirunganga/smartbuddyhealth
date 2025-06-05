import os  # Module for interacting with the operating system
import json  # Module for working with JSON data

DATA_DIR = "data"  # Directory where user data will be stored

def ensure_data_dir():
    # Function to ensure that the data directory exists
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)  # Create the data directory if it does not exist

def get_user_path(username):
    # Function to get the file path for a user's data file
    return os.path.join(DATA_DIR, f"{username}.json")  # Return the full path for the user's JSON file

def get_auth_path(username):
    # Function to get the file path for a user's authentication data
    return os.path.join(DATA_DIR, f"{username}_auth.json")  # Return the full path for the user's auth JSON file

def load_json(path):
    # Function to load JSON data from a file
    if os.path.exists(path):
        with open(path, "r") as file:
            return json.load(file)  # Return the loaded JSON data
    return {}  # Return an empty dictionary if the file does not exist

def save_json(path, data):
    # Function to save data to a JSON file
    with open(path, "w") as file:
        json.dump(data, file, indent=4)  # Write the data to the file in JSON format with indentation
