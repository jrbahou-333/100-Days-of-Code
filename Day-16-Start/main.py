# from turtle import Turtle, Screen
#
# Jimmy = Turtle()
# print(Jimmy)
# Jimmy.shape("turtle")
# Jimmy.color("blue")
# my_screen = Screen()
# Jimmy.bk(100)
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Suck", ["My", "Baws"])
table.add_column("My Baws", ["my", "skin"])
print(table.align)
table.align = "l"
print(table)