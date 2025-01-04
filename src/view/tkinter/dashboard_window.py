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
        tk.Label(master, text=f"Membership status: {self.get_membership_status()}").pack(pady=5)
        tk.Label(master, text=f"Booked classes: {self.get_booked_classes()}").pack(pady=5)

        # Book a class

        # Navigation section
        tk.Label(master, text="Navigation Section:", font=("Arial", 18)).pack(pady=15)
        # Edit Member Details section
        # Payment information section
        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=5)

    def get_name(self):
        pass

    def get_membership_status(self):
        pass

    def get_booked_classes(self):
        pass

    def go_back(self):
        self.controller.show_login_window()



