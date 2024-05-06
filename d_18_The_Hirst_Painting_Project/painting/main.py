# import colorgram
#
# colors = colorgram.extract('image_jpg.jpg', 16)
# colors_list = []
# for color in colors:
#     colors_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
from turtle import *
from random import choice

rgb_colors = [(38, 48, 42), (55, 42, 30), (33, 38, 58), (182, 158, 124), (121, 89, 62), (16, 45, 177), (207, 213, 211),
              (33, 123, 58), (77, 72, 170), (201, 151, 32), (91, 90, 222), (214, 213, 203), (147, 166, 197),
              (237, 221, 61), (165, 19, 17)]

t = Turtle()
t.penup()
t.goto(-230, -230)
t.speed('fastest')
t.hideturtle()
colormode(255)


def draw():
    t.pendown()
    t.dot(20, choice(rgb_colors))
    t.penup()
    t.forward(50)


for row in range(10):

    for _ in range(10):
        draw()
    y = t.ycor() + 50
    t.goto(-230, y)


screen = Screen()
screen.exitonclick()
