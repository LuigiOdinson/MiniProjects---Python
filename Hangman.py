# HANGMAN GAME
from random import choice
from colorama import Fore

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

stages = ["  +---+",
          "  |   |",
          "  O   |",
          " /|\  |",
          " / \  |",
          "      |"]
stages_shown = []
stage_number = 0
lives = 6
key_word = choice(words)
length = len(key_word)
print((Fore.LIGHTBLUE_EX + "_ " + Fore.RESET) * length)
guesses = ""

while lives > 0:
    print(f"LIVES => {Fore.LIGHTBLUE_EX + str(lives) + Fore.RESET}")
    trues = 0
    guess = input("Enter your guess: ")
    while len(guess) > 1:
        print("Enter only one character at a time")
        guess = input("Enter your guess: ")
    guesses += guess
    print()
    for char in key_word:
        if char in guesses:
            trues += 1
            print(Fore.LIGHTBLUE_EX + char + Fore.RESET, end=" ")
        else:
            print(Fore.LIGHTBLUE_EX + "_" + Fore.RESET, end=" ")
    print()
    if trues == length:
        print(Fore.LIGHTGREEN_EX + "You won" + Fore.RESET)
        break

    if guess not in key_word:
        lives -= 1
        print(Fore.LIGHTRED_EX + "The letter was not in the word." + Fore.RESET)
        stages_shown.append(stages[stage_number])
        stage_number += 1

        if lives == 0:
            print(Fore.RED + "you lost" + Fore.RESET)
            print(f"The word was {key_word}")
    for i in stages_shown:
        print(Fore.YELLOW + i + Fore.RESET)
