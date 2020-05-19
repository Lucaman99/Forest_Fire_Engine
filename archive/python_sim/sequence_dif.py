import numpy as np
import MySQLdb
import math

sequenced_values = [4, 87, 54, 23, 4, 6]
n_differences = sequenced_values
matching_value = False
counter = 0

while matching_value == False:
    final = []
    store = 0
    for i in range(1, len(n_differences)):
        term = n_differences[i] - n_differences[i - 1]
        final.append(term)

    n_differences = final
    counter = counter + 1

    if n_differences.count(n_differences[0]) == len(n_differences):
        matching_value = True

multiplier = []

dif = n_differences[0]


for j in range(0, counter - 1):
    factorial = 1
    if j > 0:
        for u in range(1, j + 1):
            factorial = factorial * u
    multiplier.append(factorial)

print(multiplier)

expression = list(map(lambda x: dif / float(x), multiplier))

print(expression)
