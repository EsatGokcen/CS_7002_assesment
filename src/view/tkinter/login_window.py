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
        self.gym_map = {str(gym): gym for gym in self.gyms}  # Extract gym names from objects
        self.gym_dropdown = tk.OptionMenu(master, self.gym_var, *self.gym_map.keys())
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
        user_type, user_object = self.get_login_data()

        if user_type == "member":
            messagebox.showinfo("Login Success", "Welcome to the Dashboard!")
            self.open_dashboard_window(user_object)
        elif user_type == "manager":
            messagebox.showinfo("Login Success", "Welcome to Admin Dashboard!")
            self.open_admin_dashboard_window()
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

    def open_register_window(self):
        messagebox.showinfo("Redirect", "Redirecting to Registration...")
        self.controller.show_registration_window()

    def open_dashboard_window(self, member):
        selected_gym_str = self.gym_var.get()
        try:
            selected_gym = self.gym_map[selected_gym_str]
        except KeyError:
            messagebox.showerror("Error", "Invalid GYM selection.")
            return

        self.controller.show_dashboard_window(selected_gym, member)

    def open_admin_dashboard_window(self):
        selected_gym_str = self.gym_var.get()
        # Get object values of gym string
        try:
            selected_gym = self.gym_map[selected_gym_str]
        except KeyError:
            messagebox.showerror("Error", "Invalid GYM selection.")
            return
        self.controller.show_admin_dashboard_window(selected_gym)

    def get_login_data(self):
        selected_gym_str = self.gym_var.get()
        username_entry = self.username_entry.get()
        password_entry = self.password_entry.get()

        # Demand data entry
        if selected_gym_str == "Select a gym":
            messagebox.showerror("Error", "Please select a gym.")
            return None, None

        if not username_entry or not password_entry:
            messagebox.showerror("Error", "Username and Password cannot be empty.")
            return None, None

        # Find the corresponding GymController object using the __str__ representation
        selected_gym = next((gym for gym in self.gyms if str(gym) == selected_gym_str), None)

        if not selected_gym:
            messagebox.showerror("Error", "Selected gym not found.")
            return None, None

        # Compare the username and password to existing data
        members_list = selected_gym.model.get_list_of_members()
        manager = selected_gym.model.get_gym_manager()
        manager_username = manager.get_username()
        manager_password = manager.get_password()

        if manager_username == username_entry and manager_password == password_entry:
            return "manager", None

        for member in members_list:
            if member.get_username() == username_entry and member.get_password() == password_entry:
                return "member", member

        return None, None


