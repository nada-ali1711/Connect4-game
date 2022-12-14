import numpy as np


ROW = 6
COLUMN = 7
player = 0
AI = 1

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


            # Ask for player2 input
