from itertools import count
from socket import inet_ntoa
import pygame
import os

SCR_WIDTH, SCR_HEIGHT = 1920,1080
WIN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
pygame.display.set_caption("Knight's Tour Puzzle")
BOARD_BG = (98,47,34)
CHESSBLACK = (20,20,20)
CHESSWHITE = (255,255,255)

squarepositions={}

def createboard():
    SQUAREWIDTH, SQUAREHEIGHT = 100,100
    boardwidth=8
    boardheight=8
    count=0
    totalcount=0
    whitestart=5
    blackstart=105
    squaresacross=0
    vertoffset=5
    
    
    while count < boardheight:
        while squaresacross<boardwidth:
            if count%2==0:
                pygame.draw.rect(WIN,CHESSWHITE,(whitestart,vertoffset,SQUAREWIDTH,SQUAREHEIGHT))
                squarepos="square%d"%totalcount
                squarepositions[squarepos]=[whitestart,vertoffset]
                whitestart=whitestart+200
                totalcount=totalcount+1
                squaresacross=squaresacross+1
                pygame.draw.rect(WIN, CHESSBLACK,(blackstart,vertoffset,SQUAREWIDTH,SQUAREHEIGHT))
                squarepos="square%d"%totalcount
                squarepositions[squarepos]=[blackstart,vertoffset]
                blackstart=blackstart+200
                totalcount=totalcount+1
                squaresacross=squaresacross+1
            else:
                pygame.draw.rect(WIN, CHESSBLACK,(blackstart,vertoffset,SQUAREWIDTH,SQUAREHEIGHT))
                squarepos="square%d"%totalcount
                squarepositions[squarepos]=[blackstart,vertoffset]
                blackstart=blackstart+200
                totalcount=totalcount+1
                squaresacross=squaresacross+1
                pygame.draw.rect(WIN,CHESSWHITE,(whitestart,vertoffset,SQUAREWIDTH,SQUAREHEIGHT))
                squarepos="square%d"%totalcount
                squarepositions[squarepos]=[whitestart,vertoffset]
                whitestart=whitestart+200
                totalcount=totalcount+1
                squaresacross=squaresacross+1
        count=count+1
        if count%2==0:
            whitestart=5
            blackstart=105
        else:
            whitestart=105
            blackstart=5
        vertoffset=vertoffset+100
        squaresacross=0
 
    pygame.draw.rect(WIN, (255,0,0), (squarepositions["square27"][0],squarepositions["square27"][1],SQUAREWIDTH,SQUAREHEIGHT))
    # example of how to access squarepositions coordinates
    
# def knightdrop():
    

        
        



def draw_window():
    WIN.fill((BOARD_BG))
    createboard()
    
    print(squarepositions)
    
    pygame.display.update()






def main():
    run=True
    while run:
        clock=pygame.time.Clock()
        clock.tick(2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        esckey=pygame.key.get_pressed()
        if esckey[pygame.K_ESCAPE]:
            run=False
        
        draw_window()
    
        
    pygame.QUIT

if __name__ == "__main__":
    main()