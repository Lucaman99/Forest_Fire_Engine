import math
import random
import numpy as np

# Creates the simulator class, which bundles together all of the necessary componenets for a simulation
class Simulator:

    def __init__(self, graph, state_function, burn_function, termination, fire_init):

        self.graph = graph
        self.state_function = state_function
        self.burn_function = burn_function
        self.termination = termination
    
    def simulate(self, graph, state_function, burn_function, termination, fire_init):

        self.state_function(self.graph, 0)
        initialize = self.fire_init(self.graph)
        return_list_1 = []
        return_list_2 = initialize
        final_list = [initialize]
        execution = 0

        while ((return_list_1 != return_list_2) and (executions < termination)):

            return_list = self.burn_function(self.graph, return_list_2)
            self.state_function(self.graph, execution+1)
            return_list_1 = return_list_2
            return_list_2 = return_list
            final_list.append(return_list)
            execution = execution + 1
        
        return final_list





