foods = []
prices = []
total = 0

while True:
    choice = input("Enter food: (e to exit)")
    if choice == "e" or choice == "E":
        break
    else:
        cost = float(input(f"Enter price of {choice}: "))
        prices.append(cost)
        foods.append(choice)
  


for food in foods:
    print(f"{food} {cost}")