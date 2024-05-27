from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button
from tkinter import messagebox
from random import randint, shuffle, choice
from pyperclip import copy
import json

FONT_NAME = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    random_password = (''.join(password_list))
    password_entry.delete(0, 'end')
    password_entry.insert(0, random_password)
    copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web_site = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()
    new_entry = {web_site: {'email': email, 'password': password}}

    if len(web_site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Error', message='Empty fields are not allowed')
    else:
        ok = messagebox.askokcancel(title=web_site,
                                    message=f'This are the details entered:\n'
                                            f'Email: {email}\n'
                                            f'Password: {password}'
                                    )
        if ok:
            try:
                with open('passwords.json', 'r') as file:
                    # Reading old data
                    data = json.load(file)

            except FileNotFoundError:
                with open('passwords.json', 'w') as file:
                    json.dump(new_entry, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_entry)
                with open('passwords.json', 'w') as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)
window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=0)
window.grid_columnconfigure(2, weight=0)

image_file = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200, highlightthickness=5)
canvas.create_image(100, 100, image=image_file)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text='Website:', font=FONT_NAME)
website_label.grid(row=1, column=0)
user_label = Label(text='Email/Username:', font=FONT_NAME)
user_label.grid(row=2, column=0)
password_label = Label(text='Password:', font=FONT_NAME)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=59)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
user_entry = Entry(width=59)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, 'rosty_d@abv.bg')
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)
password_entry.config()

# Buttons
password_gen_btn = Button(text='Generate Password', font=FONT_NAME, command=generate_pass)
password_gen_btn.grid(row=3, column=2)

add_btn = Button(text='ADD', font=FONT_NAME, width=39, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
