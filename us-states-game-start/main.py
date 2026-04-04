import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(height=491, width=725)
screen.bgpic("blank_states_img.gif")


def write_state(state, x, y):
    pen = turtle.Turtle()
    pen.ht()
    pen.penup()
    pen.goto(x, y)
    pen.write(f"{state}", font=("Comic Sans", 10, "normal"))


game_on = True
correct_guesses = []
# get list of states
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


while game_on:
    answer_state = screen.textinput(title=f"Correct States: {len(correct_guesses)}/50", prompt="Type another State: ").title()
    answer_row = data[data.state == answer_state].values.tolist()

    if answer_state in states and answer_state not in correct_guesses:
        # save correct guess to list
        correct_guesses.append(answer_state)

        # call the 'write state' function giving sate, X, and Y
        write_state(answer_row[0][0], answer_row[0][1], answer_row[0][2])

    if len(correct_guesses) == 50:
        game_on = False
        write_state("YOU WIN", 0, 0)

    if answer_state == "Exit":
        # write any missing states to a csv file.
        unknown_states = [state for state in states if state not in correct_guesses]
        data = {"Unknown States": unknown_states}
        df = pandas.DataFrame(data)
        df.to_csv("List of Unknown States")
        break

screen.exitonclick()
