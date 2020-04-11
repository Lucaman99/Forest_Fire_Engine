import inferno
from matplotlib import pyplot as plt
from tqdm import tqdm
import copy

trials = 20
num = 30
y = []

lattice_graph = inferno.sgraph.SquareLatticeGraph(length=num)

for i in tqdm(range(1, num)):
    sum = 0
    for j in range(0, trials):

        # Start by creating the grid

        for k in lattice_graph.graph.vertex_set:
            k.state = 0
            k.burn = 0

        # We define the necessary variables

        init_number = 1
        density = float(i/num)

        # We define the necessary functions used in the simulation
        init_function = inferno.sim.initialize.Random_Init_Number(number=init_number)
        state_function = inferno.sim.state.Density_State(density=density)
        update_function = inferno.sim.update.Von_Neumann_CA_Basic()

        # We then create the simulation object

        simulator = inferno.Simulator(
            graph=lattice_graph, 
            state_function=state_function, 
            burn_function=update_function,
            init_function=init_function,
            )
        
        # Run the simulation

        results = simulator.simulate(termination=1e14)

        # Calculate the completion of the final graph

        final_graph = results.final_graph
        completion = inferno.completion(final_graph)
        sum += completion
    
    y.append(float(sum / trials))

plt.plot(range(1, num), y)
plt.show()