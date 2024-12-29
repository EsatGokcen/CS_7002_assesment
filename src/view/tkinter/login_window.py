import tkinter as tk
from tkinter import messagebox


# LOGIN LOGIC WILL CHANGE
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome to the Dashboard!")
        # Logic to transition to the Dashboard Window
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

def open_register_window():
    # Logic to open the Registration Window
    messagebox.showinfo("Redirect", "Redirecting to Registration...")

# Initialize Tkinter Window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("600x400")

# Username Label and Entry
username_label = tk.Label(login_window, text="Username:")
username_label.pack(pady=5)
username_entry = tk.Entry(login_window)
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(login_window, text="Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(login_window, show="*")
password_entry.pack(pady=5)

# Login Button
login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=10)

# Register Button
register_button = tk.Button(login_window, text="Register", command=open_register_window)
register_button.pack(pady=5)

# Run the Tkinter Main Loop
login_window.mainloop()
