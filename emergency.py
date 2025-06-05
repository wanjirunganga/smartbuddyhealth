import tkinter as tk  # Import the tkinter module for GUI creation
import json  # Module for working with JSON data
import os  # Module for interacting with the operating system
from dashboard_page import open_dashboard  # Function to open the dashboard page

DATA_DIR = "data"  # Directory where emergency contact data will be stored

def open_emergency_info(root, username, logout_callback):
    # Function to open the emergency contact information page for the logged-in user
    if root:
        root.destroy()  # Destroy the previous window if it exists

    # Create a new Tkinter window for emergency info
    root = tk.Tk()
    root.title("Emergency Info")  # Set the window title
    root.geometry("400x400")  # Set the window size
    root.configure(bg="#ffe6e6")  # Set the background color

    # Create the file path for the user's emergency contact data
    filepath = os.path.join(DATA_DIR, f"{username}_emergency.json")
    data = {"contact_name": "", "phone": "", "note": ""}  # Default emergency data

    # Check if the emergency info file exists
    if os.path.exists(filepath):
        # Load existing emergency contact data from the JSON file
        with open(filepath, "r") as f:
            data.update(json.load(f))  # Update the data dictionary with loaded values

    # Create StringVars for each emergency field to hold user input
    name_var = tk.StringVar(value=data["contact_name"])
    phone_var = tk.StringVar(value=data["phone"])
    note_var = tk.StringVar(value=data["note"])

    # Emergency contact title label
    tk.Label(root, text="🚨 Emergency Contact", font=("Helvetica", 18, "bold"), bg="#ffe6e6").pack(pady=20)

    # Create input fields for contact name, phone, and notes
    for label, var in [("Contact Name:", name_var), ("Phone:", phone_var), ("Note:", note_var)]:
        tk.Label(root, text=label, bg="#ffe6e6").pack()  # Label for each field
        tk.Entry(root, textvariable=var).pack(pady=5)  # Entry box for user input

    def save_emergency():
        # Function to save the emergency contact data when the save button is pressed
        data = {
            "contact_name": name_var.get(),  # Get contact name from input
            "phone": phone_var.get(),  # Get phone number from input
            "note": note_var.get()  # Get additional notes from input
        }
        # Write the updated emergency data to the JSON file
        with open(filepath, "w") as f:
            json.dump(data, f)  # Save data in JSON format

    # Button to save the emergency contact data
    tk.Button(root, text="Save", bg="#dc3545", fg="white", command=save_emergency).pack(pady=10)
    # Button to go back to the dashboard
    tk.Button(root, text="← Back to Dashboard", command=lambda: open_dashboard(root, username, logout_callback)).pack(pady=10)

    root.mainloop()  # Start the Tkinter event loop to display the emergency info page
