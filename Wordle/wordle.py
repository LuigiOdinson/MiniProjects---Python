from letter_state import LetterState


class Wordle:
    word_size = 5
    max_attempts = 6

    def __init__(self, secret: str):
        self.secret: str = secret.upper()
        self.attempts = []

    def guess_condition(self, guess: str):
        guess = guess.upper()
        result = []
        for i in range(self.word_size):
            char = guess[i]
            letter = LetterState(char)
            letter.in_word = char in self.secret
            letter.in_position = char == self.secret[i]
            result.append(letter)
        return result

    def add_attempt(self, guess: str):
        guess = guess.upper()
        self.attempts.append(guess)

    @property  # so we can use the function like a variable and not in-woke it
    def is_solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret

    @property
    def remaining_attempts(self):
        return self.max_attempts - len(self.attempts)

    @property
    def has_attempts(self):
        return self.remaining_attempts > 0 and not self.is_solved
