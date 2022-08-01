
#Method
#Draw number from draw
#Find every instance of number in boards
#Mark every instance of number in mark_boards
#Remove numbers in board_scores by marking as 'X'
#Check for a winner by checking rows and columns in mark_boards
#Repeat until a winner is found

#When a winning board is found
#SUM_UNMARKED NUMBERS * DRAW NUMBER

#draw = open('Numbers.txt').read().split()
#boards = open('Boards.txt').read().split()

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

test_board_marks = []
test_board_score = []
def mark_boards(locations): # A COPY OF THE ARRAY WITH JUST ' ' & 'X' DENOTING THE FOUND NUMBERS
    pass
def board_scores(draw): # A COPY OF THE ARRAY WITH JUST UNDRAWN NUMBERS LEFT
    pass
def win_cond(boards): # CHECKS MARK_BOARDS FOR 5 IN A ROW
    pass
def winner_score(board):
    pass



print(test_boards)

