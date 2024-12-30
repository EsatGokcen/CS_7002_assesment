import tkinter as tk
from src.view.tkinter.login_window import LoginWindow
from src.view.tkinter.registration_window import RegistrationWindow

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

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()