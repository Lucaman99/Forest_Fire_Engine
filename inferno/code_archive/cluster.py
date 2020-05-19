from base_grid import *


def CreateClusterGrid(
    width,
    length,
    meanclustersize,
    frac_allowed,
    tree_density,
    starting_coordinate_width,
    starting_coordinate_length,
):
    # Generates an empty grid forest
    grid = generate_grid(width, length, starting_coordinate_width, starting_coordinate_length)
    co = generate_coordinates(width, length, starting_coordinate_width, starting_coordinate_length)

    # Defines how trees will be clustered on the grid
    num_trees_for_cluster = int(math.floor(frac_allowed * tree_density))
    num_trees_for_connection = int(math.floor((1 - frac_allowed) * tree_density))

    # Define the tree clusters
    cluster = []
    while num_trees_for_cluster >= meanclustersize:
        num_trees_for_cluster = num_trees_for_cluster - meanclustersize
        cluster.append(meanclustersize)
    if len(cluster) > 0:
        while num_trees_for_cluster > 0:
            for i in range(len(cluster)):
                cluster[i] += 1
                num_trees_for_cluster -= 1
    else:
        num_trees_for_connection += num_trees_for_cluster

    random_placement = False
    truth = False

    # Place the tree clusters on the grid
    cluster_count = len(cluster)

    for cu, i in enumerate(cluster):
        h = False

        while h == False:
            random_placement = random.randint(0, len(grid) - 1)
            if grid[random_placement][1] == 0:
                grid[random_placement][1] = 1
                h = True

        trees_to_spread_from = [grid[random_placement][0]]

        holding = trees_to_spread_from
        counter = 0

        trees_are_here = [grid[random_placement][0]]

        while len(trees_are_here) < i:

            meantime = []

            for tr in trees_to_spread_from:
                movements = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for xc in range(0, 4):

                    random_move = random.choice(movements)
                    if [tr[0] + random_move[0], tr[1] + random_move[1]] in co:
                        cor = co.index([tr[0] + random_move[0], tr[1] + random_move[1]])

                        if grid[cor][1] == 0 and len(trees_are_here) < i:
                            grid[cor][1] = 1
                            trees_are_here.append(grid[cor][0])
                            counter = counter + 1
                            del movements[movements.index(random_move)]
                            meantime.append(grid[cor][0])

            trees_to_spread_from = meantime

            if meantime == []:
                num_trees_for_connection = num_trees_for_connection + i - (counter + 1)
                break

    no_tree = []
    for bn in grid:
        if bn[1] == 0:
            no_tree.append(bn)

    counter2 = 0
    while counter2 < num_trees_for_connection:
        num = random.randint(0, len(no_tree) - 1)  # Chooses a random coordinate to place the tree
        if grid[grid.index(no_tree[num])][1] == 0:  # If the coordinate is empty place a tree
            grid[grid.index(no_tree[num])][1] = 1
            counter2 += 1

    return grid
