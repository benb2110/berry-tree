duties = []
with open('Data.txt') as d: #importing data
    for line in d:
        duties.append(line.strip())
d.close()

#result = [x.split('-',) for x in duties]
print(duties)

def overlap_counter(data):
    count = 0
    for i in range(len(result)):
        if result[i][0][0] <= result[i][1][0] and result[i][0][2] >= result[i][1][2]:
            count += 1
            print(result[i])
        elif result[i][0][0] >= result[i][1][0] and result[i][0][2] <= result[i][1][2]:
            count += 1
            print(result[i])
    return count

#print(result[0][0])
#print(result[0][1])
print(overlap_counter(result))

#if a =< x and b =>y or a =>x and b=<y

#Counter is taking single digits, must convert to ints
