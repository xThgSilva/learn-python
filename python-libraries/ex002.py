"""
Create a mini game where the computer chooses a number from 1 to 20.
The user tries to guess it and the program says:
- "Too high"
- "Too low"
- "Correct!"
"""
import random

print("Try to guess the number from 1 to 20!\nYou have 5 attempts.")
generated_number = random.randint(1, 20)
guessed = False

for i in range(1, 6):
    guess = int(input("Enter a number: "))

    if guess == generated_number:
        print(f"Correct! The number was {generated_number}")
        guessed = True
        break
    elif guess > generated_number:
        print("Too high!")
    else:
        print("Too low!")

if not guessed:
    print(f"You didn't guess it. The number was {generated_number}")
