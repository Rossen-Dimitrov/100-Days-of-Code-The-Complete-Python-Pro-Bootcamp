from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data_file:
            self.high_score = int(data_file.read())
        self.penup()
        self.speed('fastest')
        self.goto(0, 267)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data_file:
                data_file.write(str(self.high_score))
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
