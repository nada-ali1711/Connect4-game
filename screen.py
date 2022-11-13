import pygame

import sys





pygame.init()

width = 800

height = 600

screen = pygame.display.set_mode((width, height))

#define font

font = pygame.font.SysFont('arial',75)

pygame.display.set_caption("Connect4 Game")

#define font color

fontColor=(255,255,255)



def draw_text(text,font, color,x,y):

    show = font.render(text,True,color)

    screen.blit(show,(x,y))







run = True

while run:

    screen.fill((50,80,90))

    for event in pygame.event.get():

        draw_text("Connect4 Game",font,fontColor,160,160)

        if event.type==pygame.QUIT:

            run=False

        pygame.display.update()

pygame.quit()

