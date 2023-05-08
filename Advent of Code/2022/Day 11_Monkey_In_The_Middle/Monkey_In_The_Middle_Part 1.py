##Work in Progress##

monkeys = []

with open('Data.txt') as d: #importing data
    for line in d:
        monkeys.append(line.split())
d.close()

print(monkeys)

rounds = 20


class Monkey:
    name = "None"
    inspection_count = 0
    items = []     #FILO list of items
    operation = None

    test_number = None    #divisble by (int)

    if_true = None         #If true throw to monkey (int)
    if_false = None        #If false throw to monkey (int)

    def __init__(self, name, items, operation, test_number, if_true, if_false):
        self.name = name
        self.items = items
        self.operation = operation
        self.test_number = test_number
        self.if_true = if_true
        self.if_false = if_false


def create_instances(monkeys):
    for i in range(4):
        if i == 0:
            Monkey.name = monkeys[i][1][1]
            pass
        if i == 1:
            pass
            #for j in range(len(monkeys[1]-2)):
        if i == 2:
            pass
        if i == 3:
            pass
        if i == 4:
            pass



#1: Initialise monkey name -- monkeys[0][1][1] (int?/string?)
#2: Add items -- #for i in range(len(monkeys[1]-2))   (list)
#3 add operation -- monkeys[2][3:] (string?)
#4 Add test -- monkeys[3][3] (int)
#5 Add true condition -- monkeys[4][5](int)
#6 Add false condition -- monkeys[5][5] (int)
