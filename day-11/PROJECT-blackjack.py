############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###########################################################

import sys, os, signal
from random import choice
from time import sleep
from blackjack_art import logo, spades,clubs,diamonds,hearts,computer,player,unknown_card


cards = {
    "numbers": [1,2,3,4,5,6,7,8,9,10,11,12,13],
    "suits" : ["spades", "clubs", "diamonds", "hearts"],
    "suits_decks": [
        {
            "spades": spades
        },
        {
            "clubs": clubs,
        },
        {
            "diamonds": diamonds,
        },
        {
            "hearts": hearts
        }]
            
    }
    
# Function to handle the CTRL+C signal
def signal_handler(sig, frame):
    print("\nCTRL+C detected. Exiting gracefully...")
    # Add any cleanup code or actions you want to perform before exiting.
    sys.exit(0)

# Set the signal handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, signal_handler)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_cards(deck,hide_dealer=False):
    """ 
    Explanation:

    card.splitlines(): This splits each card drawing (string) into individual lines using the newline character (\n) as the separator.

    [card.splitlines() for card in output]: This list comprehension processes each card in the output list and splits them into individual lines, resulting in a list of lists containing lines for each card.

    zip(*cards_lines): This uses the zip function to group the corresponding lines from all the cards together. It takes the first line from each card, then the second line from each card, and so on, effectively transposing the lines.

    " ".join(lines) for lines in zip(*cards_lines): This joins the corresponding lines together with two spaces (" ") as the separator.

    "\n".join(...): Finally, we join all the joined lines together with newline characters (\n) as the separator, effectively displaying the cards side by side.
    """

    drawings = []
    for card in deck:
        if hide_dealer and deck.index(card) != 0:
            drawings.append(unknown_card)
        else:        
            suit_index = cards["suits"].index(card["suit"])
            drawings.append(cards["suits_decks"][suit_index][card["suit"]][card["value"]-1])

    # Split each card drawing into individual lines
    cards_lines = [card.splitlines() for card in drawings]

    # Join the corresponding lines of all the cards together
    formatted_drawings = "\n".join("  ".join(lines) for lines in zip(*cards_lines))
    return formatted_drawings

def print_game(player_deck,dealer_deck,player_score,dealer_score,hide_dealer=False):
    """Prints the current status of the game and displays the cards of either the player and the dealer

    Args:
        player_deck (array []): the player's cards
        dealer_deck (array []): the dealer's cards
    """
    clear_console()
    print(computer)
    print("-"*40)
    print("Current score: %d" % dealer_score)
    print(draw_cards(dealer_deck,hide_dealer=hide_dealer))
    print("-"*40)
    print(draw_cards(player_deck))
    print("\nCurrent score: %d"  % player_score)
    print("-"*40)
    print(player)

def deal_card():
    return choice(cards["numbers"]),choice(cards["suits"])

def deal_to(deck):
    card_num,suit = deal_card()
    deck.append({
        "suit":suit,
        "value":card_num
    })

def get_score(deck):
    score = 0
    ace_founded = False
    for card in deck:
        card_value =  min(card["value"],10)
        score += card_value
    
    if ace_founded and score > 21:
        score -= 10

    return score

def game_over(winner):
    if winner == "None":
        print("It's a tie!")
    else:
        print("%s won the game..." % (winner))
    
    restart_game = input("Press 1 to restart the game or any key to end the game: ")
    if restart_game == "1":
        init_game()
    else:
        exit()

def game():
    player_deck = []
    dealer_deck = []

    dealer_score = 0
    player_score = 0

    game_is_over = ""

    # Deal 2 cards to the player
    for _ in range(2):
        deal_to(player_deck)
    
    # Deal 2 cards to the player
    for _ in range(2):
        deal_to(dealer_deck)

    dealer_score = min(dealer_deck[0]["value"],10)
    player_score = get_score(player_deck)
    
    print_game(player_deck=player_deck,dealer_deck=dealer_deck,player_score=player_score,dealer_score=dealer_score,hide_dealer=True)

    player_choice = input("Press '1' for 'HIT' or '2' for 'STAND': ")
    while player_choice != '2':
        if player_choice != '1':
            print("Choose a valid option.")
        else:
            deal_to(player_deck)
            player_score = get_score(player_deck)
            print_game(player_deck=player_deck,dealer_deck=dealer_deck,player_score=player_score,dealer_score=dealer_score)

            if player_score > 21:
                game_is_over ="Dealer"
                break
            elif player_score == 21:
                game_is_over ="Player"
                break

        player_choice = input("Press '1' for 'HIT' or '2' for 'STAND': ")

    dealer_score = get_score(dealer_deck)
    if game_is_over == "": 
        while dealer_score <= 16:
            deal_to(dealer_deck)
            dealer_score = get_score(dealer_deck)
            print_game(player_deck=player_deck,dealer_deck=dealer_deck,player_score=player_score,dealer_score=dealer_score)

            if dealer_score > 21:
                game_is_over ="Player"
                break
            elif dealer_score == 21:
                game_is_over ="Dealer"
                break
            sleep(2)
    
    if game_is_over == "": 
            if dealer_score < player_score:
                game_is_over ="Player"
            elif dealer_score > player_score:
                game_is_over ="Dealer"
            else:
                game_is_over ="None"
    
    game_over(game_is_over)

def init_game():
    while True:
        clear_console()
        print(logo)
        print("Welcome to Victor van der Kolk's Blackjack game edition!")
        print("Blackjack is about to start. To exit the game, press Ctrl+C in any moment")
        print("Shuffling cards...")
        sleep(1)
        clear_console()
        game()

init_game()