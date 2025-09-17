# Create a random number guessing game with python.

import random

def game():
    num = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if guess == num:
            print(f"You guessed it right in {attempts} attempts! 🎉")
            break
        elif guess < num:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

game()
