from data import MENU, resources

"""
Penny = 1 cent = 0.01
Nickel = 5 cents = 0.05
Dime = 10 cents = 0.10
Quarter = 25 cents = 0.25
"""

def resources_sufficient(coffee_type):
    for value in resources:
        if resources[value] < MENU[coffee_type]["ingredients"][value]:
            print(f"Sorry there is not enough {value}")
            return False
    return True

def check_transaction(user_coins, coffee_type):
    change = 0
    if user_coins >= MENU[coffee_type]["cost"]:
        change += user_coins - MENU[coffee_type]["cost"]
        print(f"Here is ${round(change, 2)} in change.")
        global profit
        profit += MENU[coffee_type]["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def calculate_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def make_coffee(coffee_type):
    for value in resources:
        resources[value] -= MENU[coffee_type]["ingredients"][value]
    print(f"Here is your {coffee_type}")

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

profit = 0
user_wallet = 0
machine_on = True

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        report()
    else:
        if resources_sufficient(user_choice):
            user_wallet = calculate_coins()
            if check_transaction(user_wallet, user_choice):
                make_coffee(user_choice)