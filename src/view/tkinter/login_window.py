import tkinter as tk
from tkinter import messagebox

from src.model.gym_model import GymModel
from src.view.tkinter.tk_controller import TkController


class LoginWindow:

    def __init__(self, master, controller: TkController):
        self.master = master
        self.controller = controller
        self.master.title("Login")
        self.master.geometry("600x400")
        #self.master.configure(bg="#b0c4de") # For colour

        # Gym Selection Label and Dropdown
        tk.Label(master, text="Select Gym:").pack(pady=5)
        self.gym_var = tk.StringVar(master)
        self.gym_var.set("Select a gym")  # Default value
        self.gyms = []  # Example gym list
        self.gym_dropdown = tk.OptionMenu(master, self.gym_var, *self.gyms)
        self.gym_dropdown.pack(pady=5)

        # Username Label and Entry
        tk.Label(master, text="Username:").pack(pady=5)
        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=5)

        # Password Label and Entry
        tk.Label(master, text="Password:").pack(pady=5)
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=5)

        # Login Button
        tk.Button(master, text="Login", command=self.login).pack(pady=10)

        # Register Button
        tk.Button(master, text="Register", command=self.open_register_window).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            messagebox.showinfo("Login Success", "Welcome to the Dashboard!")
            # Logic to transition to the Dashboard Window
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

    def open_register_window(self):
        messagebox.showinfo("Redirect", "Redirecting to Registration...")
        self.controller.show_registration_window()

    def get_gyms_list(self) -> list[GymModel]:
        return self.gyms
