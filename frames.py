import tkinter as tk
from graph import GameTree
from ui_entities import VerticeUI


RADIUS = 9
PADDING = 1.75 * RADIUS


class Root(tk.Tk):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__()
        self.title("MiniMax Python")
        self.geometry(f"{WIDTH}x{HEIGHT}")


class GraphFrame(tk.Tk):
    def __init__(self, WIDTH, HEIGHT, parent: Root):
        self.CANVAS_SIZE_X = WIDTH
        self.CANVAS_SIZE_Y = HEIGHT
        self.c = tk.Canvas(
            parent,
            width=self.CANVAS_SIZE_X - PADDING,
            height=self.CANVAS_SIZE_Y - PADDING
        )
        self.entities = []

        self.c.pack()

    def draw_game_tree(self, game_tree: GameTree):
        graph_by_levels = game_tree.get_graph_by_levels()

        cur_y = RADIUS + PADDING
        cur_x = self.CANVAS_SIZE_X//2
        for level in graph_by_levels.keys():
            vertices = graph_by_levels[level]
            vertice_index = 0

            diff = len(vertices)//2
            if not len(vertices) % 2:
                for i in range(-diff, diff, 1):
                    if diff:
                        new_vertice = VerticeUI(
                            cur_x + i * (2*RADIUS + PADDING),
                            cur_y,
                            RADIUS,
                            vertices[vertice_index]
                        )
                        self.entities.append(new_vertice)
                        vertice_index += 1
            else:
                if not diff:
                    new_vertice = VerticeUI(
                            cur_x,
                            cur_y,
                            RADIUS,
                            vertices[vertice_index]
                        )
                    self.entities.append(new_vertice)
                    vertice_index += 1
                else:
                    for i in range(-diff, diff+1, 1):
                        new_vertice = VerticeUI(
                            cur_x + i * (2*RADIUS + PADDING),
                            cur_y,
                            RADIUS,
                            vertices[vertice_index]
                        )
                        self.entities.append(new_vertice)
                        vertice_index += 1

            cur_y += RADIUS + PADDING

        for entity in self.entities:
            entity.draw(self.c)

        self.c.pack()
