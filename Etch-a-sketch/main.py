from turtle import Turtle, Screen

screen = Screen()
screen.listen()

pen = Turtle()


def move_fd():
    pen.fd(10)


def move_bk():
    pen.bk(10)


def turn_cw():
    pen.right(5)


def turn_acw():
    pen.left(5)

def clear():
    pen.reset()

screen.onkey(key='w', fun=move_fd)
screen.onkey(key='s', fun=move_bk)
screen.onkey(key='a', fun=turn_acw)
screen.onkey(key='d', fun=turn_cw)
screen.onkey(key='c', fun=clear)

screen.exitonclick()
