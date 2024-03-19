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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """
    Checks if the resources are sufficient and return true or falls
    """
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def is_transaction_successful(inserted_money, cost):
    """
    Checks if the inserted money are enough and return true or falls
    """
    if inserted_money >= cost:
        global profit
        profit += cost
        if inserted_money > cost:
            print(f"Here is ${inserted_money - cost:.2f} dollars in change.")
        return True
    else:
        print(f"Sorry there is not enough money. Money refunded.")
        return False


def process_coins():
    """
    Returns calculated total sum of inserted coins:
    """
    print("Please insert coins")
    total = float(input("How many quarters: ")) * 0.25
    total += float(input("How many dimes: ")) * 0.10
    total += float(input("How many nickles: ")) * 0.05
    total += float(input("How many pennies: ")) * 0.01

    return total


def make_coffee(drink_resources):
    for resource in drink_resources:
        resources[resource] -= drink_resources[resource]
    print(f"Enjoy your drink")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[choice.lower()]
        ingredients = drink["ingredients"]
        if is_resource_sufficient(ingredients):
            inserted_money = process_coins()
            if is_transaction_successful(inserted_money, drink["cost"]):
                make_coffee(drink["ingredients"])
            else:
                print("Not enough money")
