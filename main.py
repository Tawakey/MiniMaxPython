from frames import Root
from frames import GraphFrame
from graph import GameTree


WIDTH, HEIGHT = 1200, 800


if __name__ == "__main__":
    root = Root(WIDTH, HEIGHT)
    game_tree = GameTree()
    game_tree.generate_tree(5)
    frame = GraphFrame(WIDTH, HEIGHT, root)
    frame.draw_game_tree(game_tree)

    root.mainloop()
