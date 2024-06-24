from random import choice
from tkinter import Tk, Canvas, PhotoImage, Button, messagebox
import pandas

BACKGROUND_COLOR = "#B1DDC6"
flip_timer = None
to_learn = {}

try:
    to_learn_data = pandas.read_csv('./data/words_to_learn.csv')

except FileNotFoundError:
    original_words_file = pandas.read_csv('./data/en_bg_top_words.csv')
    to_learn = original_words_file.to_dict(orient='records')

except Exception as e:
    # Show a general error message for any other exceptions
    messagebox.showerror(title='Error', message=f'An error occurred: {e}')

else:
    to_learn = to_learn_data.to_dict(orient='records')

current_word = {}


def get_random_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(to_learn)
    canvas.itemconfig(language, text='English', fill='black')
    canvas.itemconfig(eng_word, text=current_word['English'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language, text='Български', fill='white')
    canvas.itemconfig(eng_word, text=current_word['Bulgarian'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


def is_known_word():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    get_random_word()


window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

card_front_img = PhotoImage(file='./images/card_front.png')
card_back_img = PhotoImage(file='./images/card_back.png')

canvas = Canvas(width=800, height=526)
card_background = canvas.create_image(408, 264, image=card_front_img)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
language = canvas.create_text(400, 150, text='', font=("Arial", 40, "italic"))
eng_word = canvas.create_text(400, 263, text='', font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

unknown_img = PhotoImage(file='./images/wrong.png')
known_img = PhotoImage(file='./images/right.png')

unknown_btn = Button(image=unknown_img, highlightthickness=0, command=get_random_word)
unknown_btn.grid(row=1, column=0)
known_btn = Button(image=known_img, highlightthickness=0, command=is_known_word)
known_btn.grid(row=1, column=1)
get_random_word()

window.mainloop()
