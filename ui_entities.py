import tkinter as tk
from graph import Vertice as GraphVertice

FONT_SIZE = 8


class Vertice:
    def __init__(self, x, y, radius, vertice: GraphVertice):
        self.x = x
        self.y = y
        self.r = radius
        self.reference = vertice

    def get_reference(self):
        return self.reference

    def is_pruned(self):
        return self.reference.check_if_pruned()

    def draw(self, canvas: tk.Canvas):
        canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            outline="red" if self.is_pruned() else "black"
        )

        if self.is_pruned():
            text_to_draw = self.reference.get_reason()
        else:
            value = self.reference.get_value()
            text_to_draw = value if value is not None else ""

        canvas.create_text(
            self.x,
            self.y,
            text=text_to_draw,
            font=("Purisa", FONT_SIZE)
        )


class StartValue:
    def __init__(self, x, y, number, vertice: GraphVertice):
        self.x = x
        self.y = y
        self.reference = vertice
        self.number = number

    def is_pruned(self):
        return False

    def draw(self, canvas: tk.Canvas):
        value_to_draw = self.reference.get_value()
        if value_to_draw is not None:
            canvas.create_text(
                self.x,
                self.y,
                text=value_to_draw,
                font=("Purisa", FONT_SIZE)
            )
        else:
            canvas.create_text(
                self.x,
                self.y,
                text=f"p{self.number}",
                font=("Purisa", FONT_SIZE)
            )
