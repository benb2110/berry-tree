#  a
# b  c
#  d
# e  f
#  g

#segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

zero = 'abcefg'
one = 'cf'
two = 'acdeg'
three = 'acdfg'
four = 'bcdf'
five = 'abdfg'
six = 'abdefg'
seven = 'acf'
eight = 'abcdefg'
nine = 'abcdfg'


def in_common(n): # outputs 4 unique bool signatures
    sig = [], [], []
    for i in range(len(n)):
        if n[i] in one:
            sig[0].append(True)
        else:
            sig[0].append(False)
    for j in range(len(n)):
        if n[j] in four:
            sig[1].append(True)
        else:
            sig[1].append(False)
    for k in range(len(n)):
        if n[k] in seven:
            sig[2].append(True)
        else:
            sig[2].append(False)

    return sig



zero_sig = in_common(zero)
one_sig = in_common(one)
two_sig = in_common(two)
three_sig = in_common(three)
four_sig = in_common(four)
five_sig = in_common(five)
six_sig = in_common(six)
seven_sig = in_common(seven)
eight_sig = in_common(eight)
nine_sig = in_common(nine)

#print(zero_sig)   #6
#print(one_sig)
print(two_sig)  #5
print(three_sig)  #5
#print(four_sig)
print(five_sig)   #5
#print(six_sig)   #6
#print(seven_sig)
#print(eight_sig)
#print(nine_sig)   #6

    #6 letters
#zero   2, 3, 3
#six    1, 3, 2
#nine   2, 4, 3

    #5 letters
#two    1, 2, 2
#three  2, 3, 3
#five   1, 3, 2
