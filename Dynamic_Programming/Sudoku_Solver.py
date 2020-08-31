""" 
Python Sudoku Code with backtracking
 """

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == 0):
                return i,j
    return False

def is_valid(row,column,number,board):
    """ 
    We need to check this square, columns and rows
     """
    sqr = row // 3 
    sqc = column // 3
    for i in range(9):
        if (i !=column  and board[row][i] == number):
            return False
        if (i!= row and board[i][column] == number):
            return False
    for i in range(3):
        for j in range(3):
            if (board[3*sqr + i][3*sqc + j] == number and (3*sqr + i!=row or 3*sqc + j!=column)):
                return False
    return True


def solve(board):
    x = find_empty(board)
    if (x == False):
        return True
    else:
        e_r,e_c = x
    for number in range(1,10):
        if (is_valid(e_r,e_c,number,board)):
            board[e_r][e_c] = number
            if (solve(board)):
                return True
            board[e_r][e_c] = 0
    return False

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
print_board(board)
print(solve(board))
print_board(board)
