monkeys = []

with open('Data.txt') as d: #importing data
    for line in d:
        monkeys.append(line.strip())
d.close()

print(monkeys)
