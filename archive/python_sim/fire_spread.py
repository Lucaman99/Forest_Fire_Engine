import random
import time
import numpy as np
from matplotlib import pyplot as plt

# Initialize variables within the script
# Grid size is 100 X 100

import random

# Grid size is 100X100


def measure(tree_density):

    fire_movement = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    matrix = []
    the_master = []
    operator = []

    def grid_init(density):
        a = []
        k = density
        while k > 0:
            b = 0
            one = [random.randrange(0, 10, 1), random.randrange(0, 10, 1)]
            for v in a:
                if v != one:
                    b = b + 1
            if b == len(a):
                a.append(one)
                k = k - 1
        return a

    fire_start = grid_init(tree_density)

    for i in range(0, 10):
        row = []
        for j in range(0, 10):
            if fire_start.count([i, j]) > 0:
                row.append("tree")
            else:
                row.append("none")
        matrix.append(row)

    def initial():

        init_fire_one = random.randrange(0, len(fire_start), 1)
        start = fire_start[init_fire_one]
        return start

    firespark = [2, 3]

    the_master.append(firespark)

    matrix[firespark[0]][firespark[1]] = "burn"

    for v in fire_movement:
        if firespark[0] + v[0] < 10 and firespark[1] + v[1] < 10:
            if matrix[firespark[0] + v[0]][firespark[1] + v[1]] == "tree":
                if firespark[0] + v[0] > -1 and firespark[1] + v[1] > -1:
                    matrix[firespark[0] + v[0]][firespark[1] + v[1]] = "burn"
                    the_master.append([firespark[0] + v[0], firespark[1] + v[1]])

    if len(the_master) > 1:
        place = []
        h = 0
        for u in range(0, 100):
            jl = len(the_master)
            for i in range(0, jl):
                for v in fire_movement:
                    if the_master[i][0] + v[0] < 10 and the_master[i][1] + v[1] < 10:
                        if matrix[the_master[i][0] + v[0]][the_master[i][1] + v[1]] == "tree":
                            if the_master[i][0] + v[0] > -1 and the_master[i][1] + v[1] > -1:
                                matrix[the_master[i][0] + v[0]][the_master[i][1] + v[1]] = "burn"
                                the_master.append(
                                    [the_master[i][0] + v[0], the_master[i][1] + v[1]]
                                )
                                operator.append(h)
                h = h + 1

    store = []

    for n in operator:
        if store.count(n) == 0:
            store.append(n)

    return len(the_master)


final = []
for y in range(1, 100):
    a = 0
    for x in range(0, 50):
        a = a + measure(y)
    final.append(a / 50)

print(final)

x = np.arange(1, 100, 1)
y = final
plt.title("The Spatial Density in a Forest vs. The Amount of Forest Land Burned")
plt.xlabel("Spatial Density")
plt.ylabel("Forest Land Burned")
plt.plot(x, y)
plt.show()
