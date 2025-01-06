import tkinter as tk
from tkinter import messagebox

class DashboardWindow:
    def __init__(self, master, controller, selected_gym, member):
        self.master = master
        self.controller = controller
        self.selected_gym = selected_gym
        self.member = member
        self.master.title("Dashboard")
        self.master.geometry("600x600")

        # Show Member Details
        tk.Label(master, text="Member Details:", font=("Arial", 24)).pack(pady=10)
        tk.Label(master, text=f"Name: {self.get_name()}").pack(pady=5)
        tk.Label(master, text=f"Membership status: {self.get_membership_status()}").pack(pady=5)
        tk.Label(master, text=f"Booked classes: {self.get_booked_classes()}").pack(pady=5)

        # Navigation section
        tk.Label(master, text="Navigation Section:", font=("Arial", 24)).pack(pady=15)
        # Booking Management section
        tk.Button(master, text="Booking Management", command=self.open_booking_management_window).pack(pady=5)
        # Edit Member Details section
        tk.Button(master, text="Edit Member Details", command=self.open_edit_member_details_window).pack(pady=5)
        # Payment information section
        tk.Button(master, text="Payment Information", command=self.open_payment_information_window).pack(pady=5)
        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=5)

    def get_name(self) -> str:
        return self.member.get_name()

    def get_membership_status(self) -> str:
        return f"{self.member.get_member_type()} member"

    def get_booked_classes(self) -> list:
        list_of_classes = self.selected_gym.model.get_list_of_classes()
        list_of_booked_classes = []
        for a_class in list_of_classes:
            list_of_attendees = a_class.get_attendees()
            for attendee in list_of_attendees:
                if attendee == self.member:
                    list_of_booked_classes.append(a_class)
        return list_of_booked_classes

    def open_booking_management_window(self):
        messagebox.showinfo("Opening...", "Opening booking management window")
        self.controller.show_booking_management_window()

    def open_payment_information_window(self):
        messagebox.showinfo("Opening...", "Opening payment information window")
        self.controller.show_payment_information_window(self.selected_gym, self.member)

    def open_edit_member_details_window(self):
        messagebox.showinfo("Opening...", "Opening edit member details window")
        self.controller.show_member_details_window(self.member)

    def go_back(self):
        self.controller.show_login_window()



