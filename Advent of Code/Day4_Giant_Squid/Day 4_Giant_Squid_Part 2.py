#Importing the boards
b = open('Boards.txt').read().strip().split()
n = 0
board = []
while n < (len(b)):
    for i in range(5):
        line = []
        board.append(line)
        for j in range(5):
            items = []
            line.append(items)
            for k in range(5):
                items.append(int(b[n]))
                n += 1

#Importing the draw
d = open('Numbers.txt').read().strip().split(',')
draw = []
for i in d:
    draw.append(int(i))


test_data = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
test_boards = [[[22, 13, 17, 11,  0], [8,  2, 23,  4, 24], [21,  9, 14, 16,  7],[6, 10,  3, 18,  5],[1, 12, 20, 15, 19]],
[[3, 15,  0,  2, 22],
 [9, 18, 13, 17,  5],
[19,  8,  7, 25, 23],
[20, 11, 10, 24,  4],
[14, 21, 16, 12,  6]],

[[14, 21, 17, 24,  4],
[10, 16, 15,  9, 19],
[18,  8, 23, 26, 20],
[22, 11, 13,  6,  5],
 [2,  0, 12,  3, 7]]]

def winning_board(boards): #Checks the boards for horizontal win or vertical, then returns the winning board
    for k in range(len(boards)):
        for i in range(5):
            vert = []
            if boards[k][i] == ['X', 'X', 'X', 'X', 'X']:  #Horizontal victory
                print("Hor: board[" + str(k) + "] is the winning board")
                return k
            for j in range(5):
                vert.append(boards[k][j][i])
            if vert == ['X', 'X', 'X', 'X', 'X']: #Checks Vertical Victory
                print("Vert: board[" + str(k) + "] is the winning board")
                return k
    return None

def number_draw(draw, boards): #Checks each spot on the boards for the draw number, and then checks for a win, and then checks the score
    for i in range(len(draw)):
        for j in range(len(boards)):
            for h in range(5):
                for k in range(5):
                    if draw[i] == boards[j][h][k]:
                        boards[j][h][k] = 'X'
                        winner = winning_board(boards)
                        if winner is not None:
                            if len(boards) >= 2:
                                new_boards = boards
                                new_boards.remove(new_boards[winner])
                                new_nums = draw[i:]
                                return number_draw(new_nums, new_boards) #testing recursion
                            else:  #find score of last board
                                winning_number = draw[i]
                                score = 0
                                for k in range(5):
                                    for h in range(5):
                                        if boards[winner][h][k] == 'X':
                                            continue
                                        else:
                                            score += boards[winner][h][k]
                                score = score * winning_number
                                return score

#print(number_draw(test_data, test_boards))
print(number_draw(draw, board))
