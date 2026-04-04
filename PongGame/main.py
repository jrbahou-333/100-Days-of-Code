from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_l = Paddle((-350, 0))
paddle_r = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_dn, "Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_dn, "s")

time.sleep(2)
while True:
    screen.update()
    # time.sleep(0.1)
    ball.move_ball()
    scoreboard.display_score()

    # detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 330 or ball.distance(paddle_l) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # detect if out of bounds
    elif ball.xcor() > 370 or ball.xcor() < -370:

        if ball.xcor() < 0:
            scoreboard.increase_score_r()

        else:
            scoreboard.increase_score_l()

        ball.reset()
screen.exitonclick()
