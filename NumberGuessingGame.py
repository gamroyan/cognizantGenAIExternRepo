# Project: Number Guessing Game
import random

def numberGuessingGame():
    number_to_guess = random.randint(1, 100)
    number_of_tries = 0

    while True:
        num = int(input("Guess the number (between 1 and 100): "))

        # number 
        if num > number_to_guess:
            number_of_tries += 1
            if number_of_tries == 10:
                print("Game over! Better luck next time!")
                break
            print("Too high! Try again.")

        elif num < number_to_guess:
            number_of_tries += 1
            if number_of_tries == 10:
                print("Game over! Better luck next time!")
                break
            print("Too low! Try again.")
        else:
            number_of_tries += 1
            print("Congratulations! You guessed it in " + str(number_of_tries) + " attempts!")
            break

    return

numberGuessingGame()
