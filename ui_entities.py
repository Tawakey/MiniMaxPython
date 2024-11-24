import tkinter as tk
from graph import Vertice as GraphVertice


class Vertice:
    def __init__(self, x, y, radius, vertice: GraphVertice):
        self.x = x
        self.y = y
        self.r = radius
        self.alpha = float("-inf")
        self.beta = float("inf")
        self.reference = vertice

    def get_reference(self):
        return self.reference

    def draw(self, canvas: tk.Canvas):
        canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

        value_to_draw = self.reference.get_value()
        if value_to_draw is not None:
            canvas.create_text(
                self.x,
                self.y,
                text=value_to_draw,
                font=("Purisa", 9)
            )


class StartValue:
    def __init__(self, x, y, number, vertice: GraphVertice):
        self.x = x
        self.y = y
        self.reference = vertice
        self.number = number

    def draw(self, canvas: tk.Canvas):
        value_to_draw = self.reference.get_value()
        if value_to_draw is not None:
            canvas.create_text(
                self.x,
                self.y,
                text=value_to_draw,
                font=("Purisa", 9)
            )
        else:
            canvas.create_text(
                self.x,
                self.y,
                text=f"p{self.number}",
                font=("Purisa", 9)
            )
