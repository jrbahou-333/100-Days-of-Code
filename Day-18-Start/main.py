import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()

turtle.colormode(255)
tim.shape("turtle")


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

tim.speed(0)

n = 0

while n < 360:
    tim.circle(100)
    tim.left(5)
    tim.fd(5)
    tim.color(random_colour())
    n += 5




screen = Screen()
screen.exitonclick()