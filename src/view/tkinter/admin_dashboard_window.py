import tkinter as tk
from tkinter import messagebox

from src.controller.classes_controller import ClassesController


class AdminDashboardWindow:
    def __init__(self, master, controller, selected_gym):
        self.master = master
        self.controller = controller
        self.selected_gym = selected_gym
        self.master.title("Admin Dashboard")
        self.master.geometry("1000x800")

        # Title Label
        tk.Label(master, text=f"Admin Dashboard - {str(selected_gym)}", font=("Arial", 16)).pack(pady=10)

        # Add Classes Section
        tk.Label(master, text="Add New Class:", font=("Arial", 12)).pack(pady=5)
        tk.Label(master, text="Class Name:").pack(pady=5)
        self.class_name_entry = tk.Entry(master)
        self.class_name_entry.pack(pady=5)
        tk.Label(master, text="Class Schedule (e.g., 13/01/25 - 6PM):").pack(pady=5)
        self.class_schedule_entry = tk.Entry(master)
        self.class_schedule_entry.pack(pady=5)
        tk.Label(master, text="Class Capacity").pack(pady=5)
        self.class_capacity_entry = tk.Entry(master)
        self.class_capacity_entry.pack(pady=5)

        # Teacher Dropdown
        tk.Label(master, text="Select Teacher:").pack(pady=5)
        self.teacher_var = tk.StringVar(master)
        self.teacher_var.set("Select a teacher")
        self.teacher_map = {str(teacher): teacher for teacher in self.selected_gym.model.get_list_of_staff()}
        self.teacher_dropdown = tk.OptionMenu(master, self.teacher_var, *self.teacher_map.keys())
        self.teacher_dropdown.pack(pady=5)

        # Location Dropdown
        tk.Label(master, text="Select Location:").pack(pady=5)
        self.location_var = tk.StringVar(master)
        self.location_var.set("Select a location")
        self.location_map = {str(location): location for location in self.selected_gym.model.get_gym_workout_zones()}
        self.location_dropdown = tk.OptionMenu(master, self.location_var, *self.location_map.keys())
        self.location_dropdown.pack(pady=5)

        tk.Button(master, text="Add Class", command=self.add_class).pack(pady=10)

        # Attendance Tracking Section
        tk.Label(master, text="Attendance Tracking:", font=("Arial", 12)).pack(pady=20)
        tk.Button(master, text="View Attendance Records", command=self.view_attendance).pack(pady=5)
        tk.Button(master, text="Generate Class Popularity Report", command=self.generate_class_popularity_report).pack(pady=5)
        tk.Button(master, text="Analyze Peak Hours", command=self.analyze_peak_hours).pack(pady=5)

        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=20)

    def add_class(self):
        class_name = self.class_name_entry.get()
        class_schedule = self.class_schedule_entry.get()
        class_capacity = self.class_capacity_entry.get()
        class_teacher_str = self.teacher_var.get()
        class_location_str = self.location_var.get()

        # Make sure each field has been filled
        if not class_name or not class_schedule or not class_capacity or not class_teacher_str == "Select a teacher" or class_location_str == "Select a location":
            messagebox.showerror("Error", "Class Attributes cannot be empty.")
            return

        # Get object values of teacher and location string
        try:
            class_teacher = self.teacher_map[class_teacher_str]
            class_location = self.location_map[class_location_str]
        except KeyError:
            messagebox.showerror("Error", "Invalid selection.")
            return

        # Logic to add class to the gym
        class_controller = ClassesController()
        created_class = class_controller.create_class(name=class_name,date=class_schedule,capacity=int(class_capacity),
                                                      teacher=class_teacher,location=class_location)
        self.selected_gym.create_class(created_class)
        messagebox.showinfo("Success", f"Class '{class_name}' added successfully with schedule '{class_schedule}'.")

    def view_attendance(self):
        # Logic to view attendance records
        messagebox.showinfo("Attendance Records", "Displaying attendance records (placeholder).")

    def generate_class_popularity_report(self):
        # Logic to generate class popularity report
        messagebox.showinfo("Class Popularity Report", "Generating class popularity report (placeholder).")

    def analyze_peak_hours(self):
        # Logic to analyze peak hours
        messagebox.showinfo("Peak Hours Analysis", "Analyzing peak hours (placeholder).")

    def go_back(self):
        self.controller.show_login_window()
