test_lanternfish_data = [3, 4, 3, 1, 2]
lanternfish_data = []
l = open('Lanternfish_Numbers.txt').read().strip().split(',')
for i in l:
    lanternfish_data.append(int(i))


print(lanternfish_data)
print(test_lanternfish_data)


def lanternfish_breeding(data):
    day = 0
    while day != 80:
        for i in range(len(data)):
            if data[i] == 0:
                data.append(8)
                data[i] = 6
            else:
                data[i] -= 1
        day += 1
    return len(data)


#print(lanternfish_breeding(test_lanternfish_data))
print(lanternfish_breeding(lanternfish_data))
