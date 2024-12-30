import tkinter as tk
from tkinter import messagebox


class RegistrationWindow:

    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Registration")
        self.master.geometry("600x600")
        #self.master.configure(bg="#b0c4de") # For colour

        # Name Label and Entry
        tk.Label(master, text="Name: ").pack(pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.pack(pady=5)

        # Email Label and Entry
        tk.Label(master, text="Email: ").pack(pady=5)
        self.email_entry = tk.Entry(master)
        self.email_entry.pack(pady=5)

        # Phone Number Label and Entry
        tk.Label(master, text="Phone Number: ").pack(pady=5)
        self.phone_number_entry = tk.Entry(master)
        self.phone_number_entry.pack(pady=5)

        # Username Label and Entry
        tk.Label(master, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5)

        # Password Label and Entry
        tk.Label(master, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=5)

        # Confirm Password Label and Entry
        tk.Label(master, text="Confirm Password:").pack(pady=5)
        self.confirm_password_entry = tk.Entry(master, show="*")
        self.confirm_password_entry.pack(pady=5)

        # Register Button
        tk.Button(master, text="Register", command=self.register).pack(pady=10)

        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=5)

    def register(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone_number = self.phone_number_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        registration_details = [name, email, phone_number, username, password]

        if not name or not email or not phone_number or not username or not password or not confirm_password:
            messagebox.showerror("Registration Failed", "All fields are required")
            return

        if password != confirm_password:
            messagebox.showerror("Registration Failed", "Passwords do not match")
            return

        messagebox.showinfo("Registration Success", "Account created successfully")
        self.open_subscription_window(registration_details)

    def open_subscription_window(self, registration_details: list):
        messagebox.showinfo("Subscribe", "Complete your subscription...")
        self.controller.show_subscription_window(registration_details)

    def go_back(self):
        self.controller.show_login_window()
