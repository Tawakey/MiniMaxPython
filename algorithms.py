from graph import GameTree, Vertice


MIN, MAX = 0, 1


def prun_verticies(cur_vertice: Vertice, reason: str):
    children_list = cur_vertice.get_children()
    if not cur_vertice.get_visited():
        cur_vertice.prun(reason)
        for child in children_list:
            if not child.get_visited():
                prun_verticies(child, "")


def _get_next_move(cur_move: int):
    if cur_move == MIN:
        return MAX
    else:
        return MIN


def _recurcively_run_minimax(
    cur_vertice: Vertice,
    cur_level,
    levels_count,
    cur_move
):
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


def run_minimax(game_tree: GameTree, first_move: str):
    root = game_tree.get_root()
    levels_count = game_tree.get_levels_count()
    if first_move == "MIN":
        value_to_pass = MIN
    else:
        value_to_pass = MAX
    _recurcively_run_minimax(root, 0, levels_count, value_to_pass)


def _min_value(
    cur_vertice: Vertice,
    alpha: float,
    beta: float,
    direction: int
):
    was_prunned = False
    children_list = cur_vertice.get_children()
    if not direction:
        children_list = children_list[::-1]
    if not len(children_list):
        return cur_vertice.get_value()

    v = float("inf")
    for i, child in enumerate(children_list):
        if not was_prunned:
            new_v = _max_value(child, alpha, beta, direction)
            child.set_visited()
            if new_v < v:
                v = new_v
            if alpha is not None and new_v <= alpha and i != len(children_list)-1:
                reason = f"{new_v}<={alpha}"
                prun_verticies(cur_vertice, reason)
                was_prunned = True
            if (beta is None) or (new_v < beta):
                beta = new_v
        else:
            child.prun()

    cur_vertice.set_value(v)
    return v


def _max_value(
    cur_vertice: Vertice,
    alpha: float,
    beta: float,
    direction: int
):
    was_prunned = False
    children_list = cur_vertice.get_children()
    if not direction:
        children_list = children_list[::-1]
    if not len(children_list):
        return cur_vertice.get_value()

    v = -float("inf")
    for i, child in enumerate(children_list):
        if not was_prunned:
            new_v = _min_value(child, alpha, beta, direction)
            child.set_visited()
            if new_v > v:
                v = new_v
            if beta is not None and new_v >= beta and i != len(children_list)-1:
                reason = f"{new_v}>={beta}"
                prun_verticies(cur_vertice, reason)
                was_prunned = True
            if alpha is None or new_v > alpha:
                alpha = new_v
        else:
            child.prun()

    cur_vertice.set_value(v)
    return v


def run_minimax_with_pruning(game_tree: GameTree, first_move: str, direction: str):
    root = game_tree.get_root()

    alpha, beta = None, None
    if direction == "СЛЕВА НАПРАВО":
        direction = 1
    else:
        direction = 0

    if first_move == "MIN":
        _min_value(root, alpha, beta, direction)
    else:
        _max_value(root, alpha, beta, direction)
