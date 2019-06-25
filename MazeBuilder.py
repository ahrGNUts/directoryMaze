import os
import random
import string
import Node
import json
from shutil import rmtree, move
DEFAULT_NAME_LEN = 7

class MazeBuilder:

    def __init__(self, to_hide_path, maze_root_path, root_node_name, layers, num_branches):
        self.to_hide_path = to_hide_path
        self.to_hide_filename = self.__parse_payload_filename(to_hide_path)
        self.maze_root_path = self.__set_root_path(maze_root_path)
        self.root_node_name = self.__set_root_node_name(root_node_name)
        self.layers = layers
        self.num_branches = num_branches
        self.debug_mode = True
        self.endpoint_path = self.maze_root_path + '/' + self.root_node_name + '/'

    def build(self):
        # cleanup previous dir tree
        if self.debug_mode:
            self.__remove_prev_root()
        # create root node
        root_node = Node.Node(self.maze_root_path, self.root_node_name)
        os.mkdir(self.maze_root_path + '/' + self.root_node_name)
        if self.debug_mode:
            self.__set_cleanup_info()
        current_depth = 1
        # todo: progress bar or spinner while the tree is being created
        # recursively create directory tree
        self.__create_branches(root_node.path, root_node, current_depth)
        # randomly walk through tree to find random end node (sets self.endpoint_path)
        self.__find_end_node_path(root_node)
        # move file to end node
        self.__move_payload()

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
        if depth < self.layers:
            for i in range(self.num_branches):
                name = self.__verify_dir_name(self.__generate_dir_name(DEFAULT_NAME_LEN), path)
                p = path + '/' + name
                os.mkdir(p)
                node = Node.Node(path, name)
                parent.append(node)
                self.__create_branches(p, node, depth+1)

    def __verify_dir_name(self, name, path):
        while name in os.listdir(path):
            name = self.__generate_dir_name(DEFAULT_NAME_LEN)
        return name

    def __set_cleanup_info(self):
        # todo: set info for old map file
        try:
            with open('debuginfo.json', 'w') as file:
                json.dump({"prevRoot": self.maze_root_path + '/' + self.root_node_name}, file)
        except FileNotFoundError:
            with open('debuginfo.json', 'a') as file:
                json.dump({"prevRoot": self.maze_root_path + '/' + self.root_node_name}, file)

    def __remove_prev_root(self):
        try:
            with open('debuginfo.json', 'r') as file:
                data = json.load(file)
                rmtree(data['prevRoot'])
        except FileNotFoundError:
            return
    # todo: general cleanup method that acts as a caller for the cleanup methods that actually clean
    # todo: cleanup method that deletes the old map file
    # todo: maybe a testing method that dynamically creates the dirs and test files
    def __find_end_node_path(self, head):
        if len(head.children) > 0:
            rnd = random.randrange(0, len(head.children))
            self.endpoint_path += head.children[rnd].name + '/'
            self.__find_end_node_path(head.children[rnd])

    def __parse_payload_filename(self, path):
        # if we split a path of a directory that has a trailing slash, the last element will be an empty string
        # this will make sure we don't get a blank filename
        if not path.split('/')[-1]:
            return path.split('/')[-2]
        return path.split('/')[-1]

    def __move_payload(self):
        # todo: error handling
        move(self.to_hide_path, self.endpoint_path + self.to_hide_filename)

    def generate_mapfile(self):
        filename = self.maze_root_path + '/' + self.root_node_name + '_map.txt'
        lines = [
            "The path to your file is as follows:\r\n",
            self.endpoint_path + '/' + self.to_hide_filename
        ]

        with open(filename, 'w+') as file:
            file.writelines(lines)

    def completion_message(self):
        print('Done.')
        print("A file containing the path to your file has been created at:")
        print(self.maze_root_path + '/' + self.root_node_name + '_map.txt')
        print("")
        print("The path in the file is: ")
        print(self.endpoint_path + self.to_hide_filename)
