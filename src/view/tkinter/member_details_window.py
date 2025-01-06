import tkinter as tk
from tkinter import messagebox

class MemberDetailsWindow:
    def __init__(self, master, controller, member):
        self.master = master
        self.controller = controller
        self.member = member
        self.master.title("Member Details")
        self.master.geometry("600x600")

        # Edit Member Details
        tk.Label(master, text="Edit Member Details:", font=("Arial", 24)).pack(pady=10)
        tk.Label(master, text="Name:").pack(pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.pack(pady=5)
        tk.Label(master, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5)
        tk.Label(master, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(master)
        self.password_entry.pack(pady=5)
        tk.Label(master, text="Email:").pack(pady=5)
        self.email_entry = tk.Entry(master)
        self.email_entry.pack(pady=5)
        tk.Label(master, text="Phone Number:").pack(pady=5)
        self.phone_number_entry = tk.Entry(master)
        self.phone_number_entry.pack(pady=5)
        tk.Label(master, text="Health Information:").pack(pady=5)
        self.health_info_entry = tk.Entry(master)
        self.health_info_entry.pack(pady=5)

        # Submit Button
        tk.Button(master, text="Submit", command=self.submit).pack(pady=15)
        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=5)

    def submit(self):
        pass

    def go_back(self):
        self.controller.show_login_window()