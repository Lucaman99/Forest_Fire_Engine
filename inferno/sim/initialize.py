import random
import math
import numpy as np


class Random_Init_Number:
    def __init__(self, number):
        self.number = number

    def execute(self, input_graph):

        num = len(input_graph.vertex_set) - 1
        final = []
        for i in range(0, self.number):
            h = False
            while h == False:
                r = random.randint(0, num)
                if input_graph.vertex_set[r].state == 1 and input_graph.vertex_set[r].burn == 0:
                    h = True
                    input_graph.vertex_set[r].burn = 1
                    final.append(input_graph.vertex_set[r])

        return final
