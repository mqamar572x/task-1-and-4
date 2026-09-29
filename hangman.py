import random

WORDS = ["python", "hangman", "computer", "keyboard", "program"]
MAX_WRONG = 6


def play():
    word = random.choice(WORDS)
    guessed = []
    wrong = 0

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters. You can make {MAX_WRONG} wrong guesses.\n")

    while wrong < MAX_WRONG:
        display = " ".join(letter if letter in guessed else "_" for letter in word)
        print("Word:", display)
        print("Guessed letters:", ", ".join(guessed) if guessed else "none")
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")

        if "_" not in display:
            print(f"\nYou win! The word was '{word}'.")
            return

        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong += 1
            print("Wrong!\n")

    print(f"Game over! The word was '{word}'.")


if __name__ == "__main__":
    play()
