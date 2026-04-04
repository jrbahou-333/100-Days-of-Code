from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.display_level()

    def display_level(self):
        self.clear()
        self.ht()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", font=FONT, align="left")

    def game_over(self):
        self.goto(0, 0)
        self. write("SPLAT THE RAT\n  GAME OVER", font=FONT, align="center")

    def level_up(self):
        self.level += 1
        self.display_level()
