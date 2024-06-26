from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        if position == 'left':
            position = -370
        if position == 'right':
            position = 370

        super().__init__()
        self.speed('fastest')
        self.color('white')
        self.shape('square')
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
