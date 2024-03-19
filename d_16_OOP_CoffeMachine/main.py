from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
caffe_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    user_choice = input(f"What would you like to: {menu.get_items()}? ")
    if user_choice == "report":
        caffe_maker.report()
        money_machine.report()
    elif user_choice == "off":
        print("Shutting down")
        is_on = False
    else:
        order = menu.find_drink(user_choice)
        if order is not None:
            if caffe_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                caffe_maker.make_coffee(order)
