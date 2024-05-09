from turtle import Turtle
MOVE_DISTANCE = 10
START_POS = -234
FINISH_LINE = 224

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.speed('fastest')
        self.setheading(90)
        self.reset_player()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.sety(START_POS)

    def is_finished(self):
        if self.ycor() > FINISH_LINE:
            self.reset_player()
            return True
        else:
            return False
