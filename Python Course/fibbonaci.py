fterm = 0
sterm = 1
temp = 0
i = 0

while i < 40:
    print(fterm, end = ' ')
    temp = sterm
    sterm = fterm + sterm
    fterm = temp
    i += 1

