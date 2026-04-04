# import colorgram
#
# colours = colorgram.extract('image.jpg', 30)
#
# rgb_list = []
# for item in colours:
#     colour_tuple = tuple(item.rgb)
#     rgb_list.append(colour_tuple)
#
# print(rgb_list)

from turtle import Turtle, Screen, colormode
import random

screen = Screen()
screen.setworldcoordinates(-10, -10, screen.window_width() - 1, screen.window_height() - 1)

colour_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
               (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
               (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
               (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
               (107, 127, 153), (176, 192, 208), (168, 99, 102)]

paint_brush = Turtle()
paint_brush.hideturtle()
paint_brush.penup()
colormode(255)

def draw_line():
    for dots in range(10):
        paint_brush.dot(20, random.choice(colour_list))
        paint_brush.fd(50)

for height in range(50, 500, 50):
    draw_line()
    paint_brush.setx(0)
    paint_brush.sety(height)






screen.exitonclick()
