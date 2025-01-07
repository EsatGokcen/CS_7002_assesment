import tkinter as tk
from tkinter import messagebox

class StaffManagementWindow:
    def __init__(self, master, controller, selected_gym):
        self.master = master
        self.controller = controller
        self.selected_gym = selected_gym
        self.master.title("Admin Dashboard")
        self.master.geometry("500x600")

        # Staff Management Section
        tk.Label(master, text="Staff Management Dashboard:", font=("Arial", 24)).pack(pady=20)
        tk.Button(master, text="View Membership Growth", command=self.view_membership_growth).pack(pady=5)
        tk.Button(master, text="View Monthly Revenue Trends", command=self.view_monthly_revenue_trends).pack(pady=5)
        tk.Button(master, text="View Trainer Schedules", command=self.view_trainer_schedules).pack(pady=5)
        tk.Button(master, text="Check Equipment Maintenance", command=self.check_equipment_maintenance).pack(pady=5)

        # Back Button
        tk.Button(master, text="Back", command=self.go_back).pack(pady=20)

    def view_membership_growth(self):
        try:
            # Get the list of members
            members = self.selected_gym.model.get_list_of_members()

            if not members:
                messagebox.showinfo("Membership Growth", "No members available to analyze growth.")
                return

            # Count members by type
            membership_summary = {}
            for member in members:
                member_type = member.get_member_type()
                if member_type not in membership_summary:
                    membership_summary[member_type] = 0
                membership_summary[member_type] += 1

            # Create a summary report
            report = "Membership Growth Analysis:\n\n"
            for member_type, count in membership_summary.items():
                report += f"{member_type}: {count} members\n"

            # Display the report
            messagebox.showinfo("Membership Growth", report)

        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve membership data: {e}")

    def view_monthly_revenue_trends(self):
        try:
            # Get the list of members
            members = self.selected_gym.model.get_list_of_members()

            if not members:
                messagebox.showinfo("Revenue Trends", "No revenue data available.")
                return

            # Calculate total revenue from memberships
            total_revenue = 0
            revenue_breakdown = {}

            for member in members:
                fee = member.get_member_fee()
                member_type = member.get_member_type()

                # Update total revenue
                total_revenue += fee

                # Update revenue breakdown by member type
                if member_type not in revenue_breakdown:
                    revenue_breakdown[member_type] = 0
                revenue_breakdown[member_type] += fee

            # Generate a summary report
            report = f"Total Monthly Revenue: ${total_revenue:.2f}\n\nRevenue Breakdown:\n"
            for member_type, revenue in revenue_breakdown.items():
                report += f"{member_type}: ${revenue:.2f}\n"

            # Display the report
            messagebox.showinfo("Revenue Trends", report)

        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve revenue data: {e}")

    def view_trainer_schedules(self):
        try:
            list_of_staff = self.selected_gym.model.get_list_of_staff()
            list_of_classes = self.selected_gym.model.get_list_of_classes()

            # Get the list of trainers
            list_of_trainers = [
                staff for staff in list_of_staff if staff.get_job_title() == "Personal Trainer"
            ]

            if not list_of_trainers:
                messagebox.showinfo("Trainer Schedules", "No trainer data available.")
                return

            # Prepare trainer schedules
            schedules = {}

            for trainer in list_of_trainers:
                # Personal training sessions
                num_of_sessions = len(trainer.get_booked_sessions())  # Assuming this returns an integer

                # Classes assigned to the trainer
                classes = [a_class for a_class in list_of_classes if a_class.get_teacher() == trainer]

                # Schedule summary for the trainer
                schedules[trainer.get_name()] = {
                    "sessions": num_of_sessions,
                    "classes": classes,
                }

            # Generate a readable report
            report = "Trainer Schedules Report:\n\n"
            for trainer_name, schedule in schedules.items():
                report += f"Trainer: {trainer_name}\n"
                report += f"  Personal Training Sessions: {schedule['sessions']}\n"
                report += f"  Assigned Classes: {len(schedule['classes'])}\n"
                for assigned_class in schedule['classes']:
                    report += f"      - {assigned_class}\n"
                report += "\n"

            # Display the report
            messagebox.showinfo("Trainer Schedules", report)

        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve trainer data: {e}")

    def check_equipment_maintenance(self):
        try:
            # Get the list of equipments from each workout zone in selected gym
            equipments = self.selected_gym.model.get_equipments_for_workout_zones()

            if not equipments:
                messagebox.showinfo("Equipment Maintenance", "No equipment available for maintenance check.")
                return

            # Generate a maintenance report
            report = "Equipment Maintenance Report:\n\n"
            for equipment in equipments:
                report += f"{equipment}: maintained\n"

            # Display the report
            messagebox.showinfo("Equipment Maintenance", report)

        except Exception as e:
            messagebox.showerror("Error", f"Could not retrieve equipment data: {e}")

    def go_back(self):
        self.controller.show_admin_dashboard_window(self.selected_gym)