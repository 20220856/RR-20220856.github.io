from socket import inet_ntoa
import pygame
import os

SCR_WIDTH, SCR_HEIGHT = 1920,1080
# Screen Dimensions - 1920x1080 for fullscreen on (most) PCs
WIN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
# This sets Pygame's display mode to a window with the dimensions specified above
pygame.display.set_caption("Knight's Tour Puzzle")
# This sets the name of the window produced

CHESSBLACK = (20,20,20)
CHESSWHITE = (255,255,255)
BOARD_BG = (98,47,34)
# The colour of the board backdrop (dark brown)


squarevalues = {}

def create_board():
    # Create the function "create_board"
    SQUAREWIDTH, SQUAREHEIGHT = 100,100
    # The width and height of a chess square on the chessboard
    boardwidth=4
    # Variable for the total width of the generated chess board
    boardheight=4
    # Variable for the total height of the generated chess board
    
    squares_across = 0
    squares_down = 0
    whitestart = 2.5
    blackstart=53.5
    loopcount=0
    squarenumber=0
    for i in range(boardheight):
        while squares_across<boardwidth/2:
            pygame.draw.rect(WIN, CHESSWHITE,(whitestart*2,squares_down+5,SQUAREWIDTH,SQUAREHEIGHT))
            pygame.draw.rect(WIN, CHESSBLACK,(blackstart*2,squares_down+5,SQUAREWIDTH,SQUAREHEIGHT))
            squarenumber=squarenumber+1
            
            for i in range(boardwidth*boardheight):
                if i%2==0:
                    squarepos="square%d"%i
                    squarevalues[squarepos]=i=[squarenumber,whitestart*2,squares_down+5]
                else:
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
    
     
            
    tempwidth=10
    tempheight=10     
    pygame.draw.rect(WIN,(0,255,0),((((whitestart*2))-(tempwidth/2)),((squares_down)-(tempheight/2)) , tempwidth, tempheight))


        
def draw_window():
    WIN.fill((BOARD_BG))
    create_board()
    
    pygame.display.update()



def main():
    run=True
    while run:
        clock=pygame.time.Clock()
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        esckey=pygame.key.get_pressed()
        if esckey[pygame.K_ESCAPE]:
            run=False
        
        
        
        draw_window()
        print(squarevalues)  
    
        
    pygame.QUIT

if __name__ == "__main__":
    main()