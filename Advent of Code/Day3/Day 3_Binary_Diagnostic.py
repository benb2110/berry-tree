#OPTMISE THIS!(Turn A-L variables into single array)

#test_diagnostic_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
test_diagnostic_report = open('Day 3_Diagnostic_Data.txt').read().split()

a = [word[0] for word in test_diagnostic_report]
b = [word[1] for word in test_diagnostic_report]
c = [word[2] for word in test_diagnostic_report]
d = [word[3] for word in test_diagnostic_report]
e = [word[4] for word in test_diagnostic_report]
f = [word[5] for word in test_diagnostic_report]
g = [word[6] for word in test_diagnostic_report]
h = [word[7] for word in test_diagnostic_report]
i = [word[8] for word in test_diagnostic_report]
j = [word[9] for word in test_diagnostic_report]
k = [word[10] for word in test_diagnostic_report]
l = [word[11] for word in test_diagnostic_report]

data = [a, b, c, d, e, f, g, h, i, j, k, l]
gamma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
epsilon = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# shrink all this down to one loop
for item in range(len(test_diagnostic_report)):
    for jitem in range(0, 12):
        x = data[jitem].count('1')
        y = data[jitem].count('0')
        if x > y:
            gamma[jitem] = 1
        else:
            gamma[jitem] = 0    # I got a nested loop working woohooo!

for item in range(len(test_diagnostic_report)):
    for jitem in range(0, 12):
        x = data[jitem].count('1')
        y = data[jitem].count('0')
        if x < y:
            epsilon[jitem] = 1
        else:
            epsilon[jitem] = 0

#convert to decimal and multiply the gamma and epsilon rate to get fuel consumption
print(gamma)
print(epsilon)
gamma = ''.join(str(i) for i in gamma)
epsilon = ''.join(str(i) for i in epsilon)
print(int(gamma, 2))
print(int(epsilon, 2))
power_consumption = (int(gamma, 2)) * (int(epsilon, 2))
print(power_consumption)
