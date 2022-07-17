#assert(1+1 == 3)

#assert(1+1 == 3), 'One and one is two'

lines = [1, 4, 6, 3, 2, 56, 3, 5]
with open('sometext.txt', 'wt') as f:
    for i in lines:
        f.write(', {:0>8}'.format(i))

for i in range(11):
    if i % 5:
        print('_', end=' ')
    else:
        print('+', end=' ')
for i in range(11):
    if i % 5:
        print(' ', end=' ')
    else:
        print('|', end=' ')
