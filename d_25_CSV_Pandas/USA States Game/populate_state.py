from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 8, "normal")
GAME_OVER = ("Courier", 50, "normal")


class StateObject(Turtle):
    def __init__(self, x, y, text):
        super().__init__()
        self.score = 0
        self.penup()
        # self.speed('fastest')
        self.hideturtle()
        self.goto(x, y)
        self.write(text, align=ALIGNMENT, font=FONT)
