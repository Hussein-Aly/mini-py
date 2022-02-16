
import json
from tkinter import messagebox
from tkinter import *
import random
import pyperclip
from win10toast import ToastNotifier


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter_list = ([random.choice(letters) for char in range(nr_letters)])

    symbol_list = ([random.choice(symbols) for symbol in range(nr_symbols)])

    number_list = ([random.choice(numbers) for number in range(nr_numbers)])

    password_list = letter_list + symbol_list + number_list
    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)

    n = ToastNotifier()
    n.show_toast("Password generated!", "password copied to clipboard!", threaded=True)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get()
    with open("data.json", "r") as file:
        data = json.load(file)
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo("Search Results", f" Email: {email}, Password: {password}"
                                "\n\npassword copied to clipboard!")
            pyperclip.copy(password)
        else:
            messagebox.showinfo("Search Results", "Not Found!!")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    password = pass_entry.get()
    email = email_entry.get()
    website = web_entry.get()
    data = {website: {
        "email": email,
        "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Entry Error", message="Please don't leave any empty fields")
    else:
        try:
            with open("data.json", 'r') as file:
                json_data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        else:
            data.update(json_data)
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)

web_entry = Entry(width=21)
web_entry.grid(row=1, column=1)

email_entry = Entry(text="myemail@email.com", width=35)
email_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)

generate_button = Button(text="Generate Password", width=14, command=generate_pass)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=35, command=add)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
