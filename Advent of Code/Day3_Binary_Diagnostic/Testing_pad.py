test_diagnostic_report = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
#diagnostic_report = open('Day 3_Diagnostic_Data.txt').read().split()

#Task: Verify 'life support rating' by multiplying 'oxygen generator rating' and the 'CO2 scrubber rating'
#To find 'oxygen genrator rating first identify the most common value in the current bit position and then keeping only numbers with that value
#If 0 and 1 are equally common, keep only 1's

#To find C02 scrubber rating find the least common bit for each bit position and then discard the most common
#If 0 and 1 are equally common, keep only 0's


#Method
#Parse the numbers and first most common value
#Parse the numbers and remove all other values
#Continue to next bit position

print(max(test_diagnostic_report))
print(test_diagnostic_report[1].count('0'))

