# import help

fruits = ["pawpaw", "apple", "cider", "lemon", "mango", "banana"]
fruits.append("man")
fruits.remove("pawpaw")
# print(fruits[::-1])

def search_fruit(search):
    for fruit in fruits:
        if fruit == search:
            print(fruit)
            break
    else:
        print(f"{search.capitalize()} not found")

# print(fruits)
# search_fruit("apple")
# # print("Step 2")
# search_fruit("goat")


def print_fruits():
    for fruit in range(0, len(fruits)):
        print(f"{fruits[fruit]} \n")



print_fruits()