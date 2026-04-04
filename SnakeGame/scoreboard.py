from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode='r') as file:
            contents = file.read()
            self.high_score = int(contents[-1])
        self.score = 0
        self.pencolor("white")
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f'Score: {self.score}  High Score: {self.high_score} ', font=FONT, align=ALIGN)

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over\n\nFinal Score: {self.score}', font=FONT, align=ALIGN)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(f"high_score = {self.high_score}")
            
        self.score = 0
        self.display_score()
