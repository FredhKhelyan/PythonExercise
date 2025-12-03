#!/usr/bin/env python3
"""
Simple terminal Hangman game.

Run: python hangman.py

Features:
- Random word selection from a built-in list
- Case-insensitive single-letter guesses
- ASCII hangman stages (6 wrong guesses allowed)
- Replay support
"""
import random
import sys

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =======
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =======
    """,
]

WORDS = (
    "python", "hangman", "challenge", "computer", "programming",
    "openai", "testing", "function", "variable", "algorithm",
)


def choose_word():
    return random.choice(WORDS)


def display_state(secret, guessed_letters, wrong_guesses):
    print(HANGMAN_PICS[min(len(wrong_guesses), len(HANGMAN_PICS)-1)])
    display = " ".join(c if c in guessed_letters else "_" for c in secret)
    print("Word: ", display)
    if guessed_letters:
        print("Guessed:", ", ".join(sorted(guessed_letters)))
    if wrong_guesses:
        print("Wrong guesses:", ", ".join(sorted(wrong_guesses)))
    print()


def prompt_guess(already_guessed):
    while True:
        guess = input("Enter a letter: ").strip().lower()
        if not guess:
            print("Please enter a letter.")
            continue
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue
        if not guess.isalpha():
            print("Please enter a letter (a-z).")
            continue
        if guess in already_guessed:
            print("You've already guessed that letter.")
            continue
        return guess


def play_round():
    secret = choose_word().lower()
    guessed_letters = set()
    wrong_guesses = set()
    max_wrong = len(HANGMAN_PICS) - 1

    while True:
        display_state(secret, guessed_letters, wrong_guesses)

        if set(secret) <= guessed_letters:
            print("Congratulations — you guessed the word!\n")
            return True

        if len(wrong_guesses) >= max_wrong:
            print(HANGMAN_PICS[-1])
            print(f"Game over — the word was: {secret}\n")
            return False

        guess = prompt_guess(guessed_letters | wrong_guesses)

        if guess in secret:
            guessed_letters.add(guess)
            print(f"Good: {guess} is in the word!\n")
        else:
            wrong_guesses.add(guess)
            print(f"Nope: {guess} is not in the word.\n")


def main():
    print("Welcome to Hangman!\n")
    try:
        while True:
            play_round()
            again = input("Play again? (y/n): ").strip().lower()
            if not again or again[0] != "y":
                print("Thanks for playing — goodbye!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
