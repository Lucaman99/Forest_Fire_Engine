import numpy as np
import MySQLdb

sequenced_values = [4, 87, 54, 23, 4, 6]
n_differences = sequenced_values
matching_value = False

while (matching_value == False):
    final = []
    store = 0
    counter = 0
    for i in range (1, len(n_differences)):
        term = n_differences[i]-n_differences[i-1]
        final.append(term)

    n_differences = final

    print(n_differences)

    if (n_differences.count(n_differences[0]) == len(n_differences)):
        matching_value = True
