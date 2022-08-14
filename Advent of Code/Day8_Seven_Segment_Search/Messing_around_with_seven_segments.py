#  a
# b  c
#  d
# e  f
#  g

#This approach involves comparing the segments in each unknown number against our four known numbers (1, 4, 7, 8). if the segment is shared
# we append True into its signature.
# It turns out each unknown number has a unique combination of shared segments with numbers (1, 4, 7)

    #6 letters
#zero   2, 3, 3  =8 #Zero and Nine shares two 2 segments with One, but six uniquely shares 1
#six    1, 3, 2  =6
#nine   2, 4, 3  =9

    #5 letters
#two    1, 2, 2  =5
#three  2, 3, 3  =8
#five   1, 3, 2  =6

    #                0           2         3          5          6          9
#  signatures = [[2, 3, 3], [1, 2, 2], [2, 3, 3], [1, 3, 2], [1, 3, 2], [2, 4, 3]]

#Now that we know the signatures for our unknown numbers we can compare them with the knowns and output the correct ones

test_data = 'ec', 'cabfe', 'afebd', 'dbagef', 'afbcg', 'feabcd', 'cdef', 'eafdcbg', 'ecb', 'caegdb',

            #    0       1      2        3        4       5        6        7        8          9
#segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

unknowns = ['abcefg', 'acdeg', 'acdfg', 'abdfg', 'abdefg', 'abcdfg', '']
knowns = ['cf', 'bcdf', 'acf', 'abcdefg']


numbers = ['', '', '', '', '', '', '', '', '', '']


def known_numbers(segs):
    kn = ['', '', '', '', '', '', '', '', '', '']
    for i in range(len(segs)):
        if len(segs[i]) == 2:
            kn[1] = segs[i]
        if len(segs[i]) == 3:
            kn[7] = segs[i]
        if len(segs[i]) == 4:
            kn[4] = segs[i]
        if len(segs[i]) == 7:
            kn[8] = segs[i]
    return kn


def in_common(string):
    sig = []
    temp = None
    for i in range(len(string)):
        sig.append(temp)
        temp = [0, 0, 0]
        for k in range(3):
            for j in range(len(string[i])):
                if string[i][j] in knowns[k]:
                    temp[k] += 1
    return sig[1:]


def identify_unknowns(data):
    pass


signatures = in_common(unknowns)
print(signatures)

#numbers = known_numbers(test_data)
#print(numbers)




