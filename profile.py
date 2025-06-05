import tkinter as tk  # Import the tkinter module for GUI creation
import json  # Module for working with JSON data
import os  # Module for interacting with the operating system

DATA_DIR = "data"  # Directory where user profile data will be stored

def open_profile(root, username, logout_callback):
    # Function to open the user profile page
    # Import open_dashboard here to avoid circular imports
    from dashboard_page import open_dashboard

    if root:
        root.destroy()  # Destroy the previous window if it exists

    # Create a new Tkinter window for the profile
    root = tk.Tk()
    root.title("Profile")  # Set the window title
    root.geometry("400x400")  # Set the window size
    root.configure(bg="#f0fff0")  # Set the background color

    # Create the file path for the user's profile data
    file_path = os.path.join(DATA_DIR, f"{username}_profile.json")
    data = {"name": "", "age": "", "gender": "", "password": ""}  # Default profile data

    # Check if the profile file exists
    if os.path.exists(file_path):
        # Load existing profile data from the JSON file
        with open(file_path, "r") as file:
            data.update(json.load(file))  # Update the data dictionary with loaded values

    # Create StringVar for each profile field to hold user input
    name_var = tk.StringVar(value=data.get("name", ""))
    age_var = tk.StringVar(value=data.get("age", ""))
    gender_var = tk.StringVar(value=data.get("gender", ""))

    # Profile info label
    tk.Label(root, text="👤 Profile Info", font=("Helvetica", 18, "bold"), bg="#f0fff0").pack(pady=20)

    # Create input fields for name, age, and gender
    for label, var in [("Name:", name_var), ("Age:", age_var), ("Gender:", gender_var)]:
        tk.Label(root, text=label, bg="#f0fff0").pack()  # Label for each field
        tk.Entry(root, textvariable=var).pack(pady=5)  # Entry box for user input

    def save_profile():
        # Function to save the profile data when the save button is pressed
        data["name"] = name_var.get()  # Get the name from the input field
        data["age"] = age_var.get()  # Get the age from the input field
        data["gender"] = gender_var.get()  # Get the gender from the input field
        
        # Write the updated profile data to the JSON file
        with open(file_path, "w") as file:
            json.dump(data, file)  # Save data in JSON format

    # Button to save the profile data
    tk.Button(root, text="Save", bg="#28a745", fg="white", command=save_profile).pack(pady=10)
    # Button to go back to the dashboard
    tk.Button(root, text="← Back to Dashboard", command=lambda: open_dashboard(root, username, logout_callback)).pack(pady=10)

    root.mainloop()  # Start the Tkinter event loop to display the profile page
