import tkinter as tk  # Import the tkinter module for GUI creation
import json  # Module for working with JSON data
import os  # Module for interacting with the operating system
from dashboard_page import open_dashboard  # Function to open the dashboard page
from datetime import datetime  # Module to work with date and time

DATA_DIR = "data"  # Directory where health log data will be stored

def open_health_log(root, username, logout_callback):
    # Function to open the health log page for the logged-in user
    if root:
        root.destroy()  # Destroy the previous window if it exists

    # Create a new Tkinter window for the health log
    root = tk.Tk()
    root.title("Health Log")  # Set the window title
    root.geometry("450x500")  # Set the window size
    root.configure(bg="#fff5e6")  # Set the background color

    # Create the file path for the user's health log data
    filepath = os.path.join(DATA_DIR, f"{username}_healthlog.json")

    logs = []  # List to hold health log entries
    # Check if the health log file exists
    if os.path.exists(filepath):
        # Load existing health log data from the JSON file
        with open(filepath, "r") as f:
            logs = json.load(f)  # Load logs into the list

    # StringVars to hold user input for blood pressure and temperature
    bp_var = tk.StringVar()
    temp_var = tk.StringVar()

    # Health log title label
    tk.Label(root, text="🩺 Health Log", font=("Helvetica", 18, "bold"), bg="#fff5e6").pack(pady=20)

    # Input field for blood pressure
    tk.Label(root, text="Blood Pressure:", bg="#fff5e6").pack()
    tk.Entry(root, textvariable=bp_var).pack(pady=5)

    # Input field for temperature
    tk.Label(root, text="Temperature (°C):", bg="#fff5e6").pack()
    tk.Entry(root, textvariable=temp_var).pack(pady=5)

    # Text area to display the last health log entries
    display = tk.Text(root, height=10, width=45)
    display.pack(pady=10)

    def log_health():
        # Function to log health data when the save button is pressed
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),  # Current date and time
            "bp": bp_var.get(),  # Get blood pressure from input
            "temp": temp_var.get()  # Get temperature from input
        }
        logs.append(entry)  # Add the new entry to the logs list
        
        # Write the updated logs to the JSON file
        with open(filepath, "w") as f:
            json.dump(logs, f)  # Save logs in JSON format

        # Clear input fields after saving
        bp_var.set("")
        temp_var.set("")
        refresh_display()  # Refresh the display to show updated logs

    def refresh_display():
        # Function to refresh the display area with the latest log entries
        display.delete(1.0, tk.END)  # Clear the display area
        # Show the last 5 entries in reverse order
        for entry in logs[-5:][::-1]:  
            display.insert(tk.END, f"{entry['date']} | BP: {entry['bp']}, Temp: {entry['temp']}°C\n")

    # Button to save the health log data
    tk.Button(root, text="Save Log", bg="#007bff", fg="white", command=log_health).pack()
    # Button to go back to the dashboard
    tk.Button(root, text="← Back to Dashboard", command=lambda: open_dashboard(root, username, logout_callback)).pack(pady=10)

    refresh_display()  # Initial call to display existing logs
    root.mainloop()  # Start the Tkinter event loop to display the health log page
