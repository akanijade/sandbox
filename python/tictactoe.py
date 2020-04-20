#create a list
board = []
#initialize the board
for i in range(3):
    board.append([" "] * 3)
#print board
def print_board(board):
    for row in board:
        print (" | ".join(row))
        #for col in row:
            #print ("- ".join(col))
print_board(board)
#pick player O or X
def CheckWin(board, x, y):
    if board

row_p1 = int(input("Pick a row: ")) - 1
col_p2 = int(input("Pick a col: ")) - 1
board[row_p1][col_p2] = "O"
print_board(board)
