from random import choice
from tkinter import Tk, Canvas, PhotoImage, Button, messagebox
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    with open('./data/en_bg_top_words.csv', 'r', encoding='utf-8') as data_file:
        words_file = pandas.read_csv(data_file).to_dict(orient='records')

except FileNotFoundError:
    messagebox.showerror(title='Error', message='Words file not found')

except Exception as e:
    # Show a general error message for any other exceptions
    messagebox.showerror(title='Error', message=f'An error occurred: {e}')


def get_random_word():
    word = choice(words_file)
    canvas.itemconfig(language, text='English')
    canvas.itemconfig(eng_word, text=word['English'])



window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

front_img = PhotoImage(file='./images/card_front.png')

canvas = Canvas(width=800, height=526)
canvas.create_image(408, 264, image=front_img)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
language = canvas.create_text(400, 150, text='', font=("Arial", 40, "italic"))
eng_word = canvas.create_text(400, 263, text='', font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

unknown_img = PhotoImage(file='./images/wrong.png')
known_img = PhotoImage(file='./images/right.png')

unknown_btn = Button(image=unknown_img, highlightthickness=0, command=get_random_word)
unknown_btn.grid(row=1, column=0)
known_btn = Button(image=known_img, highlightthickness=0, command=get_random_word)
known_btn.grid(row=1, column=1)
get_random_word()

window.mainloop()
