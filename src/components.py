import tkinter as tk
from typing import List
from src.hangman_pieces import Arms, Body, HangmanPost, Head, Legs, HangmanPiece


class Canvas:
        
    # hangman_pieces = [
    #     HangmanPost(), Head(), Body(), Legs(), Arms()
    # ]
    
    hangman_pieces: List[HangmanPiece] = [
        HangmanPost, Head, Body, Legs, Arms
    ]

    def __init__(self, master:tk.Frame, pieces_to_draw:int) -> None:
        self.master:tk.Frame = master
        self.pieces_to_draw:int = pieces_to_draw
        self.current_piece:int = 0

        self._build_canvas()

    def _build_canvas(self) -> None:
        self.canvas: tk.Canvas = tk.Canvas(master=self.master)
        self.canvas.config(width=300, height=200)
        self.canvas.grid(row=1, column=1)

    def draw_next_piece(self) -> None:
        hangman_piece: HangmanPiece = Canvas.hangman_pieces[self.current_piece]
        hangman_piece.draw(canvas=self.canvas)
        
        self.current_piece += 1
        


class WordGrid:

    def __init__(self, master:tk.Frame, max_number: int) -> None:
        self.master: tk.Frame = master
        self.block_size: int = 2
        self.current_box_index: int = 0

        self._build_component_frame()
        self._build_child_components(size=max_number)
        
    
    def _build_component_frame(self) -> None:
        self.container_frame: tk.Frame = tk.Frame(master=self.master)
        self.container_frame.grid(row=1, column=2, padx=7)

    def _build_child_components(self, size:int) -> None:
        self.labels: list = []
        row = col = 1
        count: int = 1

        for _ in range(9):
            if col > 3: 
                col , row = 1, row + 1

            frame = tk.Frame(master=self.container_frame, bg="blue", border=2) 
            frame_label = tk.Label(master=frame, width=self.block_size, height=(self.block_size - 1))

            if count <= size:
                string: tk.StringVar = tk.StringVar(value="   ")
                frame_label.config(textvariable=string) 
                self.labels.append(string)
            
            else:
                frame_label.config(bg="blue")

            frame_label.pack()
            frame.grid(row=row, column=col)

            col += 1
            count += 1
    
    def insert_letter_to_grid(self, letter:str) -> None:
        label:tk.StringVar = self.labels[self.current_box_index]
        label.set(letter)
        self.current_box_index += 1