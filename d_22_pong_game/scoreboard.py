from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.v = 0
        self.penup()
        self.speed('fastest')
        self.goto(x=0, y=200)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'{self.l_score} - {self.r_score}', align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.update_score()

    def increase_r_score(self):
        self.r_score += 1
        self.update_score()
