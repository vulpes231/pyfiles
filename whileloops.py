# username = input("Enter username: ")

# while username == "":
#     print("Name cannot be blank")
#     username = input("Enter username: ")
# print(f"Welcome {username}")


def dumb_food_check():
    fav = input("Enter favorite meal: ")

    while not fav == "q":
        print(f"Your fav meal is {fav}")
        fav = input("Enter favorite meal: ")
    
    print("You quit bye.")



dumb_food_check()