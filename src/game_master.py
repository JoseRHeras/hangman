import random
from typing import List

GAME_WORDS: List[str] = ["Hello"]

MESSAGES = {
        "default":"Your guess must be one character long!!", 
        "short_input": "The given input must be 1 char long", 
        "long_input": "The give input is too long", 
        "incorrect_guess": "Wrong guess keep trying",
        "good_input" : "Nice!!",
        "game_lost" : "Tuff luck!! Maybe next time!!",
        "win_message" : "We got a winner"
    }

class GameMaster:

    def __init__(self) -> None:
        self._set_game_word()
        self.message: str = MESSAGES['default']
        
    def _set_game_word(self) -> None:
        self.word: str = GAME_WORDS[random.randint(0, len(GAME_WORDS) - 1)]
        self.word_set: set = {letter for letter in self.word}
        self.allowed_attempts: int = len(self.word) + 3
        
    def _update_number_of_attempts(self, usr_input: str) -> None:
        self.allowed_attempts -= 1 if len(usr_input) == 1 else 0
        
        
    def load_and_evaluate_usr_input(self, usr_input: str) -> None:
        self._update_number_of_attempts(usr_input=usr_input)
        self.is_input_valid = True if usr_input in self.word_set and self.allowed_attempts >= 0 else False
        
        print(f'Turns left {self.allowed_attempts}')
        if self.is_input_valid: 
            self.message = MESSAGES['good_input']
            self.word_set.remove(usr_input)
            
            if len(self.word_set) == 0 and self.allowed_attempts >= 0:
                self.message = MESSAGES['win_message']
        else:
            size = len(usr_input)
            if self.allowed_attempts == 0:
                self.message = MESSAGES['game_lost']
            
            elif size < 1:
                self.message = MESSAGES['short_input']
            elif size > 1:
                self.message = MESSAGES['long_input']
            else:
                self.message = MESSAGES['incorrect_guess']
      

    def get_word(self) -> str:
        return self.word

    def get_status_of_usr_input(self) -> bool:
        return self.is_input_valid

    def get_allowed_attempts(self) -> int:
        return self.allowed_attempts

    def get_message(self) -> str:
        return self.message

    def is_game_over(self) -> bool:
        if self.allowed_attempts == 0 or len(self.word_set) == 0: 
            return True
        return False
    