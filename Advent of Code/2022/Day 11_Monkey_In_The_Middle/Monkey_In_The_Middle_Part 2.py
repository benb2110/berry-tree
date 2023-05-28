##Work in Progress##
#Factor all items store remainders in a monkey inventory list of lists
# for each item store all remainder for the other monkeys  primes also
                        #item 1   #item2   ...
    #monkey0.items = [[m1,m2,m3][m1,m2,m3][...]]

# We can now perform operation on the item and apply to all versions in the list
    #monkey0.items = [[m1+1,m2+1,m3+1][m1,m2,m3][...]]

#Testing the item we use the index for current monkey
    #if monkey[x][x] == 0 then throw to monkey[y]
    #else throw to monkey[z]

#Then move the item to the inventory of monkey[y]
    #monkey[y].items.append(monkey[0][x])


data = []
with open('Data.txt') as d: #importing data
    for line in d:
        data.append(line.split())
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


def print_out(r):  #troubleshoot
    print("Round: " + str(r))
    for m in range(len(monkey_objects)):
        print("Monkey: " + str(m) + str(monkey_objects[m].items))


def create_instances(monkeys):
    monkey = Monkey(int(monkeys[0][1][0]), monkeys[2][4:], int(monkeys[3][3]), int(monkeys[4][5]), int(monkeys[5][5]))
    items = monkeys[1][2:]
    for num in range(len(items)):
        monkey.add_item(int(items[num].strip(',')))
    return monkey


def populate_monkey_items():
    factors = []
    for monkey in monkey_objects:
        factors.append(monkey.test_number)
    for monkey in range(len(monkey_objects)):
        for item in range(len(monkey_objects[monkey].items)):
            item_list = []
            for factor in factors:
                item_list.append(monkey_objects[monkey].items[item] % factor)
            monkey_objects[monkey].add_item(item_list)
        monkey_objects[monkey].items = monkey_objects[monkey].items[int(len(monkey_objects[monkey].items)/2):]


def monkey_operation(m, item):
    monkey = monkey_objects[m]
       #second_value defaults to old ##HEERERE #make sure which old we are multiplying
    operator = monkey.operation[0]

    if monkey.operation[1] != 'old':
        op = int(monkey.operation[1])
        second_value = [op, op, op, op, op, op, op, op]  #this needs work
    else:
        second_value = item

    if operator == '+':
        new_worry = []
        for x in range(len(item)):
            new_worry.append((item[x] + second_value[x]) % monkey_objects[x].test_number)
        return new_worry
    else:
        new_worry = []
        for x in range(len(item)):
            new_worry.append((item[x] * second_value[x]) % monkey_objects[x].test_number)
        return new_worry


#create monkey objects

start = 0
end = len(data)
step = 7
for i in range(start, end, step):
    x = i
    monkey_objects.append(create_instances(data[x:x + step]))
populate_monkey_items()


#rounds loop

def keep_away():
    rounds = 10000
    for r in range(rounds):
        for m in range(len(monkey_objects)):
            monkey = monkey_objects[m]
            spare_list = monkey.items.copy()
            for item in range(len(spare_list)):
                monkey.inspections += 1
                new_worry = monkey_operation(m, spare_list[item])

                if new_worry[m] == 0:
                #    throw to true
                    receiver = monkey.if_true
                    monkey_objects[receiver].items.append(new_worry)
                    monkey.items.pop(0)
                else:
                #    throw to false
                    receiver = monkey.if_false
                    monkey_objects[receiver].items.append(new_worry)
                    monkey.items.pop(0)
        #print_out(r)


keep_away()


result = []

for i in range(len(monkey_objects)):
    result.append(monkey_objects[i].inspections)
result = sorted(result, reverse=True)
print(result[0]*result[1])
