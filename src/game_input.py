import tkinter as tk 

class Console:

    def __init__(self, master:tk.Tk) -> None:
        self.master: tk.Tk = master
        self._build_component()
        self._build_child_components()
        

    def _build_component(self) -> None:
        self.component_frame: tk.Frame = tk.Frame(master=self.master)
        self.component_frame.config(bg="blue")

        self.component_frame.grid(row=3, sticky="we")


    def _build_child_components(self) -> None:
        self.input_box: InputBox = InputBox(master=self.component_frame)



class InputBox:

    def __init__(self, master:tk.Frame) -> None:
        self.master:tk.Frame = master
        self._build_component()
        self._build_children_components()

    def _build_component(self) -> None:
        self.component_frame:tk.Frame = tk.Frame(master=self.master)
        self.component_frame.grid(row=1, column=2)


    def _build_children_components(self) -> None:
        self.label: tk.Label = tk.Label(master=self.component_frame, text="Guess")
        self.label.pack()

        self._build_and_setup_entry_widget()
       
        self.button: tk.Button = tk.Button(master=self.component_frame)
        self.button.config(text="Try!!", command=self.get_user_input)
        self.button.pack()

    def _build_and_setup_entry_widget(self) -> None:
        self.entry_section:tk.Entry = tk.Entry( master=self.component_frame)
        self.entry_section.config(width=3)
        self.entry_section.pack()


    def get_user_input(self) -> str:
        return self.entry_section.get()
        


