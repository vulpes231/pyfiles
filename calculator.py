# simple calculator to add, multiply, divide, subtract


print("simple calculator to add(+), multiply(*), divide(/), subtract(-)")
print("Steps\n\n- Input first number\n\n- Select an operator\n\n- Input second number\n\n")

first_number = float(input("Enter first number: "))
print("\n")
symbol = input("Enter operator (-, +, /, *): ")
print("\n")
second_number = float(input("Enter second number: "))
print("\n")

print("Calculating...\n\n")

if symbol == "+":
    result = first_number + second_number
    print(f"result {first_number} {symbol} {second_number} = {round(result)}")
elif symbol == "-":
    result = first_number - second_number
    print(f"result {first_number} {symbol} {second_number} = {round(result)}")
elif symbol == "/":
    result = first_number / second_number
    print(f"result {first_number} {symbol} {second_number} = {round(result)}")
elif symbol == "*":
    result = first_number * second_number
    print(f"result {first_number} {symbol} {second_number} = {round(result)}")
else:
    print("Unsupported Operation!")



