elfinvent = []
with open('Calorie_Data.txt') as d: #importing data
    temp = 0
    for line in d:
        if line.strip():
            temp += int(line)
        else:
            elfinvent.append(temp)
            temp = 0
    elfinvent.append(temp)

d.close()


elfinvent.sort()
stockpile = elfinvent[-1]+elfinvent[-2]+elfinvent[-3]

print(elfinvent)
print(stockpile)
