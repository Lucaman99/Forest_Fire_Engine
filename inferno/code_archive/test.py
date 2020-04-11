import inferno
from matplotlib import pyplot as plt
import math


#METHOD --> Pick the graph that has the greatest coorelation to the "average" graph

def cumulative_burn_sum(length, width, tree_density, iterations):
    max_length = 0
    final = []
    for n in range(0, iterations):
        g = inferno.CreateRandomGrid(length, width, tree_density, 0, 0)
        fire = inferno.spread_random_fire(g)
        maximum = 0
        for i in fire:
            if (i[3] > maximum):
                maximum = i[3]

        y = []
        add = 0
        for i in range(0, maximum+1):
            for j in fire:
                if (j[3] == i and j[2] == 1):
                    add = add + 1
            y.append(add)
        if (len(y) > max_length):
            max_length = len(y)
        final.append(y)

    tell = final

    append_arr = []

    for i in range (0, len(final)):
        counting = 0
        for n in range(0, max_length-len(final[i])):
            final[i].append(final[i][len(final[i])-1])
            counting = counting+1
        append_arr.append(counting)

    all = [sum(v) for v in zip(*list(final))]
    #This is the so-called "cost" list
    all_two = [a/iterations for a in all]

    cost = math.inf
    the_chosen_one = []
    for h in final:
        transport = 0
        for j in range(0, len(h)):
            transport = transport + abs(h[j]-all_two[j])
        if (transport < cost):
            cost = transport
            the_chosen_one = tell[final.index(h)][0:(len(h)-append_arr[final.index(h)])]

    the_chosen_one = all_two

    x = range(0, len(the_chosen_one))
    print(the_chosen_one)
    print(cost)
    plt.plot(x, the_chosen_one)
    plt.show()

cumulative_burn_sum(50, 50, 100, 10)
