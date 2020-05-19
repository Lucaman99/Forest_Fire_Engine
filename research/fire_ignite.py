def spread_fire(grid_found):

    better_grid = []

    for h in range(0, len(grid_found)):
        if grid_found[h][1] == 1:
            better_grid.append(grid_found[h][0])

    random_num = random.randint(0, len(better_grid) - 1)

    trees_to_spread_from = [better_grid[random_num]]
    trees_are_here = [better_grid[random_num]]

    counter = 0

    while len(trees_to_spread_from) > 0:
        meantime = []
        for tr in trees_to_spread_from:
            movements = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for xc in range(0, 4):

                random_move = movements[xc]

                if [tr[0] + random_move[0], tr[1] + random_move[1]] in better_grid and [
                    tr[0] + random_move[0],
                    tr[1] + random_move[1],
                ] not in trees_are_here:
                    trees_are_here.append(
                        better_grid[
                            better_grid.index([tr[0] + random_move[0], tr[1] + random_move[1]])
                        ]
                    )
                    meantime.append(
                        better_grid[
                            better_grid.index([tr[0] + random_move[0], tr[1] + random_move[1]])
                        ]
                    )

        trees_to_spread_from = meantime
        counter = counter + 1

    return counter


final = []
for i in range(0, 100):
    sum = 0
    for h in range(0, 20):
        percentage = i / float(100)
        sum = sum + spread_fire(CreateClusterGrid(40, 40, 30, percentage, 1000))
    sum = sum / float(100)
    final.append(sum)
    print(str(i + 1) + " / 100 complete")


x = np.arange(0, 100, 1)
y = final
plt.title("The Spatial Density in a Forest vs. Iterations")
plt.xlabel("Iterations")
plt.ylabel("Forest Land Burned")
plt.plot(x, y)
plt.show()
