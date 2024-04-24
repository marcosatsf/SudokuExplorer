import os
import sys
import time

WAIT_PERIOD = 1e-7
BOARD_INPUT = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


def isValidSudoku(board) -> bool:
    return isValidSudoku_with_positions(board, 0,0)
    
def filled_all_blank_spaces(board):
    for i in board:
        for j in i:
            if j == '.':
                return False
    return True

def minor_square(board,x,y):
    x_floor, y_floor = (x//3)*3, (y//3)*3
    mini_board_flattened = []
    for x_list in board[x_floor:x_floor+3]:
        mini_board_flattened.extend(x_list[y_floor:y_floor+3])
    return mini_board_flattened


def is_valid_pos(value, board, x, y):
    if not value in board[x]:
        if not value in [row[y] for row in board]:
            if not value in minor_square(board, x, y):
                return True
    return False
    

def next_position(x,y):
    if y < 8:
        return x,y+1
    else:
        return x+1,0

def print_current_state(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print(row)
    time.sleep(WAIT_PERIOD)


def isValidSudoku_with_positions(board, x, y):
    if filled_all_blank_spaces(board):
        return board
    
    print_current_state(board)

    if board[x][y] == '.':
        for choice in range(1,10):
            str_choice = str(choice)
            if is_valid_pos(str_choice, board, x, y):
                board[x][y] = str_choice
                if isValidSudoku_with_positions(board, *next_position(x,y)):
                    return board
                board[x][y] = '.'   
    else:
        return isValidSudoku_with_positions(board, *next_position(x,y))


print_current_state(isValidSudoku(BOARD_INPUT))