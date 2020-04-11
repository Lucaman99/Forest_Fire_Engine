'''
SPARK v1.0 --> Generating grid-based forests for cellular-automata wildfire simulation backend
Spark is a software package built and distributed by Ignite Labs developed by Jack Ceroni and Abdullah Hadi
---------------------------------------------------------------
At the moment, grids and composite grids must be rectangular,
but support for irregularly shaped grids/composite grids will be
introduced in the next version of Spark
---------------------------------------------------------------
sparklib.CreateFixedGrid('width', 'length', 'coordinate_file')
--> Creates a grid with fixed tree coordinates (read from a file)
sparklib.CreateRandomGrid('width', 'length', 'tree_density')
--> Creates a grid with randomly placed trees, but with a fixed tree density (unless the 'random') keyword is passed
sparklib.CreateClusterGrid('width', 'length', 'meanclustersize', 'frac_allowed' 'tree_density')
--> Creates a grid of trees with patches that clustered close together (NEW FEATURE)
sparklib.CreateEvenGrid('width', 'length', 'probradius', 'tree_density')
--> Creates a grid that distributes trees very evenly and tries to avoid clusters
sparklib.CreateCompositeGrid('width', 'length', arg1.coordinate('top_left'), ..., argn.coordinate('top_left'))
--> Creates a grid that involved a mixture of different grid types (previously defined methods)
---------------------------------------------------------------
Output of all functions should be an array with coordinates [ [ [0, 0], 0], [ [0, 1], 1 ], ..., [ [n, n], 0 ] ]
Given [[0, 0], 0], the two values in the first bracket represents the coordinates of the tree (x, y), the third
value can take on the numbers 0, 1, or 2.
0 indicates no tree in the given coordinate, 1 indicates that a tree exists in that coordinate, and 2 indicates
 that there was a tree in that coordinate but it was burned down after an iteration of the simulation
'''

#FUTURE FUNCTIONALITY: CHANGE THE FUNCTIONS TO CLASSES

import random
import numpy
import math
import numpy as np
from matplotlib import pyplot as plt

#General function that can be called to generate an empty forest grid

#Grid looks likes this --> [ [ [0, 0], 0], [ [0, 1], 0 ], ..., [ [n, n], 0 ] ]

def generate_coordinates(width, length, starting_coordinate_width, starting_coordinate_length):
    grid_array = []
    for i in range(starting_coordinate_width, width+starting_coordinate_width):
        for j in range(starting_coordinate_length, length+starting_coordinate_length):
            grid_array.append([i, j])
    return grid_array

def generate_grid(width, length, starting_coordinate_width, starting_coordinate_length):
    grid_array = []
    for i in range(starting_coordinate_width, width+starting_coordinate_width):
        for j in range(starting_coordinate_length, length+starting_coordinate_length):
            grid_array.append([[i, j], 0])
    return grid_array

def generate_prob_grid(width, length, starting_coordinate_width, starting_coordinate_length):
    grid_array = []
    for i in range(starting_coordinate_width, width+starting_coordinate_width):
        for j in range(starting_coordinate_length, length+starting_coordinate_length):
            grid_array.append([[i, j], 0, 0])
    return grid_array

#Creates a random grid with randomly dispersed trees
# Creates a random grid with randomly dispersed trees
def CreateRandomGrid(width, length, tree_density, starting_coordinate_width, starting_coordinate_length):
    counter = 0
    grid = generate_grid(width, length, starting_coordinate_width, starting_coordinate_length)  # Initialize grid
    while (counter < tree_density):
        num = random.randint(0, len(grid) - 1)  # Chooses a random coordinate to place the tree
        if (grid[num][1] == 0):  # If the coordinate is empty place a tree
            grid[num][1] = 1
            counter += 1
    return grid  # Generates grid


# Coordinates in file in form of [ [0, 1], [9, 18], ..., [x, y] ]

def CreateFixedGrid(width, length, coordinate_file, starting_coordinate_width, starting_coordinate_length):
    grid = generate_grid(width, length, starting_coordinate_width, starting_coordinate_length)
    filename = coordinate_file
    f = open(filename, 'r')
    data = f.read()
    data = data.replace(', ', ',').split(' ')
    a = []
    for x in data:
        x = eval(x)
        a.append(x)
    for x in a:
        for i in grid:
            if (x in i):
                i[1] = 1
    return grid

#FUTURE FUNCTIONALITY: Create chain-links between the different clusters, add in function with the prob_grid for searching for spots where clusters may work
