import random


class Edge:
    def __init__(
        self,
        number: int = 1,
        value: float = None,
    ):
        self.number = number,
        self.value = value,
        self.children = list()

    def add_edge_to_children(
        self,
        new_edge,
    ):
        self.children.append(new_edge)

    def get_number(
        self,
    ):
        return self.number[0]

    def __str__(self):
        ancestors = [child.get_number() for child in self.children]
        return f"Вершина #{self.number[0]}\nЗначение: {self.value[0]}\nПотомки: {ancestors}\n"


class Graph:
    def __init__(
        self,
        depth: int = 5,
        max_children: int = 3
    ):
        self.depth = depth
        self.root = Edge()
        self.edge_number = 1
        self.leaves = list()
        self.graph_as_dict = dict()
        self.max_children = max_children

        random.seed()

        # start from root
        self._generate_graph(self.root, 1)

    def _generate_graph(self, current_edge: Edge, current_depth: int = 1):
        if current_depth < self.depth:
            self.graph_as_dict[current_edge.number] = []

            children_number = random.randrange(1, self.max_children+1)
            for _ in range(children_number):
                self.edge_number += 1
                new_edge = Edge(
                    number=self.edge_number
                )
                current_edge.add_edge_to_children(new_edge)
                self.graph_as_dict[current_edge.number].append(new_edge.number)

                if current_depth == self.depth:
                    self.leaves.append(new_edge)

                self._generate_graph(new_edge, current_depth + 1)

    def print_leaves(self):
        for leaf in self.leaves:
            print(leaf)

    def get_graph_as_dict(self):
        return self.graph_as_dict

    def get_graph_by_levels(self):
        from collections import defaultdict
        res_dict = defaultdict(list)
        self._recursively_get_graph_by_levels(self.root, 1, res_dict=res_dict)
        for key in res_dict:
            res_dict[key] = sorted(res_dict[key])

        return res_dict

    def _recursively_get_graph_by_levels(
        self,
        current_edge: Edge,
        current_level,
        res_dict
    ):
        res_dict[current_level].append(current_edge.number)
        for child in current_edge.children:
            self._recursively_get_graph_by_levels(
                child,
                current_level + 1,
                res_dict
            )

    def _recursively_print_graph(self, current_edge: Edge):
        print(current_edge)
        for child in current_edge.children:
            self._recursively_print_graph(child)

    def __str__(self):
        self._recursively_print_graph(self.root)
        return ""


if __name__ == "__main__":
    test_edge = Edge()
    print(test_edge)

    test_graph = Graph(3)
    print(test_graph)

    print(test_graph.get_graph_by_levels())
