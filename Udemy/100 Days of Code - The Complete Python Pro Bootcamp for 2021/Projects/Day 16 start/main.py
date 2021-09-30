from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# object for report
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# object to get menu items
menu = Menu()

# turn coffee machine on or off
coffee_machine_on = True



while coffee_machine_on:
    options = menu.get_items()
    user_input = input(f'What would you like? {options}: ').lower()
    if user_input == 'off':
        coffee_machine = False
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        is_enough_ingreds = coffee_maker.is_resource_sufficient(drink)
        is_enough_mula = money_machine.make_payment(drink.cost)
        if is_enough_mula and is_enough_ingreds:
            coffee_maker.make_coffee(drink)














