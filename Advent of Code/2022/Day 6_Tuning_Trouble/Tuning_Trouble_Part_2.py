data = []

with open('Data.txt') as d: #importing data
    for line in d:
        data.append(str(line))
d.close()

data = data[0]


def unique_string(string):
    flag_count = 0
    if len(string) == 14:
        for i in range(14):
            for j in range(14):
                if string[j-1] == string[i-1]:
                    flag_count += 1
    if flag_count == 14:
        return True

    return False


def signal_start(signal):
    for i in range(len(signal)):
        if unique_string(signal[i-14:i]):
            return i


print(signal_start(data))
