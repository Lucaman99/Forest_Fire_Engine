import math
import random
import numpy as np


class Simulation:
    def __init__(self, steps, final_graph):

        self.steps = steps
        self.final_graph = final_graph


# Creates the simulator class, which bundles together all of the necessary componenets for a simulation
class Simulator:
    def __init__(self, graph, state_function, burn_function, init_function):

        self.graph = graph
        self.state_function = state_function
        self.burn_function = burn_function
        self.init_function = init_function

    def simulate(self, termination):

        self.state_function.execute(self.graph, 0)
        initialize = self.init_function.execute(self.graph)
        return_list_1 = []
        return_list_2 = initialize
        final_list = [initialize]
        execution = 0

        while (return_list_1 != return_list_2) and (execution < termination):

            return_list = self.burn_function.execute(self.graph, return_list_2)
            self.state_function.execute(self.graph, execution + 1)
            return_list_1 = return_list_2
            return_list_2 = return_list
            final_list.append(return_list)
            execution = execution + 1

        return Simulation(steps=final_list[: len(final_list) - 2], final_graph=self.graph)
