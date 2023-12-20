import random

def select_word():
    word_bank = [
        "PYTHON", "JAVASCRIPT", "JAVA", "HTML", "CSS", "GITHUB", "COMPUTER",
        "DATABASE", "PROGRAMMING", "CODE", "SERVER", "ALGORITHM", "VARIABLE",
        "FUNCTION", "ARRAY", "INTERFACE", "BACKEND", "FRONTEND", "DEBUGGING",
        "DEVELOPER", "FRAMEWORK", "COMPILER", "SECURITY",
        "NETWORK", "DATABASES", "SOFTWARE", "INTEGRATION", "WEB", "MOBILE",
        "VERSION", "CONTROL", "LOOP", "ITERATION",
        "RECURSION", "EXCEPTION", "PERFORMANCE", "OPTIMIZATION", "SYNTAX",
        "BOOLEAN", "CONDITIONAL", "REFACTORING", "DEPENDENCY", "LIBRARY"]

    return random.choice(word_bank)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def take_guess():
    guess = input("Guess a letter: ").upper()
    return guess

def update_state(word, guessed_letters, incorrect_guesses):
    guess = take_guess()

    if guess.isalpha() and len(guess) == 1:
        if guess in word:
            guessed_letters.add(guess)
        else:
            incorrect_guesses.append(guess)
    else:
        print("Invalid input. Please enter a single letter.")

def check_win(word, guessed_letters):
    return set(word) <= guessed_letters

def check_loss(incorrect_guesses, max_attempts):
    return len(incorrect_guesses) >= max_attempts

def main():
    max_attempts = 7
    word = select_word()
    guessed_letters = set()
    incorrect_guesses = []

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while not check_win(word, guessed_letters) and not check_loss(incorrect_guesses, max_attempts):
        update_state(word, guessed_letters, incorrect_guesses)
        print(display_word(word, guessed_letters))
        print(f"Incorrect guesses: {', '.join(incorrect_guesses)}")

    if check_win(word, guessed_letters):
        print("Congratulations! You guessed the word.")
    else:
        print(f"Sorry, you ran out of attempts. The word was {word}.")

if __name__ == "__main__":
    main()
