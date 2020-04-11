import random
import math
import numpy as np
import copy

class Density_State:

    def __init__(self, density):
        self.density = density
    
    def execute(self, input_graph, time):

        number = []
        if (time == 0):

            s = input_graph.graph.vertex_index_set
            selection = copy.deepcopy(s)
            x = 0

            total_number = math.floor(len(selection)*self.density)
            for i in range(0, int(total_number)):
                r = int(random.randint(0, len(input_graph.graph.vertex_set)-x-1))
                chosen = selection[r]
                for i in input_graph.graph.vertex_set:
                    if (i.v_index == chosen):
                        i.state = 1
                        number.append(i)
                del selection[r]
                x = x + 1
        
        return number

    
