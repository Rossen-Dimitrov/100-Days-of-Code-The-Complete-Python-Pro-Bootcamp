import random
from turtle import *

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title='Make your bet', prompt='Enter turtle name')
colors = ['red', 'green', 'brown', 'gold', 'blue', 'orange']

y_pos = -100
turtles = []

for color in colors:
    t = Turtle(shape='turtle')
    t.color(color)
    t.penup()
    t.goto(x=-235, y=y_pos)
    y_pos += 40
    turtles.append(t)

is_race_on = True

while is_race_on:
    for t in turtles:
        t.forward(random.randint(1, 10))
        if t.xcor() > 222:
            is_race_on = False
            if bet == t.pencolor():
                print('You win')
            else:
                print(f'You lost. The winner is {t.pencolor()}')
            break

screen.exitonclick()
