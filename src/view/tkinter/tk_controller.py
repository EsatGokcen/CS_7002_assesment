import tkinter as tk

from src.controller.gym_controller import GymController
from src.view.tkinter.login_window import LoginWindow
from src.view.tkinter.registration_window import RegistrationWindow
from src.view.tkinter.subscripiton_window import SubscriptionWindow


class TkController:
    def __init__(self, gyms: list[GymController]):
        self.root = tk.Tk()
        self.gyms = gyms

    def start(self):
        self.show_login_window()
        self.root.mainloop()

    def show_login_window(self):
        self.clear_window()
        LoginWindow(self.root, self)

    def show_registration_window(self):
        self.clear_window()
        RegistrationWindow(self.root, self)

    def show_subscription_window(self, registration_details: list):
        self.clear_window()
        SubscriptionWindow(self.root, self, registration_details, self.gyms)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
