import tkinter as tk

from src.displayer import GameStatusDisplayer, HiddenWordDisplayer
from src.game_input import Console


class Hangman:

    def __init__(self) -> None:
        self.__build_root_box()
        self._build_graphical_components()
        
    def __build_root_box(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title("Hangman")

    def _build_graphical_components(self) -> None:
        self.game_status_displayer: GameStatusDisplayer = GameStatusDisplayer(parent=self.root)
        self.hidden_word_displayer: HiddenWordDisplayer = HiddenWordDisplayer(master=self.root, hidden_word="This is hidden")
        self.game_input: Console = Console(master=self.root)

    def run(self) -> None:
        self.root.mainloop()



