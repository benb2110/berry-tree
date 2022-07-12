def bleh(): # prints a diagonal
    for i in range(40):
        print('{0:>{1}}'.format(i, i+5))

def blah(): # prints a grid with numbers on diagonal
    for i in range(20):
        for j in range(20):
            if i == j:
                print('{:^3}'.format(i), end='')
            print(' x ', end='')
        print()

#print(bleh())


def storing_data():
    pass


for i in range(10):
    for j in range(10):
        print('{:>5}'.format(i*j))


