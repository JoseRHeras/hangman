import tkinter as tk


class GameStatusDisplayer:

    def __init__(self, parent:tk.Tk) -> None:
        self.parent: tk.Tk = parent
        self._build_component()

    def _build_component(self) -> None:
        self.component: tk.Frame = tk.Frame(master=self.parent)
        self.component.config(bg="red")

        self.canvas: Canvas = Canvas(parent=self.component)
        self.guessed_displayer: GuessDisplayer = GuessDisplayer(parent=self.component)
        self.component.grid(row=1)



class Canvas:

    def __init__(self, parent:tk.Frame) -> None:
        self.parent:tk.Frame = parent
        self._build_canvas_component()

    def _build_canvas_component(self) -> None:
        self.canvas: tk.Canvas = tk.Canvas(master=self.parent)
        self.canvas.config(width=300, height=200)
        self.canvas.grid(row=1, column=1)

    
class GuessDisplayer:

    def __init__(self, parent:tk.Frame) -> None:
        self.parent: tk.Frame = parent
        self.max_number_of_words: int = 7
        self.block_size: int = 30

        self._build_component()
    
    def _build_component(self) -> None:
        self.container: tk.Frame = tk.Frame(master=self.parent)
        self.container.config(height=200, bg="darkblue")
        self._build_label_grid()
        self.container.grid(row=1, column=2, padx=7)

    def _build_label_grid(self) -> None:
        self.labels: list = []
        row = col = 1
        
        for _ in range(self.max_number_of_words):
            if col > 3: 
                col = 1
                row += 1 

            frame = tk.Frame(master=self.container, width=self.block_size, height=self.block_size, bg="pink", border=2)
            frame_label = tk.Label(master=frame)
            string = tk.StringVar(value="  ")
            frame_label.config(textvariable=string)
            
            frame_label.pack()
            frame.grid(row=row, column=col)

            self.labels.append(frame_label)

            col += 1



class HiddenWordDisplayer:

    def __init__(self, master, hidden_word: str) -> None:
        self.master = master
        self.hidden_word: str = hidden_word
        self._build_component()
        self._build_grid()

    def _build_component(self) -> None:
        self.component_frame: tk.Frame = tk.Frame(master=self.master)
        self.component_frame.grid(row=2)


    def _build_grid(self) -> None:
        
        for index in range(len(self.hidden_word)):
            frame = tk.Frame(master=self.component_frame, height=15, width=15, bg="pink", padx=3, pady=3)
            
            label = tk.Label(master=frame)
            string = tk.StringVar(value=f"{self.hidden_word[index]}")
            label.config(textvariable=string)
            
            label.pack()

            frame.grid(row=2, column=index)

