# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

even_divisible_by_4 = ((year % 4)) == 0
even_divisible_by_100 = ((year % 100)) == 0
even_divisible_by_400 = ((year % 400)) == 0

if not even_divisible_by_4:
    print("Not leap year.")
else:
    if not even_divisible_by_100:
            print("Leap year.")
    elif even_divisible_by_100 and even_divisible_by_400:
        print("Leap year.")
    else:
        print("Not leap year.")

