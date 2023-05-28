##WORK IN PROGRESS##

import math
import numpy as np


infinity = math.inf

grid = []
with open('Test Data.txt') as d: #importing data
    for line in d:
        items = []
        for item in line.strip():
            items.append(ord(item)-96) #storing number instead of letter
        grid.append(items)
d.close()
print(grid)

a = np.array(grid)


#store start and end co-ordinates (S and E)
start = np.where(a == -13) #make start == 0
end = np.where(a == -27) #make end == 27
print(start, end)


#create a seperate 2D grid to store distance dataheightmap = []
heightmap = []
for line in grid:
    for item in line:
        pass





#Create a visited list and a queue list

