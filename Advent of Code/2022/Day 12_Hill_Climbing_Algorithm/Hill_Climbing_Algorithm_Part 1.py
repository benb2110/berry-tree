##WORK IN PROGRESS##

import math
import numpy as np
import string

infinity = math.inf

grid = []
with open('Test Data.txt') as d: #importing data
    for line in d:
        items = []
        for item in line.strip():
            items.append(ord(item)-96)
        grid.append(items)
d.close()
print(grid)

a = np.array(grid)

start = np.where(a == -13)
end = np.where(a == -27)
print(start, end)


#assign height values to each cell
heightmap = []
for line in grid:
    for item in line:
        pass

#create a seperate 2D grid to store distance data

#store start and end co-ordinates (S and E)

#Create a visited list and a queue list



t = ord('E') - 96
print(t)
