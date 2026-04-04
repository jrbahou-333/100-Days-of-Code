from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_let = [choice(letters) for _ in range(randint(8, 10))]
    pass_sym = [choice(symbols) for _ in range(randint(2, 4))]
    pass_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_let + pass_sym + pass_num
    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_pass():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty Fields", message="Please fill in all fields")

    else:
        try:
            with open(file="data.json", mode="r") as f:
                data = json.load(f)

        except FileNotFoundError:
            with open(file="data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)

        else:
            data.update(new_data)

            with open(file="data.json", mode="w") as f:
                json.dump(data, f, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search_pass():
    website = website_entry.get().title()

    # read json file and find appropriate email/password
    try:
        with open("data.json", "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        messagebox.showinfo("Password Search", f" Error: no file found")

    else:
            if website in data:
                # return window showing email/pass for that website
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo("Password Search", f"Website: {website}\nEmail: {email}\nPassword: {password}")

            else:
                messagebox.showinfo("Password Search", f"No password for {website}")








# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# website
website_text = Label(text="Website: ")
website_text.grid(column=0, row=1)
website_entry = Entry(width=18)
website_entry.grid(column=1, row=1)
search_button = Button(text="Search", command=search_pass, width=13)
search_button.grid(column=2, row=1)

# email\user
email_text = Label(text="Email/Username: ")
email_text.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(0, "jrbahou@gmail.com")
email_entry.grid(column=1, columnspan=2, row=2)

# password
password_text = Label(text="Password: ")
password_text.grid(column=0, row=3)
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", command=gen_pass, width=13)
password_button.grid(column=2, row=3)

# add
add_button = Button(text="Add", width=33, command=add_pass)
add_button.grid(column=1, columnspan=2, row=4)

window.mainloop()
