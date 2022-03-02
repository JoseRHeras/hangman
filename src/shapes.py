from abc import ABC, abstractmethod
import tkinter as tk
from typing import List

class Shape(ABC):
    
    @abstractmethod
    def draw(self, canvas: tk.Canvas, coordinates: List[int]) -> None:
        pass

class Circle(Shape):
    
    def draw(self, canvas: tk.Canvas, coordinates: List[int]) -> None:
        canvas.create_oval(*coordinates)
        
class Line(Shape):
    
    def draw(self, canvas: tk.Canvas, coordinates: List[int]) -> None:
        canvas.create_line(*coordinates)
    


def get_shape(shape:str) -> Shape:
    
    shapes: dict = {
        "line" : Line(),
        "circle" : Circle()
    }
    
    return shapes[shape]
