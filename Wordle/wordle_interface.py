from wordle import Wordle
from colorama import Fore
from random import choice


def main():
    word_list = ["SNAKE", "APPLE", "BRICK", "PRICE", "FIRST"]
    wordle = Wordle(choice(word_list))
    while wordle.has_attempts:
        guess = input("\n Enter your guess: ")
        if len(guess) != wordle.word_size:
            print(Fore.RED + f"The word must be {wordle.word_size} characters long"
                  + Fore.RESET)
            continue
        wordle.add_attempt(guess)
        display_results(wordle)
    if wordle.is_solved:
        print(Fore.LIGHTGREEN_EX + "Correct" + Fore.RESET)
    else:
        print(Fore.LIGHTRED_EX + f"You lost. The secret word was {wordle.secret}"
              + Fore.RESET)


def display_results(wordle):
    print(Fore.LIGHTBLUE_EX + f"You have {wordle.remaining_attempts} lives left"
          + Fore.RESET)
    lines = []
    for word in wordle.attempts:
        result = wordle.guess_condition(word)
        colored_result = result_to_color(result)
        lines.append(colored_result)
    for i in range(wordle.remaining_attempts):
        lines.append(" ".join("_" * wordle.word_size))

    draw_border(lines)


def result_to_color(result):
    colored_result = []
    for letter in result:  # each letter in the loop is going to be an instance of LetterState
        if letter.in_position:
            color = Fore.GREEN
        elif letter.in_word:
            color = Fore.YELLOW
        else:
            color = Fore.RED
        colored_letter = color + letter.character + Fore.RESET
        colored_result.append(colored_letter)
    return " ".join(colored_result)


def draw_border(lines: list[str], size: int = 9, pad: int = 1):
    length = size + pad * 2
    top = "┌" + "─" * length + "┐"
    bottom = "└" + "─" * length + "┘"
    space = " " * pad
    print(top)
    for line in lines:
        print("│" + space + line + space + "│")
    print(bottom)


if __name__ == "__main__":
    main()
