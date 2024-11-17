from graph import GameTree, Vertice, Leaf
from typing import Union


MIN, MAX = 0, 1


def _get_next_move(cur_move: int):
    if cur_move == MIN:
        return MAX
    else:
        return MIN


def _recurcively_run_minimax(
    cur_vertice: Union[Vertice, Leaf],
    cur_level,
    levels_count,
    cur_move
):
    if cur_level == levels_count:
        start_values = cur_vertice.get_start_values()
        if cur_move == MAX:
            cur_vertice.set_value(max(start_values))
        else:
            cur_vertice.set_value(min(start_values))
    else:
        children_list = cur_vertice.get_children()
        for child in children_list:
            _recurcively_run_minimax(
                child,
                cur_level+1,
                levels_count,
                _get_next_move(cur_move)
            )  # get child value

            # now we have child value
            child_value = child.get_value()
            if cur_vertice.get_value() is None:
                cur_vertice.set_value(child_value)
            else:
                cur_value = cur_vertice.get_value()
                if cur_move == MAX:
                    cur_vertice.set_value(
                        max(cur_value, child_value)
                    )
                else:
                    cur_vertice.set_value(
                        min(cur_value, child_value)
                    )


def run_minimax(game_tree: GameTree, first_move: int):
    root = game_tree.get_root()
    levels_count = game_tree.get_levels_count()
    _recurcively_run_minimax(root, 1, levels_count, first_move)
