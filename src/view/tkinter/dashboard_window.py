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

        # Booked Classes Section
        tk.Label(master, text="Booked Classes:", font=("Arial", 18)).pack(pady=5)
        self.classes_text = tk.Text(master, width=60, height=10, wrap=tk.WORD)
        self.classes_text.pack(pady=5)
        self.display_booked_classes()

        # Booked Sessions Section
        tk.Label(master, text="Booked Sessions:", font=("Arial", 18)).pack(pady=5)
        self.sessions_text = tk.Text(master, width=60, height=10, wrap=tk.WORD)
        self.sessions_text.pack(pady=5)
        self.display_booked_sessions()

        # Navigation Section
        tk.Label(master, text="Navigation Section:", font=("Arial", 24)).pack(pady=15)
        tk.Button(master, text="Booking Management", command=self.open_booking_management_window).pack(pady=5)
        tk.Button(master, text="Edit Member Details", command=self.open_edit_member_details_window).pack(pady=5)
        tk.Button(master, text="Payment Information", command=self.open_payment_information_window).pack(pady=5)
        tk.Button(master, text="Back", command=self.go_back).pack(pady=5)

    def get_name(self) -> str:
        return self.member.get_name()

    def get_membership_status(self) -> str:
        if self.member.get_new_member_type() is None:
            return f"{self.member.get_member_type()} member"
        else:
            return f"{self.member.get_new_member_type()} member"

    def get_booked_classes(self) -> list:
        list_of_classes = self.selected_gym.model.get_list_of_classes()
        list_of_booked_classes = []
        for a_class in list_of_classes:
            if self.member in a_class.get_attendees():
                list_of_booked_classes.append(a_class)
        return list_of_booked_classes

    def get_booked_sessions(self) -> list:
        list_of_booked_sessions = []
        for staff in self.selected_gym.model.get_list_of_staff():
            for session in staff.get_booked_sessions():
                if self.member == session:
                    list_of_booked_sessions.append(staff)
        return list_of_booked_sessions

    def display_booked_classes(self):
        self.classes_text.delete(1.0, tk.END)
        booked_classes = self.get_booked_classes()
        for a_class in booked_classes:
            self.classes_text.insert(tk.END, f"{a_class}\n")
        self.classes_text.config(state=tk.DISABLED)

    def display_booked_sessions(self):
        self.sessions_text.delete(1.0, tk.END)
        booked_sessions = self.get_booked_sessions()
        for session in booked_sessions:
            self.sessions_text.insert(tk.END, f"{session}\n")
        self.sessions_text.config(state=tk.DISABLED)

    def open_booking_management_window(self):
        messagebox.showinfo("Opening...", "Opening booking management window")
        self.controller.show_booking_management_window(self.selected_gym, self.member)

    def open_payment_information_window(self):
        messagebox.showinfo("Opening...", "Opening payment information window")
        self.controller.show_payment_information_window(self.selected_gym, self.member)

    def open_edit_member_details_window(self):
        messagebox.showinfo("Opening...", "Opening edit member details window")
        self.controller.show_member_details_window(self.selected_gym, self.member)

    def go_back(self):
        self.controller.show_login_window()
