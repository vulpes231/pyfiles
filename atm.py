import time

user = {
    "username": "vulpes26",
    "password": "12345",
    "user_pin": 1234,
    "account_balance": 4000
}

print("Welcome to Vulpes ATM Banking.")
amount = 0
# user_bal =  user.get("account_balance") 

while True:
    pin = int(input("Enter pin to proceed: "))
    if not user.get("user_pin") == pin:
        print("Invalid pin!")
    else:
        print("Select Action.")
        choice = int(input("\n 1. Withdraw \n 2. Transfer \n 3. Check Balance \n 4. Quit \n: "))
       
        if choice == 4:
            print("Exiting...")
            time.sleep(2)
            print("Thanks for banking with us.")
            break
        else:
            if choice == 1:
                amount = int(input("Enter amount: $"))
                withdraw_pin = int(input("Enter withdrawal pin: "))
                if not withdraw_pin == user.get("user_pin"):
                    print("Invalid withdrawal pin!")
                else:
                    print("Withdrawing")
                    time.sleep(3)
                    print(f"${amount:.2f} withdrawn successfully.")
                    new_bal = user.get("account_balance") - amount
                    user.update({"account_balance": new_bal})
                    print(f"New balance ${user.get('account_balance'):.2f}")
                    prompt = input("Do you want to perform another transaction? Y/N: ")
                    if prompt.lower() == "y":
                        continue
                    else:
                        print("Thanks for banking with us.")
                        break
            elif choice == 2:
                amount = int(input("Enter amount: $"))
                to_account = int(input("Enter recepient account number: "))
                print("Sending money...")
                time.sleep(3)
                print(f"${amount:.2f} sent to {to_account}")
                new_bal = user.get("account_balance") - amount
                user.update({"account_balance": new_bal})
                print(f"New balance ${user.get('account_balance'):.2f}")
                prompt = input("Do you want to perform another transaction? Y/N: ")
                if prompt.lower() == "y":
                    continue
                else:
                    print("Thanks for banking with us.")
                    break
            elif choice == 3:
                check_pin = int(input("Enter pin: "))
                if not check_pin == user.get("user_pin"):
                    print("Invalid pin!")
                else:
                    print("Loading balance...")
                    time.sleep(3)
                    bal = user.get('account_balance')
                    print(f"Your account balance is ${bal:.2f}")
            else:
                print("Invalid action") 
