questions = (
    "biggest planet is?: ",
    "coldest planet is?: ",
    "what is ronaldo number?: ",
    "which country did Gareth bale play for?: ",
    "how many minutes is standard time for soccer?: ",
)

options = (
    ("A. Earth", "B. Jupiter", "C. Pluto", "D. Mars", "E. Uranus"), 
    ("A. Mars", "B. Pluto", "C. Venus", "D. Mercury", "E. Earth"), 
    ("A. 7", "B. 11" , "C. 9", "D. 10", "E. 17"), 
    ("A. England", "B. Spain" , "C. Italy", "D. Japan", "E. Wales"), 
    ("A. 60", "B. 25" , "C. 120", "D. 90", "E. 80")
    )

answers = ("B", "B", "A", "E", "D")
guesses = []

score = 0
question_no = 0


for question in questions:
    print("----------------------")
    print(question)

    for option in options[question_no]:
        print(option, end="\n")
    print()
  

    guess = input("Enter (A, B, C, D, E): ").upper()
    guesses.append(guess)

    if guess == answers[question_no]:
        print("Correct!")
        score += 1
    else:
         print("Incorrect!")
       
    question_no += 1

print("--------------------------")
print("         RESULT           ")
print("--------------------------")
print(f"Guesses: {guesses}")
print(f"Correct answers: {answers}")
print(f"You scored {score}/{len(questions)}")