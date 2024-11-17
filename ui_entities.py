import tkinter as tk
from graph import Vertice


class VerticeUI:
    def __init__(self, x, y, radius, vertice: Vertice):
        self.x = x
        self.y = y
        self.r = radius
        self.reference = vertice

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
                font=("Purisa", 12)
            )
