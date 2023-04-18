class LetterState:
    def __init__(self, character: str):
        self.character: str = character
        self.in_word: bool = False
        self.in_position: bool = False

    def __repr__(self):  # we can define our own representation of class objects
        return f"{self.character} in word: {self.in_word} and in position: {self.in_position}"
