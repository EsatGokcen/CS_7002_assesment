import tkinter as tk
from src.view.tkinter.login_window import LoginWindow
from src.view.tkinter.registration_window import RegistrationWindow
from src.view.tkinter.subscripiton_window import SubscriptionWindow


class TkController:
    def __init__(self):
        self.root = tk.Tk()

    def start(self):
        self.show_login_window()
        self.root.mainloop()

    def show_login_window(self):
        self.clear_window()
        LoginWindow(self.root, self)

    def show_registration_window(self):
        self.clear_window()
        RegistrationWindow(self.root, self)

    def show_subscription_window(self):
        self.clear_window()
        SubscriptionWindow(self.root, self)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def might_be_useful_later(self, master):
        # Gym Selection Label and Dropdown
        tk.Label(master, text="Select Gym:").pack(pady=5)
        self.gym_var = tk.StringVar(master)
        self.gym_var.set("Select a gym")  # Default value
        self.gyms = ["Other"]  # Example gym list
        self.gym_dropdown = tk.OptionMenu(master, self.gym_var, *self.gyms)
        self.gym_dropdown.pack(pady=5)