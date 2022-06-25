test_diagnostic_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
diagnostic_report = open('Day 3_Diagnostic_Data.txt').read().split()

#Task: Verify 'life support rating' by multiplying 'oxygen generator rating' and the 'CO2 scrubber rating'
#To find 'oxygen genrator rating first identify the most common value in the current bit position and then keeping only numbers with that value
#If 0 and 1 are equally common, keep only 1's

#To find C02 scrubber rating find the least common bit for each bit position and then discard the most common
#If 0 and 1 are equally common, keep only 0's




def diagnostics_convert(diagnostics):
    data_set = []
    for i in range(len(diagnostics[0])):
        data = []
        for j in range(len(diagnostics)):
            data.append([diagnostics[j]])
    data_set.append(data)
    return data_set[0] #Creates an extra list element: Fix! but working

diagnostics = diagnostics_convert(test_diagnostic_report)  #test
#diagnostics = diagnostics_convert(diagnostic_report)
print(diagnostic_report)



oxygen_generator_rating = diagnostics
C02_scrubber_rating = diagnostics


def ox_gen_rating(diags, q):
    x = 0
    y = 0
    new_list = []
    for j in range(len(diags)):
        if oxygen_generator_rating[j][0][q] == '1':
            x += 1
        else:
            y += 1
    if x >= y:
        for h in range(len(diags)):
            if oxygen_generator_rating[h][0][q] == '1':
                new_list.append(diags[h])
        return new_list
    elif y > x:
        for h in range(len(diags)):
            if diagnostics[h][0][q] == '0':
                new_list.append(diags[h])
        return new_list


def c02_scrubb_rating(diags, q):
    x = 0
    y = 0
    new_list = []
    for j in range(len(diags)):
        if C02_scrubber_rating[j][0][q] == '1':
            x += 1
        else:
            y += 1
    if y <= x:
        for h in range(len(diags)):
            if C02_scrubber_rating[h][0][q] == '0':
                new_list.append(diags[h])
        return new_list
    elif x < y:
        for h in range(len(diags)):
            if diagnostics[h][0][q] == '1':
                new_list.append(diags[h])
        return new_list


for q in range(5):
    oxygen_generator_rating = ox_gen_rating(oxygen_generator_rating, q)
print(oxygen_generator_rating)

#for q in range(5):
    #C02_scrubber_rating = c02_scrubb_rating(C02_scrubber_rating, q)
#print(C02_scrubber_rating)



