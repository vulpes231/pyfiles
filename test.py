import time

bank_data = [
    {
        "balance": 10000,
        "pin": 1234,
        "account_number": "01900190",
        "username": "vulpes",
        "id": 1
    },
    {
        "balance": 5000,
        "pin": 1090,
        "account_number": "22452409",
        "username": "scoring",
        "id": 2
    },
    {
        "balance": 200000,
        "pin": 2202,
        "account_number": "10435678",
        "username": "admin",
        "id": 3
    },
]


print("-------------------------------------")
print("		VULPES ATM BANKING.	  			")
print("-------------------------------------")


def display_options():
    print("Select an action to proceed")   
    print("1. Withdraw")   
    print("2. Transfer")   
    print("3. Deposit")
    print("4. Check Balance")
    print("5. Exit")
    
def quit_program():
    print("Exiting...")
    time.sleep(1)
    print("Thanks for banking with us.")
    exit()
    
def withdraw(user_bal, user_pin, amount):
    if amount > user_bal:
        print("Insufficient funds!")
        return False
    
    pin = int(input("Enter pin: "))
    if pin != user_pin:
        print("Invalid pin!")
        return False
    else:
        print(f"Withdrawing ${amount:.2f}...")
        time.sleep(1)
        return True

def transfer(account_found):
    user_bal = account_found["balance"]
    user_pin = account_found["pin"]

    amount = int(input("Enter amount: "))
    if amount > user_bal:
        print("Insufficient funds!")
        return False
    
    pin = int(input("Enter pin: "))
    if pin != user_pin:
        print("Invalid pin!")
        return False
    
    account_to = input("Enter account number: ")  # Keep as string to match bank_data

    recipient_account = None
    for acct in bank_data:
        if acct["account_number"] == account_to:
            recipient_account = acct
            break
    
    if not recipient_account:
        print("Invalid account number")
        return False
    
    if recipient_account["account_number"] == account_found["account_number"]:
        print("You cannot transfer to yourself!")
        return False
    
    print(f"Transfering ${amount:.2f} to {account_to}...")
    time.sleep(1)
    account_found["balance"] -= amount
    recipient_account["balance"] += amount
    print(f"Transfer to {recipient_account['username']} successful. New balance ${account_found['balance']}")
    print(f"Recipient balance updated ${recipient_account['balance']}")
    return True

def prompt_user():
    prompt = input("Do you want to perform another transaction? (Y/N): ")
    if prompt.upper() != "Y":
        quit_program()


while True:
    pin = int(input("Enter PIN to proceed: "))
    
    account_found = None
    for acct in bank_data:
        if acct["pin"] == pin:
            account_found = acct
            break
    
    if not account_found:
        print("Pin not recognized!")
        continue
        
    print(f"Welcome {account_found['username']}")
    print()
    
    display_options()
    print()
    
    choice = int(input("Enter a number: "))
    if choice == 5:
        quit_program()
    
    if choice == 1:
        print("Withdrawal")
        user_bal = account_found["balance"]
        user_pin = account_found["pin"]
        
        amount = int(input("Enter amount: "))
        withdraw_success = withdraw(user_bal, user_pin, amount)

        if withdraw_success:
            account_found["balance"] = user_bal - amount
            print(f"${amount:.2f} withdrawn succesfully. New balance ${account_found['balance']}")
            prompt_user()
        else:
            print("Withdrawal failed. Try again Later")
    elif choice == 2:
        print("Transfer")
        transfer_success = transfer(account_found)

        if transfer_success:
            prompt_user()
        else:
            print("Transfer failed. Try again Later")
    elif choice == 3:
        print("Deposit feature coming soon...")
        prompt_user()
    elif choice == 4:
        print("Checking Balance...")
        time.sleep(2)
        user = account_found["username"]
        bal = account_found["balance"]
        print(f"{user} your balance is: ${bal:.2f}")
        
        prompt_user()
    else:
        print("Unrecognized operation!")