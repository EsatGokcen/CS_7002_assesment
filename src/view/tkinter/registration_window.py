import tkinter as tk
from tkinter import messagebox


class RegistrationWindow:

    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Registration")
        self.master.geometry("600x400")
        #self.master.configure(bg="#b0c4de") # For colour

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
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not password or not confirm_password:
            messagebox.showerror("Registration Failed", "All fields are required")
            return

        if password != confirm_password:
            messagebox.showerror("Registration Failed", "Passwords do not match")
            return

        messagebox.showinfo("Registration Success", "Account created successfully")
        self.go_back()

    def go_back(self):
        self.controller.show_login_window()
