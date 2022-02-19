import tkinter as tk

from src.canvas import HangmanCanvas


class Hangman:

    def __init__(self) -> None:
        self.__build_root_box()
        self._build_graphical_components()
        
    def __build_root_box(self) -> None:
        self.root: tk.Tk = tk.Tk()
        self.root.title("Hangman")

    def _build_graphical_components(self) -> None:
        self.canvas: HangmanCanvas = HangmanCanvas(parent=self.root)

    def run(self) -> None:
        self.root.mainloop()


