# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / (height**2))

if BMI < 18.5:
    print("Your BMI is %d, you are underweight." % BMI)
elif 18.5 < BMI < 25:
    print("Your BMI is %d, you have a normal weight." % BMI)
elif 25 < BMI < 30:
    print("Your BMI is %d, you are slightly overweight." % BMI)
elif 30 < BMI < 35:
    print("Your BMI is %d, you are obese." % BMI)
else:
    print("Your BMI is %d, you are clinically obese." % BMI)

