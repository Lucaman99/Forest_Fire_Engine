'''
SPARK v1.0 --> Generating grid-based forests for cellular-automata wildfire simulation backend

Spark is a software package built and distributed by Ignite Labs

Operations that can be called in order to generate a forest:

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

import random
import numpy

#General function that can be called to generate an empty forest grid

#Grid looks likes this --> [ [ [0, 0], 0], [ [0, 1], 0 ], ..., [ [n, n], 0 ] ]

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

#Creates a random grid with randomly dispersed trees
# Creates a random grid with randomly dispersed trees
def CreateRandomGrid(width, length, tree_density):
    counter = 0
    grid = generate_grid(width, length)  # Initialize grid
    while (counter < tree_density):
        num = random.randint(0, len(grid) - 1)  # Chooses a random coordinate to place the tree
        if (grid[num][1] == 0):  # If the coordinate is empty place a tree
            grid[num][1] = 1
            counter += 1
    return grid  # Generates grid


# Coordinates in file in form of [ [0, 1], [9, 18], ..., [x, y] ]

def CreateFixedGrid(width, length, coordinate_file):
    grid = generate_grid(width, length)
    file = open(coordinate_file, "r") # BUG: Coordinate file is a string
    converted_file = list(file)
    for x in converted_file:
        for i in grid:
            if (x in i):
                i[1] == 1
    return grid



def CreateClusterGrid(width, length, meanclustersize, frac_allowed, tree_density):
    #Generates an empty grid forest
    grid = generate_grid(width, length)

    #Defines how trees will be clustered on the grid
    num_trees_for_cluster = frac_allowed*tree_density
    num_trees_for_connection = (1-frac_allowed)*tree_density

    #Define the tree clusters
    cluster = []
    while (num_trees_for_cluster >= 5):
        num_trees_for_cluster = num_trees_for_cluster - meanclustersize
        cluster.append(meanclustersize)
    for i in range(num_trees_for_cluster):
        cluster[i] += 1

    #Place the tree clusters on the grid
    cluster_count = len(cluster)
    for i in (cluster_count):
        pass

# Uses a calculated probability radius

#IN THE FUTURE, WE WILL CONSIDER USING THE OUTWARD STAGGERED SUM SQUARED METHOD OF DATA-DISTRIBUTION (WEIGHTED RANDOM CHOICE BASED ON AVERAGE TAXICAB METRIC FROM TREE)

# [GridObject, [x, y], width, length]

'''

UNDER CONSTRUCTION!

Class CreateCompositeGrid:
    def __init__(self, *args)
    generate_grid(width, length)

'''
