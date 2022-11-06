import numpy as np
import pygame
import sys
import math

ROW = 6
COLUMN = 7
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,100)
SQUARESIZE = 100

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
    #check horizontally
    for c in range(COLUMN-3):
        for r in range(ROW):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    #check vertically
    for r in range(ROW-2):
        for c in range(COLUMN):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    #check positively sloped diagonls
    for c in range(COLUMN-3):
        for r in range(ROW-2):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    #check negatively sloped diagonals
    for c in range(COLUMN-3):
        for r in range(ROW - 2):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for r in range(ROW):
        for c in range(COLUMN):

            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE+SQUARESIZE/2), int(r * SQUARESIZE + SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for r in range(ROW):
        for c in range(COLUMN):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), height-int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), height-int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()
board = creat_board()
print_board(board)
turn = 0

game_over = False

pygame.init()


width = COLUMN*SQUARESIZE
height = (ROW+1)*SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2-5)

screen = pygame.display.set_mode(size)

draw_board(board)
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

                   # print(event.pos)
            #ask for player1 input
            if turn == 0:
                posx = event.pos[0]
                col = int(math.floor(posx/SQUARESIZE))

                #print(col)
                #print(type(col))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    # check if player 1 wins

                    if winning_game(board,1):
                        print("PLAYER 1 WINS !")
                        game_over=True


            #Ask for player2 input
            else:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    #check if player 2 wins

                    if winning_game(board,1):
                        print("PLAYER 2 WINS !")
                        game_over=True
#board=creat_board()
            draw_board(board)
            print_board(board)

            turn += 1
            turn = turn % 2
