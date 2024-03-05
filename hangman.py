import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'computer', 'science', 'algorithm', 'openai']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word. You have 6 attempts.")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            if set(guessed_letters) == set(word):
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Incorrect. You have", attempts, "attempts left.")

    if attempts == 0:
        print("Sorry, you've run out of attempts. The word was:", word)

if __name__ == "__main__":
    hangman()
