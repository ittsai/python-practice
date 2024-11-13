import random
import turtle
from turtle import Turtle
COLORS = ["red", "pink", "orange", "yellow", "blue", "purple", "gray"]
CAR_SPEED = 10
LEVEL_SPEED = {
    1: "normal",
    2: "fast",
    3: "fastest"
}
turtle.colormode(255)

class Car:
    def __init__(self):
        self.all_cars = []
        self.random_chances = [1]
        self.speed = CAR_SPEED

    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance in self.random_chances:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(CAR_SPEED)

    def increase_speed(self, level):
        self.random_chances.append(self.random_chances[-1] + 1)
        for car in self.all_cars:
            car.speed(LEVEL_SPEED[level])