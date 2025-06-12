import tkinter as tk
from tkinter import messagebox
import json
import os
from dashboard_page import open_dashboard
from datetime import datetime

DATA_DIR = "data"

def open_health_log(root, username, logout_callback):
    if root:
        root.destroy()

    os.makedirs(DATA_DIR, exist_ok=True)

    root = tk.Tk()
    root.title("Health Log")
    root.geometry("450x600")
    root.configure(bg="#fff5e6")

    filepath = os.path.join(DATA_DIR, f"{username}_healthlog.json")

    logs = []
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            logs = json.load(f)

    # Input variables
    bp_var = tk.StringVar()
    temp_var = tk.StringVar()
    weight_var = tk.StringVar()
    mood_var = tk.StringVar()

    # Title
    tk.Label(root, text="🩺 Health Log", font=("Helvetica", 18, "bold"), bg="#fff5e6").pack(pady=20)

    # Input fields
    tk.Label(root, text="Blood Pressure:", bg="#fff5e6").pack()
    tk.Entry(root, textvariable=bp_var).pack(pady=5)

    tk.Label(root, text="Temperature (°C):", bg="#fff5e6").pack()
    tk.Entry(root, textvariable=temp_var).pack(pady=5)

    tk.Label(root, text="Weight (kg):", bg="#fff5e6").pack()
    tk.Entry(root, textvariable=weight_var).pack(pady=5)

    tk.Label(root, text="Mood:", bg="#fff5e6").pack()
    tk.Entry(root, textvariable=mood_var).pack(pady=5)

    # Text area to display logs
    display = tk.Text(root, height=12, width=50)
    display.pack(pady=10)

    def log_health():
        # Input validation
        if not (bp_var.get().strip() and temp_var.get().strip() and 
                weight_var.get().strip() and mood_var.get().strip()):
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            float(temp_var.get())
            float(weight_var.get())
        except ValueError:
            messagebox.showerror("Input Error", "Temperature and Weight must be numbers.")
            return

        # Create entry
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "bp": bp_var.get(),
            "temp": temp_var.get(),
            "weight": weight_var.get(),
            "mood": mood_var.get()
        }
        logs.append(entry)

        # Save to file
        with open(filepath, "w") as f:
            json.dump(logs, f)

        # Clear inputs
        bp_var.set("")
        temp_var.set("")
        weight_var.set("")
        mood_var.set("")

        refresh_display()

    def refresh_display():
        display.delete(1.0, tk.END)
        for entry in logs[-5:][::-1]:
            display.insert(tk.END, (
                f"{entry['date']} | BP: {entry['bp']}, Temp: {entry['temp']}°C, "
                f"Weight: {entry['weight']}kg, Mood: {entry['mood']}\n"
            ))

    # Buttons
    tk.Button(root, text="Save Log", bg="#007bff", fg="white", command=log_health).pack()
    tk.Button(root, text="← Back to Dashboard", command=lambda: open_dashboard(root, username, logout_callback)).pack(pady=10)

    refresh_display()
    root.mainloop()
