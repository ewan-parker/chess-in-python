import chess
import pygame

clock = pygame.time.Clock()





# SIZING:
TILE_SIZE = 100 # size of each square. 
OFFSET_X = 350 # moves the board over
OFFSET_Y = 50 # moves the board down

# COLOURS:
WHITE_TILE = pygame.Color(227,226,228)
BLACK_TILE = pygame.Color(68,67,68)
TILE_COLOR = pygame.Color(255,0,0) 
BACKGROUND_COLOR = pygame.Color(59,59,59)
HIGHLIGHT_COLOR = (255, 255, 0)




pygame.init()

font = pygame.font.SysFont(None, 95)  # None = default font, 60 = size

screen = pygame.display.set_mode((1600,900),0,0,0,0)
pygame.display.set_caption("Chess (Python)")

board = chess.Board()

clicked_square = None


running = True
while running:
    clock.tick(60)
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
            
            text_surface = font.render("P", True, (0, 0, 0))

            y = (i * 100) + OFFSET_Y
            x = (j * 100) + OFFSET_X

            SINGLE_TILE = pygame.Rect(x,y,TILE_SIZE,TILE_SIZE)
            pygame.draw.rect(screen, TILE_COLOR, SINGLE_TILE) 

            text_color = pygame.Color(0,0,0)

            
            
            if i < 2 or i > 5:
                initial_square = chess.square(j,7-i)
                piece_symbol = board.piece_at(initial_square).symbol()
                text_surface = font.render(piece_symbol, True, text_color, None)
                x += 27
                y+= 25

                
                screen.blit(text_surface, (x, y))

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos

            col = (mouse_x - OFFSET_X) // TILE_SIZE
            row = (mouse_y - OFFSET_Y) // TILE_SIZE

            if 0 <= row < 8 and 0 <= col < 8:
                clicked_square = (row, col)
            else:
                clicked_square = None

    if clicked_square:
        row, col = clicked_square
        highlight_rect = pygame.Rect(
        col * TILE_SIZE + OFFSET_X,
        row * TILE_SIZE + OFFSET_Y,
        TILE_SIZE,
        TILE_SIZE
        )
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, highlight_rect, 4)   

    pygame.display.flip()