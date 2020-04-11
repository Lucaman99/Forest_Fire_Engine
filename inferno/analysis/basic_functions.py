import numpy
import math
import random

# Defines the completion of a graph

def completion(graph):

    burn_total = 0
    tree_total = 0
    for i in graph.graph.vertex_set:
        if (i.state == 1):
            tree_total += 1
        if (i.burn == 1):
            burn_total += 1
    
    return (burn_total / tree_total)