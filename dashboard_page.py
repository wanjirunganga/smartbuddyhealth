import tkinter as tk  # Import the tkinter module for GUI creation

def open_dashboard(root, username, logout_callback):
    # Function to open the dashboard window for the logged-in user
    if root:
        root.destroy()  # Destroy the previous window if it exists

    # Create a new Tkinter window for the dashboard
    root = tk.Tk()
    root.title("Smart Health Buddy - Dashboard")  # Set the window title
    root.geometry("400x400")  # Set the window size
    root.configure(bg="#e6f2ff")  # Set the background color

    # Welcome label displaying the username
    tk.Label(root, text=f"Welcome, {username}!", font=("Helvetica", 18, "bold"), bg="#e6f2ff").pack(pady=20)

    # Import necessary functions inside this function to avoid circular imports
    from profile import open_profile  # Function to open the profile page
    from health_log import open_health_log  # Function to open the health log page
    from emergency import open_emergency_info  # Function to open the emergency info page

    # Button to open the profile page
    tk.Button(root, text="👤 Profile", width=25, bg="#007bff", fg="white",
              command=lambda: open_profile(root, username, logout_callback)).pack(pady=10)

    # Button to open the health log page
    tk.Button(root, text="🩺 Health Log", width=25, bg="#28a745", fg="white",
              command=lambda: open_health_log(root, username, logout_callback)).pack(pady=10)

    # Button to open the emergency info page
    tk.Button(root, text="🚨 Emergency Info", width=25, bg="#dc3545", fg="white",
              command=lambda: open_emergency_info(root, username, logout_callback)).pack(pady=10)

    # Button to log out the user
    tk.Button(root, text="🔒 Logout", width=25, bg="#6c757d", fg="white", 
              command=lambda: (root.destroy(), logout_callback())).pack(pady=30)

    root.mainloop()  # Start the Tkinter event loop to display the dashboard
