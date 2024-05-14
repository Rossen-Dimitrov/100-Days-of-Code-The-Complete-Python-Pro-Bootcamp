from tkinter import *


def calculate():
    result = round(float(entry_box.get()) * 1.60934, 2)
    result_label.config(text=result)


window = Tk()
window.minsize(width=300, height=160)
window.title('Miles To Km Converter')
window.config(padx=20, pady=30)

entry_box = Entry(width=10)
entry_box.insert(END, string="0")
entry_box.grid(column=1, row=0)

miles_label = Label(text='Miles', font=('Arial', 16))
miles_label.grid(column=2, row=0)
miles_label.config(padx=4)

is_equal = Label(text='is equal to ', font=('Arial', 16))
is_equal.grid(column=0, row=1)

result_label = Label(text='0', font=('Arial', 16))
result_label.grid(column=1, row=1)

km_label = Label(text='Km', font=('Arial', 16))
km_label.grid(column=2, row=1)

button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)
button.config(pady=5, padx=10)

window.mainloop()
