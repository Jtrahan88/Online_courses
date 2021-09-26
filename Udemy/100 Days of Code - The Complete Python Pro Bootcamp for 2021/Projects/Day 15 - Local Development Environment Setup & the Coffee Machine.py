#Coffee Maker

# Program Requirements
# 1) Print a report of Resources
# 2) Check for resource and are there enough
# 3) Process coins
# 4) Check transaction is is successful? if not refund money and not give drink
# 5) if successful make coffee and deduct resources.


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


coffee_machine_on = True
money = 0


def enough_resources(order_resources):
    """checks if our machine has enough resources left to make a drink. True if we can False if not"""
    for item in order_resources:
        if order_resources[item] >= resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def payment_success(money_received, cost_of_drink):
    """Return true if user can pay fro drink if not false """
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f"Your change is {change}")
        global money
        money += cost_of_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def count_coins():
    """counts to money given"""
    print("insert coins")
    total = int(input("How many quarters?: ")) *.25
    total += int(input("How many dimes?: ")) *.10
    total += int(input("How many nickles?: ")) *.05
    total += int(input("How many pennies?: ")) *.01
    return total


def make_drink(drink_name, ordered_ingredients):
    """reduce ingredients from our resources"""
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {drink_name}☕")




# Start a while loop to continue untill coffe machince if off
while coffee_machine_on:
    userOrder = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if userOrder == 'off':
        coffee_machine_on = False
    elif userOrder == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[userOrder]
        if enough_resources(drink['ingredients']):
            payment = count_coins()
            if payment_success(payment, drink['cost']):
                make_drink(userOrder, drink['ingredients'])










