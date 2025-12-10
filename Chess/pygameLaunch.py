import pygame
import chess

pygame.init()

# Chessboard settings
WINDOW_SIZE = 800
TILE_SIZE = 100
BOARD_SIZE = TILE_SIZE * 8
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pygame.display.set_caption("Chess")

WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
BLACK = (0, 0, 0)
DOT_COLOR = (0, 0, 0)  # Green dots for valid moves

# Load images
piece_files = {
    "P": "white_pawn.png",
    "N": "white_knight.png",
    "B": "white_bishop.png",
    "R": "white_rook.png",
    "Q": "white_queen.png",
    "K": "white_king.png",
    "p": "black_pawn.png",
    "n": "black_knight.png",
    "b": "black_bishop.png",
    "r": "black_rook.png",
    "q": "black_queen.png",
    "k": "black_king.png",
}

piece_images = {}
for symbol, filename in piece_files.items():
    piece_images[symbol] = pygame.image.load("PythonProjects/Chess/pieces/" + filename)


font = pygame.font.SysFont(None, 80)
text = font.render("Coming Soon", True, BLACK)
text_rect = text.get_rect(center=(WINDOW_SIZE//2, WINDOW_SIZE//2))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)  # fill background
    screen.blit(text, text_rect)  # draw text

    pygame.display.flip()  # update the display

pygame.quit()