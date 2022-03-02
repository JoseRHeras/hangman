import tkinter as tk
from typing import List

from src.shapes import Line, Shape, get_shape


class Canvas:
    
    hangman_pieces = [["circle", 80, 180, 120, 130], ]

    def __init__(self, master:tk.Frame, pieces_to_draw:int) -> None:
        self.master:tk.Frame = master
        self.pieces_to_draw:int = pieces_to_draw

        self._build_canvas()

    def _build_canvas(self) -> None:
        self.canvas: tk.Canvas = tk.Canvas(master=self.master)
        self.canvas.config(width=300, height=200)
        self.canvas.grid(row=1, column=1)

    

    def draw_next_piece(self) -> None:
        shape_name, coordinates = self.hangman_pieces[0][0], self.hangman_pieces[0][1:]
        shape: Shape = get_shape(shape=shape_name)
        
        shape.draw(canvas=self.canvas, coordinates=coordinates)



class WordGrid:

    def __init__(self, master:tk.Frame, max_number: int) -> None:
        self.master: tk.Frame = master
        self.block_size: int = 30
        self.current_box_index: int = 0

        self._build_component_frame()
        self._build_child_components(size=max_number)
        
    
    def _build_component_frame(self) -> None:
        self.container_frame: tk.Frame = tk.Frame(master=self.master)
        self.container_frame.config(height=200)
        self.container_frame.grid(row=1, column=2, padx=7)

    def _build_child_components(self, size:int) -> None:
        self.labels: list = []
        row = col = 1
        
        for _ in range(size):
            if col > 3: 
                col , row = 1, row + 1

            frame = tk.Frame(master=self.container_frame, width=self.block_size, height=self.block_size, bg="pink", border=2)
            frame_label = tk.Label(master=frame)
            string = tk.StringVar(value="  ")
            frame_label.config(textvariable=string)
            
            frame_label.pack()
            frame.grid(row=row, column=col)

            self.labels.append(string)
            col += 1
    
    def insert_letter_into_grid(self, letter:str) -> None:
        label:tk.StringVar = self.labels[self.current_box_index]
        label.set(letter)
        self.current_box_index += 1