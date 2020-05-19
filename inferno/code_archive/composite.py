from cluster import *
from even import *
from base_grid import *


def CompositeGrid(*args):

    # Checks whether the grids being added together are compatible
    final_list = list(args)
    output = 0

    def join_squares():

        for k in range(1, len(final_list)):
            for n in range(0, len(final_list[0])):
                j = args[0][n]

                holding_arr = []
                for i in range(0, 2):
                    for g in range(0, 2):
                        holding_arr.append([[j[0][0] + r[0], j[0][1] + r[0]], i, g])
                    holding_arr.append([[j[0][0] + r[0], j[0][1] + r[0]], g])

                nice = False
                for v in holding_arr:
                    if (v in final_list[k]) and (v not in final_list[k]):
                        final_list[0] = final_list[0] + final_list[k]
                        nice = True
                        del final_list[k]
                        break
            if nice == True:
                break

    for b in range(0, len(final_list)):
        join_squares()

    if len(final_list) == 1:
        output = final_list[0]
    else:
        output = "Error, could not join"

    return output
