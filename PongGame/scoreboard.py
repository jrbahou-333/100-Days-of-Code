from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.pencolor("blue")
        self.ht()
        self.penup()
        self.goto(0, 260)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f'{self.score_l} : {self.score_r}', font=FONT, align=ALIGN)

    def increase_score_l(self):
        self.score_l += 1

    def increase_score_r(self):
        self.score_r += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over\n\nFinal Score: {self.score}', font=FONT, align=ALIGN)