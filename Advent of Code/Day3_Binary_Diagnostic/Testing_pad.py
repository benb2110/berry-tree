test_diagnostic_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
diagnostic_report = open('Day 3_Diagnostic_Data.txt').read().split()

#Task: Verify 'life support rating' by multiplying 'oxygen generator rating' and the 'CO2 scrubber rating'
#To find 'oxygen genrator rating first identify the most common value in the current bit position and then keeping only numbers with that value
#If 0 and 1 are equally common, keep only 1's

#To find C02 scrubber rating find the least common bit for each bit position and then discard the most common
#If 0 and 1 are equally common, keep only 0's

#Test case working
#Not working with data

diagnostics = diagnostic_report

oxygen_generator_rating = diagnostics
C02_scrubber_rating = diagnostics


def ox_gen_rating(diags, q):
    x = 0
    y = 0
    new_list = []
    for j in range(len(diags)):
        if diags[j][q] == '1':
            x += 1
        else:
            y += 1
    if x >= y:
        for h in range(len(diags)):
            if diags[h][q] == '1':
                new_list.append(diags[h])
        return new_list
    else:
        for h in range(len(diags)):
            if diagnostics[h][q] == '0':
                new_list.append(diags[h])
        return new_list

def c02_scrub_rating(diags, q):
    x = 0
    y = 0
    new_list = []
    for j in range(len(diags)):
        if diags[j][q] == '1':
            x += 1
        else:
            y += 1
    if y <= x:
        for h in range(len(diags)):
            if diags[h][q] == '0':
                new_list.append(diags[h])
        return new_list
    else:
        for h in range(len(diags)):
            if diags[h][q] == '1':
                new_list.append(diags[h])
        return new_list


for q in range(len(diagnostics[0])):
    if len(oxygen_generator_rating) == 1:
        break
    oxygen_generator_rating = ox_gen_rating(oxygen_generator_rating, q)
print(oxygen_generator_rating)

for q in range(len(diagnostics[0])):
    if len(C02_scrubber_rating) == 1:
        break
    C02_scrubber_rating = c02_scrub_rating(C02_scrubber_rating, q)
print(C02_scrubber_rating)


oxygen_generator_rating = ''.join(str(i) for i in oxygen_generator_rating)
C02_scrubber_rating = ''.join(str(i) for i in C02_scrubber_rating)

life_support_rating = (int(oxygen_generator_rating, 2)) * (int(C02_scrubber_rating, 2))
print(life_support_rating)
