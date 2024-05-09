from turtle import Screen
import time

from scoreboard import Score
from car import CarManager
from player import Player

S_WIDTH = 800
S_HEIGHT = 500

screen = Screen()
screen.setup(width=S_WIDTH, height=S_HEIGHT)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Score()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_car()

    # Detect car hit
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # Detects finish line
    if player.is_finished():
        score.increase_score()
        car_manager.level_up()

screen.exitonclick()
