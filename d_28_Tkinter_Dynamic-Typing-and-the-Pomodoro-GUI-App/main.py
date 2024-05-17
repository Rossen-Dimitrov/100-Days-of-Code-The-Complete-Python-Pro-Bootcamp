from tkinter import Tk, Canvas, PhotoImage, Label, Button
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
GREEN_BTN = "#06960b"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repeats = 0
timer = None

# ---------------------------- AUDIO ------------------------------- #
pygame.mixer.init()


def make_sound():
    pygame.mixer.music.load("emergency-alarm.mp3")
    set_volume = 0.01
    pygame.mixer.music.set_volume(set_volume)
    pygame.mixer.music.play(loops=0)


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global repeats
    repeats = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global repeats
    repeats += 1

    if repeats % 8 == 0:
        period = LONG_BREAK_MIN
        timer_label.config(text='L Break', fg=RED)
    elif repeats % 2 == 0:
        period = SHORT_BREAK_MIN
        timer_label.config(text='S Break', fg=PINK)
    else:
        period = WORK_MIN
        timer_label.config(text='Work', fg=GREEN)

    count_down(period * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minutes = count // 60
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    global timer

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        make_sound()
        start_timer()
        check_marks.config(text=repeats // 2 * "✔")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
image_file = PhotoImage(file='tomato.png')

timer_label = Label(text='TIMER', font=(FONT_NAME, 30, 'bold'), fg=GREEN, highlightthickness=0, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 110, image=image_file)
timer_text = canvas.create_text(107, 132, text='00:00', font=(FONT_NAME, 30, 'bold'), fill='white')
canvas.grid(column=1, row=1)

start_btn = Button(text='START', command=start_timer, font=(FONT_NAME, 20, 'bold'), fg=GREEN_BTN)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='RESET', command=reset_timer, font=(FONT_NAME, 20, 'bold'), fg=RED)
reset_btn.grid(column=2, row=2)

check_marks = Label(font=(FONT_NAME, 24, 'bold'), fg=GREEN, highlightthickness=0, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
