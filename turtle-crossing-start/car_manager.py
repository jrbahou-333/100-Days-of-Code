from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_CARS = 20


class CarManager():

    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

        for i in range(NUM_CARS + 1):
            self.regen_car()
            self.cars[i].goto(random.randint(-300, 300), random.randint(-250, 250))

        self.finish_line()

    def move_cars(self):
        for car in self.cars:
            car.bk(self.speed)
            if car.xcor() < -320:
                self.cars.remove(car)
                if len(self.cars) < NUM_CARS:
                    self.regen_car()

    def regen_car(self):
        car = Turtle(shape="square")
        car.color(random.choice(COLORS))
        car.penup()
        car.resizemode("user")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(300, random.randint(-250, 250))
        self.cars.append(car)

    def level_up(self):
        # increase speed
        self.speed += MOVE_INCREMENT

    def finish_line(self):
        line = Turtle("square")
        line.color("red")
        line.penup()
        line.goto(0, 260)
        line.resizemode("user")
        line.shapesize(stretch_len=(600/20), stretch_wid=(1/20))




