import os
import random
import string


class MazeBuilder:

    def __init__(self, to_hide_path, maze_root_path, root_node_name, layers, num_branches):
        self.to_hide_path = to_hide_path
        self.maze_root_path = self.__set_root_path(maze_root_path)
        self.root_node_name = self.__set_root_node_name(root_node_name)
        self.layers = layers
        self.num_branches = num_branches

    def build(self):
        pass

    def __set_root_path(self, maze_root_path):
        if maze_root_path == "":
            return os.getcwd()

        return maze_root_path

    def __set_root_node_name(self, root_node_name):
        if root_node_name == "":
            return self.__generate_dir_name(7)

        return root_node_name

    def __generate_dir_name(self, name_length):
        char_pool = string.ascii_lowercase + string.digits
        return ''.join(random.choice(char_pool) for i in range(name_length))
