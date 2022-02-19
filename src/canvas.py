import tkinter as tk

class HangmanCanvas:

    def __init__(self, parent:tk.Tk) -> None:
        self.parent:tk.Tk = parent
        self._build_canvas_component()

    def _build_canvas_component(self) -> None:
        self.canvas: tk.Canvas = tk.Canvas()
        self.canvas.config(width=200, height=200)
        self.canvas.grid(row=1, column=1)

    

