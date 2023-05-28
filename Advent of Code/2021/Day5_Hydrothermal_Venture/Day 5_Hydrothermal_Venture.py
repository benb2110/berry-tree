instructions = []

with open('Test_Vent_Data.txt') as d: #importing data
    for line in d:
        instructions.append(line.split())
d.close()

print(instructions)

array = []
for i in range(9):
    temp = []
    for j in range(9):
        temp.append(0)
    array.append(temp)

print(array)


def vent_mapper(instructions):
    for i in range(len(instructions)):
        x1, x2 = instructions[i][0][0], instructions[i][2][0]
        y1, y2 = instructions[i][0][2], instructions[i][2][2]
        x_len = abs(x1 - x2)
        y_len = abs(y1 - y2)
        if x1 == x2 or y1 == y2:
            if x_len > y_len:
                pass
            else


vent_mapper(instructions)
##Work in Progress##
