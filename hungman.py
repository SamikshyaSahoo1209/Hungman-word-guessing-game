import random
from pathlib import Path

# Maximum incorrect attempts
MAX_ATTEMPTS = 6

# ASCII Hangman stages
HANGMAN = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


# Load words from the text file
def load_words():

    file_path = Path(__file__).with_name("english_words.txt")

    with open(file_path, "r", encoding="utf-8") as file:

        words = [
            line.strip().lower()
            for line in file
            if line.strip().isalpha()
            and 4 <= len(line.strip()) <= 12
        ]

    if not words:
        raise ValueError("No valid words found in the file.")

    return words


# Display the hidden word
def display_word(word, guessed_letters):

    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )


# Main game
def play_game(words):

    secret_word = random.choice(words)

    guessed_letters = set()
    wrong_guesses = set()

    print("\n===== HANGMAN GAME =====")

    while len(wrong_guesses) < MAX_ATTEMPTS:

        print(HANGMAN[len(wrong_guesses)])

        print("\nWord:", display_word(
            secret_word, guessed_letters))

        print("Incorrect attempts:",
              len(wrong_guesses), "/", MAX_ATTEMPTS)

        print("Guessed letters:",
              " ".join(sorted(guessed_letters)))

        guess = input("\nEnter one letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():

            print("Please enter only one alphabet letter.")
            continue

        # Check duplicate guesses
        if guess in guessed_letters:

            print("You already guessed this letter!")
            continue

        # Store guessed letter
        guessed_letters.add(guess)

        # Check whether the letter is correct
        if guess in secret_word:

            print("Correct guess!")

        else:

            wrong_guesses.add(guess)
            print("Wrong guess!")

        # Check winning condition
        if all(letter in guessed_letters
               for letter in secret_word):

            print("\nCongratulations! You won!")

            print("The word was:", secret_word)

            return

    # Losing condition
    print(HANGMAN[MAX_ATTEMPTS])

    print("\nGame Over!")

    print("The correct word was:", secret_word)


# Main function
def main():

    words = load_words()

    while True:

        play_game(words)

        choice = input(
            "\nDo you want to play again? (yes/no): "
        ).lower().strip()

        if choice != "yes":

            print("\nThank you for playing!")
            break


if __name__ == "__main__":
    main()