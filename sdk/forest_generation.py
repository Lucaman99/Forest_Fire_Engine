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

#FUTURE FUNCTIONALITY: CHANGE THE FUNCTIONS TO CLASSES

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

def CreateClusterGrid(width, length, meanclustersize, frac_allowed, tree_density):
    #Generates an empty grid forest
    grid = generate_grid(width, length)
    co = generate_coordinates(width, length)

    #Defines how trees will be clustered on the grid
    num_trees_for_cluster = math.floor(frac_allowed*tree_density)
    num_trees_for_connection = math.floor((1-frac_allowed)*tree_density)

    #Define the tree clusters
    cluster = []
    while (num_trees_for_cluster >= meanclustersize):
        num_trees_for_cluster = num_trees_for_cluster - meanclustersize
        cluster.append(meanclustersize)
    for i in range(num_trees_for_cluster):
        cluster[i] += 1

    random_placement = False
    truth = False

    #Place the tree clusters on the grid
    cluster_count = len(cluster)

    for cu, i in enumerate(cluster):
        h = False

        while (h == False):
            random_placement = random.randint(0, len(grid)-1)
            if (grid[random_placement][1] == 0):
                grid[random_placement][1] = 1
                h = True

        trees_to_spread_from = [grid[random_placement][0]]

        holding = trees_to_spread_from
        counter = 0

        trees_are_here = [grid[random_placement][0]]

        while (len(trees_are_here) < i):


            for tr in trees_to_spread_from:

                meantime = []

                for xc in range(0, 4):

                    movements = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    random_move = random.choice(movements)
                    if ([tr[0]+random_move[0], tr[1]+random_move[1]] in co):
                        cor = co.index([tr[0]+random_move[0], tr[1]+random_move[1]])

                        if (grid[cor][1] == 0 and len(trees_are_here) < i):
                            grid[cor][1] = 1
                            trees_are_here.append(grid[cor][0])
                            counter = counter + 1
                            del movements[movements.index(random_move)]
                            meantime.append(grid[cor][0])

            if (meantime == []):
                num_trees_for_connection = num_trees_for_connection + i - (counter+1)
                break

    no_tree = []
    for bn in grid:
        if (bn[1] == 0):
            no_tree.append(bn)

    counter2 = 0
    while (counter2 < num_trees_for_connection):
        num = random.randint(0, len(no_tree) - 1)  # Chooses a random coordinate to place the tree
        if (grid[grid.index(no_tree[num])][1] == 0):  # If the coordinate is empty place a tree
            grid[grid.index(no_tree[num])][1] = 1
            counter2 += 1

    return grid








    #Scatter the rest of the trees randomlly


# Uses a calculated probability radius

#IN THE FUTURE, WE WILL CONSIDER USING THE OUTWARD STAGGERED SUM SQUARED METHOD OF DATA-DISTRIBUTION (WEIGHTED RANDOM CHOICE BASED ON AVERAGE TAXICAB METRIC FROM TREE)

# [GridObject, [x, y], width, length]

def CreateEvenGrid(width, length, prob_iter, tree_density):
    trees = tree_density
    grid = generate_grid(width, length)
    prob_grid = generate_prob_grid(width, length)
    co = generate_coordinates(width, length)

    trees_are_here = []

    #How much the probability increases as the distance from a tree increases
    #In the grid-based simulation, the taxicab metric is used: d(x, y) = |x_2 - x_1| + |y_2 - y_1|

    #Place the first tree at some random location
    num = random.randint(0, len(grid)-1)

    counter = 0

    while (trees > 0):
        # Places a tree wherever the random function selected it
        grid[num][1] = 1
        prob_grid[num][1] = 1
        #Calculate maximum taxicab metric distance from random point to any other point on grid
        #distance = max(abs(grid[num][0][0]-0), abs(grid[num][0][0]-width)) + max(abs(grid[num][0][1]-0), abs(grid[num][0][1]-length))
        trees_are_here.append(grid[num][0])

        max_value = 0

        for g in prob_grid:
            taxicab = abs(grid[num][0][0]-g[0][0])+abs(grid[num][0][1]-g[0][1])
        #Checks whether the square is occupied by a tree
            if (g[1] != 1):
                if (g[2] == 0):
                    # If there is no distance value assigned to the coordinate yet, add it in
                    g[2] = taxicab
                else:
                    # Add the new distance value to the coordinate
                    g[2] = math.floor(((g[2]*(tree_density-trees))+taxicab)/((tree_density-trees)+1))

                if (g[2] > max_value):
                    max_value = math.floor(g[2])

        #all_squares = storage
        #This happens once all the distances have been distributed on the grid
        trees = trees - 1
        #print(trees)

        landing = False
        toggle = False

        distance = max_value

        while (toggle == False):
            counting_value = 0
            while (landing == False):
                for i in range(0, int(math.floor(distance))):
                    val = distance-i
                    if (np.random.choice([True, False], 1, [prob_iter, (1-prob_iter)])):
                        landing = val
                        break


            shuffled_array = []
            for n in prob_grid:
                shuffled_array.append(n)
            random.shuffle(shuffled_array)
            for h in range (0, len(shuffled_array)):
                if (shuffled_array[h][2] == landing and shuffled_array[h][0] not in trees_are_here and shuffled_array[h][1] != 1):
                    num = prob_grid.index(shuffled_array[h])
                    toggle = True
                    break;
            landing = False

    return grid

'''

UNDER CONSTRUCTION!

Class CreateCompositeGrid:
    def __init__(self, *args)
    generate_grid(width, length)

'''
