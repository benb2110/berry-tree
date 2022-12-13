elfinvent = []
with open('Calorie_Data.txt') as d: #importing data
    temp = 0
    for line in d:
        if line.strip():
            temp += int(line)
        else:
            elfinvent.append(temp)
            temp = 0
d.close()

print(elfinvent)
print(max(elfinvent))
