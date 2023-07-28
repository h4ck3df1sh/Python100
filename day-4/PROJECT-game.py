"""
    This is a rock paper scissors game programmed using python.
        - Rock wins scissors
        - Paper wins rock
        - Scissors wins paper
"""

from random import randint as randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

printable_options = [rock,paper,scissors]
index_options = ["rock","paper","scissors"]

human_input = input("Choose one: paper, rock or scissors. ")
if human_input not in index_options:
    print("Not a valid option. Run again")
    exit()
human_choice = index_options.index(human_input)
human_play = printable_options[human_choice]

computer_choice = randint(0,2)
computer_input = index_options[computer_choice]
computer_play = printable_options[computer_choice]


print("You choosed %s. \n %s" % (human_input,human_play))
print("Machine choosed %s. \n %s" % (computer_input,computer_play))


if human_input == computer_input:
    print("Draw. 🟰")
elif human_input == "rock" and computer_input == "scissors":
    print("Victory. ✌️")
elif human_input == "paper" and computer_input == "rock":
    print("Victory. ✌️")
elif human_input == "scissors" and computer_input == "paper":
    print("Victory. ✌️")
else:
    print("Lose. 👎")