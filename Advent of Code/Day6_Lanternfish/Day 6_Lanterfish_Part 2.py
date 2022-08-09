test_lanternfish_data = [3, 4, 3, 1, 2]
lanternfish_data = []
l = open('Lanternfish_Numbers.txt').read().strip().split(',')
for i in l:
    lanternfish_data.append(int(i))

    #      0  1  2  3  4  5  6  7
cohorts = [0, 1, 1, 2, 1, 0, 0, 0,]

#print(lanternfish_data)
#print(test_lanternfish_data)


def optimised_breeding(data):
    day = 1
    while day != 256:
        temp = data[0]
        data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], =  data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[0]
        data[6] = data[6] + temp
        day += 1
        print(day)
        print(data)
    return sum(data[:])


#print(lanternfish_breeding(test_lanternfish_data))
#print(lanternfish_breeding(lanternfish_data))
print(optimised_breeding(cohorts))
