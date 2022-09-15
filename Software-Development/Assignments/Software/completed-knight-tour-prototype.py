
# THIS IS THE MAIN ITERATION OF THE KNIGHT'S TOUR PROJECT - CURRENTLY A WORKING PROTOTYPE OF BOARD GENERATION AND RECORDING

from itertools import count
from socket import inet_ntoa
import pygame
import os
# This imports necessary dependancies, including Pygame, the main framework for this Project


WIN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
# This creates a fullscreen window upon which the Knight's Tour is drawn
pygame.display.set_caption("Knight's Tour Puzzle")
# This sets the name of the window to "Knight's Tour Puzzle"
BOARD_BG = (98,47,34)
CHESSBLACK = (20,20,20)
CHESSWHITE = (255,255,255)
# These are the RGB values for colours used throughout the program.

squarepositions={}
# This establishes the creation of a global dictionary for recording square positions - needed for the createboard function

def createboard():
    SQUAREWIDTH, SQUAREHEIGHT = 100,100
    # This defines the dimensions of chessboard squares to be drawn; 100x100px
    
    boardwidth=8
    boardheight=8
    # These are the variables responsible for determining the generated width and height of the chessboard. For a knight's tour, the minimum size is 3x4, but this particular model can generate anything larger than that
    
    totalcount=0
    # This counter keeps track of the total iterations of a square being drawn - for example, on a 4x4 board, this will be 16, an 8x8 board, 64, etc.
    count=0
    # This is a counter to keep track of how many times one full row has been completed (for the purpose of starting a new row)
    squaresacross=0
    # This is a measurement for the number of squares that have been currently drawn in a row
    
    whitestart=5
    # This is the white starting position (x axis)
    blackstart=105
    # This is the black starting position (x axis)
    vertoffset=5
    # This is the starting positions for both black and white (y axis)
    
    
    
    while count < boardheight:
        while squaresacross<boardwidth:
            if count%2==0:
                # This IF is used to determine whether the row is an even number. This distinction is required to solve issues with labelling dictionary values
                
                pygame.draw.rect(WIN,CHESSWHITE,(whitestart,vertoffset,SQUAREWIDTH,SQUAREHEIGHT))
                # This draws a white square, according to the variables shown
                
                squarepos="square%d"%totalcount
                squarepositions[squarepos]=[whitestart,vertoffset]
                # This utilised the "totalcount" variable to assign the newly drawn square a value in the dictionary "squarepositions", labelled according to the position in which it was drawn, with its x and y values as keys
                
                whitestart=whitestart+200
                # This increments the x axis position of the next white square by 200px (the width of two squares)
                
                totalcount=totalcount+1
                squaresacross=squaresacross+1
                # This increments the count for the total number of squares, AND the metric for the squares in the current row by one
                
                
                pygame.draw.rect(WIN, CHESSBLACK,(blackstart,vertoffset,SQUAREWIDTH,SQUAREHEIGHT))
                # This draws a black square, in the same manner that the white square is drawn above
                
                squarepos="square%d"%totalcount
                squarepositions[squarepos]=[blackstart,vertoffset]
                blackstart=blackstart+200
                totalcount=totalcount+1
                squaresacross=squaresacross+1
                # This is the same as the process for the white square, shown above, aside from the fact that values for the black square are used
                
            else:
                # The IF/ELSE is used to see whether black or white must be drawn first, depending on whether the row is even or odd. For odd, black is drawn first. Again, this is to solve issues with labelling dictionary values
                
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
                # This is an identical process to the first iteration, but with black being drawn and processed first instead of white
            
            # THIS CONCLUDES THE DRAWING OF THE ROW
                
        count=count+1
        # This increments the counter for the height of the board by one
        
        if count%2==0:
            whitestart=5
            blackstart=105
        # If the counter is even, white is drawn as the first square
        
        else:
            whitestart=105
            blackstart=5
        # Else, if the counter is odd, black is drawn as the first square
        
        vertoffset=vertoffset+100
        # The y axis for black AND white is increased by 100, bringing it to be vertically adjacent to the previously drawn row
        
        squaresacross=0
        # This resets the "squaresacross" variable to 0, allowing the function to draw a row to begin anew
        
        # THIS PROCESS WILL REPEAT UNTIL THE BOARD HEIGHT IS EQUAL TO THE VARIABLE SPECIFIED. THE DRAWING OF THE BOARD IS THEN CONCLUDED
        
 
    pygame.draw.rect(WIN, (255,0,0), (squarepositions["square27"][0],squarepositions["square27"][1],SQUAREWIDTH,SQUAREHEIGHT))
    # This is an example of how to access the coordinates of the squares within the dictionary. In this instance, it is coloring square 27 red.


def draw_window():
    WIN.fill((BOARD_BG))
    # This fills the window with the colour specified within "BOARD_BG" (dark brown)
    
    createboard()
    # This references the function defined above, to draw the board atop the brown backdrop
    
    pygame.display.update()
    # This forces the window to draw the above, without which they would not show onscreen






def main():
    run=True
    while run:
        clock=pygame.time.Clock()
        clock.tick(1)
        # This sets frames/sec to 1, as endless reiteration is highly unneeded, at least at this stage
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        esckey=pygame.key.get_pressed()
        if esckey[pygame.K_ESCAPE]:
            run=False
        # This adds a clause to close the window through pressing the "Escape" key, without which, the only way to close the window is force-closing
        
        draw_window()
        # This draws the board and background, as described in the corresponding function
    
        
    pygame.QUIT
    # This stops the program if run becomes false (in the event of "Escape" being pressed)


if __name__ == "__main__":
    main()
# This ensures that this program is only run directly, and not called upon by other programs
