test_diagnostic_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
diagnostic_report = open('Day 3_Diagnostic_Data.txt').read().split()

#Task: Verify 'life support rating' by multiplying 'oxygen generator rating' and the 'CO2 scrubber rating'
#To find 'oxygen genrator rating first identify the most common value in the current bit position and then keeping only numbers with that value
#If 0 and 1 are equally common, keep only 1's

#To find C02 scrubber rating find the least common bit for each bit position and then discard the most common
#If 0 and 1 are equally common, keep only 0's


#Method
#Parse the numbers and first most common value
#Parse the numbers and remove all other values
#Continue to next bit position

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
print(diagnostics)
#print(len(diagnostics[0][0])) #len diag = 12


oxygen_generator_rating = []
C02_scrubber_rating = []

def ox_gen_rating(diagnostics):
    for i in range(len(diagnostics[0][0])):
        x = 0
        y = 0
        for j in range(len(diagnostics)):
            if diagnostics[j][0][i] == '1':
                x += 1
            else:
                y += 1


        print(x, y)
    return diagnostics

print(ox_gen_rating(diagnostics))



#for i in range(len(diagnostics[0][0])):
#    x = 0
#    y = 0
#    for j in range(len(diagnostics)):
#        if diagnostics[j][0][i] >= '1':
#            x += 1
#        else:
#            y += 1
#if x >= y:
#    oxygen_generator_rating.append([1])
#else:
#    oxygen_generator_rating.append([0])




print(oxygen_generator_rating)



#we want to check 1.1, 2.1, 3.1, 4.1, 5.1, 6.1 {write most common} , 1.2, 2.2, 3.2, 4.2, 5.2, 6.2 {write most common} , 1,3...
