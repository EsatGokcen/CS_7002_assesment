import tkinter as tk
from tkinter import messagebox

class DashboardWindow:
    def __init__(self, master, controller, selected_gym, username: str, password: str):
        self.master = master
        self.controller = controller
        self.selected_gym = selected_gym
        self.username = username
        self.password = password
        self.master.title("Dashboard")
        self.master.geometry("500x1000")

        # Show Member Details
        tk.Label(master, text="Member Details:", font=("Arial", 24)).pack(pady=10)
        tk.Label(master, text=f"Name: {self.get_name()}").pack(pady=5)

    def get_name(self):
        pass


