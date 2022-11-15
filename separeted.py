import pygame
#from pygame_functions import  *
#from pygame.locals import *
import sys
#import pygame_gui
import math
import numpy as np
import random
import Utilities as UT
textboxGroup = pygame.sprite.OrderedUpdates()
ROW = 6
COLUMN = 7
BLUE = (0,0, 255)
BLACK = (0 ,0 ,0)
RED = (255 ,0 ,0 )
YELLOW = (255, 255, 100)
SQUARESIZE = 100
player = 0
AI = 1

pygame.font.init()
pygame.init()

class newTextBox(pygame.sprite.Sprite):
    def __init__(self, text, xpos, ypos, width, case, maxLength, fontSize):
        pygame.sprite.Sprite.__init__(self)
        self.text = ""
        self.width = width
        self.initialText = text
        self.case = case
        self.maxLength = maxLength
        self.boxSize = int(fontSize * 1.7)
        self.image = pygame.Surface((width, self.boxSize))
        self.image.fill((255, 255, 255))
        pygame.draw.rect(self.image, (0, 0, 0), [0, 0, width - 1, self.boxSize - 1], 2)
        self.rect = self.image.get_rect()
        self.fontFace = pygame.font.match_font("Arial")
        self.fontColour = pygame.Color("black")
        self.initialColour = (180, 180, 180)
        self.font = pygame.font.Font(self.fontFace, fontSize)
        self.rect.topleft = [xpos, ypos]
        newSurface = self.font.render(self.initialText, True, self.initialColour)
        self.image.blit(newSurface, [10, 5])


def makeTextBox(xpos, ypos, width, case=0, startingText="Please type here", maxLength=0, fontSize=22):

    thisTextBox = newTextBox(startingText, xpos, ypos, width, case, maxLength, fontSize)
    textboxGroup.add(thisTextBox)
    return thisTextBox

def textBoxInput(textbox, functionToCall=None, args=[]):
    # starts grabbing key inputs, putting into textbox until enter pressed
    global keydict
    textbox.text = ""
    returnVal = None
    while True:
        pygame.display.update()
        if functionToCall:
            returnVal = functionToCall(*args)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    textbox.clear()
                    if returnVal:
                        return textbox.text, returnVal
                    else:
                        return textbox.text
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    textbox.update(event)
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def showTextBox(textBoxName):
    textboxGroup.add(textBoxName)
    pygame.display.update()
        #updateDisplay()

class Button:
    def __init__(self,text,width,height,pos,elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elecation = elevation
        self.original_y_pos = pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = '#475F77'

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = '#000000'
        #text
        self.text_surf = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    print('click')
                    #draw_menu()
                    #button3.draw()
                    self.pressed = False
        else:
            self.dynamic_elecation = self.elevation
            self.top_color = '#475F77'


def creat_board():
    board = np.zeros((ROW,COLUMN))
    return board

def print_board(board):
    print(np.flip(board, 0))


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
pygame.display.set_caption('Connect4 Game')
clock = pygame.time.Clock()
gui_font = pygame.font.SysFont(None,30)
font = pygame.font.SysFont('arial',75)
#k = int(input("Enter maximum depth"))

#define font color
fontColor=(255,255,255)
#game_over = False

def draw_text(text,font, color,x,y):
    show = font.render(text,True,color)
    screen.blit(show,(x,y))

def draw_menu():
    screen.fill((52, 78, 91))
    draw_text("Connect4 Game", font, fontColor, 80, 100)
    #button1 = Button('PLAY WITHOUT PRUNING', 260, 130, (220, 480), 10)
    #button2 = Button('PLAY WITH PRUNING', 260, 130, (220, 280), 10)
    button1.draw()
    button2.draw()
    wordBox = makeTextBox(10, 80, 300, 0, "enter text here", 0, 24)
    showTextBox(wordBox)
    entery = textBoxInput(wordBox)

    #instructionLabel = makeLabel("plese enter the max depth", 40, 10, 10, "black", "Agency FB")
    #showLabel(instructionLabel)

   # wordBox = makeTextBox(10, 80, 300, 0, "enter text here", 0, 24)
    #showTextBox(wordBox)
    #entery = textBoxInput(wordBox)


    #instructionLabel = makeLabel("plese enter the max depth", 40, 10, 10, "black", "Agency FB")
    #showLabel(instructionLabel)



#if check_click(self) == True:
    #	menu = True
    #else:
    #	menu = False
    #return menu
#pygame.display.update()

#def draw_game():
 #   turn = 0
  #  pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
   # if event.type == pygame.MOUSEMOTION:
    #    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
     #   posx = event.pos[0]
      #  if turn == 0:
       #     pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
       # else:
        #    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
    #pygame.display.update()

    #if event.type == pygame.MOUSEBUTTONDOWN:

        # print(event.pos)
        # ask for player1 input
     #   if turn == player:
      #      posx = event.pos[0]
       #     col = int(math.floor(posx / SQUARESIZE))

            # print(col)
            # print(type(col))

        #    if is_valid_location(board, col):
         #       row = get_next_open_row(board, col)
          #      drop_piece(board, row, col, 1)

                # check if player 1 wins
           #     if winning_game(board, 1):
            #        label = Font.render("Player1 wins!", 1, RED)
             #       screen.blit(label, (40, 10))
              #      run = False
               #     pygame.display.update()
        #draw_board(board)
        #print_board(board)

        #turn += 1
        #turn = turn % 2

        # Ask for player2 input
        #if turn == AI :
            #posx = event.pos[0]
            #col = random.randint(0,COLUMN-1)
         #   col = best_move(board, AI_PIECE)
          #  if is_valid_location(board, col):
                #pygame.time.wait(200)
           #     row = get_next_open_row(board, col)
            #    drop_piece(board, row, col, 2)

                # check if player 2 wins

             #   if winning_game(board, 2):
              #      label = Font.render("Player2 wins!", 2, YELLOW)
               #     screen.blit(label, (40, 10))
                #    pygame.display.update()
                  #  run = False
        # board=creat_board()
       # draw_board(board)
       # print_board(board)

        #turn += 1
        #turn = turn % 2
#pygame.display.update()




#def draw_game2():
#	screen.fill((100, 100, 100))
#	button4.draw()
#	draw_text("hi", font, fontColor, 80, 100)
#pygame.display.update()


button1 = Button('PLAY WITHOUT PRUNING',260,130,(220,400),5)
button2 = Button('PLAY WITH PRUNING',260,130,(220,250),5)
#button3 = Button('HEY!',260,130,(220,280),5)
#button4 = Button('hi!',260,130,(220,280),5)
#a_b_pruning = True
#with_pruning = UT.GameTree(k,True)
#without_pruning = UT.GameTree(k,False)
#pygame.init()


width = COLUMN*SQUARESIZE
height = (ROW+1)*SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2-5)

screen = pygame.display.set_mode(size)

draw_board(board)
pygame.display.update()

Font = pygame.font.SysFont("monospace", 75)
clock=pygame.time.Clock()
#label = pygame_gui.UIManager((width, height))
#text_input=pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((250,550),(200,50)), manager=label,object_id="#main_text_entry")

main_menu=True
run= True

while run:
    for event in pygame.event.get():
        #pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))

        if main_menu:
            draw_menu()
            #UI_REFRESH_RATE = clock.tick(60)
            #label.process_events(event)
            #label.update(UI_REFRESH_RATE)
            #label.draw_ui(screen)
            #k = int(input("Enter maximum depth"))
            pygame.display.update()
            if button1.pressed == True:
                #without_pruning.apply_move()
                main_menu = False
                pygame.display.update()
            elif button2.pressed==True:
                #with_pruning.apply_move(5)
                main_menu = False
            pygame.display.update()

        if event.type == pygame.QUIT:
            run = False
            #sys.exit()


            #if not run:
               # pygame.time.wait(2000)

    clock.tick(60)
pygame.quit()
sys.exit()
