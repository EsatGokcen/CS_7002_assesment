import tkinter as tk
from tkinter import messagebox

class BookingManagementWindow:

    def __init__(self, master, controller, selected_gym, member):
        self.master = master
        self.controller = controller
        self.selected_gym = selected_gym
        self.member = member
        self.master.title("Booking Management")
        self.master.geometry("600x600")

        # Show Available classes

        # Book a class

        # Show available nutritionists and personal trainers

        # Book a session

        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=5)

    def go_back(self):
        self.controller.show_dashboard_window()

