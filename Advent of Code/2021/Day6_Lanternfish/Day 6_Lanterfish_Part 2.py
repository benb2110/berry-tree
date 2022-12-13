test_lanternfish_data = [3, 4, 3, 1, 2]

    #      0  1  2  3  4  5  6  7  8(new)
cohorts = [0, 0, 0, 0, 0, 0, 0, 0, 0]


l = open('Lanternfish_Numbers.txt').read().strip().split(',')
for i in l:
    cohorts[int(i)] = cohorts[int(i)] + 1
#close txt, delete l


def optimised_breeding(data):
    day = 0
    while day != 256:
        temp = data[0]
        data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8] = data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[0]
        data[6] = data[6] + temp
        day += 1
        print(day)
        print(data)
    return sum(data[:])


print(optimised_breeding(cohorts))
