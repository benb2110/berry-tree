##Work in Progress##
#Factor all items store remainders in a monkey inventory list of lists
# for each item store all remainder for the other monkeys  primes also
                        #item 1   #item2   ...
    #monkey0.items = [[m1,m2,m3][m1,m2,m3][...]]

# We can now perform operation on the item and apply to all versions in the list
    #monkey0.items = [[m1+1,m2+1,m3+1][m1,m2,m3][...]]

#Testing the item we use the index for current monkey
    #if monkey[0][x] == 0 then throw to monkey[y]
    #else throw to monkey[z]

#Then move the item to the inventory of monkey[y]
    #monkey[y].items.append(monkey[0][x])
    
data = []
with open('Test Data.txt') as d: #importing data
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


def print_out(r):
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
            for factor in range(len(factors)):
                item_list.append(monkey_objects[monkey].items[item] % factors[factor])
            #print(item_list)
            monkey_objects[monkey].add_item(item_list)
        monkey_objects[monkey].items = monkey_objects[monkey].items[int(len(monkey_objects[monkey].items)/2):]


def monkey_operation(i, old):
    monkey = monkey_objects[i]
    sec = int(old[i]) #check this

    if monkey.operation[1] != 'old':
        sec = int(monkey.operation[1])

    if monkey.operation[0] == '+':  #must recalculate % after operation
        new_worry = []
        for z in range(len(old)):
            new_worry.append((old[z] + sec) % monkey_objects[z].test_number)
        print(new_worry)
        return new_worry
    elif monkey.operation[0] == '*':
        new_worry = []
        for x in range(len(old)):
            new_worry.append((old[x] * sec) % monkey_objects[x].test_number)
        print(new_worry)
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
    rounds = 20
    for r in range(rounds):
        for m in range(len(monkey_objects)):
            SPARE_LIST = monkey_objects[m].items.copy()
            for item in SPARE_LIST:
                monkey_objects[m].inspections += 1
                print(str(m) + " " + str(item))
                new_worry = monkey_operation(m, item)

                if new_worry[m] == 0:
                    #throw to true
                    receiver = monkey_objects[m].if_true
                    monkey_objects[receiver].items.append(new_worry)
                    monkey_objects[m].items.remove(item)
                #else:
                #    #throw to false
                    receiver = monkey_objects[m].if_false
                    monkey_objects[receiver].items.append(new_worry)
                    monkey_objects[m].items.remove(item)
        #print_out(r)


keep_away()
result = []
answer = [99, 97, 8, 103]
for i in range(len(monkey_objects)):
    result.append(monkey_objects[i].inspections)

a = result == answer
print(a)
