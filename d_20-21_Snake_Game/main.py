from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

S_WIDTH = 600
S_HEIGHT = 600

screen = Screen()
screen.setup(width=S_WIDTH, height=S_HEIGHT)
screen.title("Snake Game")
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    # Detects collision with the food
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend()
        food.create_food()

    # Detects collision with the wall
    if (
            snake.head.xcor() < -280
            or snake.head.xcor() > 280
            or snake.head.ycor() < -280
            or snake.head.ycor() > 280
    ):
        game_is_on = False
        score.game_over()

    # Detects collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
