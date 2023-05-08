##Work in Progress##

trees = []
#trees = ['30373',
#'25512',
#'65332',
#'33549',
#'35390']

with open('Data.txt') as d: #importing data
    for line in d:
        trees.append(line)
d.close()

print(trees)

width = len(trees)
length = len(trees[0])

print(width)
print(length)

visible = 0



def visibility_checker(x, y):
    counter = x
    while counter != length-1:
        if trees[counter][y] <= trees[x][y]:
            counter +=1
        else:
            return True
    counter = x
    while counter != 0:
        if trees[counter][y] <= trees[x][y]:
            counter -=1
        else:
            return True
    counter = y
    while counter != width-1:
        if trees[x][counter] <= trees[x][y]:
            counter +=1
        else:
            return True
    counter = y
    while counter != 0:
        if trees[x][counter] <= trees[x][y]:
            counter -=1
        else:
            return True
    return False


for i in range(width):
    for j in range(length):
        if 0 < i < length - 1 and 0 < j < width - 1:
            if visibility_checker(i, j) is True:
                visible +=1
        else:
          visible+=1

print(visible)
