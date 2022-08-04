board = [None, " ", " ", " ", " ", " ", " ", " ", " ", " "]


def print_board():
    print(board[1:4:])
    print(board[4:7:])
    print(board[7:10:])


def win_check(player):
    p = player
    for i in range(9):
        if board[i:i+3] == [p, p, p]:
            return True
        if board[1::3] == [p, p, p] or board[2::3] == [p, p, p] or board[3::3] == [p, p, p]:
            return True
        if board[1::4] == [p, p, p] or board[3:8:2] == [p, p, p]:
            return True


def player_turn(player):
    p = player
    z = 0
    valid_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while z < 1:
        y = input("Player " + p + ": Which square would you like to place your move? ")
        if y == "end":
            print("Thanks for playing!")
            exit()
        elif y not in valid_input:
            print("Input not valid: Please enter a number from 1 to 9")
            continue
        elif board[int(y)] != " ":
            print("That square has already been taken")
            continue
        else:
            board[int(y)] = p
        z += 1


def game(): #Gameloop
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


while True: #Start & Restart gameloop
    game()
    x = input("Would you like to restart? X(Yes) or O(No) ")
    if x == "X":
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    elif x == "O":
        exit()
