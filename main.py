from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffe_machine=CoffeeMaker()
menu=Menu()
money=MoneyMachine()
while True:
    decision=input("What would you like? (espresso/latte/cappuccino/):")
    if decision=="off":
        break
    elif decision=="report":
        coffe_machine.report()
        if money.profit>0:
            money.report()
        continue
    elif decision=="espresso" or decision=="latte" or decision=="cappuccino":
        drink=menu.find_drink(order_name=decision)
        if not coffe_machine.is_resource_sufficient(drink):
            for key in drink.ingredients:
                if coffe_machine.resources[key]<drink.ingredients[key]:
                    if isinstance(drink.ingredients[key],str):
                        print(f"Sorry there is not enough {drink.ingredients[key]}")
                    break
            continue
    if money.make_payment(drink.cost):
        coffe_machine.make_coffee(drink)
        if money.money_received-drink.cost>0:
            print(f"Here is ${money.money_received-drink.cost:1} dollars in change.")


    


