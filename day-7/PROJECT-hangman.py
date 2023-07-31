import random
import os
import signal
import sys

from hangman_art import stages,logo
from hangman_words import word_list as word_list

# Function to handle the CTRL+C signal
def signal_handler(sig, frame):
    print("\nCTRL+C detected. Exiting gracefully...")
    # Add any cleanup code or actions you want to perform before exiting.
    sys.exit(0)

# Set the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_up_game():
    #word_list = ["aardvark", "baboon", "camel"]
    chosen_word = random.choice(word_list)
    #Testing code
    print(f'Pssst, the solution is {chosen_word}.')

    # Create blanks
    display = ["_"]*len(chosen_word)
    # Set up player lives
    lives = 6
    return chosen_word, display, lives

def play_game(chosen_word,display,lives):
    while "_" in display and lives > 0:
        print(stages[lives])
        print(' '.join(display) + "\n")

        guess = input("Guess a letter: ").lower()
        missed = True
        # Check guessed letter
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position]=guess
                missed = False
        if missed:
            lives -=1

    clear_console()
    if lives > 0:
        print("Congratulations. You won the game!")
    else:
        print("Sorry, you lost the game! The solution was: %s" % (chosen_word))

def main():
    clear_console()
    print(logo)
    chosen_word,display,lives = set_up_game()
    play_game(chosen_word,display,lives)

main()