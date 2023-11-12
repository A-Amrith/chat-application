import tkinter as tk
from tkinter import messagebox

def show_message_box(message):
    # Create the main Tkinter window (if not already created)
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show the message box
    messagebox.showinfo("Message", message)


def show_error_box(message):
    # Create the main Tkinter window (if not already created)
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show the error message box
    messagebox.showerror("Error", message)

def show_info_box(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Information", message)

def show_warning_box(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("Warning", message)