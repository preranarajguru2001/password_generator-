import customtkinter as ctk
import string
import random
from tkinter import messagebox

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("500x500")
root.title("Password Generator")
root.resizable(False, False)

def password_generate():
    try:
        length_password = solidboss.get()
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        digits = string.digits
        special_character = string.punctuation
        all_list = list(small_letters + capital_letters + digits + special_character)
        random.shuffle(all_list)
        password.set("".join(all_list[:length_password]))
    except:
        messagebox.askretrycancel("A Problem Has Occurred", "Please Try Again")

# Label for title
Title = ctk.CTkLabel(root, text="Password Generator", font=("futura", 24, "bold"))
Title.pack(anchor="center", pady=20)

# Label for password length
length = ctk.CTkLabel(root, text="Select the Length of Your Password", font=("ubuntu", 16))
length.place(x=120, y=90)

# Combobox for password length selection
solidboss = ctk.IntVar()
Selector = ctk.CTkComboBox(root, variable=solidboss, values=[str(i) for i in range(1, 30)], width=130)
Selector.set("8")  # Default selection
Selector.place(x=160, y=140)

# Button with hover effects for generating password
def on_enter(e):
    generate_btn.configure(fg_color="grey")

def on_leave(e):
    generate_btn.configure(fg_color="orange")

generate_btn = ctk.CTkButton(root, text="Generate Password", fg_color="orange", text_color="black", command=password_generate)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)
generate_btn.place(x=155, y=195)

# Label for showing the result
result_label = ctk.CTkLabel(root, text="Generated Password Here:", font=("ubuntu", 16))
result_label.place(x=140, y=250)

# Entry box to display generated password
password = ctk.StringVar()
password_final = ctk.CTkEntry(root, textvariable=password, state="readonly", width=220, font=("ubuntu", 15))
password_final.place(x=125, y=290)

root.mainloop()
