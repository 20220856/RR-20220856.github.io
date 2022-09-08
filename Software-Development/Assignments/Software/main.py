
from turtle import width
import pygame
import os

pygame.font.init()
KNIGHT_FONT=pygame.font.SysFont("arial",70,bold=True)

WIDTH,HEIGHT = 1920,1080
#WIDTH,HEIGHT = 900,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Knight's Tour Puzzle")

KNIGHT_WIDTH=115/2
KNIGHT_HEIGHT=238/2
BOARD_BLACK=(10,10,10)
BOARD_WHITE=(250,250,250)
EDEL_PINK=(255,200,200)
KNIGHT_PIECE_IMAGE=pygame.image.load(os.path.join("assets", "knight_piece.png"))
KNIGHT_PIECE=pygame.transform.scale(KNIGHT_PIECE_IMAGE, (KNIGHT_WIDTH,KNIGHT_HEIGHT))
knight_text = KNIGHT_FONT.render("Knight's Tour Puzzle",1,BOARD_WHITE)

def draw_window(knightpos,knight_text):
    WIN.fill((EDEL_PINK))
    WIN.blit(KNIGHT_PIECE, (knightpos.x,knightpos.y))
    WIN.blit(knight_text,(WIDTH/2-knight_text.get_width()/2,20))
    
    pygame.display.update()

def handle_knight_movement(keys_pressed, knightpos):
    if keys_pressed[pygame.K_a] and knightpos.x>=3:
        knightpos.x-=5
    if keys_pressed[pygame.K_d] and knightpos.x<=WIDTH-KNIGHT_WIDTH-3:
        knightpos.x+=5
    if keys_pressed[pygame.K_w] and knightpos.y>=3:
        knightpos.y-=5
    if keys_pressed[pygame.K_s] and knightpos.y<=HEIGHT-KNIGHT_HEIGHT-3:
        knightpos.y+=5

def main():
    knightpos = pygame.Rect(WIDTH/2-KNIGHT_WIDTH,HEIGHT/2-KNIGHT_HEIGHT,KNIGHT_WIDTH,KNIGHT_HEIGHT)
    CLOCK=pygame.time.Clock()
    run=True
    while run:
        CLOCK.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_ESCAPE]:
            run=False
        handle_knight_movement(keys_pressed,knightpos)
        draw_window(knightpos,knight_text)
           
    pygame.quit()

if __name__ == "__main__":
    main()