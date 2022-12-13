depth_data = []
test_depth_data = [2, 1, 9, 9, 9, 4, 3, 2, 1, 0], [3, 9, 8, 7, 8, 9, 4, 9, 2, 1], [9, 8, 5, 6, 7, 8, 9, 8, 9, 2], [8, 7, 6, 7, 8, 9, 6, 7, 8, 9], [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]

with open('Depth_Data.txt') as d: #importing data
    for line in d:
        temp_line = []
        for i in line:
            try:
                temp_line.append(int(i))
            except ValueError:
                pass
        depth_data.append(temp_line)
d.close()

test_depth_data = depth_data

def find_basin_size(i, j):
    basin_size = 1
    pass

trophs = []
checker = [False, False, False, False]

for i in range(len(depth_data)):
    for j in range(len(depth_data[0])):
        if j != 0:
            if depth_data[i][j] < depth_data[i][j - 1]: ##
                checker[0] = True
        else:
            checker[0] = True
        if j != len(depth_data[0])-1:
            if depth_data[i][j] < depth_data[i][j + 1]: ##
                checker[1] = True
        else:
            checker[1] = True
        if i != 0:
            if depth_data[i][j] < depth_data[i - 1][j]: ##
                checker[2] = True
        else:
            checker[2] = True
        if i != len(depth_data)-1:
            if depth_data[i][j] < depth_data[i + 1][j]: ##
                checker[3] = True
        else:
            checker[3] = True

        if checker == [True, True, True, True]:
            #basin size function call here
            find_basin_size(i, j)
        checker = [False, False, False, False]

