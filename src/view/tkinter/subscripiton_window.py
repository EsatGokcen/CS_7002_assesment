import tkinter as tk
from tkinter import messagebox

from src.controller.gym_controller import GymController
from src.controller.member_controller import MemberController


class SubscriptionWindow:
    def __init__(self, master, controller, registration_details: list, gyms: list[GymController]):
        self.master = master
        self.controller = controller
        self.registration_details = registration_details
        self.gyms = gyms
        self.master.title("Gym Subscription")
        self.master.geometry("600x600")
        #self.master.configure(bg="#b0c4de") # for colour

        # Gym Selection Label and Dropdown
        tk.Label(master, text="Select Gym:").pack(pady=5)
        self.gym_var = tk.StringVar(master)
        self.gym_var.set("Select a gym")
        self.gym_names = [str(gym) for gym in self.gyms]  # Extract gym names from objects
        self.gym_dropdown = tk.OptionMenu(master, self.gym_var, *self.gyms)
        self.gym_dropdown.pack(pady=5)

        # Subscription Type Label and Dropdown
        tk.Label(master, text="Select Subscription Type:").pack(pady=5)
        self.subscription_var = tk.StringVar(master)
        self.subscription_var.set("Select a type")
        self.subscriptions = ["Trial", "Regular", "Premium"]
        self.subscription_dropdown = tk.OptionMenu(master, self.subscription_var, *self.subscriptions)
        self.subscription_dropdown.pack(pady=5)

        # Payment Frequency Label and Dropdown
        tk.Label(master, text="Select Payment Frequency:").pack(pady=5)
        self.payment_var = tk.StringVar(master)
        self.payment_var.set("Select a frequency")
        self.payment_frequencies = ["Monthly", "Quarterly", "Annually"]
        self.payment_dropdown = tk.OptionMenu(master, self.payment_var, *self.payment_frequencies)
        self.payment_dropdown.pack(pady=5)

        # Confirm Button
        tk.Button(master, text="Confirm", command=self.confirm_subscription).pack(pady=10)

        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=5)

        # Payment Amount for Duration Label
        self.amount_label = tk.Label(master, text=f"Payment Amount: ")
        self.amount_label.pack(pady=5)
        self.duration_label = tk.Label(master, text=f"Subscription duration: ")
        self.duration_label.pack(pady=5)
        tk.Button(master, text="Reveal", command=self.get_payment_amount_and_duration).pack(pady=10)

    def confirm_subscription(self):
        selected_gym_str = self.gym_var.get()
        selected_subscription = self.subscription_var.get()
        selected_payment = self.payment_var.get()

        if selected_gym_str == "Select a gym" or selected_subscription == "Select a type" or selected_payment == "Select a frequency":
            messagebox.showerror("Error", "All fields must be selected.")
        else:
            # Find the corresponding GymController object using the __str__ representation
            selected_gym = next((gym for gym in self.gyms if str(gym) == selected_gym_str), None)

            if not selected_gym:
                messagebox.showerror("Error", "Selected gym not found.")
                return

            # Create member and add to the gym
            member = self.create_member_object(selected_subscription)
            selected_gym.create_member(member)

            selected_gym.read_gym()

            messagebox.showinfo(
                "Subscription Confirmed",
                f"You have selected {selected_subscription} subscription at {selected_gym_str} with {selected_payment} payments."
            )
            # Navigate to the next window or dashboard
            self.open_dashboard_window()

    def open_dashboard_window(self):
        self.controller.show_dashboard_window()

    def create_member_object(self, selected_subscription: str):
        name = self.registration_details[0]
        email = self.registration_details[1]
        phone_number = self.registration_details[2]
        username =  self.registration_details[3]
        password = self.registration_details[4]

        member_controller = MemberController()

        if selected_subscription == "Trial":
            member = member_controller.create_trial_member(name, email, phone_number, username, password)
        elif selected_subscription == "Regular":
            member = member_controller.create_regular_member(name, email, phone_number, username, password)
        elif selected_subscription == "Premium":
            member = member_controller.create_premium_member(name, email, phone_number, username, password)
        else:
            raise ValueError("Incorrect input, chosen subscription does not exist!")

        return member

    def go_back(self):
        self.controller.show_registration_window()

    def get_payment_amount_and_duration(self):
        amount = "£0"
        duration = "0 days"

        selected_subscription = self.subscription_var.get()
        selected_payment = self.payment_var.get()

        if selected_subscription == "Trial":
            amount = "£0"
            duration = "7 days"
        elif selected_subscription == "Regular":
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

        self.amount_label.config(text=f"Payment Amount: {amount}")
        self.duration_label.config(text=f"Subscription duration: {duration}")