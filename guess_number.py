import random

print("---------------------------------------")
print("------------VULPES BEEPOP--------------")
print("---------------------------------------")

while True:
    secret_number = random.randint(1, 100)
    guess_count = 5
    
    print("I have selected a secret number. Can you guess it?")
    print("Hint: The number is between 1 - 100")

    while guess_count > 0:
        print(f"\nGuesses left: {guess_count}")
        try:
            user_guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if user_guess == secret_number:
            print("Correct! You guessed the number!")
            break
        elif user_guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
        
        guess_count -= 1

    if guess_count == 0:
        print(f"\nYou ran out of guesses! The number was {secret_number}.")

    play_again = input("\nDo you want to play again? (Y/N): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break