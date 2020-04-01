import graph
import numpy as np
import random
import math

class SquareLatticeGraph:

    def __init__(self, length, state_function):

        # Initializes the length and state_function attributes
        self.length = length
        self.state_function = state_function

        #Initializes the vertex structure of the square lattice graph
        vertices = []
        for i in range(0, length):
            for j in range(0, length):
                vertex = graph.Vertex(index=[i, j])
                vertices.append(vertex)
        
        vertices = graph.index_arrange(vertices)
        self.vertices = vertices

        # Initializes the edge structure of the square lattice graph
        edges = []

        # Creates the horizontal edge connection
        for i in range(0, length):
            for j in range(0, length-1):
                edges.append(graph.Edge(start_vertex=vertices[j, i], end_vertex=vertices[j+1, i]))

        # Creates the vertical edge connections
        for i in range(0, length-1):
            for j in range(0, length):
                edges.append(graph.Edge(start_vertex=vertices[j, i], end_vertex=vertices[j, i+1]))
        
        # TODO: Sort the list of edges with the index sorting function?

        self.graph = graph.Graph(vertices, edges)
    

def function(x, t):
    return 0

test_graph = SquareLatticeGraph(10, function)

