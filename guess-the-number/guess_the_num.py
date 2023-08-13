# Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint
from art import number_guessing_art

HARD_MODE = 5
EASY_MODE = 10
GREETING = "Welcome to the Number Guessing Game!"


def difficulty_level():
    """
    sets the difficulty to hard or easy, according to user input and returns number of attempts
    """
    difficulty = input("Please Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == "hard":
        return HARD_MODE
    return EASY_MODE


def check_guess(my_number, your_guess, attempts):
    """
    Check user's guess against guessed num. prints feedback and return attempts left
    """
    if your_guess == my_number:
        print(f"You got it! The answer was {my_number}.")
        return -1

    if your_guess > my_number:
        print("Too high.")
    else:
        print("Too low.")
    return attempts - 1


def number_guessing_game():
    """
    Number Guessing Game
    """
    # clear()  # clears screen
    print("\n\n\n\n")
    # TODO-1: Include an ASCII art logo.
    print(number_guessing_art)
    print(GREETING)

    # TODO-2: Include two different difficulty levels
    # (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
    attempts = difficulty_level()

    print(f"You have {attempts} attempts remaining to guess the number.")

    # TODO-3: Allow the player to submit a guess for a number between 1 and 100.
    print("I'm thinking of a number between 1 and 100")
    my_number = randint(1, 100)

    while attempts > 0:
        your_guess = input("Make a guess:")
        if your_guess and your_guess.isdigit() and 1 <= int(your_guess) <= 100:

            # TODO-4: Check user's guess against actual answer. Print "Too high." or "Too low."
            #  depending on the user's answer. If they got the answer correct, show the actual answer to the player.

            attempts = check_guess(my_number, int(your_guess), attempts)

            # TODO-5: Track the number of turns remaining.
            if attempts == 0:
                print("You Lose!")
                break
            elif attempts == -1:
                print("You win!")
                break
            else:
                print("Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print("Invalid input")


keep_playing = True

while keep_playing:
    user_answer = input("Do You want to play a Number Guessing Game? ")
    if user_answer and user_answer in ("y", "yes", "1"):
        number_guessing_game()
    else:
        keep_playing = False
