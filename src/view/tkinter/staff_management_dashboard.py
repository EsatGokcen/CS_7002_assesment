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
        tk.Button(master, text="View Revenue Trends", command=self.view_revenue_trends).pack(pady=5)
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
        self.controller.show_admin_dashboard_window(self.selected_gym)