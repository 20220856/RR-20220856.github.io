from turtle import width
from venv import create
import pygame
import os

SCR_WIDTH, SCR_HEIGHT = 1920,1080
# Screen Dimensions - 1920x1080 for fullscreen on (most) PCs
WIN = pygame.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
# This sets Pygame's display mode to a window with the dimensions specified above
pygame.display.set_caption("Knight's Tour Puzzle")
# This sets the name of the window produced
CHESSBLACK = (20,20,20)
CHESSWHITE = (255,255,255)
BOARD_BG = (98,47,34)
SQUAREWIDTH, SQUAREHEIGHT = 100,100
# The colour of the board backdrop (dark brown)
boardwidth=8
# Variable for the total width of the generated chess board
boardheight=8
# Variable for the total height of the generated chess board

squarepositions={}
for i in range(boardwidth*boardheight):
    squarepos="square%d"%i
    squarepositions[squarepos]=i

print(squarepositions)

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