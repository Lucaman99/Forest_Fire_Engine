import MySQLdb
import random
import time
import numpy as np
from matplotlib import pyplot as plt
import pyowm

location_key = "0123"

db = MySQLdb.connect(host="localhost", user="root", passwd="Password", db="forest_fire_data")
cur = db.cursor()
cur.execute("SELECT * FROM real_time_2")
lists = cur.fetchall()[len(cur.fetchall())-1]
cur.execute("SELECT * FROM robot WHERE location = "+location_key)
current_factors = cur.fetchall()[len(cur.fetchall())-1]
cur.execute("SELECT * FROM trees WHERE location = "+location_key)
trees = cur.fetchall()[len(cur.fetchall())-1]
cur.execute("SELECT * FROM old_data WHERE location = "+location_key)
old_data = cur.fetchall()[len(cur.fetchall())-1]
db.close()

humidity = [[5, 5, 0.8], [9, 1, 0.7], [7, 8, 0.3], [7, 7, 0.3]]
hum_init = [[5, 5], [9, 1], [7, 8], [7, 7]]

temperature = [[6, 1, 24], [3, 2, 19], [4, 7, 23]]
temp_init = [[6, 1], [3, 2], [4, 7]]

wind = [8, 9, "NE"]
wind2 = [3, 2, "S"]

grid_size = 10

def generate(init_grid, init):

    def grid_init(size):
        base = []
        for j in range (0, size):
            for t in range (0, size):
                base.append([j, t])
        return base

    fire_start = grid_init(grid_size)


    grid_spread = []
    for i in init_grid:
        a = []
        a.append(i[0])
        a.append(i[1])
        a.append(i[2])
        for y in fire_start:
            a.append(y)
            a.append(abs(y[0]-i[0])+abs(y[1]-i[1]))
        grid_spread.append(a)

    for o in  fire_start:
        for j in grid_spread[0]:
            if (j == o):
                first_list = []
                for z in range (0, len(grid_spread)):
                    first_list.append((grid_spread[z][grid_spread[z].index(j)+1]))

                fifth = 0;

                for v in first_list:
                    if (v > 0):
                        fifth = fifth + 1/float(v)

                final = 1/fifth

                final_boy = 0;

                for p in range (0, len(first_list)):

                    if (first_list[p] > 0):

                        final_boy = final_boy + final*(1/float(first_list[p]))*grid_spread[p][2]

                if (init.count(o) < 1):

                    o.append(final_boy)

                else:
                    o.append(init_grid[init.index(o)][2])


    return fire_start




factor_grid_one = generate(humidity, hum_init)
factor_grid_two = generate(temperature, temp_init)
#print(factor_grid_one)
#print("")
#print(factor_grid_two)

def wind(winds):

    def grid_init(size):
        base = []
        for j in range (0, size):
            for t in range (0, size):
                base.append([j, t])
        return base

    fire_start = grid_init(grid_size)

    for u in fire_start:
        if (abs(u[0]-winds[0])+abs(u[1]-winds[1]) < 5):
            if (abs(u[0]-winds[0])+abs(u[1]-winds[1]) == 0):
                fire_start[fire_start.index(u)].append(100)
            else:
                fire_start[fire_start.index(u)].append(160/(2**(abs(u[0]-winds[0])+abs(u[1]-winds[1]))))
    return fire_start

#print(wind([3, 2, "S"]))

def slope(slopes):

    def grid_init(size):
        base = []
        for j in range (0, size):
            for t in range (0, size):
                base.append([j, t])
        return base

    fire_start = grid_init(grid_size)

    for u in slopes:
        for f in fire_start:
            if (abs(u[0]-f[0])+abs(u[1]-f[1]) < 3):
                if (abs(u[0]-f[0]) == 0 and abs(u[1]-f[1]) == 2):
                    b = True
                elif (abs(u[0]-f[0]) == 2 and abs(u[1]-f[1]) == 0):
                    b = True
                else:
                    fire_start[fire_start.index(f)].append(u[2])

    return fire_start


print(slope([[6, 7, 30], [0, 9, 30]]))

#Wind will affect the way the fire spreads by accelerating the ROS within a certain range, and will increase the probability
#of a fire starting in the direction of the wind, and decreasing the probability in the direction opposite the wind.
#This will be also dependent on the wind speed.
