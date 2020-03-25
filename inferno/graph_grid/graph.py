'''
Date: March 22nd, 2020
Author: Jack Ceroni
'''

# Defines the Edge class

class Edge:
    def __init__(self, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node

# Defines the Graph class

class Graph:
    def __init__(self, edges_set):
        self.edges_set = edges_set
        self.node_set = []
        for i in edges_set:
            if (i.start_node not in self.node_set):
                self.node_set.append(i.start_node)
            if (i.end_node not in self.node_set):
                self.node_set.append(i.end_node)

#Connects nodes with an edge

    def connect_nodes(self, edge):
        if (edge not in self.edges_set and edge.start_node in self.node_set and edge.end_node in self.node_set):
            self.edges_set.append(edge)

#Adds a node to the graph

    def add_nodes(self, node):
        if (node not in self.node_set):
            self.node_set.append(node)

#Removes nodes from the graph. If a node is removed, all edges connected to that node are removed as well

    def remove_nodes(self, node):
        if (node in self.node_set):
            del self.node_set[self.node_set.index(node)]
            new = []
            for i in range (0, len(self.edges_set)):
                if (node != self.edges_set[i].start_node and node != self.edges_set[i].end_node):
                    new.append(self.edges_set[i])
            self.edges_set = new

#Disconnects nodes, thereby removing an edge

    def disconnect_nodes(self, edge):
        if (edge in self.edges_set):
            del self.edges_set[self.edges_set.index(edge)]
