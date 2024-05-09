from turtle import Screen
import time

from d_22_pong_game.ball import Ball
from d_22_pong_game.scoreboard import Score
from paddle import Paddle

S_WIDTH = 800
S_HEIGHT = 600

screen = Screen()
screen.setup(width=S_WIDTH, height=S_HEIGHT)
screen.title("Pong Game")
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle('right')
l_paddle = Paddle('left')
ball = Ball()

score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detects collision with the wall
    if ball.ycor() <= -290 or ball.ycor() >= 290:
        ball.bounce_wall()

    # Detects collision with the paddle
    if (
            ball.distance(r_paddle) < 50 and ball.xcor() > 350
            or ball.distance(l_paddle) < 50 and ball.xcor() < -350
    ):
        ball.bounce_paddle()

    # Detects goal R player
    if ball.xcor() < -390:
        score.increase_r_score()
        ball.resset_ball()

    # Detects goal L player
    if ball.xcor() > 390:
        score.increase_l_score()
        ball.resset_ball()
screen.exitonclick()
