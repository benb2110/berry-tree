##Work in Progress##
import numpy as np

trees = []


with open('Test Data.txt') as d: #importing data
    for line in d:
        temp = []
        for item in line:
            temp.append(item.strip())
        trees.append(temp[:len(temp)-1])
d.close()

width, length = len(trees), len(trees[0])


def printout():
    print(trees)
    print(width)
    print(length)


trees = np.array(trees)
#print(printout())


def visibility_checker(x, y):
    global width, length
    results = [True, True, True, True]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #UP, DOWN, RIGHT, LEFT

    for direction in directions:
        i = directions.index(direction)
        dx, dy = direction

        pos = (x, y)
        next_pos = (pos[0] + dx, pos[1] + dy)
        while 0 <= next_pos[0] < width and 0 <= next_pos[1] < length:  #
            if trees[x][y] > trees[next_pos] and trees[pos] >= trees[next_pos]:
                pos = next_pos
                next_pos = (pos[0] + dx, pos[1] + dy)
            else:
                results[i] = False
                break

    print(results, trees[x][y])

    if results == [False, False, False, False]:
        return False
    else:
        return True


def func():
    visible = 0
    for i in range(length):
        for j in range(width):
            if visibility_checker(i, j) is True:
                visible += 1
    print(visible)

#print(trees[2][1])
#visibility_checker(2, 1)
func()

