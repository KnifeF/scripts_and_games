from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt
# TODO: 3. Print report
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# TODO: 8. Make Coffee

# Models the Menu with drinks.
machine_menu = Menu()
# new obj of money machine
my_machine = MoneyMachine()
# Models the machine that makes the coffee
my_coffee_mk = CoffeeMaker()

running_machine = True
while running_machine:
    # choice = input(f"What would you like? espresso/latte/cappuccino: ")
    choice = input(f"What would you like? {machine_menu.get_items()}: ")
    if choice == "off":
        # Turn off the machine (stops while loop, and ends execution)
        running_machine = False
    elif choice == "report":
        # Prints a report of all resources.
        my_coffee_mk.report()
        # Prints the current profit
        my_machine.report()
    else:
        # Returns all the names of the available menu items
        # coffee_types = machine_menu.get_items().split("/")[:-1]

        # Searches the menu for a particular drink by name.
        # Returns that item if it exists, otherwise returns None
        drink = machine_menu.find_drink(order_name=choice)
        if drink:
            # checks if order can be made, and ingredients are sufficient.
            enough_resources = my_coffee_mk.is_resource_sufficient(drink=drink)
            if enough_resources:
                # checks if payment is accepted, or insufficient.
                if my_machine.make_payment(cost=drink.cost):
                    # Deducts the required ingredients from the resources.
                    my_coffee_mk.make_coffee(order=drink)
