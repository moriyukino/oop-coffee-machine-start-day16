profit = 0

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry, not enough {item}.")
            return False
    return True

should_continue = True

while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        should_continue = False
        continue

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        continue

    drink = MENU.get(choice)
    if drink is None:
        print("Invalid choice.")
        continue

    if not is_resource_sufficient(drink["ingredients"]):
        continue

    print("Please insert coins.")
    quarters  = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    money = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    cost = drink["cost"]


    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        continue

    change = round(money - cost, 2)
    print(f"Here is ${change} in change.")
    profit += cost

    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]

    print(f"Here is your {choice} ☕️. Enjoy!")




