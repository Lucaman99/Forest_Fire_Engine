'''
IGNITE LABS
Date: March 22nd, 2020
Author: Jack Ceroni
'''

# Defines the Edge class

class Edge:
    def __init__(self, start_node_index, end_node_index):

        self.start_node = start_node_index
        self.end_node = end_node_index
        self.e_index = [start_node_index, end_node_index]

# Defines the Vertex class

class Vertex:
    def __init__(self, v_index):
        self.v_index = v_index

# Defines the Graph class

class Graph:

    def __init__(self, vertices, edges):

        node_set = vertices
        edges_set = edges

        self.node_set = node_set

        edges_index_set = []
        for i in edges_set:
            edges_index_set.append(i.e_index)

        vertex_index_set = []
        for i in node_set:
            vertex_index_set.append(i.v_index)
        self.vertex_index_set = vertex_index_set

        new_edges_set = []
        new_edges_index_set = []

        for i in range(0, len(edges_index_set)):
            for j in edges_index_set[i]:
                switch = True
                if (j not in vertex_index_set):
                    switch = False

            if (switch == True):
                new_edges_set.append(edges_set[i])
                new_edges_index_set.append(edges_index_set[i])
        
        self.edges_set = new_edges_set
        self.edges_index_set = new_edges_index_set

'''
#Connects nodes with an edge

    def connect_nodes(self, vertex1,  vertex2):
        if (edge.e_index not in self.edges_index_set and edge.start_node in self.vertex_index_set and edge.end_node in self.vertex_index_set):
            self.edges_set.append(edge)
            self.edges_index_set.append(edge.e_index)
'''

'''
#Adds a node to the graph

    def add_nodes(self, node):
        if (node.v_index not in self.vertex_index_set):
            self.node_set.append(node)
            self.vertex_index_set.append(node.v_index)
'''

'''
#Removes nodes from the graph. If a node is removed, all edges connected to that node are removed as well

    def remove_nodes(self, node):
        if (node in self.node_set):
            del self.node_set[self.node_set.index(node)]
            new = []
            for i in range (0, len(self.edges_set)):
                if (node != self.edges_set[i].start_node and node != self.edges_set[i].end_node):
                    new.append(self.edges_set[i])
            self.edges_set = new
'''

'''
#Disconnects nodes, thereby removing an edge

    def disconnect_nodes(self, edge):
        if (edge in self.edges_set):
            del self.edges_set[self.edges_set.index(edge)]
'''

# Arranges the vertices in a dictionary order, based on their index

#def index_arrange(




