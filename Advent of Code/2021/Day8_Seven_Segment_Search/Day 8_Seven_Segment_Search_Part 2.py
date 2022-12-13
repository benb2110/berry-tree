
display_data = []

with open('Display_Data.txt') as d: #importing data
    for line in d:
        display_data.append(line.strip().split('|'))
d.close()


temp = []

for j in range(len(display_data)): #string manupilation for data
    for k in range(len(display_data[j])):
        temp.append(display_data[j][k].split(' '))
display_data = temp
del temp


def identify_unknowns(data, code): #organises each scrambled signal into its correct position
    numbers = ['', '', '', '', '', '', '', '', '', '']
    for i in range(len(data)):
        if len(data[i]) == 2:
            numbers[1] = data[i]
        if len(data[i]) == 3:
            numbers[7] = data[i]
        if len(data[i]) == 4:
            numbers[4] = data[i]
        if len(data[i]) == 7:
            numbers[8] = data[i]

    knowns = [numbers[1], numbers[4], numbers[7], numbers[8]]
    for i in range(len(data)):
        if signature_checker(data[i], knowns) == [6, 8]:
            numbers[0] = data[i]
        if signature_checker(data[i], knowns) == [6, 6]:
            numbers[6] = data[i]
        if signature_checker(data[i], knowns) == [6, 9]:
            numbers[9] = data[i]
        if signature_checker(data[i], knowns) == [5, 5]:
            numbers[2] = data[i]
        if signature_checker(data[i], knowns) == [5, 8]:
            numbers[3] = data[i]
        if signature_checker(data[i], knowns) == [5, 6]:
            numbers[5] = data[i]
    return code_solver(numbers, code)


def signature_checker(n, knowns): #Each digit shares a unique number of segments with our four known numbers. Checking this means we can identify the unknown numbers
    sig = [len(n), 0]
    for i in range(len(n)):
        for j in range(3):
            if n[i] in knowns[j]:
                sig[1] += 1
    return sig


def code_solver(key, code):
    output = ''
    for i in range(len(code)):
        for k in range(10):
            if sorted(code[i]) == sorted(key[k]):
                output += str(k)

    return output


total = 0
q = 0
for i in range(200):
    total += int(identify_unknowns(display_data[q], display_data[q+1]))
    q += 2

print(total)





