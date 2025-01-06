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
        name_entry = self.name_entry.get()
        username_entry = self.username_entry.get()
        password_entry = self.password_entry.get()
        email_entry = self.email_entry.get()
        phone_number_entry = self.phone_number_entry.get()
        health_info_entry = self.health_info_entry.get()

        if not name_entry or not username_entry or not password_entry or not email_entry or not phone_number_entry or not health_info_entry:
            messagebox.showerror("Error", "Text boxes cannot be empty.")
            return None

        self.member.set_name(name_entry)
        self.member.set_username(username_entry)
        self.member.set_password(password_entry)
        self.member.set_email(email_entry)
        self.member.set_phone_number(phone_number_entry)
        self.member.set_health_info(health_info_entry)

        return messagebox.showinfo("Submit", "Member information submitted successfully!")

    def go_back(self):
        self.controller.show_dashboard_window()