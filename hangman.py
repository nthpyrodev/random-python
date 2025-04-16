"""Basic hangman game. Will maybe add some ascii for the hanging man"""
import random

words = ["dolphin", "wolf", "python", "gopher", "crab", "elephant"]

play = input("Do you want to play hangman? (y/n)")

def hangman():
    word = random.choice(words)
    max_guesses = len(word) + 5
    seperated = list(word)
    guesses = []
    display = ["_" for _ in seperated]
    incorrect_guesses = 0

    while incorrect_guesses < max_guesses:
        print(" ".join(display))
        guess = input("Guess a letter: ").lower()

        if len(guess) <= 1 and not any(char.isdigit() for char in guess):
            if guess not in guesses:
                guesses.append(guess)
                if guess in seperated:
                    for index, letter in enumerate(seperated):
                        if letter == guess:
                            display[index] = guess
                else:
                    incorrect_guesses += 1
                    print(f"Incorrect guess! You have {max_guesses - incorrect_guesses} guesses left.")
            else:
                print("Already tried")
            if "_" not in display:
                print("Congrats! You guessed the word:", word)
                break
        else:
            print("Invalid Input")
    else:
        print("You lost because you ran out of guesses. The word was:", word)

if play == "y" or play == "yes":
    hangman()
else:
    print("If you didn't want to play, why on earth did you run me?")
    exit
