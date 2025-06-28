weight = float(input("Enter your weight: "))
print("\n")
unit = input("Kilograms or Pound (K or L)?: ")
print("\n")

if unit == "K" or unit == "k":
    weight *= 2.205
    unit = "kgm"
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "L" or unit == "l":
    weight /= 2.205
    unit = "lbs"
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print("Unsupported operation!")

