import random
import time
import numpy as np
from matplotlib import pyplot as plt

#Initialize variables within the script
#Grid size is 100 X 100

import random
#Grid size is 100X100

def measure(tree_density):

    g = ["placeholder", "placeholder2"]
    h = []

    fire_movement = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    matrix = []
    the_master = []
    operator = []


    def grid_init(density):
      a = []
      k = density
      while (k > 0):
        b = 0
        one = [random.randrange(0, 10, 1), random.randrange(0, 10, 1), "tree"]
        for v in a:
          if (v != one):
            b = b + 1
        if (b == len(a)):
          a.append(one)
          k = k - 1
      return a

    fire_start = grid_init(tree_density)

    counter = []

    if (fire_start.count([2, 3, "tree"]) == 0):
      fire_start.pop()
      fire_start.append([2, 3, "tree"])


    firespark = [2, 3]
    fire_start[fire_start.index([2, 3, "tree"])] = [2, 3, "burn"]
    h.append([2, 3, "burn"])

    for v in fire_movement:
      if (fire_start.count([firespark[0] + v[0], firespark[1] + v[1], "tree"]) > 0):
        fire_start[fire_start.index([firespark[0] + v[0], firespark[1] + v[1], "tree"])] = [firespark[0] + v[0], firespark[1] + v[1], "burn"]
        h.append([firespark[0] + v[0], firespark[1] + v[1], "burn"])


    while (g[len(g) - 1] != g[len(g) - 2]):
      base = len(h)
      g.append(str(fire_start).count("burn"))
      place = len(h)
      for x in range (0, place):
        for v in fire_movement:
          if (fire_start.count([h[x][0] + v[0], h[x][1] + v[1], "tree"]) > 0):
            fire_start[fire_start.index([h[x][0] + v[0], h[x][1] + v[1], "tree"])] = [h[x][0] + v[0], h[x][1] + v[1], "burn"]
            h.append([h[x][0] + v[0], h[x][1] + v[1], "burn"])
      counter.append(len(h))
      if (base == len(h)):
        break;


    k = []

    for n in g:
      if (k.count(n) == 0):
        k.append(n)

    if (len(h) > 5):
      j = len(counter)+1
    elif (len(h) > 1):
      j = 1
    else:
      j = 0

    return j

final = []
for y in range (1, 100):
    a = 0
    for x in range (0, 50):
        a = a + measure(y)
    final.append(float(a)/50)

print(final)

x = np.arange(1, 100, 1)
y = final
plt.title("The Spatial Density in a Forest vs. Iterations")
plt.xlabel("Spatial Density")
plt.ylabel("Iterations")
plt.plot(x, y)
plt.show()
