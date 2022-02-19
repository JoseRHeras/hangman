import random

class Logic:

    def __init__(self) -> None:
        self.words: list = ["Hello", "Three"]
        self.__initialize_game()

    def __initialize_game(self) -> None:

        word_index: int = random.randint(0, len(self.words) - 1)
        self.word: str = self.words[word_index]
        self.number_of_tries: int = len(self.word) + 3

    def get_current_word(self) -> str:
        return self.word

    def is_user_input_valid(self, usr_input: str, usr_index: int) -> bool:
        if self.word[usr_index] == usr_input.lower(): return True
        return False

    def is_game_over(self) -> bool:
        return False
    