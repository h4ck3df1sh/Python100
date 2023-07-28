# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true_score = 0
love_score = 0
for letter in name1.lower() + name2.lower():
    if letter in ("true"):
        true_score +=1
    if letter in ("love"):
        love_score += 1

score = int(str(true_score)+str(love_score))    

if score < 10 or score > 90:
    print("Your score is %d, you go together like coke and mentos." % (score))
elif 40 <= score <= 50:
    print("Your score is %d, you are alright together." % (score))
else:
    print("Your score is %d." % (score))