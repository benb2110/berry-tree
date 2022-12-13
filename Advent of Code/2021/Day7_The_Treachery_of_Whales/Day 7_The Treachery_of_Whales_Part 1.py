test_data = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
crab_pos_data = []
l = open('Crab_Positions.txt').read().strip().split(',')
for i in l:
    crab_pos_data.append(int(i))
print(crab_pos_data)

def fuel_efficient_pos(data):
    fuel_ratings = []
    temp = 0
    for i in range(len(data)):
        fuel_ratings.append(temp)
        temp = 0
        for j in range(len(data)):
            if data[i] == data[j]:
                continue
            temp += abs(data[i]-data[j])

    return min(fuel_ratings[1:])


print(fuel_efficient_pos(crab_pos_data))
