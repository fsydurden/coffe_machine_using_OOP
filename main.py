from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    order_name = input(f"What drink you want {options}?")
    if order_name == "off":
        is_on = False
    elif order_name == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order_name)
        if (coffe_maker.is_resource_sufficient(drink)):
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)

