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


# for validating numeric input from the user
def get_valid_number(prompt, max_limit):
    input_str = input(prompt)

    try:
        val = int(input_str)
        if val == 0 or val > max_limit:
            raise ValueError
    except ValueError:
        while not input_str.isnumeric() or (input_str.isnumeric() and (int(input_str) < 1 or int(input_str) > max_limit)):
            print("Value out of range. Please enter a value greater than 0 and no more than " + str(max_limit))
            input_str = input(prompt)

    return int(input_str)


if __name__ == '__main__':
    to_hide_path = input("Enter the path to the file or directory you want to obfuscate: ")
    maze_root_path = input("Enter the path where you want the maze to start: ")
    root_node_name = input("Enter the name of the root folder node (Leave blank for random): ")
    layers = get_valid_number("How many layers deep should the maze be? (Enter a number; max 20): ", 20)
    num_branches = get_valid_number("How many branches per node should there be? (Enter a number; max 7): ", 7)

    builder = MazeBuilder.MazeBuilder(to_hide_path, maze_root_path, root_node_name, layers, num_branches)
    builder.build()


