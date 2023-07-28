# Import the random module here

from random import randint as randint

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Example_input = "Angela, Ben, Jenny, Michael, Chloe"

#Write your code below this line 👇
random_person = randint(0,len(names)-1)
selected_person = names[random_person]
print("%s is going to buy the meal today!" %(selected_person)) 