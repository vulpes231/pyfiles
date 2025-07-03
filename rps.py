import random
import time
user_score = 0
ai_score = 0

choices = ("rock", "paper", "scissors")

print("---------------------------------------")
print("----------------------RPS--------------")
print("---------------------------------------")


rounds = int(input("Enter number of rounds: "))

while True:
    if rounds == 0:
        print("---------------------------------------")
        print("-------------FINAL RESULT--------------")
        print("---------------------------------------")
        print("Game up")
        print("Calculating scores...")
        time.sleep(3)
        if ai_score > user_score:
            print(f"Computer {ai_score} - {user_score} User")
            print("Computer won!")
        elif ai_score < user_score:
            print(f"User {user_score} - {ai_score} Computer")
            print("User won!")
        else:
            print(f"User {user_score} - {ai_score} Computer")
            print("Tie game!")
        print("---------------------------------------")
        exit()
    print(f"Rounds left: {rounds}")
  
    computer_choice = random.choice(choices)
    user_choice = input("Enter choice: (rock, paper, scissors) ")
    print()

    if user_choice == computer_choice:
        print("It's a tie!")
        print(f"user choice: {user_choice} \ncomputer choice {computer_choice}")
        print()
    elif user_choice == "rock" and computer_choice == "paper":
        print("Computer wins!")
        print(f"user choice: {user_choice} \ncomputer choice {computer_choice}")
        print()
        ai_score += 1
    elif computer_choice == "rock" and user_choice == "paper":
        print("User wins! ")
        print(f"user choice: {user_choice} \ncomputer choice {computer_choice}")
        print()
        user_score += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("User wins!")
        print(f"user choice: {user_choice} \ncomputer choice {computer_choice}")
        print()
        user_score += 1
    elif computer_choice == "rock" and user_choice == "scissors":
        print("Computer wins!")
        print(f"user choice: {user_choice} \ncomputer choice {computer_choice}")
        print()
        ai_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("User wins!")
        print(f"user choice: {user_choice} \ncomputer choice {computer_choice}")
        print()
        user_score += 1
    elif computer_choice == "scissors" and user_choice == "paper":
        print("Computer wins!")
        print(f"user choice: {user_choice} \ncomputer choice {computer_choice}")
        print()
        ai_score += 1

    rounds -= 1