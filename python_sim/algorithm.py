#Non-probabilistic engine


#Fix the double-counting append issue today!!!!!
#Wind speeds up fire spread in its direction
#SELECT * FROM light WHERE time < set_limit ........ Example
#With wind, the robot is not going to incorporate exact winds, but rther take an average of all the wind that are measured, and then use that to randomly place gusts of wind into the simulation.

#In regard to slope, we use the general rule set forth by Pyne et al. (1996), that with every 10 degree increment, fire ROS doubles, and vice versa
#This cellular autonoma uses a von Neumann neighbourhood

avg_hill = 1
ros = 5
wind_freq = 3
directional_freq = [10, 50, 20, 20] #[N, E, S, W]
init_pos = "N"
hilltop = 4
max_slope = 75

import MySQLdb
import random
import time
import numpy as np
from matplotlib import pyplot as plt
import pyowm

def random_thing(prob):

  g = random.randrange(0, 1001, 1)
  counter = 1001


  a = []
  b = []

  for v in range (0, 1001):
    a.append(v)

  for m in range (0, prob):
    x = random.randrange(0, counter, 1)
    b.append(a[x])
    del a[x]
    counter = counter-1

  if (b.count(g) > 0):
    return True
  else:
    return False


location_key = "0123"

final_thing = []

humidity = []
hum_init = []

temperature = []
temp_init = []

light = []
light_init = []

db = MySQLdb.connect(host="localhost", user="root", passwd="Password", db="testing")
cur = db.cursor()
cur.execute("SELECT value2 FROM test")
lists = cur.fetchall()
db.close()

for r in range (0, len(lists)):
    frarr = lists[r][0].split(",")
    da_boi2_temp = int(frarr[1][frarr[1].index(":")+4:len(frarr[1])])
    da_boi2_hum = int(frarr[2][frarr[2].index(":")+4:len(frarr[2])])
    da_boi3_co = int(frarr[3][frarr[3].index(":")+4:len(frarr[3])])
    da_boi2_light = int(frarr[5][frarr[5].index(":")+4:len(frarr[5])])
    da_boi2_tree = int(frarr[6][frarr[6].index(":")+4:len(frarr[6])])
    if (hum_init.count([da_boi3_co, da_boi3_co]) > 0):
        humidity[hum_init.index([da_boi3_co, da_boi3_co])] = [da_boi2_hum, da_boi3_co, da_boi3_co]
    else:
        humidity.append([da_boi2_hum, da_boi3_co, da_boi3_co])
        hum_init.append([da_boi3_co, da_boi3_co])

    if (temp_init.count([da_boi3_co, da_boi3_co]) > 0):
        temperature[temp_init.index([da_boi3_co, da_boi3_co])] = [da_boi2_temp, da_boi3_co, da_boi3_co]
    else:
        temperature.append([da_boi2_temp, da_boi3_co, da_boi3_co])
        temp_init.append([da_boi3_co, da_boi3_co])

    if (light_init.count([da_boi3_co, da_boi3_co]) > 0):
        light[light_init.index([da_boi3_co, da_boi3_co])] = [da_boi2_light, da_boi3_co, da_boi3_co]
    else:
        light.append([da_boi2_light, da_boi3_co, da_boi3_co])
        light_init.append([da_boi3_co, da_boi3_co])


hill=[[7, 8, 30], [7, 9, 30], [7, 10, 30], [8, 8, 30], [8, 9, 0], [8, 10, 30], [9, 8, 30], [9, 9, 30], [9, 10, 30]]
hill_init = [[7, 8], [7, 9], [7, 10], [8, 8], [8, 9], [8, 10], [9, 8], [9, 9], [9, 10]]

grid_size = 40

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


                if (fifth > 0):
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
factor_grid_three = generate(light, light_init)

#print(factor_grid_one)
#print(factor_grid_one)
#print("")
#(factor_grid_two)

#def wind(winds):

    #def grid_init(size):
    #    base = []
    #    for j in range (0, size):
    #        for t in range (0, size):
    #            base.append([j, t, 0])
    #    return base

    #fire_start = grid_init(grid_size)

    #for u in fire_start:
    #    if (abs(u[0]-winds[0])+abs(u[1]-winds[1]) < 5):
    #        if (abs(u[0]-winds[0])+abs(u[1]-winds[1]) == 0):
    #            fire_start[fire_start.index(u)][2] = 100
    #        else:
    #            if (fire_start[fire_start.index(u)][2] < 160/(2**(abs(u[0]-winds[0])+abs(u[1]-winds[1])))):
    #                fire_start[fire_start.index(u)][2] = 160/(2**(abs(u[0]-winds[0])+abs(u[1]-winds[1])))
    #    else:
    #        fire_start[fire_start.index(u)][2] = 0
    #return fire_start

#def slope(slopes):

    #def grid_init(size):
    #    base = []
    #    for j in range (0, size):
    #        for t in range (0, size):
    #            base.append([j, t, 0])
    #    return base

    #fire_start = grid_init(grid_size)

    #for u in slopes:
    #    for f in fire_start:
    #        if (abs(u[0]-f[0])+abs(u[1]-f[1]) < avg_hill+1):
    #            if (abs(u[0]-f[0]) == 0 and abs(u[1]-f[1]) == avg_hill):
    #                b = True
    #            elif (abs(u[0]-f[0]) == avg_hill and abs(u[1]-f[1]) == 0):
    #                b = True
    #            else:
    #                fire_start[fire_start.index(f)][2] = u[2]




    #return fire_start


hill=[[7, 8, [30, 3]], [7, 9, [30, 3]], [7, 10, [30, 3]], [8, 8, [30, 3]], [8, 9, [0, 3]],
[8, 10, [30, 3]], [9, 8, [30, 3]], [9, 9, [30, 3]], [9, 10, [30, 3]]]
hill_init = [[7, 8], [7, 9], [7, 10], [8, 8], [8, 9], [8, 10], [9, 8], [9, 9], [9, 10]]


def slope():


    def grid_init(size):
        base = []
        for j in range (0, size):
            for t in range (0, size):
                base.append([j, t])
        return base

    fire_start = grid_init(grid_size)

    for b in range (0, len(fire_start)):
        if (hill_init.count(fire_start[b]) > 0):
            fire_start[b].append(hill[hill_init.index(fire_start[b])][2])
        else:
            fire_start[b].append(False)
    return fire_start

factor_grid_four = slope()


def putitalltogether(factor1, factor2, factor3, factor4):

    def grid_init(size):
        base = []
        for j in range (0, size):
            for t in range (0, size):
                base.append([j, t])
        return base

    itbethefinalcountdown = grid_init(grid_size)

    for g in range (0, len(itbethefinalcountdown)):
        itbethefinalcountdown[g].append(factor1[g][2])
        itbethefinalcountdown[g].append(factor2[g][2])
        itbethefinalcountdown[g].append(factor3[g][2])
        itbethefinalcountdown[g].append(factor4[g][2])

    return itbethefinalcountdown

boi = putitalltogether(factor_grid_one, factor_grid_two, factor_grid_three, factor_grid_four)


winds = [[5, 7, "E", 55], [32, 23, "E", 75], [18, 17, "E", 75]]

def windy_boi(windy_bois):
    windy_total = 0;
    north = 0;
    south = 0;
    west = 0;
    east = 0;
    total = 0;
    if (len(windy_bois) > 0):
        if (windy_bois[0][2] == "N"):
            north = north + 1
        if (windy_bois[0][2] == "S"):
            south = south + 1
        if (windy_bois[0][2] == "W"):
            west = west + 1
        if (windy_bois[0][2] == "E"):
            east = east + 1
        if (len(windy_bois) > 1):
            for n in range (1, len(windy_bois)):
                boi = 0
                if (windy_bois[n][2] == "N"):
                    north = north + 1
                if (windy_bois[n][2] == "S"):
                    south = south + 1
                if (windy_bois[n][2] == "W"):
                    west = west + 1
                if (windy_bois[n][2] == "E"):
                    east = east + 1
                total = total + windy_bois[n][3]
                #hour_part = 60*int(windy_bois[n][3][0:windy_bois[n][3].index(":")])
                #minute_part = int(windy_bois[n][3][windy_bois[n][3].index(":")+1:len(windy_bois[n][3])])
                #hour_part_next = 60*int(windy_bois[n-1][3][0:windy_bois[n-1][3].index(":")])
                #minute_part_next = int(windy_bois[n-1][3][windy_bois[n-1][3].index(":")+1:len(windy_bois[n-1][3])])
                #boi = boi + hour_part + minute_part - hour_part_next - minute_part_next
                #total = total + boi
            #windy_total = total/len(windy_bois)-1
            #percentages = [N, E, S, W]
            dir_tot = north + south + east + west
            total = total/len(windy_bois)
            percentages = [float(north)/dir_tot, float(east)/dir_tot, float(south)/dir_tot, float(west)/dir_tot]

        return [percentages, total]

    #This means that every windy_total minutes (converted to timestamps), we can simulate a gust of wind

boi2 = windy_boi(winds)

def measure(tree_density, grid_size):

    g = ["placeholder", "placeholder2"]
    h = []

    fire_movement = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    matrix = []
    the_master = []
    operator = []


    def grid_init(density, size):
      a = []
      k = density
      base = []
      for j in range (0, size):
          for t in range (0, size):
              base.append([j, t, "tree"])
      for lm in range (0, k):
          sell = random.randrange(0, size*size-lm, 1)
          a.append(base[sell])
          del base[sell]
      return a

    fire_start = grid_init(tree_density, grid_size)

    counter = []

    if (fire_start.count([9, 1, "tree"]) == 0):
      fire_start.pop()
      fire_start.append([9, 1, "tree"])


    firespark = [9, 1]
    fire_start[fire_start.index([9, 1, "tree"])] = [9, 1, "burn", 0]
    h.append([9, 1, "burn", 0])

    for v in fire_movement:
      if (fire_start.count([firespark[0] + v[0], firespark[1] + v[1], "tree"]) > 0):
        fire_start[fire_start.index([firespark[0] + v[0], firespark[1] + v[1], "tree"])] = [firespark[0] + v[0], firespark[1] + v[1], "burn", 1]
        h.append([firespark[0] + v[0], firespark[1] + v[1], "burn", 1])


    counting = 2
    while (g[len(g) - 1] != g[len(g) - 2]):
      base = len(h)
      g.append(str(fire_start).count("burn"))
      place = len(h)
      for x in range (0, place):
        for v in fire_movement:
            if (fire_start.count([h[x][0] + v[0], h[x][1] + v[1], "tree"]) > 0):
                if (counting - h[x][3] <= 3):
                    r_var = 0;
                    for b in boi:
                        if (b[0] == h[x][0] + v[0] and b[1] == h[x][1] + v[1]):
                            r_var_hum = b[2]
                            r_var_temp = b[3]
                            r_var_light = b[4]
                            r_var_slope = b[5]
                            if (r_var_temp < 35):
                                prob_boy1 = int(round((((r_var_temp/1.7+36)/82)+0.08)*1310))
                            else:
                                prob_boy1 = 1000
                            if (r_var_hum > 5):
                                prob_boy2 = int(round(((-1*r_var_hum/1.6+33)/70 + 0.3)*1310))
                            else:
                                prob_boy2 = 1000
                            if (r_var_light < 800):
                                prob_boy3 = int(round(((r_var_light/1.9+600)/28 + 0.8)*27))
                            else:
                                prob_boy3 = 1000
                            if (boi.index(b)+40*v[0]+v[1] < 1600):
                                if (b[5] == False):
                                    slope_style = 0
                                    elev = 0
                                if (boi[boi.index(b)+40*v[0]+v[1]][5] == False):
                                    slope_style2 = 0
                                    elev2 = 0
                                if (b[5] != False):
                                    slope_style = b[5][0]
                                    elev = b[5][1]
                                if (boi[boi.index(b)+40*v[0]+v[1]][5] != False):
                                    slope_style2 = boi[boi.index(b)+40*v[0]+v[1]][5][0]
                                    elev2 = boi[boi.index(b)+40*v[0]+v[1]][5][1]
                                if (elev2 - elev == 0):
                                    slope_fin = 0
                                elif (elev2 - elev > 0):
                                    slope_fin = 2**(abs(slope_style2 - slope_style)/10)*5 + 20
                                elif (elev2 - elev < 0):
                                    slope_fin = -1*(2**(abs(slope_style2 - slope_style)/10)*5 + 20)

                                directional_prob = 0
                                if (boi2 != None):
                                    if (v[0] == 0 and v[1] == 1):
                                        if (boi2[0][1] < 0.1 and boi2[0][1] > 0.01 and len(boi2) > 2):
                                            directional_prob = -1*(3/boi2[0][1])
                                        elif (boi2[0][3] < 0.01 and len(boi2) > 2):
                                            directional_prob = -300
                                        elif (boi2[0][1] < 0.1 and len(boi2) <= 2):
                                            directional_prob = 0
                                        else:
                                            directional_prob = int(round((boi2[1]*35/(1.4)+boi2[0][1]*600)/7)-30)


                                    if (v[0] == 0 and v[1] == -1):
                                        if (boi2[0][3] < 0.1 and boi2[0][3] > 0.01 and len(winds) > 2):
                                            directional_prob = -1*(3/boi2[0][3])
                                        elif (boi2[0][3] < 0.01 and len(winds) > 2):
                                            directional_prob = -300
                                        elif (boi2[0][3] < 0.1 and len(winds) <= 2):
                                            directional_prob = 0
                                        else:
                                            directional_prob = int(round((boi2[1]*35/(1.4)+boi2[0][3]*600)/7)-30)

                                    if (v[0] == 1 and v[1] == 0):
                                        if (boi2[0][0] < 0.1 and boi2[0][0] > 0.01 and len(winds) > 2):
                                            directional_prob = -1*(3/boi2[0][0])
                                        elif (boi2[0][0] < 0.01 and len(winds) > 2):
                                            directional_prob = -300
                                        elif (boi2[0][0] < 0.1 and len(winds) <= 2):
                                            directional_prob = 0
                                        else:
                                            directional_prob = int(round((boi2[1]*35/(1.4)+boi2[0][0]*600)/7)-10)

                                    if (v[0] == -1 and v[1] == 0):
                                        if (boi2[0][2] < 0.1 and boi2[0][2] > 0.01 and len(winds) > 2):
                                            directional_prob = -1*(3/boi2[0][2])
                                        elif (boi2[0][2] < 0.01 and len(winds) > 2):
                                            directional_prob = -300
                                        elif (boi2[0][2] < 0.1 and len(winds) <= 2):
                                            directional_prob = 0
                                        else:
                                            directional_prob = int(round((boi2[1]*35/(1.4)+boi2[0][2]*600)/7)-30)
                                final = int(round((prob_boy1 + prob_boy2 + prob_boy3)/3 + slope_fin + directional_prob + 50))
                            if (final > 1000):
                                final = 1000
                            if (final < 100):
                                final = 100
                            final_prob = random_thing(final)
                            if (h[x][3] < counting and h[x][3] > counting-3):
                                if (final_prob == True):
                                    #if (ros == False):
                                    fire_start[fire_start.index([h[x][0] + v[0], h[x][1] + v[1], "tree"])] = [h[x][0] + v[0], h[x][1] + v[1], "burn", counting]
                                    h.append([h[x][0] + v[0], h[x][1] + v[1], "burn", counting])
                                    #if (ros == True):
                                    #    fire_start[fire_start.index([h[x][0] + v[0], h[x][1] + v[1], "tree"])] = [h[x][0] + v[0], h[x][1] + v[1], "burn", counting+1]
                                    #    h.append([h[x][0] + v[0], h[x][1] + v[1], "burn", counting+1])
      counter.append(len(h))
      counting = counting + 1
      if (base == len(h)):
        break;


    k = []

    for n in g:
      if (k.count(n) == 0):
        k.append(n)

    if (len(h) > 5):
      j = len(counter)
    elif (len(h) > 1):
      j = 1
    else:
      j = 0

    fire_start

    return [fire_start, j, int(round((float(len(h))/1100)*100))]


#measure(int(round((float(da_boi2_tree)/da_boi3_co)*1600)), 40)

sel = 0


thisboi = measure(1100, 40)

print(thisboi[2])

db = MySQLdb.connect(host="localhost", user="root", passwd="Password", db="forest_fire_data")
cur = db.cursor()
lists = ""
for g in thisboi[0]:
    for t in g:
        lists = lists + str(t) + ","
    lists = lists+";"
cur.execute("INSERT INTO real_time_2 (data2) VALUES ('%s')" % lists)
db.commit()
db.close()

if (sel == 0):

    final_data = []

    for gf in range (0, 20):
        final_data.append(measure(1100, 40)[1])

    print(final_data)

    x = np.arange(0, 20, 1)
    y = final_data
    plt.title("Simulation Trial vs. Iterations")
    plt.xlabel("Simulation Trial")
    plt.ylabel("Iterations")
    plt.plot(x, y)
    plt.show()

if (sel == 1):

    final_data = []

    for gf in range (0, 20):
        final_data.append(measure(1100, 40)[2])

    x = np.arange(0, 20, 1)
    y = final_data
    plt.title("Simulation Trial vs. Land Area Burned")
    plt.xlabel("Simulation Trial")
    plt.ylabel("Land Area Burned")
    plt.plot(x, y)
    plt.show()


#Wind will affect the way the fire spreads by accelerating the ROS within a certain range, and will increase the probability
#of a fire starting in the direction of the wind, and decreasing the probability in the direction opposite the wind.
#This will be also dependent on the wind speed.
