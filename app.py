import tkinter as tk
import tkinter.ttk as ttk
from graph import Graph
from graph import Edge


class GraphFrame(tk.Canvas):
    def __init__(self, parent, graph_depth=5):
        super().__init__(parent)
        self.graph_depth = graph_depth
        self.graph = Graph(self.graph_depth)
        self.configure(
            highlightthickness=0
        )
        self.graph_level_frames = []
        self.edge_to_widget = dict()
        self.canvas = tk.Canvas(self)
        graph_by_level = self.graph.get_graph_by_levels()

        for r in range(self.graph_depth):
            self.rowconfigure(index=r, weight=1)
            edges = graph_by_level[r]
            new_frame = GraphLevelCanvas(self, edges)
            self.graph_level_frames.append(new_frame)

        self._connect_graph(self.graph.root)
        self.canvas.grid(rowspan=self.graph_depth)

        for r in range(self.graph_depth):
            self.graph_level_frames[r].grid(row=r, column=0)

    def _connect_graph(self, current_edge: Edge):
        edge_widget: ttk.Button = self.edge_to_widget[current_edge]
        cur_x, cur_y = edge_widget.winfo_pointerx(), edge_widget.winfo_pointery()
        for child in current_edge.children:
            child_edge_widget: ttk.Button = self.edge_to_widget[child]
            child_x = child_edge_widget.winfo_pointerx()
            child_y = child_edge_widget.winfo_pointery()
            
            self.canvas.create_line(cur_x, cur_y, child_x, child_y, fill="black", width=5)

            self._connect_graph(child)


class GraphLevelCanvas(tk.Canvas):
    def __init__(self, parent: GraphFrame, edges):
        super().__init__(parent)
        self.configure(
            highlightthickness=0,
        )
        for i in range(len(edges)):
            btn = ttk.Button(self, text=f"{i}", width=3)
            btn.pack(side='left', padx=10, pady=10)
            parent.edge_to_widget[edges[i]] = btn


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zalupa osla")
        self.geometry('600x400')


if __name__ == "__main__":
    root = Root()
    GraphFrame(root, 5).pack()
    root.mainloop()
