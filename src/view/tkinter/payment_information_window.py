import tkinter as tk
from tkinter import messagebox

class PaymentInformationWindow:

    def __init__(self, master, controller, selected_gym, member):
        self.master = master
        self.controller = controller
        self.selected_gym = selected_gym
        self.member = member
        self.master.title("Payment Information")
        self.master.geometry("600x600")

        # Show Payment Information
        tk.Label(master, text="Payment Information:", font=("Arial", 20)).pack(pady=10)
        tk.Label(master, text=f"Subscription type: {self.get_member_type()}").pack(pady=5)
        tk.Label(master, text=f"Amount due: {self.member.get_payment_amount()}").pack(pady=5)
        tk.Label(master, text=f"Subscription duration: {self.member.get_payment_duration()}").pack(pady=5)

        # Edit Payment Information
        tk.Label(master, text="Edit Payment Information:", font=("Arial", 20)).pack(pady=10)
        # Subscription Type Label and Dropdown
        tk.Label(master, text="Select Subscription Type:").pack(pady=5)
        self.subscription_var = tk.StringVar(master)
        self.subscription_var.set("Select a type")
        self.subscriptions = ["Regular", "Premium"]
        self.subscription_dropdown = tk.OptionMenu(master, self.subscription_var, *self.subscriptions)
        self.subscription_dropdown.pack(pady=5)
        # Payment Frequency Label and Dropdown
        tk.Label(master, text="Select Payment Frequency:").pack(pady=5)
        self.payment_var = tk.StringVar(master)
        self.payment_var.set("Select a frequency")
        self.payment_frequencies = ["Monthly", "Quarterly", "Annually"]
        self.payment_dropdown = tk.OptionMenu(master, self.payment_var, *self.payment_frequencies)
        self.payment_dropdown.pack(pady=5)

        # Submit Button
        tk.Button(master, text="Submit", command=self.submit).pack(pady=15)
        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=5)

    def get_member_type(self):
        if self.member.get_new_member_type() is None:
            return f"{self.member.get_member_type()} member"
        else:
            return f"{self.member.get_new_member_type()} member"

    def submit(self):
        amount = "£0"
        duration = "0 days"

        selected_subscription = self.subscription_var.get()
        selected_payment = self.payment_var.get()

        if selected_subscription == "Regular":
            if selected_payment == "Monthly":
                amount = "£30"
                duration = "1 month"
            elif selected_payment == "Quarterly":
                amount = "£90"
                duration = "3 months"
            elif selected_payment == "Annually":
                amount = "£330"
                duration = "12 months"
        elif selected_subscription == "Premium":
            if selected_payment == "Monthly":
                amount = "£50"
                duration = "1 month"
            elif selected_payment == "Quarterly":
                amount = "£150"
                duration = "3 months"
            elif selected_payment == "Annually":
                amount = "£550"
                duration = "12 months"

        self.member.set_new_member_type(selected_subscription)
        self.member.set_payment_amount(amount)
        self.member.set_payment_duration(duration)

        return (
            messagebox.showinfo("Submit", "New payment information submitted successfully!"),
            messagebox.showinfo("Details", f"New amount due: {amount}, subscription duration: {duration}, subscription type: {selected_subscription}")
        )

    def go_back(self):
        self.controller.show_dashboard_window(self.selected_gym, self.member)