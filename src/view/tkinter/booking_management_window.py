import tkinter as tk
from tkinter import messagebox

class BookingManagementWindow:

    def __init__(self, master, controller, selected_gym, member):
        self.master = master
        self.controller = controller
        self.selected_gym = selected_gym
        self.member = member
        self.master.title("Booking Management")
        self.master.geometry("600x600")

        # Title
        tk.Label(master, text="Booking Management", font=("Arial", 24)).pack(pady=10)

        # Available Classes Section
        tk.Label(master, text="Available Classes:", font=("Arial", 18)).pack(pady=5)
        self.classes_listbox = tk.Listbox(master, width=50, height=10)
        self.classes_listbox.pack(pady=5)
        for a_class in self.selected_gym.model.get_list_of_classes():
            self.classes_listbox.insert(tk.END, str(a_class))

        # Book a Class Button
        tk.Button(master, text="Book Selected Class", command=self.book_class).pack(pady=5)

        # Available Nutritionists and Personal Trainers Section
        tk.Label(master, text="Available Nutritionists and Personal Trainers:", font=("Arial", 18)).pack(pady=10)
        self.sessions_listbox = tk.Listbox(master, width=50, height=10)
        self.sessions_listbox.pack(pady=5)
        # logic to select staff

        # Book a Session Button
        tk.Button(master, text="Book Selected Session", command=self.book_session).pack(pady=5)

        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=20)

    def book_class(self):
        try:
            selected_index = self.classes_listbox.curselection()
            if not selected_index:
                raise ValueError("No class selected.")
            selected_class = self.selected_gym.model.get_list_of_classes()[selected_index[0]]
            selected_class.add_attendee(self.member)
            messagebox.showinfo("Success", f"Class '{selected_class}' booked successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def book_session(self):
        pass

    def go_back(self):
        self.controller.show_dashboard_window(self.selected_gym, self.member)
