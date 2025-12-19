import chess
import pygame

fps = pygame.time.Clock()

# SIZING:
TILE_SIZE = 100

# COLOURS:
WHITE_TILE = pygame.Color(227,226,228)
BLACK_TILE = pygame.Color(68,67,68)
TILE_COLOR = pygame.Color(255,0,0) 
BACKGROUND_COLOR = pygame.Color(59,59,59)

pygame.init()

screen = pygame.display.set_mode((1600,900),0,0,0,0)
pygame.display.set_caption("Chess (Python)")




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(8):
        for j in range(8):
            row = i
            col = j
            if (row + col) % 2 == 0:
                    TILE_COLOR = WHITE_TILE
            else:
                TILE_COLOR = BLACK_TILE
   
            y = (i * 100) + 50
            x = (j * 100) + 350

            SINGLE_TILE = pygame.Rect(x,y,TILE_SIZE,TILE_SIZE)
            pygame.draw.rect(screen, TILE_COLOR, SINGLE_TILE) 



    pygame.display.flip()