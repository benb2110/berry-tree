#  a
# b  c
#  d
# e  f
#  g

#This approach involves comparing the segments in each unknown number against our four known numbers (1, 4, 7, 8). if the segment is shared
# we get append True into its signature.
# It turns out each unknown number has a unique combination of shared segments with numbers (1, 4, 7)

    #6 letters
#zero   2, 3, 3   #Zero and Nine shares two 2 segments with One, but six uniquely shares 1
#six    1, 3, 2
#nine   2, 4, 3

    #5 letters
#two    1, 2, 2
#three  2, 3, 3
#five   1, 3, 2

#Now that we know the signatures for our unknown numbers we can compare them with the knowns and output the correct ones


#segments = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

unknowns = ['abcefg', 'acdeg', 'acdfg', 'abdfg', 'abdefg', 'abcdfg']
knowns = ['cf', 'bcdf', 'acf', 'abcdefg']

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


def in_common2(string):
    sig = [],[],[],[],[],[]
    for i in range(len(string)):
        for k in range(3):
            temp = []
            sig[i].append(temp)
            for j in range(len(string[i])):
                if string[i][j] in knowns[k]:
                    temp.append(True)
    return sig



def in_common2(string):
    sig = [],[],[],[],[],[]
    for i in range(len(string)):
        for k in range(3):
            temp = []
            sig[i].append(temp)
            for j in range(len(string[i])):
                if string[i][j] in knowns[k]:
                    temp.append(True)
    return sig


signatures = in_common2(unknowns)

print(signatures)

