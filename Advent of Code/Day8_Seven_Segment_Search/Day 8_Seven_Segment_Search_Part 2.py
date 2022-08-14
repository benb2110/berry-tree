    #                0           2         3          5          6          9
#  signatures = [[2, 3, 3], [1, 2, 2], [2, 3, 3], [1, 3, 2], [1, 3, 2], [2, 4, 3]]

#Method
#format the string
#find the known numbers
#Determine the 6 letter digits by comparing them with known numbers(0, 2, 5, )
#Determine the 5 letter digits by comparing them with known numbers(0, 2, 5, )

t4 = 'egbfac', 'ceg', 'geacd', 'ecbda', 'ebgd', 'dbceag', 'dbgcfea', 'dbacef', 'gadfc', 'ge', 'egc', 'dcbaegf', 'acfgd', 'aegbdc'
t3= 'faegd', 'eb', 'fabe', 'efbdag', 'egb', 'fgbed', 'cbgdea', 'dcfgb', 'cbgefad', 'gfecad', 'adbgcef', 'agfed', 'ebg', 'fbegda'
t2 = 'fegbac', 'debg', 'bgc', 'cadbg', 'gdefca', 'efbagcd', 'dbgcea', 'dfbca', 'caegd', 'bg'
#t = 'adgef', 'bagcf', 'cdea', 'adfebg', 'dfgca', 'adfgec', 'cd', 'fcdgbe', 'cdf', 'cdfegab', 'afgdbe', 'facdg', 'gdfbeac', 'dcea'
#test_data = 'ec', 'cabfe', 'afebd', 'dbagef', 'afbcg', 'feabcd', 'cdef', 'eafdcbg', 'ecb', 'caegdb'
numbers = ['', '', '', '', '', '', '', '', '', '']
#knowns = ['ec', 'cdef', 'ecb', 'eafdcbg']


def identify_unknowns(data):
    numbers = ['', '', '', '', '', '', '', '', '', '']
    knowns = []
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
        if signature_checker(data[i], knowns) == [6, 7]:
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
    return(numbers)


def signature_checker(n, knowns): #Each digit shares a unique number of segments with our four known numbers. Checking this means we can identify the numbers
    sig = [len(n), 0]
    for i in range(len(n)):
        for j in range(3):
            if n[i] in knowns[j]:
                sig[1] += 1
    return sig


#print(signature_checker('feabcd', knowns))
print(identify_unknowns(t4))


