board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
def print_board():
    print(board[0])
    print(board[1])
    print(board[2])


def win_check(player):
    p = player
    for i in range(3):
        for j in range(1):
            if board[i] == [p, p, p]:
                return True
            elif board[j][i] == p and board[j+1][i] == p and board[j+2][i] == p:
                return True
            elif board[0][0] == p and board[1][1] == p and board[2][2] == p or board[0][2] == p and board[1][1] == p and board[2][0] == p:
                return True


def player_turn(player):
    p = player
    z = 0
    while z < 1:
        y = input("Player " + p + ": Which square would you like to place your move? ")
        if y == "end":
            print("Thanks for playing!")
            exit()
        if y == "1":
            if board[0][0] != " ":
                print("That square has already been taken")
                continue
            else:
                board[0][0] = p
        elif y == "2":
            if board[0][1] != " ":
                print("That square has already been taken")
                continue
            else:
                board[0][1] = p
        elif y == "3":
            if board[0][2] != " ":
                print("That square has already been taken")
                continue
            else:
                board[0][2] = p
        elif y == "4":
            if board[1][0] != " ":
                print("That square has already been taken")
                continue
            else:
                board[1][0] = p
        elif y == "5":
            if board[1][1] != " ":
                print("That square has already been taken")
                continue
            else:
                board[1][1] = p
        elif y == "6":
            if board[1][2] != " ":
                print("That square has already been taken")
                continue
            else:
                board[1][2] = p
        elif y == "7":
            if board[2][0] != " ":
                print("That square has already been taken")
                continue
            else:
                board[2][0] = p
        elif y == "8":
            if board[2][1] != " ":
                print("That square has already been taken")
                continue
            else:
                board[2][1] = p
        elif y == "9":
            if board[2][2] != " ":
                print("That square has already been taken")
                continue
            else:
                board[2][2] = p
        elif y is not int:
            print("invalid guess, please choose the number of a square to place your move")
            continue
        else:
            print("invalid guess")
        z += 1


def game():
    while win_check("O") is not True and win_check("X") is not True:
        print_board()
        player_turn("O")
        if win_check("O") is True:
            print_board()
            print("Player 0 has won the game!")
            break
        print_board()
        player_turn("X")
        if win_check("X") is True:
            print_board()
            print("Player X has won the game!")
            break


while True: #Game Start Loop
    game()
    x = input("Would you like to restart? X(Yes) or O(No) ")
    if x == "X":
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    elif x == "O":
        exit()
