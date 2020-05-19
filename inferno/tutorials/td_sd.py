# Imports the necessary dependencies

import inferno
from matplotlib import pyplot as plt
from tqdm import tqdm

# Defines initial parameters and empty list to store final values

trials = 30
length = 30
y = []

# Creates the grid

lattice_graph = inferno.sgraph.SquareLatticeGraph(length=length)

for i in tqdm(range(1, length)):
    sum = 0
    squared_sum = 0
    for j in range(0, trials):

        # Resets the graph before each iteration of the simulation

        lattice_graph.reset()

        # Defines the necessary variables

        init_number = 1
        density = float(i / length)

        # Defines the necessary functions used in the simulation

        init_function = inferno.sim.initialize.Random_Init_Number(number=init_number)
        state_function = inferno.sim.state.Density_State(density=density)
        update_function = inferno.sim.update.Von_Neumann_CA_Basic()

        # Creates the simulation object

        simulator = inferno.Simulator(
            graph=lattice_graph,
            state_function=state_function,
            burn_function=update_function,
            init_function=init_function,
        )

        # Runs the simulation

        results = simulator.simulate(termination=1e14)

        # Calculates the completion of the final graph

        final_graph = results.final_graph
        completion = inferno.completion(final_graph)
        sum += completion
        squared_sum += completion ** 2

    # Calculate the average completion for a given density and add it to the final list

    y.append(float(squared_sum / trials) - (float(sum / trials)) ** 2)

# Plots the average completion against the tree density

plt.plot([i / length for i in range(1, length)], y)
plt.xlabel("Tree Density")
plt.ylabel("SD of Measured Final Completion")
plt.show()
