import tkinter as tk

from src.displayer import GameStatusDisplayer, HiddenWordDisplayer, MessageDisplayer
from src.game_input import InputBox


class Hangman:

    def __init__(self) -> None:

        self.__build_root_box()
        self._build_graphical_components()

        
    def __build_root_box(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title("Hangman")

    def _build_graphical_components(self) -> None:
        self.game_status_displayer: GameStatusDisplayer = GameStatusDisplayer(master=self.root, row=2, allowed_attempts=9)
        self.hidden_word_displayer: HiddenWordDisplayer = HiddenWordDisplayer(master=self.root, hidden_word="This is ", row=1)
        self.input_box: InputBox = InputBox(master=self.root, row=3, cmd=self._update_interface)
        self.message_displayer: MessageDisplayer = MessageDisplayer(master=self.root, row=4)

    def _update_interface(self, word:str) -> None:
        self.game_status_displayer.update_displayer(letter=word)
        self.hidden_word_displayer.reveal_letters_on_the_displayer(letter=word)

    def run(self) -> None:
        self.root.mainloop()



