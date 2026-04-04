from data import MENU, resources

# Check resources are sufficient when user selects a drink
def check_resources(coffee):
    requirements = MENU[coffee]["ingredients"]

    for resource in requirements:
        if requirements[resource] > resources[resource]:
            print(f"Apologies, there is not enough {resource}")
            return False
        else:
            return True

def remove_resources(coffee):
    requirements = MENU[coffee]["ingredients"]

    for resource in requirements:
        resources[resource] -= requirements[resource]


print("Welcome to Coffee Machine 2000")


def main():
    machine_on = True

    while machine_on:
        user_input = input("What would you like?  (espresso/latte/cappuccino): ")

        # Allow user to turn off machine
        if user_input == "off":
            machine_on = False

        # Allow user to view resources
        elif user_input == "report":
            print(f"Here are the remaining resources: ")
            print(f"Water: {resources['water']}ml ")
            print(f"Milk: {resources['milk']}ml ")
            print(f"Coffee: {resources['coffee']}g ")
            print(f"Money: ${resources['money']} ")

        elif user_input in ["espresso", "latte", "cappuccino"]:
            if check_resources(user_input):
                # If resources sufficient take money from user:
                print("Please insert cash: ")
                money_q = int(input("how many quarters? "))
                money_d = int(input("how many dimes? "))
                money_n = int(input("how many nickels? "))
                money_p = int(input("how many pennies? "))
                money_total = (money_q * 0.25) + (money_d * 0.10) + (money_n * 0.05) + (money_p * 0.01)

                item_cost = MENU[user_input]["cost"]

                #   verify they have enough to pay for drink
                if money_total > item_cost:
                    # add correct amount to the machine
                    resources['money'] += item_cost

                    #   return change
                    change_returned = money_total - item_cost
                    if change_returned != 0:
                        print(f"Here is your change, {change_returned}")

                    # remove the relevent resources from the machine
                    remove_resources(user_input)

                    # Enjoy your drink schlagg
                    print(f"Enjoy your {user_input}")

                else:
                    print("Not enough cash. Money has been refunded")
        else:
            print("Invalid input")
main()