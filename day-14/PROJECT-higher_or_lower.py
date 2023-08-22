from art import logo, match_symbol, game_over
from game_data import data
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
    print("""Welcome to Higher or Lower game!\nYou will have to guess which of the two celebrities has more followers on Instagram.\n""")
    if input("Press any key to play or press 'c' to quit: ").lower() == 'c':
        exit(0)

def print_game_status(opt_1_data,opt_2_data, player_score):
    clear_console()
    print("\nCurrent score: %d guesses.\n" % (player_score))
    print("-"*80)
    print("%s, a %s, from %s" % (opt_1_data["name"].capitalize(), opt_1_data["description"], opt_1_data["country"].capitalize()))
    print(match_symbol + "\n")
    print("%s, a %s, from %s" % (opt_2_data["name"].capitalize(), opt_2_data["description"], opt_2_data["country"].capitalize()))
    print("-"*80)

def print_game_over(player_score):
    clear_console()
    print(game_over + "\n")
    print("Sorry, you missed.\nFinal score: %d guesses." % (player_score))


def game_loop():
    player_score = 0
    game_status = "in_progress"
    opt_1 = randint(0, len(data)-1)
    already_chosen = [opt_1]
    while game_status == "in_progress":
        opt_2 = opt_1
        while opt_1 == opt_2 or opt_2 in already_chosen:
            opt_2 = randint(0, len(data)-1)
        already_chosen.append(opt_2)
        opt_1_data = data[opt_1]
        opt_2_data = data[opt_2]
        print_game_status(opt_1_data=opt_1_data, opt_2_data=opt_2_data,player_score=player_score)
        player_choice = ""
        while player_choice  != "1" and player_choice != "2":
            player_choice = input("Make your choice! '1' or '2': ")
        correct_choice = "1" 
        if opt_1_data["follower_count"] >= opt_2_data["follower_count"]:
            correct_choice = "1"    
        else:
            correct_choice = "2"
            opt_1 = opt_2

        if player_choice == correct_choice:
            player_score += 1
            if len(already_chosen) >= len(data) -2:
                already_chosen = [opt_1]
        else:
            game_status = "ended"
    print_game_over(player_score=player_score)

def main():
    game_loop()
    if not input("Press any key to play again or press 'c' to quit: ").lower() == 'c':
        main()
    exit(0)

clear_console()
print_header()
main()