from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")
GAME_OVER = ("Courier", 50, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.speed('fastest')
        self.goto(-380, 216)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level = {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER)
