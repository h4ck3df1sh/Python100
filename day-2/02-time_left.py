# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_diff = (90 - int(age))
days =  age_diff * 365
weeks = age_diff * 52
months = age_diff * 12

print("You have %d days, %d weeks, and %d months left" % (days,weeks,months))