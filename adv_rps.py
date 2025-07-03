import random
import time

# Initialize scores and choices
user_score = 0
ai_score = 0
choices = ("rock", "paper", "scissors")
win_rules = {
    "rock": "scissors",    # Rock beats scissors
    "scissors": "paper",   # Scissors beat paper
    "paper": "rock"       # Paper beats rock
}

# Game header
print("---------------------------------------")
print("------------------ RPS ----------------")
print("---------------------------------------")

def play_game():
    global user_score, ai_score
    rounds = int(input("Enter number of rounds: "))
    
    while rounds > 0:
        print(f"\nRounds left: {rounds}")
        
        # Computer and user choices
        computer_choice = random.choice(choices)
        user_choice = input("Enter choice (rock, paper, scissors): ").lower().strip()
        
        # Validate input
        if user_choice not in choices:
            print("Invalid choice! Try again.")
            continue
        
        print(f"\nYour choice: {user_choice}\nComputer's choice: {computer_choice}")
        
        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif win_rules[user_choice] == computer_choice:
            print(win_rules[user_choice])
            print(computer_choice)
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            ai_score += 1
        
        rounds -= 1
    
    # Final results
    print("\n---------------------------------------")
    print("------------- FINAL RESULT ------------")
    print("---------------------------------------")
    time.sleep(1)
    print(f"Your score: {user_score} | Computer's score: {ai_score}")
    
    if user_score > ai_score:
        print("Congratulations! You won the game!")
    elif user_score < ai_score:
        print("Computer won the game. Better luck next time!")
    else:
        print("It's a tie game!")

# Main game loop
while True:
    play_game()
    replay = input("\nPlay again? (y/n): ").lower()
    if replay != 'y':
        print("\nThanks for playing! Goodbye!")
        break
    else:
        user_score = ai_score = 0  # Reset scores