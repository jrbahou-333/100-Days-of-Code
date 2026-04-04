from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


def main():
    # prompt user to make their bet
    user_bet = screen.textinput(title="Make your bet", prompt="Which colour turtle will win?")

    # make turtles
    colours = ["red", "yellow", "blue", "green", "orange", "purple"]
    turtles = []

    for turtle_index in range(0, 6):
        new_turtle = Turtle("turtle")
        new_turtle.color(colours[turtle_index])
        # new_turtle.hideturtle()
        new_turtle.penup()
        y_start = -150 + (turtle_index * 50)
        new_turtle.goto(-200, y_start)
        turtles.append(new_turtle)

    race_is_on = True

    while race_is_on:
        for turtle in turtles:

            turtle.fd(random.randint(0, 10))

            if turtle.xcor() >= 220:
                race_is_on = False
                winning_turtle = colours[turtles.index(turtle)]

                if user_bet == winning_turtle:
                    print(f" You won! The {winning_turtle} turtle won!")

                else:
                    print(f"you lost :( the {winning_turtle} turtle won")


continue_game = True

while continue_game:
    main()
    continue_user = screen.textinput(title="Continue?", prompt="Would you like to play again? y/n")

    if continue_user == "y":
        screen.clearscreen()

    else:
        continue_game = False

screen.exitonclick()
