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



    
monkey_list = []

with open('Test Data.txt') as d: #importing data
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


def print_out(r):
    print("Round: " + str(r))
    for m in range(len(monkey_objects)):
        print("Monkey: " + str(m) + str(monkey_objects[m].items))



def item_dist(monkeyitems):
    items = monkeyitems[1][2:]
    for num in range(len(items)):
        for monkey in range(len(monkey_objects)):
            monkey.add_item(int(items[num].strip(',')))
    return monkey



def create_instances(monkeys):
    monkey = Monkey(int(monkeys[0][1][0]), monkeys[2][4:], int(monkeys[3][3]), int(monkeys[4][5]), int(monkeys[5][5]))




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
for i in range(start, end, step): #creates instance of monkeys
    x = i
    monkey_objects.append(create_instances(monkey_list[x:x+step]))

#rounds loop


def keep_away():
    rounds = 10
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
        print_out(r)


keep_away()


for i in range(len(monkey_objects)):
    print(monkey_objects[i].inspections)
