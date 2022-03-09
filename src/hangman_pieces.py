import tkinter as tk
from src.shapes import get_geometric_figure
from abc import ABC, abstractmethod


class HangmanPiece(ABC):
    
    @classmethod
    @abstractmethod
    def draw(cls, canvas: tk.Canvas) -> None:
        pass

class HangmanPost(HangmanPiece):
    
    shapes = [
        ["line", 30, 180, 50, 180], 
        ['line', 40, 180, 40, 20], 
        ["line", 40, 20, 80, 20], 
        ["line", 80, 20, 80, 40], 
    ]
    
    @classmethod
    def draw(cls, canvas: tk.Canvas) -> None:
        
        for shape in cls.shapes:
            name, coordinates = shape[0], shape[1: ]
            shape = get_geometric_figure(key=name)
            
            shape.draw(canvas, coordinates)

class Head(HangmanPiece):
    shapes = ["circle", 70, 60, 90, 40]
    
    @classmethod
    def draw(cls, canvas: tk.Canvas) -> None:
        name, coordinates = cls.shapes[0], cls.shapes[1: ]
        shape = get_geometric_figure(key=name)
        shape.draw(canvas, coordinates)
        
        
class Body(HangmanPiece):
    shapes = ["line", 80, 60, 80, 100]
    
    @classmethod
    def draw(cls, canvas: tk.Canvas) -> None:
        name, coordinates = cls.shapes[0], cls.shapes[1: ]
        shape = get_geometric_figure(key=name)
        shape.draw(canvas, coordinates)
        
        
class Legs(HangmanPiece):
    shapes = [
        ["line", 70, 140, 80, 100],
        ["line", 80, 100, 90, 140]
    ]
    
    @classmethod
    def draw(cls, canvas: tk.Canvas) -> None:
        for shape in cls.shapes:
            name, coordinates = shape[0], shape[1: ]
            shape = get_geometric_figure(key=name)
            shape.draw(canvas, coordinates)
            

class Arms(HangmanPiece):
    shapes = [
        ["line", 70, 80, 80, 70 ],
        ["line", 80, 70, 90, 80] 
    ]
    
    @classmethod
    def draw(cls, canvas: tk.Canvas) -> None:
        for shape in cls.shapes:
            name, coordinates = shape[0], shape[1: ]
            shape = get_geometric_figure(key=name)
            shape.draw(canvas, coordinates)
            
    
  
    
            
