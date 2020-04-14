'''
IGNITE LABS
Date: April 1st, 2020
Author: Jack Ceroni
'''

from .graph import Graph, Vertex, Edge
import numpy as np
import random
import math

class SquareLatticeGraph:

    def __init__(self, length):

        # Initializes the length and state_function attributes
        self.length = length

        #Initializes the vertex structure of the square lattice graph
        vertices = []
        vertices_index = []
        for i in range(0, length):
            for j in range(0, length):
                vertex = Vertex(v_index=[i, j])
                vertices.append(vertex)
                vertices_index.append(vertex.v_index)
        
        #vertices = graph.index_arrange(vertices)

        # Searches for the longest entry in vertices_index
        '''
        longest = 0
        for i in vertices_index:
            if (len(i) > longest):
                longest = len(i)
        '''
        
        # Initializes the edge structure of the square lattice graph
        edges = []

        # Creates the horizontal edge connection
        for i in range(0, length):
            for j in range(0, length-1):
                edges.append(Edge(vertices[vertices_index.index([i, j])], vertices[vertices_index.index([i, j+1])] ))
        
        # Creates the vertical edge connections
        for i in range(0, length):
            for j in range(0, length-1):
                edges.append(Edge(vertices[vertices_index.index([j, i])], vertices[vertices_index.index([j+1, i])]))
        
        # TODO: Sort the list of edges with the index sorting function?
    
        self.graph = Graph(vertices, edges)

class CustomGraph:

    def __init__(self, vertex_index, edges_index):

        vertices = [Vertex(i) for i in vertices_index]
        edges = []
        for i in edges_index:
            holder = [0, 0]
            for j in vertices:
                if (j.v_index == i[0]):
                    holder[0] = j
                if (j.v_index == i[1]):
                    holder[1] = j
            edges.append(Edge(holder[0], holder[1]))
        
        self.graph = Graph(vertices, edges)