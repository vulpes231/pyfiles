# single variable used to store multiple values. List, Set, Tuple
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable. Duplicates not OK
# Tuple = () ordered and changeable. Duplicates OK FASTER

fruits = ["apple", "pineapple", "guava", "cashew", "orange"]

# print(fruits[0:2])

# search = input("Enter fruit to search: ")

# for fruit in fruits:
#     if fruit == search:
#         print(fruit)
#         break
#     else:
#         continue
# print("Item not found")

fruits[2] = "sugar"
fruits.append("guava")
print(fruits)