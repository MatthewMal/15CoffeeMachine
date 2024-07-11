from data import MENU, resources


# print(MENU)
# print(MENU['espresso'])

def resources_report():
    print("Current status report:")
    print(f'Water - {resources["water"]}ml')
    print(f'Milk - {resources["milk"]}ml')
    print(f'Coffee - {resources["coffee"]}g')
    print(f'Money - {resources["money"]}$')


def ingredient_check(order):  # checking whether machine has enough resources to brew the coffee
    """Returns true if there's enough ingredients"""
    for requirement in MENU[order]["ingredients"]:
        if MENU[order]["ingredients"][requirement] > resources[requirement]:
            return False
    return True


def coin_check(order):  # checking if provided coins are enough given the cost of the drink
    """Returns change"""
    print("Please enter your coins: ")
    quarters = int(input("Quarters - "))
    dimes = int(input("Dimes - "))
    nickles = int(input("Nickles - "))
    pennies = int(input("Pennies - "))
    monetary_value = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return monetary_value - MENU[order]["cost"]  # returning change, 0 means there wasn't any change


def make_coffe(order):
    for requirement in MENU[order]["ingredients"]:
        resources[requirement] -= MENU[order]["ingredients"][requirement]


keep_going = True
while keep_going:
    prompt = (input("\nWelcome to the coffe machine! "
                    "What would you like to order?\n(espresso/latte/cappuccino)\n")).lower()
    if prompt == "off":
        keep_going = False
    elif prompt == "report":
        resources_report()
    elif prompt in ("espresso", "latte", "cappuccino"):
        if not ingredient_check(prompt):  # if ingredient check returns false, means there's an ingredient missing
            print(f"Sorry, insufficient resources")
        else:
            change = coin_check(prompt)
            if change >= 0:
                if change > 0:
                    print(f"Here is your ${change} in change.")
                print(f"Here is your {prompt} ☕️. Enjoy!")
                for demand in MENU[prompt]["ingredients"]:  # using the resources to make a coffee
                    resources[demand] -= MENU[prompt]["ingredients"][demand]
                resources["money"] = MENU[prompt]["cost"]  # adding money the coffee was just bought with as profit
            elif change < 0:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Sorry, there has been a miss-input. Please make sure you type your order properly.")
