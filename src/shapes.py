from abc import ABC, abstractmethod
import tkinter as tk
from typing import List

class GeometricFigure(ABC):
    
    @abstractmethod
    def draw(self, canvas: tk.Canvas, coordinates: List[int]) -> None:
        pass

class Circle(GeometricFigure):
    
    def draw(self, canvas: tk.Canvas, coordinates: List[int]) -> None:
        canvas.create_oval(*coordinates)
        
class Line(GeometricFigure):
    
    def draw(self, canvas: tk.Canvas, coordinates: List[int]) -> None:
        canvas.create_line(*coordinates)
    


def get_geometric_figure(key:str) -> GeometricFigure:
    
    geometric_figures: dict = {
        "line" : Line(),
        "circle" : Circle()
    }
    
    return geometric_figures[key]
