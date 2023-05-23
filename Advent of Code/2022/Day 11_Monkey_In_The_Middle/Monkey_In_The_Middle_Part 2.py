##Work in Progress##

monkey_list = []

with open('Data.txt') as d: #importing data
    for line in d:
        monkey_list.append(line.split())
d.close()


monkey_objects = []


class Monkey:

    def __init__(self, name, operation, test_number, if_true, if_false):
        self.name = name
        self.items = []

        self.operation = operation

        self.test_number = test_number
        self.if_true = if_true
        self.if_false = if_false
        self.inspections = 0

    def add_item(self, item):
        self.items.append(item)


def create_instances(monkeys):

    monkey = Monkey(int(monkeys[0][1][0]), monkeys[2][4:], int(monkeys[3][3]), int(monkeys[4][5]), int(monkeys[5][5]))

    items = monkeys[1][2:]
    for num in range(len(items)):
        monkey.add_item(int(items[num].strip(',')))
    return monkey


def monkey_operation(first_value, second_value, old):
    sec = int(old)
    old = old
    if second_value != 'old':
        sec = int(second_value)

    if first_value == '+':
        return int(old) + sec

    if first_value == '*':
        return int(old) * sec


#create objects

start = 0
end = len(monkey_list)
step = 7
for i in range(start, end, step):
    x = i
    monkey_objects.append(create_instances(monkey_list[x:x+step]))

#rounds loop


def shrink_number(number, prime):
    remainder = number % prime
    return remainder


def keep_away():
    rounds = 1000
    for r in range(rounds):
        for monkey in monkey_objects:
            SPARE_LIST = monkey.items.copy()
            for item in SPARE_LIST:
                monkey.inspections += 1
                new = monkey_operation(monkey.operation[0], monkey.operation[1], item)
                worry = new // 3
                if worry % monkey.test_number:
                    #throw to false
                    receiver = monkey.if_false
                    monkey_objects[receiver].items.append(worry)
                    monkey.items.pop(0)
                else:
                    #throw to true
                    receiver = monkey.if_true
                    monkey_objects[receiver].items.append(worry)
                    monkey.items.pop(0)


keep_away()


for i in range(len(monkey_objects)):
    print(monkey_objects[i].inspections)
