"""
# Band Name Generator

The Band Name Generator is a Python program that prompts the user to enter the city they grew up in and the name of their pet. It then combines these inputs to create a fun and unique band name suggestion. 

The program provides a friendly greeting and guides the user through the process, showing the final band name as a combination of the city and pet names. It's a fun and simple tool to generate creative band names! 🎸🥁🎤
"""


#1. Create a greeting for your program.
print("Welcome to band name generator!")
#2. Ask the user for the city that they grew up in.
city = input("Please enter the city you grew up in: ")
#3. Ask the user for the name of a pet.
pet = input("Please enter your pet name: ")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be: %s %s" % (city, pet))
#5. Make sure the input cursor shows on a new line:
print()
# Solution: https://replit.com/@appbrewery/band-name-generator-end