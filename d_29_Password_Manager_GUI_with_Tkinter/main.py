from tkinter import Tk, PhotoImage, Canvas, Label, Entry, Button

FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open('passwords.txt', 'a') as file:
        new_entry = f"{website_entry.get()}|{user_entry.get()}|{password_entry.get()}"
        file.write(new_entry)
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
password_gen_btn = Button(text='Generate Password', font=FONT_NAME)
password_gen_btn.grid(row=3, column=2)

add_btn = Button(text='ADD', font=FONT_NAME, width=39, command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
