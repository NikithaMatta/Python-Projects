import random

def get_secret_number():
    """Generates a random 3-digit number with unique digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)
    return ''.join(numbers[:3])

def get_clues(guess, secret_number):
    """Returns clues based on the player's guess compared to the secret number."""
    if guess == secret_number:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("Fermi")
        elif guess[i] in secret_number:
            clues.append("Pico")

    if not clues:
        return "Bagels"
    else:
        return ' '.join(clues)

def is_valid_guess(guess):
    """Check if the guess is a valid 3-digit number with unique digits."""
    return len(guess) == 3 and guess.isdigit() and len(set(guess)) == 3

def play_game():
    print("Welcome to the Bagels Game!")
    print("I have picked a 3-digit number. Try to guess it!")
    print("You have 10 attempts to guess the number.")
    print("Hints:")
    print("Pico - One digit is correct but in the wrong position.")
    print("Fermi - One digit is correct and in the correct position.")
    print("Bagels - No digits are correct.")
    print()

    secret_number = get_secret_number()
    max_guesses = 10

    for guess_num in range(1, max_guesses + 1):
        guess = ''
        while not is_valid_guess(guess):
            guess = input(f"Guess #{guess_num}: ")

        clues = get_clues(guess, secret_number)
        print(clues)

        if guess == secret_number:
            break

    if guess != secret_number:
        print(f"Sorry, you're out of guesses. The number was {secret_number}.")

if __name__ == "__main__":
    play_game()
