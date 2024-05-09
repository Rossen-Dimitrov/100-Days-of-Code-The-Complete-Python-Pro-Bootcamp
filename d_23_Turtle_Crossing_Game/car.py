from turtle import Turtle, colormode
from random import randint, choice

START_POS = 398
START_CAR_SPEED = 6
SPEED_INCREMENT = 2


def random_colors():
    r = randint(5, 250)
    g = randint(5, 250)
    b = randint(5, 250)
    return r, g, b


class CarManager():
    colormode(255)

    def __init__(self):
        self.all_cars = []
        self.car_speed = START_CAR_SPEED

    def create_car(self):
        lanes = [lane for lane in range(-180, 219, 32)]
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.setheading(180)
            new_car.setx(START_POS)
            new_car.sety(choice(lanes))
            new_car.turtlesize(stretch_wid=1, stretch_len=2)
            new_car.color(random_colors())
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += SPEED_INCREMENT

