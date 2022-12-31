import re
duties = []
with open('Data.txt') as d: #importing data
    for line in d:
        duties.append(line.strip())
d.close()

result = [re.split('[,-]',x) for x in duties]


def is_overlap(data):
    overlaps = 0
    for i in range(len(data)):
        if int(data[i][1]) >= int(data[i][2]) and int(data[i][1]) <= int(data[i][3]):
            overlaps += 1
            print(str(data[i]) + ' x')
        elif int(data[i][0]) >= int(data[i][2]) and int(data[i][0]) <= int(data[i][3]):
            overlaps += 1
            print(str(data[i]) + ' x')
        elif int(data[i][2]) >= int(data[i][0]) and int(data[i][2]) <= int(data[i][1]):
            overlaps += 1
            print(str(data[i]) + ' x')
        else:
            print(data[i])
    return overlaps


print(is_overlap(result))
