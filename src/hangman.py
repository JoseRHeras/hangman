import tkinter as tk

from src.displayer import GameStatusDisplayer, HiddenWordDisplayer, MessageDisplayer
from src.game_input import InputBox
from src.game_master import GameMaster


class Hangman:

    def __init__(self) -> None:
        self.game_master: GameMaster = GameMaster()  # Logical class

        self._build_root_box()
        self._build_graphical_components()

    def _build_root_box(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title("Hangman")

    def _build_graphical_components(self) -> None:
        self.game_status_displayer: GameStatusDisplayer = GameStatusDisplayer(
            master=self.root, row=2, allowed_attempts=self.game_master.get_allowed_attempts())
        self.hidden_word_displayer: HiddenWordDisplayer = HiddenWordDisplayer(
            master=self.root, hidden_word=self.game_master.get_word(), row=1)
        self.input_box: InputBox = InputBox(
            master=self.root, row=3, cmd=self._update_interface)
        self.message_displayer: MessageDisplayer = MessageDisplayer(
            master=self.root, row=4)

        self.message_displayer.set_message(self.game_master.get_message())

    def _update_interface(self, word: str) -> None:
        self.game_master.load_and_evaluate_usr_input(usr_input=word)
                
        self.message_displayer.set_message(self.game_master.get_message())

        if self.game_master.get_status_of_usr_input():
            self.hidden_word_displayer.reveal_letter(letter=word)
        elif len(word) == 1:
            self.game_status_displayer.update_displayer(letter=word)
            
        if self.game_master.is_game_over():
            self._display_result_and_set_block_state()
               
    def _display_result_and_set_block_state(self) -> None:
        self.input_box.disable_button()

    def run(self) -> None:
        self.root.mainloop()
