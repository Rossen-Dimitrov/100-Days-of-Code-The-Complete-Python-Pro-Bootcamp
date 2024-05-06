# from turtle import Turtle, Screen
from turtle import *
import random


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


angles = [0, 90, 180, 270, ]
turtle = Turtle()
turtle.shape('turtle')


def draw():
    colormode(255)
    turtle.pensize(8)
    turtle.pencolor(random_colors())
    turtle.forward(20)
    turtle.setheading(random.choice(angles))


for i in range(100):
    draw()

screen = Screen()
screen.exitonclick()
