import re
#array = [], ['Z', 'N'], ['M', 'C', 'D'], ['P']  #Test array
array = [],['D','L','V','T','M','H','F'],['H','Q','G','J','C','T', 'N', 'P'],['R','S','D','M','P','H'],['L','B','V','F'],['N','H','G','L','Q'],['W','B','D','G','R','M','P'],['G','M','N','R','C','H','L','Q'],['C','L','W'],['R','D','L','Q','J','Z','M','T']

with open('Data.txt') as d: #importing data
    instructions = []
    for line in d:
        temp = []
        temp = [int(x.group()) for x in re.finditer(r'\d+', line)]
        instructions.append(temp)
d.close()

print(instructions)


def item_sort(instruction):
    items = int(instruction[0])
    start = int(instruction[1])
    destination = int(instruction[2])
    for j in range(items):
        array[destination].append(array[start].pop())


for i in range(len(instructions)):
    item_sort(instructions[i])

temp = []
for i in range(len(array)):
    if array[i]:
        temp.append(array[i].pop())
key = ''.join(map(str, temp))

print(array)
print(key)

