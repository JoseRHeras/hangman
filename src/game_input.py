import tkinter as tk 

class InputBox:

    def __init__(self, master:tk.Tk, row:int, cmd) -> None:
        self.master:tk.Tk = master
        self.cmd = cmd

        self._build_component_frame(row=row)
        self._build_child_components()
    
    def _build_component_frame(self, row:int) -> None:
        self.component_frame:tk.Frame = tk.Frame(master=self.master)
        self.component_frame.config(bg="lightblue", padx=10, pady=10)
        self.component_frame.grid(row=row, sticky="we")

    def _build_child_components(self) -> None:
        self.component_label:tk.Label = tk.Label(master=self.component_frame, text="Guess a Word!!")
        self.entry_box:tk.Entry = tk.Entry( master=self.component_frame)
        self.button:tk.Button = tk.Button(master=self.component_frame, text="Try!!", command=self._submit_usr_input)

        self.component_label.grid(row=1, column=1, padx=5)
        self.entry_box.grid(row=1, column=2 , padx=5)
        self.button.grid(row=1, column=3 , padx=5)
    
    def _submit_usr_input(self) -> None:
        usr_input = self.entry_box.get()
        self.entry_box.delete(0, tk.END)
        self.cmd(usr_input)
        
    def disable_button(self) -> None:
        self.button['state'] = 'disabled'
        
    def enable_button(self) -> None:
        self.button['state'] = 'enabled'
       
