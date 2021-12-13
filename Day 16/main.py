from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
on = True
while on:
    drink = input("What do you want? (espresso, cappuccino, latte)")
    if drink == "off":
        on = False
    elif drink == "report":
        money_machine.report()
        coffee_maker.report()
    elif drink == "available":
        available_items = menu.get_items()
        print(available_items)
    else:
        if menu.find_drink(order_name=drink):
            for n in range(3):
                if menu.menu[n].name == drink:
                    specific_drink = menu.menu[n]
            if coffee_maker.is_resource_sufficient(specific_drink):
                if money_machine.make_payment(specific_drink.cost):
                    coffee_maker.make_coffee(specific_drink)
