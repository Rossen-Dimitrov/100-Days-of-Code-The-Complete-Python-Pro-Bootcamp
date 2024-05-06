from turtle import *
import random


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


turtle = Turtle()
turtle.speed('fastest')


def draw(gap):
    colormode(255)
    turtle.pensize(2)
    turtle.pencolor(random_colors())
    turtle.circle(100)
    turtle.setheading(gap)


counter = 25
angle = 0
gap = 360 / (counter - 1)

for i in range(counter):
    draw(angle)
    angle = turtle.heading() + gap

screen = Screen()
screen.exitonclick()
