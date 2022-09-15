from turtle import width
from venv import create
import pygame
import os

#SCR_WIDTH, SCR_HEIGHT = 1920,1080
# Screen Dimensions - 1920x1080 for fullscreen on (most) PCs
# WIN = pygame.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
# This sets Pygame's display mode to a window with the dimensions specified above
#pygame.display.set_caption("Knight's Tour Puzzle")
# This sets the name of the window produced
CHESSBLACK = (20,20,20)
CHESSWHITE = (255,255,255)
BOARD_BG = (98,47,34)
SQUAREWIDTH, SQUAREHEIGHT = 100,100
# The colour of the board backdrop (dark brown)
boardwidth=2
# Variable for the total width of the generated chess board
boardheight=2
# Variable for the total height of the generated chess board

squarevalues = {}
for i in range(boardwidth*boardheight):
    if i%2==0:
        while squares_across<boardwidth/2:
            pygame.draw.rect(WIN, CHESSWHITE,(whitestart*2,squares_down+5,SQUAREWIDTH,SQUAREHEIGHT))
            squarenumber=squarenumber+1
            squarepos="square%d"%i
            squarevalues[squarepos]=i=[squarenumber,whitestart*2,squares_down+5]
        
    else:
        while squares_across<boardwidth/2:
            pygame.draw.rect(WIN, CHESSBLACK,(blackstart*2,squares_down+5,SQUAREWIDTH,SQUAREHEIGHT))
            squarenumber=squarenumber+1
            squarepos="square%d"%i
            squarevalues[squarepos]=i=[squarenumber,blackstart*2,squares_down+5]
            

        squares_across = squares_across+1
        whitestart = whitestart + SQUAREWIDTH+2
        blackstart = blackstart + SQUAREWIDTH+2
        
        
        
        squares_down=squares_down+102
        squares_across=0
        loopcount=loopcount+1
        if loopcount%2==0:
            whitestart=2.5
            blackstart=53.5
        else:
            whitestart=53.5
            blackstart=2.5

squarevalues["square2"]=[2,400,5]
#squarevalues["square1"]=[0,0,0]

print(squarevalues)








# squarevalues = {"square0": {"position":0, "x":0, "y":0 },
#                 "square1": {"position":0, "x":10, "y":10}}

#squarevalues = {0:[0,0,0],1:[1,10,10],2:[2,20,20]}




# print(squarevalues["square1"]["x"])
















# def draw_window():
#     WIN.fill((BOARD_BG))
#     pygame.draw.rect(WIN, CHESSWHITE,(100,100,SQUAREWIDTH,SQUAREHEIGHT))
#     pygame.display.update()
    
# def main():
#     clock=pygame.time.Clock()
#     run=True
#     while run:
#         clock.tick(60)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run=False
#         esckey=pygame.key.get_pressed()
#         if esckey[pygame.K_ESCAPE]:
#             run=False
        
        
        
#         draw_window()
        
#     pygame.QUIT

# if __name__ == "__main__":
#     main()