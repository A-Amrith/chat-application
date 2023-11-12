import customtkinter as ctk
import tkinter as tk
from notifier import show_error_box

root=ctk.CTk() 

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root.geometry("400x400+700+400")
root.resizable(False, False)
root.title("Login Page")


tabview = ctk.CTkTabview(master=root, width=400, height=400)
tabview.add("Log In")
tabview.add("Sign Up")
tabview.set("Log In")





def on_login_button_click():
    if "" in [login_username.get(), login_password.get()]:
        show_error_box("Please enter appropriate data in all fields")


login_container = ctk.CTkFrame(tabview.tab("Log In"), width=400, height=200)
ctk.CTkLabel(login_container, text="Log into your account", bg_color="transparent").place(relx=0.5,rely=0.1, anchor=ctk.CENTER)
login_username = ctk.CTkEntry(login_container, width=200, placeholder_text="Enter username")
login_password = ctk.CTkEntry(login_container, show="*", width=200, placeholder_text="Enter password")
login_button = ctk.CTkButton(login_container, text="Login", command=on_login_button_click)

login_username.place(relx=0.5, rely= 0.3, anchor=ctk.CENTER)
login_password.place(relx=0.5, rely= 0.5, anchor=ctk.CENTER)
login_button.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)





def on_signup_button_click():
    if "" in [signup_username.get(), signup_display_name.get(), signup_password.get(), signup_repeat_password.get()]:
        show_error_box("Please enter appropriate data in all fields")


signup_container=ctk.CTkFrame(tabview.tab("Sign Up"), width=400, height=400)

ctk.CTkLabel(tabview.tab("Sign Up"), text="Create a new account", bg_color="transparent").place(relx=0.5,rely=0.05, anchor=ctk.CENTER)
signup_display_name = ctk.CTkEntry(signup_container, width=200, placeholder_text="Enter Display Name")
signup_username = ctk.CTkEntry(signup_container, width=200, placeholder_text="Enter Username")
signup_password = ctk.CTkEntry(signup_container, show="*", width=200, placeholder_text="Enter Password")
signup_repeat_password = ctk.CTkEntry(signup_container, show="*", width=200, placeholder_text="Re-Type Password")
signup_button = ctk.CTkButton(signup_container, text="Sign Up", command=on_signup_button_click)


signup_display_name.pack(pady=10)
signup_username.pack(pady=10)
signup_password.pack(pady=10)
signup_repeat_password.pack()
signup_button.pack(pady=10)



signup_container.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
login_container.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
tabview.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
root.mainloop()