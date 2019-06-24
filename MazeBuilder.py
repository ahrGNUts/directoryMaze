import os
import random
import string
import Node
DEFAULT_NAME_LEN = 7


class MazeBuilder:

    def __init__(self, to_hide_path, maze_root_path, root_node_name, layers, num_branches):
        self.to_hide_path = to_hide_path
        self.maze_root_path = self.__set_root_path(maze_root_path)
        self.root_node_name = self.__set_root_node_name(root_node_name)
        self.layers = layers
        self.num_branches = num_branches

    def build(self):
        # create root node
        root_node = Node.Node(self.maze_root_path, self.root_node_name)
        os.mkdir(self.maze_root_path + '/' + self.root_node_name)
        current_depth = 1
        # recursively create directory tree
        self.__create_branches(root_node.path, root_node, current_depth)

    def __set_root_path(self, maze_root_path):
        if maze_root_path == "":
            return os.getcwd()

        return maze_root_path

    def __set_root_node_name(self, root_node_name):
        if root_node_name == "":
            return self.__generate_dir_name(DEFAULT_NAME_LEN)

        return root_node_name

    def __generate_dir_name(self, name_length):
        char_pool = string.ascii_lowercase + string.digits
        return ''.join(random.choice(char_pool) for i in range(name_length))

    def __create_branches(self, path, parent, depth):
        if depth <= self.layers:
            for i in range(self.num_branches):
                name = self.__generate_dir_name(DEFAULT_NAME_LEN)
                # todo: if name exists already in current dir, generate new one
                p = path + '/' + name
                os.mkdir(p)
                node = Node.Node(path, name)
                parent.append(node)
                self.__create_branches(p, node, depth+1)
