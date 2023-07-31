# Divisible by 3 → Fizz
# Divisible by 5 → Buzz
# Divisible by 3 and 5 → FizzBuzz

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)