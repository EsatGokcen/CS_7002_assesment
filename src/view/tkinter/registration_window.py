import tkinter as tk
from tkinter import messagebox

def register():
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not username or not password or not confirm_password:
        messagebox.showerror("Registration Failed", "All fields are required")
        return

    if password != confirm_password:
        messagebox.showerror("Registration Failed", "Passwords do not match")
        return

    # Placeholder for actual registration logic
    messagebox.showinfo("Registration Success", "Account created successfully")
    registration_window.destroy()  # Close the registration window after success

def go_back():
    registration_window.destroy()  # Close registration window

# Initialize Tkinter Window
registration_window = tk.Tk()
registration_window.title("Registration")
registration_window.geometry("600x400")

# Username Label and Entry
username_label = tk.Label(registration_window, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(registration_window)
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(registration_window, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(registration_window, show="*")
password_entry.pack(pady=5)

# Confirm Password Label and Entry
confirm_password_label = tk.Label(registration_window, text="Confirm Password:")
confirm_password_label.pack(pady=5)
confirm_password_entry = tk.Entry(registration_window, show="*")
confirm_password_entry.pack(pady=5)

# Register Button
register_button = tk.Button(registration_window, text="Register", command=register)
register_button.pack(pady=10)

# Back Button
back_button = tk.Button(registration_window, text="Back", command=go_back)
back_button.pack(pady=5)

# Run the Tkinter Main Loop
registration_window.mainloop()
