'''
---------------------------------------------------------------
SPARK v1.0 --> Generating grid-based forests for cellular-automata wildfire simulation backend
Spark is a software package built and distributed by Ignite Labs
---------------------------------------------------------------
'''

#Still need to fill in the header section

import random
import numpy
import math
import numpy as np
from matplotlib import pyplot as plt
from base_grid import *

def spread_fixed_fire(grid_found, fire_ignite):

    # List that stores all of the coordinates of trees
    better_grid = []
    co = []

    for h in range (0, len(grid_found)):
        #Appending to the end of each coordinate an extra entry 0, representing 'no fire'
        co.append(grid_found[0])
        grid_found[h].append(0)
        grid_found[h].append(0)
        if (grid_found[h][1] == 1):
            better_grid.append(grid_found[h][0])

    # This is the squares in which the fire is located and is presently burning
    if (fire_ignite in co):
        trees_to_spread_from = [fire_ignite]
        # All coordinates that have been burned
        trees_are_here = [fire_ignite]

    else:
        print("Invalid coordinate")

    counter = 0

    while (len(trees_to_spread_from) > 0):
        meantime = []
        for tr in trees_to_spread_from:
            movements = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for xc in range(0, 4):

                random_move = movements[xc]

                if ([tr[0]+random_move[0], tr[1]+random_move[1]] in better_grid and [tr[0]+random_move[0], tr[1]+random_move[1]] not in trees_are_here):

                    grid_found[grid_found.index([[tr[0]+random_move[0], tr[1]+random_move[1]], 1, 0, 0])][2] = 1
                    grid_found[grid_found.index([[tr[0]+random_move[0], tr[1]+random_move[1]], 1, 1, 0])][3] = counter+1

                    trees_are_here.append(better_grid[better_grid.index([tr[0]+random_move[0], tr[1]+random_move[1]])])
                    meantime.append(better_grid[better_grid.index([tr[0]+random_move[0], tr[1]+random_move[1]])])


        trees_to_spread_from = meantime
        counter = counter + 1

    return grid_found

def spread_random_fire(grid_found):

    # List that stores all of the coordinates of trees
    better_grid = []

    for h in range (0, len(grid_found)):
        #Appending to the end of each coordinate an extra entry 0, representing 'no fire'
        grid_found[h].append(0)
        grid_found[h].append(0)
        if (grid_found[h][1] == 1):
            better_grid.append(grid_found[h][0])

    # Some random index within better_grid
    random_num = random.randint(0, len(better_grid)-1)

    # This is the squares in which the fire is located and is presently burning
    trees_to_spread_from = [better_grid[random_num]]
    # All coordinates that have been burned
    trees_are_here = [better_grid[random_num]]

    counter = 0

    while (len(trees_to_spread_from) > 0):
        meantime = []
        for tr in trees_to_spread_from:
            movements = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for xc in range(0, 4):

                random_move = movements[xc]

                if ([tr[0]+random_move[0], tr[1]+random_move[1]] in better_grid and [tr[0]+random_move[0], tr[1]+random_move[1]] not in trees_are_here):

                    grid_found[grid_found.index([[tr[0]+random_move[0], tr[1]+random_move[1]], 1, 0, 0])][2] = 1
                    grid_found[grid_found.index([[tr[0]+random_move[0], tr[1]+random_move[1]], 1, 1, 0])][3] = counter+1

                    trees_are_here.append(better_grid[better_grid.index([tr[0]+random_move[0], tr[1]+random_move[1]])])
                    meantime.append(better_grid[better_grid.index([tr[0]+random_move[0], tr[1]+random_move[1]])])


        trees_to_spread_from = meantime
        '''
        print(len(trees_are_here))
        '''
        counter = counter + 1

    return grid_found
