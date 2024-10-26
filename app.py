import tkinter as tk
from graph import Graph
from graph import Edge
from collections import defaultdict

WIDTH, HEIGHT = 800, 800


class GraphFrame(tk.Canvas):
    PADDING = 20
    VERTICE_SIZE = 20
    CANVAS_SIZE_X = WIDTH
    CANVAS_SIZE_Y = HEIGHT

    def __init__(self, parent, graph_depth=5, max_children=3):
        super().__init__(parent)
        self.graph_depth = graph_depth
        self.max_children = max_children
        self.graph = Graph(self.graph_depth, max_children)
        self.configure(
            highlightthickness=0
        )
        self.canvas = tk.Canvas(
            self,
            bg="white",
            width=self.CANVAS_SIZE_X,
            height=self.CANVAS_SIZE_Y
        )
        
        self.graph_by_levels = self.graph.get_graph_by_levels()
        self.vertice_to_rectangle = dict()
        self.graph_as_dict = self.graph.get_graph_as_dict()
        
        self._draw_graph_by_levels()
        self._connect_graph()
        self.canvas.pack(anchor=tk.CENTER, expand=1)

    def _set_vertice_to_rectangle(self):
        cur_number = 1

        for key in self.graph_by_levels:
            for edge in self.graph_by_levels[key]:
                self.vertice_to_rectangle[edge[0]] = cur_number
                cur_number += 1

    def _connect_graph(self):
        self._set_vertice_to_rectangle()
        
        for key in self.graph_as_dict:
            rectangle_id = self.vertice_to_rectangle[key[0]]

            left_x, left_y, right_x, right_y = self.canvas.coords(
                rectangle_id
            )
            start_x = (left_x+right_x)//2
            start_y = (left_y+right_y)//2 + self.VERTICE_SIZE//2

            for child in self.graph_as_dict[key]:
                child_rectangle_id = self.vertice_to_rectangle[child[0]]
                left_x, left_y, right_x, right_y = self.canvas.coords(
                    child_rectangle_id
                )

                end_x = (left_x+right_x)//2
                end_y = (left_y+right_y)//2 - self.VERTICE_SIZE//2

                self.canvas.create_line(start_x, start_y, end_x, end_y)

    def _draw_rectangle(self, center_x, center_y, value=None,):
        self.canvas.create_rectangle(
            center_x - self.VERTICE_SIZE//2,
            center_y - self.VERTICE_SIZE//2,
            center_x + self.VERTICE_SIZE//2,
            center_y + self.VERTICE_SIZE//2,
            fill="white",
        )

    def _draw_graph_by_levels(self):
        cur_y = self.VERTICE_SIZE//2 + self.PADDING
        cur_x = self.CANVAS_SIZE_X//2
        for level in self.graph_by_levels.keys():
            vertices = self.graph_by_levels[level]

            diff = len(vertices)//2
            if not len(vertices) % 2:
                for i in range(-diff, diff, 1):
                    if diff:
                        self._draw_rectangle(
                            cur_x + i * (self.VERTICE_SIZE + self.PADDING),
                            cur_y
                        )
            else:
                if not diff:
                    self._draw_rectangle(
                        cur_x,
                        cur_y
                    )
                else:
                    for i in range(-diff, diff+1, 1):
                        self._draw_rectangle(
                            cur_x + i * (self.VERTICE_SIZE + self.PADDING),
                            cur_y
                        )

            cur_y += self.VERTICE_SIZE + self.PADDING


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kurwa bober")
        self.geometry(f"{WIDTH}x{HEIGHT}")


if __name__ == "__main__":
    root = Root()
    GraphFrame(root, graph_depth=5, max_children = 2).pack()
    root.mainloop()
