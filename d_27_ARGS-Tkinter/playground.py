from tkinter import *


def button_click():
    user_in = entry_box.get()
    label.config(text=user_in)


window = Tk()
window.title('Playground')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = Label(text='I am a label', font=('Arial', 24, 'bold'))
label.grid(column=0, row=0)
label.config(padx=20, pady=20)

button1 = Button(text='click me', command=button_click)
button1.grid(column=1, row=1)
# button1.config(padx=16, pady=10)

button2 = Button(text='click me', command=button_click)
button2.grid(column=2, row=0)
button2.config(padx=16, pady=10)


entry_box = Entry(width=30)
entry_box.grid(column=3, row=2)


window.mainloop()
