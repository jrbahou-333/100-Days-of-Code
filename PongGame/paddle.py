from turtle import Turtle

PADDLE_SPEED = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("purple")
        self.penup()
        self.speed(0)
        self.goto(position)

    def move_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + PADDLE_SPEED)

    def move_dn(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - PADDLE_SPEED)
