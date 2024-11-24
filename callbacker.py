from frames import GraphFrame
from frames import TableFrame
from frames import Root
from graph import GameTree
from tkinter.ttk import Combobox
from algorithms import run_minimax as algo_run_minimax

LEVELS_COUNT = 5


class Callbacker:
    def __init__(
        self,
        root: Root,
        game_tree: GameTree,
        game_tree_frame: GraphFrame,
        table_frame: TableFrame,
        combobox: Combobox
    ):
        self.root: Root = root
        self.game_tree: GameTree = game_tree
        self.game_tree_frame: GraphFrame = game_tree_frame
        self.table_frame: TableFrame = table_frame
        self.combobox: Combobox = combobox

    def pass_values_into_graph(self):
        values = self.table_frame.get_values()
        leaves = self.game_tree.get_leaves()
        for leaf_value_pair in zip(leaves, values):
            leaf, value = leaf_value_pair
            leaf.set_value(value)

        self.game_tree_frame.draw(self.game_tree)

    def run_minimax(self):
        algo_run_minimax(
            self.game_tree,
            self.game_tree_frame.get_first_move()
        )

        self.game_tree_frame.draw(self.game_tree)

    def first_move_changed(self, event):
        self.game_tree.clear_values()

        self.game_tree_frame.set_first_move(
            self.combobox.get()
        )
        self.game_tree_frame.draw(
            self.game_tree
        )

    def create_new_tree(self):
        self.game_tree = GameTree(LEVELS_COUNT)
        self.game_tree_frame.draw(self.game_tree)
        self.table_frame.create_new_table(self.game_tree.get_leaves_count())
