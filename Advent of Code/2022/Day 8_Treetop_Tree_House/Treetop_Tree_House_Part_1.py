import numpy as np

trees = []

with open('Data.txt') as d: #importing data
    for line in d:
        temp = []
        for item in line:
            temp.append(item.strip())
        trees.append(temp[:len(temp)-1])
d.close()

trees = np.array(trees)

width, length = len(trees), len(trees[0])


def visibility_checker(x, y):
    global width, length
    results = [True, True, True, True]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] #UP, DOWN, RIGHT, LEFT

    for direction in directions:
        i = directions.index(direction)
        dx, dy = direction

        next_pos = (x + dx, y + dy)
        while 0 <= next_pos[0] < width and 0 <= next_pos[1] < length:
            if trees[x][y] > trees[next_pos]:
                next_pos = (next_pos[0] + dx, next_pos[1] + dy)
            else:
                results[i] = False
                break

    print(results, trees[x][y])

    return any(results)


def func():
    visible = 0
    for i in range(length):
        for j in range(width):
            if visibility_checker(i, j) is True:
                visible += 1
    print(visible)


func()
