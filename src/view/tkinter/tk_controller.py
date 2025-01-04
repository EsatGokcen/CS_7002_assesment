import tkinter as tk

from src.controller.gym_controller import GymController
from src.view.tkinter.admin_dashboard_window import AdminDashboardWindow
from src.view.tkinter.dashboard_window import DashboardWindow
from src.view.tkinter.login_window import LoginWindow
from src.view.tkinter.registration_window import RegistrationWindow
from src.view.tkinter.staff_management_dashboard import StaffManagementWindow
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
        LoginWindow(self.root, self, self.gyms)

    def show_registration_window(self):
        self.clear_window()
        RegistrationWindow(self.root, self)

    def show_subscription_window(self, registration_details: list):
        self.clear_window()
        SubscriptionWindow(self.root, self, registration_details, self.gyms)

    def show_dashboard_window(self, selected_gym: GymController, username: str, password: str):
        self.clear_window()
        DashboardWindow(self.root, self, selected_gym, username, password)

    def show_booking_management_window(self):
        self.clear_window()
        # functionality for booking management window

    def show_payment_information_window(self):
        self.clear_window()
        # functionality for payment information window

    def show_member_details_window(self):
        self.clear_window()
        # functionality for member details window

    def show_admin_dashboard_window(self, selected_gym: GymController):
        self.clear_window()
        AdminDashboardWindow(self.root, self, selected_gym)

    def show_staff_management_dashboard(self, selected_gym: GymController):
        self.clear_window()
        StaffManagementWindow(self.root, self, selected_gym)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
