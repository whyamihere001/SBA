import tkinter as tk
from tkinter import messagebox

# Sample data storage (in-memory list for registered users)
registered_users = []

def show_register_screen():
    """Change the interface to the registration screen."""
    # Clear the current screen
    for widget in window.winfo_children():
        widget.destroy()

    # Add registration fields
    tk.Label(window, text="Register Alumni", font=("Arial", 18)).pack(pady=10)

    tk.Label(window, text="Full Name:").pack()
    name_entry = tk.Entry(window, width=30)
    name_entry.pack()

    tk.Label(window, text="Email:").pack()
    email_entry = tk.Entry(window, width=30)
    email_entry.pack()

    def register_user():
        """Save the user registration data."""
        name = name_entry.get()
        email = email_entry.get()
        if name and email:
            registered_users.append({"name": name, "email": email})
            messagebox.showinfo("Success", f"{name} has been registered!")
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Both fields are required!")

    tk.Button(window, text="Submit", command=register_user).pack(pady=10)
 

def generate_seating_plan():
    """Generate a seating plan from registered users."""
    if not registered_users:
        messagebox.showwarning("No Data", "No registered users found!")
        return

    seating_plan = "Seating Plan:\n" + "\n".join(
        f"{i+1}. {user['name']} ({user['email']})" for i, user in enumerate(registered_users)
    )
    messagebox.showinfo("Seating Plan", seating_plan)

def show_main_menu():
    """Display the main menu screen."""
    # Clear the current screen
    for widget in window.winfo_children():
        widget.destroy()

    # Add buttons to the main menu
    tk.Label(window, text="TL Secondary School - 55th Anniversary", font=("Arial", 18)).pack(pady=10)

    tk.Button(window, text="Register", command=show_register_screen, width=20).pack(pady=5)
    tk.Button(window, text="Generate Seating Plan", command=generate_seating_plan, width=20).pack(pady=5)
    tk.Button(window, text="Exit the Program", command=window.quit, width=20).pack(pady=5)

# Main program window
window = tk.Tk()
window.title("TL Secondary School - 55th Anniversary")
window.geometry("400x300")

# Show the main menu
show_main_menu()

# Run the program
window.mainloop()