instructions = []

with open('Test Data2.txt') as d: #importing data
    for line in d:
        instructions.append(line.split())
d.close()
print(instructions)

board = []
with open('Board.txt') as b: #importing data
    for line in b:
        board.append(line.split())
        line = []
        for character in line:
            line.append(str(character))

d.close()
print(board)

start = 0


length = len(board[0])
width = len(board[0][0])
print(length)
print(width)
start = [15, 12]
print(board[0][15][11])

#board = []
#for width in range(board_size):
#    line = []
#    for length in range(board_size):
#        line.append('.')
#    board.append(line)


Rope = [[start, start], [start, start], [start, start], [start, start], [start, start], [start, start], [start, start], [start, start], [start, start]]


def rope_sim(direction, moves):
    global Rope
    prev = Rope
    for move in range(moves):
  #calculate H movement
        if direction == 'U':
            Rope[0][0] -= 1
            print("up")
        elif direction == 'D':
            Rope[0][0] += 1
            print("down")
        elif direction == 'L':
            Rope[0][1] -= 1
            print("left")
        elif direction == 'R':
            Rope[0][1] += 1
            print("right")
  #calculate T movement and store
        for knot in range(8):
            if abs(Rope[knot+1][0] - Rope[knot][0]) > 1 or abs(Rope[knot+1][1] - Rope[knot][1]) > 1: #Calculating movement for 9 segments
                Rope[knot+1][0], Rope[knot+1][1] = prev[knot][0], prev[knot][1]
        y = Rope[8][0]
        z = Rope[8][1]
        if board[y][z] == '.':
            board[y][z] = '#'

#for instruction in range(len(instructions)): #Input each instruction and simulates the movement of the rope
#    rope_sim(instructions[instruction][0], int(instructions[instruction][1]))


move_count = 0
for length in range(len(board)):
    for width in range(len(board[0])):
        if board[length][width] == '#':
            move_count += 1

print(move_count)

