instructions = []

with open('Data.txt') as d: #importing data
    for line in d:
        instructions.append(line.split())
d.close()
print(instructions)


board = []
for width in range(500):
    line = []
    for length in range(500):
        line.append('.')
    board.append(line)

board[250][250] = '#'


snail_trail = board

Head = [250, 250]
Tail = [250, 250]


def rope_sim(direction, moves):
    global Head, Tail
    prev = [None, None]
    for i in range(moves):
        prev[0], prev[1] = Head[0], Head[1]
  #calculate H movement
        if direction == 'U':
            Head[0] -=1
            print("up")
        elif direction == 'D':
            Head[0]+=1
            print("down")
        elif direction == 'L':
            Head[1]-=1
            print("left")
        elif direction == 'R':
            Head[1] +=1
            print("right")
  #calculate T movement and store
        if abs(Tail[0] - Head[0]) > 1 or abs(Tail[1] - Head[1]) > 1:
            Tail[0], Tail[1] = prev[0], prev[1]
            y = Tail[0]
            z = Tail[1]
            snail_trail[y][z] = '#'


for i in range(len(instructions)):
    rope_sim(instructions[i][0], int(instructions[i][1]))


move_count = 0
for i in range(len(snail_trail)):
    for j in range(len(snail_trail[0])):
        if snail_trail[i][j] == '#':
            move_count += 1

print(move_count)
