test_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
crab_pos_data = []
l = open('Crab_Positions.txt').read().strip().split(',')
for i in l:
    crab_pos_data.append(int(i))


def innefficient_fuel(n, n2):
    difference = abs(n - n2)
    fuel = 0
    for i in range(difference+1):
        fuel += i
    return fuel


def fuel_efficiency(data):
    fuel_ratings = []
    temp = 0
    for i in range(len(data)):
        fuel_ratings.append(temp)
        temp = 0
        for j in range(len(data)):
            if data[i] == data[j]:
                continue
            temp += innefficient_fuel(data[i], data[j])
    print(fuel_ratings)
    return min(fuel_ratings[1:])


print(fuel_efficiency(test_data))


#print(innefficient_fuel(0, 3))


