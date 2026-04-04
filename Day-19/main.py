from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_fd():
    tim.fd(10)


screen.listen()
screen.onkey(fun=move_fd, key="space")
screen.exitonclick()
