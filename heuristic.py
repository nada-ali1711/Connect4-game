import random
import numpy as np


ROW = 6
COLUMN = 7
player = 0
AI = 1
AI_PIECE = 2
PLAYER_PIECE = 1
empty=0

def creat_board():
    board = np.zeros((ROW,COLUMN))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW-1][col]==0

def get_next_open_row(board, col):
    for r in range(ROW):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_game(board, piece):
    # check horizontally
    for c in range(COLUMN-3):
        for r in range(ROW):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # check vertically
    for r in range(ROW-3):
        for c in range(COLUMN):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

        ## Score posiive sloped diagonal
        for r in range(ROW - 3):
            for c in range(COLUMN - 3):
                window = [board[r + i][c + i] for i in range(4)]
                score += evaluate_window(window, piece)

        for r in range(ROW - 3):
            for c in range(COLUMN - 3):
                window = [board[r + 3 - i][c + i] for i in range(4)]
                score += evaluate_window(window, piece)

    # check positively sloped diagonls
    for c in range(COLUMN-3):
        for r in range(ROW-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # check negatively sloped diagonals
    for c in range(COLUMN-3):
        for r in range(ROW - 3):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def heuristic(board, piece):
    score=0
    #check horizontal
    for r in range(ROW):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMN-3):
            window = row_array[c:c+4]
            if window.count(piece) == 4:
                score+=100
            elif window.count(piece) == 3 and window.count(empty) == 1:
                score+=10
    return score
    #CHECK VERTICAL
    for c in range(COLUMN):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range (row-2):
            window = col_array[r:r+4]
            if window.count(piece) == 4:
                score+=100
            elif window.count(piece) == 3 and window.count(empty) == 1:
                score+=10

def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN):
        if is_valid_location(board,col):
            valid_locations.append(col)
        return valid_locations

def best_move(board, piece):
    best_score=0
    valid_locations = get_valid_locations(board)
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board,row,col,piece)
        score = heuristic(temp_board,piece)
        if score > best_score:
            best_score = score
            best_col = col
    return best_col





