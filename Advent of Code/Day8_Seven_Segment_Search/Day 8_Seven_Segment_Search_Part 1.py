#  a
# b  c
#  d
# e  f
#  g

display_data = []

with open('Display_Data.txt') as d: #importing data
    for line in d:
        display_data.append(line.strip().split('|'))
d.close()


temp = []
for j in range(len(display_data)): #string manupilation for data
    for k in range(len(display_data[j])):
        temp.append(display_data[j][k].split(' '))


def count_1_4_7_8(data): #counts instances of 1s, 4s, 7s and 8s
    counter = 0
    d = [data[1::2]]
    for i in range(len(d[0])):
        for h in range(5):
            print(d[0][i][h])
            if len(d[0][i][h]) == 2 or len(d[0][i][h]) == 3 or len(d[0][i][h]) == 4 or len(d[0][i][h]) == 7:
                counter += 1
                print(True)
    return counter


print(count_1_4_7_8(temp))
