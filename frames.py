import tkinter as tk

from graph import GameTree
from graph import Vertice
from ui_entities import Vertice as VerticeUI
from ui_entities import StartValue


RADIUS = 20
HORIZONTAL_PADDING = 16
VERTICAL_PADDING = 32


class Root(tk.Tk):
    def __init__(self, WIDTH, HEIGHT):
        super().__init__()
        self.title("MiniMax Python")
        self.geometry(f"{WIDTH}x{HEIGHT}")


class TableFrame(tk.Frame):
    def __init__(self, parent, col_count):
        tk.Frame.__init__(self, parent, background="black")
        self.entries = []
        self._widgets = []
        for row in range(2):
            current_row = []
            for column in range(col_count):
                if row:
                    label = tk.Entry(
                        self,
                        borderwidth=0,
                        width=10
                    )
                    self.entries.append(label)
                else:
                    label = tk.Label(
                        self,
                        borderwidth=0,
                        text=f"{column+1}",
                        width=10
                    )
                label.grid(
                    row=row,
                    column=column,
                    sticky="nsew",
                    padx=1,
                    pady=1
                )
                self._widgets.append(label)
                current_row.append(label)

        for column in range(col_count):
            self.grid_columnconfigure(column, weight=1)

        self.pack()

    def get_values(self):
        values = []
        for entry in self.entries:
            value = entry.get()
            if value is not None:
                values.append(int(value))

        return values

    def create_new_table(self, col_count):
        for widget in self._widgets:
            widget.destroy()

        self._widgets = []
        self.entries = []
        for row in range(2):
            current_row = []
            for column in range(col_count):
                if row:
                    label = tk.Entry(
                        self,
                        borderwidth=0,
                        width=10
                    )
                    self.entries.append(label)
                else:
                    label = tk.Label(
                        self,
                        borderwidth=0,
                        text=f"{column+1}",
                        width=10
                    )
                label.grid(
                    row=row,
                    column=column,
                    sticky="nsew",
                    padx=1,
                    pady=1
                )
                self._widgets.append(label)
                current_row.append(label)

        for column in range(col_count):
            self.grid_columnconfigure(column, weight=1)

        self.pack()


class GraphFrame(tk.Frame):
    def __init__(self, WIDTH, HEIGHT, parent: Root):
        super().__init__(master=parent)
        self.CANVAS_SIZE_X = WIDTH
        self.CANVAS_SIZE_Y = 500
        self.c = tk.Canvas(
            self,
            width=self.CANVAS_SIZE_X,
            height=self.CANVAS_SIZE_Y
        )
        self.first_move = "MIN"
        self.entities = []
        self.graph_vertice_to_ui = {}
        self.leaves_to_ui = {}
        self.c.pack()
        self.pack(anchor="center")

    def _connect_two_entities(self, first, second):
        fill = "black"
        if first.is_pruned() or second.is_pruned():
            fill = "red"

        self.c.create_line(
            first.x,
            first.y + RADIUS,
            second.x,
            second.y - RADIUS,
            fill=fill
        )

        self.c.pack()

    def _connect_entities(self):
        for entity in self.entities:
            if isinstance(entity, VerticeUI):
                graph_vertice: Vertice = entity.get_reference()
                for child in graph_vertice.get_children():
                    child_ui = self.graph_vertice_to_ui[child]
                    self._connect_two_entities(entity, child_ui)

    def set_first_move(self, first_move):
        self.first_move = first_move

    def get_first_move(self):
        return self.first_move

    def _clear(self):
        self.entities = []
        self.c.delete(tk.ALL)
        self.c.pack()

    def draw(self, game_tree: GameTree):
        self._clear()
        self._draw_game_tree(game_tree)
        self._draw_moves(game_tree.get_levels_count())

    def _draw_game_tree(self, game_tree: GameTree):
        graph_by_levels = game_tree.get_graph_by_levels()

        cur_y = RADIUS + VERTICAL_PADDING
        cur_x = self.CANVAS_SIZE_X//2
        for level in graph_by_levels.keys():
            vertices = graph_by_levels[level]
            vertice_index = 0

            diff = len(vertices)//2
            if not len(vertices) % 2:
                for i in range(-diff, diff, 1):
                    if diff:
                        new_vertice = VerticeUI(
                            cur_x + i * (2*RADIUS + HORIZONTAL_PADDING),
                            cur_y,
                            RADIUS,
                            vertices[vertice_index]
                        )
                        self.graph_vertice_to_ui[vertices[vertice_index]] = new_vertice
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
                    self.graph_vertice_to_ui[vertices[vertice_index]] = new_vertice
                    self.entities.append(new_vertice)
                    vertice_index += 1
                else:
                    for i in range(-diff, diff+1, 1):
                        new_vertice = VerticeUI(
                            cur_x + i * (2*RADIUS + HORIZONTAL_PADDING),
                            cur_y,
                            RADIUS,
                            vertices[vertice_index]
                        )
                        self.graph_vertice_to_ui[vertices[vertice_index]] = new_vertice
                        self.entities.append(new_vertice)
                        vertice_index += 1

            cur_y += RADIUS + VERTICAL_PADDING

        leaves = game_tree.get_leaves()
        leaf_index = 1

        diff = len(leaves)//2
        if not len(leaves) % 2:
            for i in range(-diff, diff, 1):
                if diff:
                    new_leaf = StartValue(
                        cur_x + i * (2*RADIUS + HORIZONTAL_PADDING),
                        cur_y,
                        leaf_index,
                        leaves[leaf_index-1]
                    )
                    self.graph_vertice_to_ui[leaves[leaf_index-1]] = new_leaf
                    self.entities.append(new_leaf)
                    leaf_index += 1
        else:
            if not diff:
                new_leaf = StartValue(
                        cur_x,
                        cur_y,
                        leaf_index,
                        leaves[leaf_index-1]
                    )
                self.entities.append(new_leaf)
                self.graph_vertice_to_ui[leaves[leaf_index-1]] = new_leaf
                leaf_index += 1
            else:
                for i in range(-diff, diff+1, 1):
                    new_leaf = StartValue(
                        cur_x + i * (2*RADIUS + HORIZONTAL_PADDING),
                        cur_y,
                        leaf_index,
                        leaves[leaf_index-1]
                    )
                    self.entities.append(new_leaf)
                    self.graph_vertice_to_ui[leaves[leaf_index-1]] = new_leaf
                    leaf_index += 1

        for entity in self.entities:
            entity.draw(self.c)

        self._connect_entities()

    def _draw_moves(self, levels_count):
        cur_y = RADIUS+VERTICAL_PADDING
        cur_move = self.first_move

        for _ in range(levels_count):
            self.c.create_text(HORIZONTAL_PADDING, cur_y, text=cur_move)

            cur_move = "MIN" if cur_move == "MAX" else "MAX"
            cur_y += RADIUS + VERTICAL_PADDING
