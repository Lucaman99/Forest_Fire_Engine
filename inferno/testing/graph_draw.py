import networkx as nx
from matplotlib import pyplot as plt

L = 7
G = nx.grid_2d_graph(L, L)
nx.draw(G)
plt.show()
