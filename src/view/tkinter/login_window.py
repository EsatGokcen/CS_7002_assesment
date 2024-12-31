import tkinter as tk
from tkinter import messagebox


class LoginWindow:

    def __init__(self, master, controller, gyms):
        self.master = master
        self.controller = controller
        self.gyms = gyms
        self.master.title("Login")
        self.master.geometry("600x400")
        #self.master.configure(bg="#b0c4de") # For colour

        # Gym Selection Label and Dropdown
        tk.Label(master, text="Select Gym:").pack(pady=5)
        self.gym_var = tk.StringVar(master)
        self.gym_var.set("Select a gym")
        self.gym_names = [str(gym) for gym in self.gyms]  # Extract gym names from objects
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
        if self.get_login_data():
            messagebox.showinfo("Login Success", "Welcome to the Dashboard!")
            # Logic to transition to the Dashboard Window
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

    def open_register_window(self):
        messagebox.showinfo("Redirect", "Redirecting to Registration...")
        self.controller.show_registration_window()

    def get_login_data(self):
        selected_gym_str = self.gym_var.get()
        username_entry = self.username_entry.get()
        password_entry = self.password_entry.get()

        # Demand data entry
        if selected_gym_str == "Select a gym":
            messagebox.showerror("Error", "Please select a gym.")
            return False

        if not username_entry or not password_entry:
            messagebox.showerror("Error", "Username and Password cannot be empty.")
            return False

        # Find the corresponding GymController object using the __str__ representation
        selected_gym = next((gym for gym in self.gyms if str(gym) == selected_gym_str), None)

        if not selected_gym:
            messagebox.showerror("Error", "Selected gym not found.")
            return

        # Compare the username and password to existing data
        members_list = selected_gym.model.get_list_of_members()
        for member in members_list:
            username = member.get_username()
            password = member.get_password()
            if username == username_entry and password == password_entry:
                return True
        return False

