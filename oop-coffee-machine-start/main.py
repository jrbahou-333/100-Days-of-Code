from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    # Ask User what drink they'd like
    user_order = input(f"Please enter what drink you would like: {menu.get_items()} ")

    # allow user to turn off machine
    if user_order == "off":
        print("Bye")
        is_on = False

    # allow user to see available resources
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()

#     check resources sufficient
    else:
        user_drink = menu.find_drink(user_order)
        if coffee_maker.is_resource_sufficient(user_drink):
            if money_machine.make_payment(user_drink.cost):
                coffee_maker.make_coffee(user_drink)





