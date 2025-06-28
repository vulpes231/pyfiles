# logical operators and, or, not

def check_weather():
    temp = int(input("Enter temperature: "))
    is_raining = False


    if temp > 35 or temp < 0 or is_raining:
        print("cancel event")
    else:
        print("Proceed with event.")    


def auth_user():
    is_logged_in = False
    username = input("Enter username: ")
    print("\n")
    password = input("Enter password: ")
    print("\n")

    if username == "" or password == "":
        print("Username AND password required!")  
    elif len(password) < 4:
        print("Password must be more than 4 characters!")
    else:
        is_logged_in = True
        print(f"You're now logged in {username}")
        print(f"is_logged_in: {is_logged_in}")

auth_user()