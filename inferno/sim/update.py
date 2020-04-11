import numpy
import random
import math

# For these simulators, the idea is that they will take one time-step of the algorithm

# A cellular-automation update function that spreads to Von Neumann neighbours (graph length 1) each time-step

class Von_Neumann_CA_Basic:

    def execute(self, graph, nodes):

        return_list = []
        for i in nodes:
            for j in i.connections:
                if (j.state == 1 and j.burn == 0):
                    j.burn = 1
                    return_list.append(j)
        
        return return_list

        


    
