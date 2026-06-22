import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")
        return turns


def set_difficulty():
    """Sets the game difficulty and returns the number of turns."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")


        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if guess == answer:
            print("Congratulations! Game Over.")
            return

        elif turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The correct answer was {answer}.")
            return
        else:
            print("Guess again.\n")


# Start the game
game()