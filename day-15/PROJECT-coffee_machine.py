import os, signal
from time import sleep
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

COINS_VALUE = {
    "quarters": 0.25,
    "dimes" : 0.1,
    "niclkes": 0.05,
    "pennies": 0.01
}

emojis = {
    "water": "💧",
    "milk": "🥛",
    "coffee": "☕"

}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Function to handle the CTRL+C signal
def signal_handler(sig, frame):
    print("\nCTRL+C detected. Exiting gracefully...")
    # Add any cleanup code or actions you want to perform before exiting.
    exit(0)

# Set the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_resource(user_choice,resource):
    return True if not resource in MENU[user_choice]["ingredients"] else MENU[user_choice]["ingredients"][resource] <= resources[resource]

def print_recipes():
    ingredient_names = sorted(set(ingredient for option in MENU for ingredient in MENU[option]["ingredients"]))
    max_ingredient_length = max(len(ingredient) for ingredient in ingredient_names)
    
    # Print header row for coffee names
    header_row = "\n".ljust(max_ingredient_length + 10)
    for option in MENU:
        header_row += option.capitalize().ljust(max_ingredient_length + 10)
    print(header_row + "\n")
    
    for ingredient in ingredient_names:
        print((ingredient.capitalize()+ " " + emojis.get(ingredient, "")).ljust(max_ingredient_length + 10), end="")
        for option in MENU:
            quantity = MENU[option]["ingredients"].get(ingredient, "")
            formatted_quantity = f"{quantity}".ljust(max_ingredient_length + 10)
            print(formatted_quantity, end="")
        print("\n")
    input("\nPress any key to continue...")

def print_report():
    print("\nShowing current Coffee Machine resources: \n\n - Water 💧: %d \n\n - Milk 🥛: %d \n\n - Coffee ☕: %d \n\n - Money 💶: $%0.2f" % (resources["water"], resources["milk"], resources["coffee"], resources["money"]))

    input("\nPress any key to continue...")

def shutdown():
    clear_console()
    print("Powering off the Coffee Machine...")
    sleep(3) & exit(0)

def main():
    #TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    valid_answers = ["espresso","latte","cappuccino","off","report","recipes"]
    user_choice = input("What would you like to take? (espresso/latte/cappuccino): ")
    while user_choice not in valid_answers:
        user_choice = input("Not a valid answer. What would you like to take? (espresso/latte/cappuccino): ")
    #TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == "off":
        shutdown()
    #TODO: 3. Print report.
    elif user_choice == "report":
        print_report()
        return
    #TODO: 8. Show recipes
    elif user_choice == "recipes":
        print_recipes()
        return
    #TODO: 4. Check resources sufficient?
    else:
        for resource in resources:
            if not check_resource(user_choice=user_choice, resource=resource):
                print("Sorry, the desired option is not available at the moment due to unsufficient resources. Try again later.")
                input("Press any key to continue...")
                return
    #TODO: 5. Process coins.
    print("Please, insert coins.")

    try:
        num_of_quarters = int(input("How many quarters?: "))
        num_of_dimes = int(input("How many dimes?: "))
        num_of_nickles = int(input("How many nickles?: "))
        num_of_pennies = int(input("How many pennies?: "))
    except ValueError:
        print("Sorry, something went wrong while introducing coins. Try again!")
        return
    
    inserted_amount = num_of_quarters * COINS_VALUE["quarters"] + num_of_dimes * COINS_VALUE["dimes"] + num_of_nickles * COINS_VALUE["niclkes"] + num_of_pennies * COINS_VALUE["pennies"]

    #TODO: 6. Check transaction successful?
    cash_to_be_returned = inserted_amount - MENU[user_choice]["cost"]
    if not cash_to_be_returned >= 0:
        print("Sorry, unsufficient funds... Refunding money...")
        sleep(1)
        return

    #TODO: 7. Make Coffee.
    print("Perfect! Here is $%0.2f in change." % cash_to_be_returned)
    print("And here is your %s ☕!" %(user_choice))
    for ingredient in MENU[user_choice]["ingredients"]:
        resources[ingredient]-=MENU[user_choice]["ingredients"][ingredient]
    resources["money"] += MENU[user_choice]["cost"]
    sleep(3)

while True:
    clear_console()
    main()


