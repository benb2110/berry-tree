instructions = []

with open('Data.txt') as d: #importing data
    for line in d:
        instructions.append(line.split())
d.close()

signal_sums = 0
ref = 20


def signal_check(X, cycle):
    global signal_sums, ref
    if cycle == ref:
        print(cycle * X)
        signal_sums += cycle * X
        ref += 40


def operations(inputs):
    X = 1
    cycle = 0
    for i in range(len(inputs)):
        if str(inputs[i][0]) == 'addx':
            for loop in range(2):
                cycle += 1
                signal_check(X, cycle)
            X += int(inputs[i][1])
        else:
            cycle += 1
            signal_check(X, cycle)


operations(instructions)
print(signal_sums)
