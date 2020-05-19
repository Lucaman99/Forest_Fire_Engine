import random
import numpy as np

# THIS MODULE IS HIGHLY EXPERIMENTAL, DOES NOT CURRENTLY WORK FOR LARGE GRID SIZES

# General function that can be called to generate an empty forest grid

# Grid looks likes this --> [ [ [0, 0], 0], [ [0, 1], 0 ], ..., [ [n, n], 0 ] ]


def generate_coordinates(width, length):
    grid_array = []
    for i in range(0, width):
        for j in range(0, length):
            grid_array.append([i, j])
    return grid_array


def generate_grid(width, length):
    grid_array = []
    for i in range(0, width):
        for j in range(0, length):
            grid_array.append([[i, j], 0])
    return grid_array


def generate_prob_grid(width, length):
    grid_array = []
    for i in range(0, width):
        for j in range(0, length):
            grid_array.append([[i, j], 0, 0])
    return grid_array


def CreateEvenGrid(width, length, prob_iter, tree_density):
    trees = tree_density
    grid = generate_grid(width, length)
    prob_grid = generate_prob_grid(width, length)
    co = generate_coordinates(width, length)

    trees_are_here = []

    # How much the probability increases as the distance from a tree increases
    # In the grid-based simulation, the taxicab metric is used: d(x, y) = |x_2 - x_1| + |y_2 - y_1|

    # Place the first tree at some random location
    num = random.randint(0, len(grid) - 1)

    counter = 0

    while trees > 0:

        # Places a tree wherever the random function selected it
        grid[num][1] = 1
        prob_grid[num][1] = 1

        trees_are_here.append(grid[num][0])

        # Calculate maximum taxicab metric distance from random point to any other point on grid
        distance = max(abs(grid[num][0][0] - 0), abs(grid[num][0][0] - width)) + max(
            abs(grid[num][0][1] - 0), abs(grid[num][0][1] - length)
        )

        # Calculate corresponding probabilities on the grid

        # Correspond to all possible movements that can be made from one grid square to another
        movements = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # All squares which the cellular automata is spreading from
        all = [grid[num][0]]
        all_squares = [grid[num][0]]

        for j in range(distance):
            storage = []
            for i in movements:
                for g in all_squares:
                    if (
                        g[0] + i[0] < width
                        and g[0] + i[0] >= 0
                        and g[1] + i[1] < length
                        and g[1] + i[1] >= 0
                    ):

                        if [g[0] + i[0], g[1] + i[1]] not in all_squares and [
                            g[0] + i[0],
                            g[1] + i[1],
                        ] not in all:
                            storage.append([g[0] + i[0], g[1] + i[1]])
                        all.append([g[0] + i[0], g[1] + i[1]])

                        # Checks whether the square is occupied by a tree
                        if grid[co.index(g)][1] != 1:
                            if prob_grid[co.index(g)][2] == 0:
                                # If there is no distance value assigned to the coordinate yet, add it in
                                prob_grid[co.index(g)][2] = j + 1
                            else:
                                # Add the new distance value to the coordinate
                                prob_grid[co.index(g)][2] = (
                                    (prob_grid[co.index(g)][2] * counter) + j + 1
                                ) / (counter + 1)
            # all_squares = storage

        # This happens once all the distances have been distributed on the grid
        trees = trees - 1
        print(trees)

        landing = False
        toggle = False

        # print(trees_are_here)

        while toggle == False:
            while landing == False:
                for i in range(1, distance + 1):
                    if np.random.choice([True, False], 1, [prob_iter, (1 - prob_iter)]):
                        landing = i

            shuffled_array = prob_grid
            random.shuffle(shuffled_array)
            for h in range(0, len(shuffled_array)):
                if shuffled_array[h][2] == landing and shuffled_array[h][0] not in trees_are_here:
                    num = prob_grid.index(shuffled_array[h])
                    toggle = True
                    break
            landing = False
    return grid
