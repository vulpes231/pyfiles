users = [
    {
        "username": "vulpes",
        "password": "12345",
        "is_logged_in": False,
    },
    {
        "username": "test",
        "password": "12345",
        "is_logged_in": False,
    },
]

def create_new_user(user, passw):
    if not user or not passw:
        print("username and password required!")
    else: 
        user_info = {
            "username": user,
            "password": passw,
            "is_logged_in": False
        }
        users.append(user_info)
        print(f"{user} account created.")
        return f"{user} account created."

def get_current_user(username):
    for user in users:
        if user.get("username") == username:
            return user
    print(f"Cannot find {username}")
    return None

def delete_user(username):
    user_to_delete = get_current_user(username)
    if not user_to_delete or user_to_delete == None:
        print("User does not exit")
    else:
        for index in range(len(users)):
            current_user = users[index].get("username")
            if current_user == user_to_delete.get("username"):
                users.remove(users[index])
                print(f"{current_user} deleted.")
                return True
        else:
            print("Unable to delete user")
            return False
        
def sell_item(username):
    current_user = get_current_user(username)
    if current_user is None or current_user.get("is_logged_in") == False:
        print("401 Unauthorized!")
        logged_in = auth_user()
        if logged_in:
            print("Item sold successfully.")
        else: 
            print("Unable to sell try again later.")
    else:
        print("Item sold successfully.")

def auth_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "" or password == "":
        print("Username AND password required!")  
        return False
    elif len(password) < 4:
        print("Password must be more than 4 characters!")
        return False
    
    current_user = get_current_user(username)
    if current_user is None:
        return False
    
    if current_user.get("password") != password:
        print("Invalid credentials!")
        return False
        
    current_user.update({"is_logged_in": True})
    print(f"You're now logged in {username}")
    print(f"is_logged_in: {current_user.get('is_logged_in')}")
    return True

# print(sell_item("test"))

# sell_item("gray")
# print(dir(users))
create_new_user("admin", "12345")
delete_user("admin")
print(users, end="\n")