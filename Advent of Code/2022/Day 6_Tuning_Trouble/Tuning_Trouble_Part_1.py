data = []


with open('Data.txt') as d: #importing data
    for line in d:
        data.append(str(line))
d.close()

data = data[0]



def unique_string(string):
    flag_count = 0
    if len(string) == 4:
        for i in range(4):
            for j in range(4):
                if string[j-1] == string[i-1]:
                    flag_count += 1
    else:
        return False

    if flag_count == 4:
        return True
    else:
        return False


def signal_start(signal):
    packet_markers = []
    for i in range(len(signal)):
        if unique_string(signal[i-4:i]):
            packet_markers.append(i)
    return packet_markers

print(signal_start(data))
