
from art import logo 
from random import randint
import os, signal

# Function to handle the CTRL+C signal
def signal_handler(sig, frame):
    print("\nCTRL+C detected. Exiting gracefully...")
    # Add any cleanup code or actions you want to perform before exiting.
    exit(0)

# Set the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print(logo)
    print("Welcome to Guess The Number Game")
    print("I'm thinking of a number between 1 and 100. Will you be able to guess it?")


def start_game():
    game_answer = randint(1, 100)
    game_status = "inProgress"
    player_tries = 5 if input("Type 'Hard' if you want to face a real challenge or skip this for default game mode: ").lower() == "hard" else 10

    while game_status == "inProgress":
        if player_tries == 0:
            game_status = "ended"
            print("Sorry, but you run out of turns. Better luck next time! The correct answer was %d" % (game_answer))
        else:
            try:
                player_answer  = int(input("You have %d trials left. Write your guess here: " % (player_tries)))
                if player_answer == game_answer:
                    print("Congratulations! You guessed that the hidden number was %d" % (game_answer))
                    game_status = "ended"
                elif player_answer < game_answer:
                    print("Too low. Try again!")
                else:
                    print("Too high. Try again!")
                player_tries -= 1
            except ValueError:
                print("Please, enter a valid number!")

def main():
    clear_console()
    print_header()
    start_game()
    if not input("Press any key to play again or press 'c' to quit: ").lower() == 'c':
        main()

main()
exit()