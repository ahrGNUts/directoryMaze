# Copyright 2019 Patrick Strube

# directoryMaze is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.

# directoryMaze is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

# This software is provided AS-IS with no warranty.
# You should have received a copy of the GNU Public License V3 with this software, but if you didn't,
# you can find it here: https://www.gnu.org/licenses/gpl-3.0.en.html

import MazeBuilder

if __name__ == '__main__':
    to_hide_path = input("Enter the path to the file or directory you want to obfuscate: ")
    maze_root = input("Enter the path where you want the maze to start: ")
    root_name = input("Enter the name of the root folder node (Leave blank for random): ")
    layer_str = input("How many layers deep should the maze be? (Enter a number; max 20): ")

    try:
        val = int(layer_str)
        if val == 0 or val > 20:
            raise ValueError
    except ValueError:
        while not layer_str.isnumeric() or (layer_str.isnumeric() and (int(layer_str) < 1 or int(layer_str) > 20)):
            print("Invalid depth.")
            layer_str = input("How many layers deep should the maze be? (Enter a number; max 20): ")

    layers = int(layer_str)

    builder = MazeBuilder.MazeBuilder()
    builder.build()
