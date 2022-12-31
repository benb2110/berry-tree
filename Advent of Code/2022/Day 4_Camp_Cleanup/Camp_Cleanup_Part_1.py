import re
duties = []
with open('Data.txt') as d: #importing data
    for line in d:
        duties.append(line.strip())
d.close()

result = [re.split('[,-]',x) for x in duties]


def does_contain(data):
    count = 0
    for i in range(len(data)):
        if int(data[i][0]) <= int(data[i][2]) and int(data[i][1]) >= int(data[i][3]) or int(data[i][0]) >= int(data[i][2]) and int(data[i][1]) <= int(data[i][3]):
            count += 1
            print(str(data[i]) + ' x')
        else:
            print(data[i])
    return count



print(does_contain(result))


