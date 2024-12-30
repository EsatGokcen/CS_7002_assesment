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
        self.gym_names = [gym.model.get_gym_city() for gym in self.gyms]  # Extract gym names from objects
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

    def confirm_subscription(self):
        selected_gym = self.gym_var.get()
        selected_subscription = self.subscription_var.get()
        selected_payment = self.payment_var.get()

        if selected_gym == "Select a gym" or selected_subscription == "Select a type" or selected_payment == "Select a frequency":
            messagebox.showerror("Error", "All fields must be selected.")
        else:
            messagebox.showinfo(
                "Subscription Confirmed",
                f"You have selected {selected_subscription} subscription at {selected_gym} with {selected_payment} payments."
            )
            # Navigate to the next window or dashboard

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
