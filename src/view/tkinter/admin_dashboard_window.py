import tkinter as tk
from tkinter import messagebox

from src.controller.classes_controller import ClassesController


class AdminDashboardWindow:
    def __init__(self, master, controller, selected_gym):
        self.master = master
        self.controller = controller
        self.selected_gym = selected_gym
        self.master.title("Admin Dashboard")
        self.master.geometry("800x600")

        # Title Label
        tk.Label(master, text=f"Admin Dashboard - {str(selected_gym)}", font=("Arial", 16)).pack(pady=10)

        # Add Classes Section
        tk.Label(master, text="Add New Class:", font=("Arial", 12)).pack(pady=5)
        tk.Label(master, text="Class Name:").pack(pady=5)
        self.class_name_entry = tk.Entry(master)
        self.class_name_entry.pack(pady=5)
        tk.Label(master, text="Class Schedule (e.g., Monday 6PM):").pack(pady=5)
        self.class_schedule_entry = tk.Entry(master)
        self.class_schedule_entry.pack(pady=5)
        tk.Button(master, text="Add Class", command=self.add_class).pack(pady=10)

        # Attendance Tracking Section
        tk.Label(master, text="Attendance Tracking:", font=("Arial", 12)).pack(pady=20)
        tk.Button(master, text="View Attendance Records", command=self.view_attendance).pack(pady=5)
        tk.Button(master, text="Generate Class Popularity Report", command=self.generate_class_popularity_report).pack(pady=5)
        tk.Button(master, text="Analyze Peak Hours", command=self.analyze_peak_hours).pack(pady=5)

        # Staff Management Section
        tk.Label(master, text="Staff Management Dashboard:", font=("Arial", 12)).pack(pady=20)
        tk.Button(master, text="View Membership Growth", command=self.view_membership_growth).pack(pady=5)
        tk.Button(master, text="View Revenue Trends", command=self.view_revenue_trends).pack(pady=5)
        tk.Button(master, text="View Trainer Schedules", command=self.view_trainer_schedules).pack(pady=5)
        tk.Button(master, text="Check Equipment Maintenance", command=self.check_equipment_maintenance).pack(pady=5)

        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=20)

    def add_class(self):
        class_name = self.class_name_entry.get()
        class_schedule = self.class_schedule_entry.get()
        if not class_name or not class_schedule:
            messagebox.showerror("Error", "Class Name and Schedule cannot be empty.")
            return

        # Logic to add class to the gym
        class_controller = ClassesController()
        created_class = class_controller.create_class(name=class_name,date=class_schedule,capacity=0,teacher=None,location=None)
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

    def view_membership_growth(self):
        # Logic to view membership growth
        messagebox.showinfo("Membership Growth", "Displaying membership growth (placeholder).")

    def view_revenue_trends(self):
        # Logic to view revenue trends
        messagebox.showinfo("Revenue Trends", "Displaying revenue trends (placeholder).")

    def view_trainer_schedules(self):
        # Logic to view trainer schedules
        messagebox.showinfo("Trainer Schedules", "Displaying trainer schedules (placeholder).")

    def check_equipment_maintenance(self):
        # Logic to check equipment maintenance
        messagebox.showinfo("Equipment Maintenance", "Checking equipment maintenance (placeholder).")

    def go_back(self):
        self.controller.show_login_window()
