"""
CodeAlpha - Task 1: Hangman Game
A simple text-based Hangman game.
"""

import random

# Small list of predefined words
WORDS = ["python", "hangman", "developer", "internship", "programming"]

MAX_WRONG_GUESSES = 6


def choose_word():
    """Randomly pick a word from the list."""
    return random.choice(WORDS)


def display_progress(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")
    print(f"You have {MAX_WRONG_GUESSES} wrong guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word: ", display_progress(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong_guesses += 1
            print(f"Wrong! ({wrong_guesses}/{MAX_WRONG_GUESSES})\n")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"You won! The word was '{word}'.")
            return

    print(f"You lost! The word was '{word}'.")


if __name__ == "__main__":
    play_hangman()