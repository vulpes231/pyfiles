# age = int(input("Enter age: "))

# if age > 22:
#     print("signup accepted.")
# elif age < 0:
#     print("Unborn baby")
# else:
#     print("Age limit flaw!")


response = input("Would you like some juice (Y/N)?: ")

if response == "Y":
    print("Juice served.")
elif response == "y":
     print("Small Juice served.")
elif response == "N":
     print("Table skipped.")
elif response == "n":
     print("Undecided.")
else:
    print("Invalid entry!.")

