import tkinter as tk
from src.components import Canvas, WordGrid


class GameStatusDisplayer:

    def __init__(self, master: tk.Tk, row: int, allowed_attempts: int) -> None:
        self.master: tk.Tk = master
        self.allowed_attempts: int = allowed_attempts

        self._build_component(row=row)
        self._build_child_components()

    def _build_component(self, row: int) -> None:
        self.component_frame: tk.Frame = tk.Frame(master=self.master)
        self.component_frame.config(bg="red")
        self.component_frame.grid(row=row)

    def _build_child_components(self) -> None:
        self.canvas: Canvas = Canvas(
            master=self.component_frame, pieces_to_draw=self.allowed_attempts)
        self.word_grid: WordGrid = WordGrid(
            master=self.component_frame, max_number=self.allowed_attempts)

    def update_displayer(self, letter: str) -> None:
        self.word_grid.insert_letter_to_grid(letter=letter)
        self.canvas.draw_next_piece()


class HiddenWordDisplayer:

    def __init__(self, master: tk.Tk, hidden_word: str, row: int) -> None:
        self.master: tk.Tk = master
        self.hidden_word: str = hidden_word

        self._build_component(row=row)
        self._build_child_components()

    def _build_component(self, row: int) -> None:
        self.component_frame: tk.Frame = tk.Frame(master=self.master)
        self.component_frame.config(bg="whitesmoke", pady=10, padx=10)
        self.component_frame.grid(row=row, sticky="we")

    def _build_child_components(self) -> None:
        self.strings: list = []

        for index in range(len(self.hidden_word)):
            frame = tk.Frame(master=self.component_frame,
                             height=15, width=15, bg="pink", padx=3, pady=3)

            label = tk.Label(master=frame)
            string = tk.StringVar(value=" ")
            label.config(textvariable=string)

            label.pack()
            self.strings.append(string)
            frame.grid(row=1, column=index)

    def reveal_letters_on_the_displayer(self, letter:str) -> None:
        for index, word in enumerate(self.hidden_word):
            if word == letter:
                hidden_block:tk.StringVar = self.strings[index]
                hidden_block.set(letter)


class MessageDisplayer:
    
    def __init__(self, master:tk.Tk, row:int, message:str) -> None:
        self.master: tk.Tk = master

        self._build_component_frame(row=row)
        self._build_child_components(message=message)

    def _build_component_frame(self, row:int) -> None:
        self.component_frame:tk.Frame = tk.Frame(master=self.master)
        self.component_frame.grid(row=row)

    def _build_child_components(self, message:str) -> None:
        self.string_var: tk.StringVar = tk.StringVar(value=message)
        label: tk.Label = tk.Label( master=self.component_frame, textvariable=self.string_var)
        label.grid(row=1, sticky="we")

    def set_message(self, msg:str) -> None:
        self.string_var.set(msg)
        self.master.update_idletasks()