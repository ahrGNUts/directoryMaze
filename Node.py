class Node:
    def __init__(self, path, name):
        self.name = name
        self.path = path
        self.children = []

    def append(self, child):
        self.children.append(child)
