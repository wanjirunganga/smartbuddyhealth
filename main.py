# main.py
# This is the main application file for the Smart Health Buddy app using Tkinter for GUI.

import tkinter as tk  # Import the tkinter module for GUI creation
from tkinter import messagebox  # Import messagebox for displaying alerts
from auth import register_user, authenticate_user  # Functions for user registration and login
from dashboard_page import open_dashboard  # Function to open the dashboard page after login
from utils import ensure_data_dir  # Function to ensure the data directory exists

class SmartHealthBuddyApp:
    def __init__(self, root):
        # Initialize the app with the main tkinter root window
        self.root = root
        self.root.title("Smart Health Buddy")  # Set the window title
        self.username = None  # Currently logged in username
        ensure_data_dir()  # Ensure the data folder exists to store user files
        self.create_login_page()  # Start with the login page

    def clear_window(self):
        # Clear all widgets from the root window; used to refresh UI pages
        for widget in self.root.winfo_children():
            widget.destroy()  # Destroy each widget in the window

    def create_login_page(self):
        # Create the login screen UI
        self.clear_window()  # Clear the window before creating a new page

        # App title label
        tk.Label(self.root, text="Smart Health Buddy", font=("Helvetica", 18, "bold")).pack(pady=20)
        
        # Username label and entry box
        tk.Label(self.root, text="Username:").pack()
        self.username_var = tk.StringVar()  # Variable to hold the username input
        tk.Entry(self.root, textvariable=self.username_var).pack()  # Entry box for username

        # Password label and entry box (masked input)
        tk.Label(self.root, text="Password:").pack()
        self.password_var = tk.StringVar()  # Variable to hold the password input
        tk.Entry(self.root, textvariable=self.password_var, show="*").pack()  # Entry box for password

        # Login button triggers login_user method
        tk.Button(self.root, text="Login", command=self.login_user).pack(pady=10)
        # Register button triggers register_user method
        tk.Button(self.root, text="Register", command=self.register_user).pack()

    def login_user(self):
        # Handle login button press
        username = self.username_var.get().strip()  # Get the username input
        password = self.password_var.get().strip()  # Get the password input

        # Check if credentials are valid using authenticate_user from auth.py
        if authenticate_user(username, password):
            self.username = username  # Save logged in user
            # Open dashboard page and pass current root, username, and logout callback (this creates login page again on logout)
            open_dashboard(self.root, self.username, self.create_login_page)
        else:
            # Show error popup if login failed
            messagebox.showerror("Error", "Invalid username or password")

    def register_user(self):
        # Handle the register button press
        username = self.username_var.get().strip()  # Get the username input
        password = self.password_var.get().strip()  # Get the password input

        # Attempt to register new user using register_user from auth.py
        if register_user(username, password):
            # Show success info popup
            messagebox.showinfo("Success", "User  registered! Please login.")
        else:
            # Show error if username already exists
            messagebox.showerror("Error", "Username already exists.")

if __name__ == "__main__":
    # Create the main Tkinter window and start the app
    root = tk.Tk()  # Create a new Tkinter window
    app = SmartHealthBuddyApp(root)  # Initialize the SmartHealthBuddyApp with the root window
    root.mainloop()  # Start the Tkinter event loop to display the app
