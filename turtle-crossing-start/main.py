import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    # detect collisions with cars
    for car in car_manager.cars:
        if player.distance(car) < 20 :
            game_is_on = False
            scoreboard.game_over()

    # detect turtle making it across and level up
    if player.ycor() > 260:
        player.reset()
        scoreboard.level_up()
        car_manager.level_up()

screen.exitonclick()


