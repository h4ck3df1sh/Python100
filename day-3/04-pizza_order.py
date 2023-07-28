# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
size_prices = [15,20,25]
size_options = ["S","M","L"]
pepperoni_prices = [2,3,3]

def get_size_price(size):
    return size_prices[size_options.index(size)]

def get_pepperoni_price(size):
    return pepperoni_prices[size_options.index(size)]

size_price = map(get_size_price,[size])
final_price = list(size_price)[0]

if add_pepperoni == "Y":
    pepp_price = map(get_pepperoni_price,[size])
    final_price += list(pepp_price)[0] 

if extra_cheese == "Y":
    final_price += 1

print("Your final bill is: $%d." %(final_price))
