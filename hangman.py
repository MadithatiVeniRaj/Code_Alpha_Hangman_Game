import random

# Small list of 5 predefined words
words = ["python", "internship", "program", "keyboard", "developer"]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=== Welcome to Hangman ===")

while wrong_guesses < max_wrong:
    # Build the word display: show guessed letters, hide the rest
    display = ""
    for letter in secret_word:
        display += (letter if letter in guessed_letters else "_") + " "
    print("\nWord:", display)
    print("Guessed:", " ".join(guessed_letters))

    guess = input("Guess a letter: ").lower()

    # Input validation (invalid input does not cost a life)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print(f"Wrong! Lives left: {max_wrong - wrong_guesses}")

    # Win check
    if all(letter in guessed_letters for letter in secret_word):
        print(f"\nYou won! The word was '{secret_word}'.")
        break
else:
    # Runs only if the loop ended without 'break' (player lost)
    print(f"\nGame over! The word was '{secret_word}'.")
