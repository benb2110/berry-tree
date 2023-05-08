##Work in Progress##

trees = []

with open('Test Data.txt') as d: #importing data
    for line in d:
        trees.append(line.split())
d.close()

#print(trees)

width = len(trees)
length = len(trees[0][0])


visible = 0
invisible = 0


def visibility_checker(i, j):
    counter = i
    while counter != length-1:
        if trees[counter][j] <= trees[i][j]:
            counter += 1
        else:
            return True
    counter = i
    while counter != 0:
        if trees[counter][j] <= trees[i][j]:
            counter -= 1
        else:
            return True
    counter = j
    while counter != length-1:
        if trees[counter][j] <= trees[i][j]:
            counter += 1
        else:
            return True
    counter = j
    while counter != 0:
        if trees[counter][j] <= trees[i][j]:
            counter -= 1
        else:
            return True


for i in range(length):
    for j in range(width):
        if 0 < i < length - 1 and 0 < j < width - 1: #inside the grid
            if visibility_checker(i, j) is True:
                visible += 1
        else:   #outside the grid (ignore)
            invisible += 1
            continue

print(visible)
print(invisible)
