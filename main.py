from frames import Root
from frames import GraphFrame
from frames import TableFrame
from graph import GameTree
from tkinter import NW
from tkinter import ttk
from callbacker import Callbacker


WIDTH, HEIGHT = 1200, 800
LEVELS_COUNT = 5


START_POSITIONS = ("MIN", "MAX")
DIRECTION = ("СЛЕВА НАПРАВО", "СПРАВА НАЛЕВО")

if __name__ == "__main__":
    root = Root(WIDTH, HEIGHT)
    game_tree = GameTree(LEVELS_COUNT)
    game_tree_frame = GraphFrame(WIDTH, HEIGHT, root)
    game_tree_frame.draw(game_tree)
    combobox = ttk.Combobox(values=START_POSITIONS)
    direction = ttk.Combobox(values=DIRECTION)

    table_frame = TableFrame(root, game_tree.get_leaves_count())
    callbacker = Callbacker(
        root,
        game_tree,
        game_tree_frame,
        table_frame,
        combobox,
        direction
    )

    pass_value_btn = ttk.Button(
        text="Задать значения",
        command=callbacker.pass_values_into_graph
    )

    combobox.current(0)
    direction.current(0)
    combobox.bind(
        "<<ComboboxSelected>>",
        callbacker.first_move_changed
    )

    direction.bind(
        "<<ComboboxSelected>>",
        callbacker.direction_changed
    )

    run_minimax_btn = ttk.Button(
        text="Запустить MiniMax",
        command=callbacker.run_minimax
    )

    run_minimax_alpha_beta_btn = ttk.Button(
        text="Запустить MiniMax с альфа-бета отсечениями",
        command=callbacker.run_minimax_alpha_beta
    )

    create_new_tree_btn = ttk.Button(
        text="Сгенерировать новое дерево",
        command=callbacker.create_new_tree
    )

    generate_tree_values_btn = ttk.Button(
        text="Сгенерировать значения для проверки",
        command=callbacker.generate_new_values
    )

    combobox.pack(anchor=NW)
    direction.pack(anchor=NW)
    pass_value_btn.pack()
    run_minimax_btn.pack()
    run_minimax_alpha_beta_btn.pack()
    create_new_tree_btn.pack()
    generate_tree_values_btn.pack()
    root.mainloop()
