import time

menu = {
    "pizza": 3.00,
    "popcorn": 5.60,
    "rice": 10.09,
    "beans": 20.15,
    "garri": 8.45
}

cart = []
total = 0

print()
print("------------VULPES EATERY MENU------------")
print()

for food, price in menu.items():
    print(f"{food:10}: ${price:.2f}")

print("-----------------------------------------")
print()

while True:
    item_to_buy = input("Enter food name (q to exit program): ")

    if item_to_buy.upper() == "Q":
        print("Thanks for your patronage. Have a nice day.")
        print()
        exit()
    
    food_found = None
    for food in menu.keys():
        if food == item_to_buy:
            food_found = item_to_buy
            break
    
    if not food_found:
        print("Invalid food item!")
    
    quantity = 0
    quantity = int(input("How many units? (1-100): "))

    item_name = food_found
    item_price = menu[food_found] * quantity

    cart.append(item_price)
    print(f"{item_name} added to cart.")
    print()

    prompt = input("Place more order? (Y/N): ")
    if prompt.upper() == "Y":
        continue
    else:
        for price in cart:
            total += price
        
        print(f"total amount of your purchase ${total:.2f}")
        print(f"Thanks for your patronage.")
        time.sleep(1)
        exit()

    # print(cart)
