from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()

coffee = CoffeeMaker()
money = MoneyMachine()

name = menu.get_items()
is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        resources = coffee.is_resource_sufficient(menu.find_drink(choice))
        if resources:
            transaction = money.make_payment(drink.cost)
            if transaction:
                coffee.make_coffee(drink)


