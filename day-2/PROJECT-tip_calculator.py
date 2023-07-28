"""
# Tip Calculator

Welcome to the Tip Calculator! This Python program helps you calculate the total amount each person should pay, including the tip, when splitting a bill.

## Instructions

1. Enter the total bill amount (e.g., $150.00).

2. Choose the tip percentage (10%, 12%, or 15%).

3. Specify the number of people sharing the bill.

4. The program will calculate each person's share of the total bill, including the tip, and display the result with 2 decimal places.
"""

people_count = float(input("How many people are going to pay: "))
bill = float(input("Introduce the total bill amount: "))
tip_percentage = float(input("Write down the tip percentage: "))
tip = tip_percentage * bill / 100
payment = (bill + tip) / people_count
print("Each person should pay %.2f €" % (payment))