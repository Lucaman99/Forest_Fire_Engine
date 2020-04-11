# Imports the necessary dependencies

import inferno
from matplotlib import pyplot as plt
from tqdm import tqdm

# Defines initial parameters and empty list to store final values

trials = 20
num = 30
y = []

# Starts by creating the grid

lattice_graph = inferno.sgraph.SquareLatticeGraph(length=num)

for i in tqdm(range(1, num)):
    sum = 0
    for j in range(0, trials):

        # Resets the graph before each iteration of the simulation

        lattice_graph.reset()

        # Defines the necessary variables

        init_number = 1
        density = float(i/num)

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

    # Calculate the average completion for a given density and add it to the final list
    
    y.append(float(sum / trials))

# Plots the average completion against the tree density

plt.plot(range(1, num), y)
plt.show()