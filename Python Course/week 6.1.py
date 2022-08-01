draw = [2, 3, 4, 8, 0, 1, 5]
boards = [[1, 4, 5], [3, 7, 8], [4, 0, 2], [3, 5, 7], [9, 2, 7], [5, 4, 9]]


def win_cond(board):
    for i in range(len(boards)):
        if board[i] == ['X', 'X', 'X']:
            return True
    return False


def marking(n):
    for i in range(len(boards)):
        for j in range(len(boards[0])):
            if boards[i][j] == n:
                boards[i][j] = 'X'
                if win_cond(boards) is True:
                    return boards
    return boards


for k in draw:
    if win_cond(boards) is True:
        break
    boards = marking(k)



print(boards)

