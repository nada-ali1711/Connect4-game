import pygame
import sys
import math
import random
from main import *

ROW = 6
COLUMN = 7
BLUE = (0,0, 255)
BLACK = (0 ,0 ,0)
RED = (255 ,0 ,0 )
YELLOW = (255, 255, 100)
SQUARESIZE = 100
player = 0
AI = 1



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

font = pygame.font.SysFont("monospace", 75)

while not game_over:
    for event in pygame.event.get():
        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0,width,SQUARESIZE))
            posx = event.pos[0]
            if turn==0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:

            # print(event.pos)
            # ask for player1 input
            if turn == player :
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))

            # print(col)
           # print(type(col))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    # check if player 1 wins
                    if winning_game(board, 1):
                        label = font.render("Player1 wins!", 1, RED)
                        screen.blit(label, (40, 10))
                        game_over = True
                        pygame.display.update()
            draw_board(board)
            print_board(board)

            turn += 1
            turn = turn % 2


            # Ask for player2 input
            if turn==AI and not game_over:
            # posx = event.pos[0]
                col = random.randint(0,COLUMN-1)

                if is_valid_location(board, col):
                    pygame.time.wait(200)
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                # check if player 2 wins

                    if winning_game(board,2):
                        label = font.render("Player2 wins!", 2, YELLOW)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        game_over = True
    # board=creat_board()
            draw_board(board)
            print_board(board)

            turn += 1
            turn = turn % 2
            if game_over:
                pygame.time.wait(7000)
