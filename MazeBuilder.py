import os
class MazeBuilder:

    def __init__(self, to_hide_path, maze_root_path, root_node_name, layers, num_branches):
        self.to_hide_path = to_hide_path
        self.root_node_name = root_node_name
        self.maze_root_path = self.__set_root_path(maze_root_path)
        self.layers = layers
        self.num_branches = num_branches

    def build(self):
        pass

    def __set_root_path(self, maze_root_path):
        if maze_root_path == "":
            return os.getcwd()

        return maze_root_path
