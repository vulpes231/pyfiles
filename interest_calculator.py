
principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter initial investment: "))

    if principal < 0:
        print("Principal can't be less than or equal to 0")
        # principal = float(input("Enter initial investment: "))
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))

    if rate < 0:
        print("Rate can't be less than or equal to 0")
        # rate = float(input("Enter initial investment: "))
    else:
        break

while True:
    time = int(input("Enter time in years: "))

    if time < 0:
        print("Time can't be less than or equal to 0")
        # time = float(input("Enter initial investment: "))
    else:
        break

interest = principal * pow((1 + rate / 100), 2)
print(f"Balance after {time} year(s) ${interest:.2f}")