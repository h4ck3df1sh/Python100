from sercret_auction_art import logo

import os
import signal
import sys

# Function to handle the CTRL+C signal
def signal_handler(sig, frame):
    print("\nCTRL+C detected. Exiting gracefully...")
    # Add any cleanup code or actions you want to perform before exiting.
    sys.exit(0)

# Set the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    users = {}
    add_people = True
    while add_people:
        clear_console()
        print(logo)
        name = input('Enter the name of the person who is going to bid: ')
        amount = int(input('Enter the amount to bid in €: '))
        users[name] = amount
        add_people = True if input('Are there more people who will bid? (yes/no)').lower() == "yes" else False
    
    highest_user = ""
    for user,bid in users.items():
        if highest_user == "" or bid > users[highest_user]:
            highest_user = user
    clear_console()
    print("The winnner is %s with a total bid of %d €" % (highest_user, users[highest_user]))

main()
