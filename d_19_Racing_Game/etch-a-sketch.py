from turtle import *


def forward():
    t.forward(10)


def backward():
    t.backward(10)


def clockwise():
    t.setheading(t.heading() + 10)
    t.forward(10)


def counter_clockwise():
    t.setheading(t.heading() - 10)
    t.forward(10)


def clear():
    screen.reset()


t = Turtle()
screen = Screen()
screen.listen()

screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
