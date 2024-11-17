import gc
from typing import Union
import random
import time
from collections import defaultdict


class Vertice:
    """
    Represents a vertice of the game tree
    """
    def __init__(self):
        self.value = None
        self.children = []

    def set_value(self, new_value: int):
        self.value = new_value

    def get_value(self):
        return self.value

    def add_children(self, new_child):
        self.children.append(new_child)

    def get_children(self):
        return self.children


class Leaf(Vertice):
    """
    Represents a leaf of the game tree
    """
    def __init__(self):
        self.value = None
        self.start_values = []

    def add_start_value(self, start_value: int):
        self.start_values.append(start_value)

    def get_start_values(self):
        return self.start_values


class GameTree:
    """
    Represents a game tree
    """
    def __init__(self):
        self.root: Vertice = Vertice()
        self.levels_count: int = 5
        self.leaves = []
        self.graph_by_level = defaultdict(list)

        random.seed(time.time())

        self.generate_tree()

    def get_root(self):
        return self.root

    def get_levels_count(self):
        return self.levels_count

    def _recursively_generate_tree(
        self,
        cur_vertice: Union[Vertice, Leaf],
        cur_level: int
    ):
        if cur_level == self.levels_count:
            new_leaf: Leaf = Leaf()
            start_values_count = random.randint(1, 2)
            for _ in range(start_values_count):
                new_leaf.add_start_value(0)

            cur_vertice.add_children(new_leaf)
        else:
            children_vertices_count = random.randint(1, cur_level+1)
            for _ in range(children_vertices_count):
                new_vertice: Vertice = Vertice()
                self._recursively_generate_tree(new_vertice, cur_level+1)

                cur_vertice.add_children(new_vertice)

    def _recursively_delete_tree(
        self,
        cur_vertice: Union[Vertice, Leaf],
        cur_level: int
    ):
        if cur_level == self.levels_count:
            del cur_vertice
        else:
            children_list = cur_vertice.get_children()
            for child in children_list:
                self._recursively_delete_tree(child, cur_level+1)
                del child

    def _recursively_get_graph_by_levels(
        self,
        cur_vertice: Union[Vertice, Leaf],
        cur_level: int
    ):
        self.graph_by_level[cur_level].append(cur_vertice)
        if cur_level != self.levels_count:
            children_list = cur_vertice.get_children()
            for child in children_list:
                self._recursively_get_graph_by_levels(
                    child,
                    cur_level+1
                )

    def generate_tree(self, levels_count: int = 5):
        self._recursively_delete_tree(self.root, 1)
        gc.collect()

        self.levels_count = levels_count

        self._recursively_generate_tree(self.root, 1)
        self.graph_by_level.clear()
        self._recursively_get_graph_by_levels(self.root, 1)

    def get_graph_by_levels(self):
        return self.graph_by_level
