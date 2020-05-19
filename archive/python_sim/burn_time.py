import random
import time
import numpy as np
from matplotlib import pyplot as plt

# Initialize variables within the script
# Grid size is 100 X 100

import random

# Grid size is 100X100


def measure(tree_density):

    g = []

    fire_movement = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    matrix = []
    the_master = []
    operator = []

    def grid_init(density):
        a = []
        k = density
        while k > 0:
            b = 0
            one = [random.randrange(0, 10, 1), random.randrange(0, 10, 1), "tree"]
            for v in a:
                if v != one:
                    b = b + 1
            if b == len(a):
                a.append(one)
                k = k - 1
        return a

    fire_start = grid_init(tree_density)

    if fire_start.count([2, 3, "tree"]) == 0:
        fire_start.pop()
        fire_start.append([2, 3, "tree"])

    firespark = [2, 3]
    fire_start[fire_start.index([2, 3, "tree"])] = [2, 3, "burn"]

    for v in fire_movement:
        if fire_start.count([firespark[0] + v[0], firespark[1] + v[1], "tree"]) > 0:
            fire_start[fire_start.index([firespark[0] + v[0], firespark[1] + v[1], "tree"])] = [
                firespark[0] + v[0],
                firespark[1] + v[1],
                "burn",
            ]

    for i in range(0, 100):
        g.append(str(fire_start).count("burn"))
        for x in fire_start:
            if x[2] == "burn":
                for v in fire_movement:
                    if fire_start.count([x[0] + v[0], x[1] + v[1], "tree"]) > 0:
                        fire_start[fire_start.index([x[0] + v[0], x[1] + v[1], "tree"])] = [
                            x[0] + v[0],
                            x[1] + v[1],
                            "burn",
                        ]

    k = []

    for n in g:
        if k.count(n) == 0:
            k.append(n)

    return len(k) + 1


final = []
for y in range(1, 100):
    a = 0
    for x in range(0, 50):
        a = a + measure(y)
    final.append(a / 50)

print(final)

x = np.arange(1, 100, 1)
y = final
plt.title("The Spatial Density in a Forest vs. Iterations")
plt.xlabel("Iterations")
plt.ylabel("Forest Land Burned")
plt.plot(x, y)
plt.show()
