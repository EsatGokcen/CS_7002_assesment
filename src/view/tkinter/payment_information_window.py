import tkinter as tk
from tkinter import messagebox

class PaymentInformationWindow:

    def __init__(self, master, controller, member):
        self.master = master
        self.controller = controller
        self.member = member
        self.master.title("Payment Information")
        self.master.geometry("600x600")

        # Show Payment Information
        tk.Label(master, text="Payment Information:", font=("Arial", 22)).pack(pady=10)

        # Edit Payment Information
        tk.Label(master, text="Edit Payment Information:", font=("Arial", 22)).pack(pady=10)

        # Submit Button
        tk.Button(master, text="Submit", command=self.submit).pack(pady=15)
        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=5)

    def submit(self):
        # Logic
        return messagebox.showinfo("Submit", "New payment information submitted successfully!")

    def go_back(self):
        self.controller.show_dashboard_window()