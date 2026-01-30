import pygame
import chess
import chess.pgn
import tkinter as tk
from tkinter import scrolledtext
import io


pygame.init()
SCREEN_W, SCREEN_H = 1100, 970
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Chess Board")

TILE_SIZE = 100
BOARD_OFFSET = 60
WHITE_TILE = (240, 240, 240)
BLACK_TILE = (80, 80, 80)

# Load piece images
PIECE_IMAGES = {}
piece_map = {
    'P': 'white_pawn', 'N': 'white_knight', 'B': 'white_bishop',
    'R': 'white_rook', 'Q': 'white_queen', 'K': 'white_king',
    'p': 'black_pawn', 'n': 'black_knight', 'b': 'black_bishop',
    'r': 'black_rook', 'q': 'black_queen', 'k': 'black_king',
}

for symbol, filename in piece_map.items():
    img = pygame.image.load(f"Chess/pieces/{filename}.png").convert_alpha()
    img = pygame.transform.smoothscale(img, (TILE_SIZE, TILE_SIZE))
    PIECE_IMAGES[symbol] = img


board = chess.Board()
moves = []
move_index = 0
white_player = "White"
black_player = "Black"


root = tk.Tk()
root.title("PGN Input")
root.geometry("400x500+1500+50")  

textbox = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 12))
textbox.pack(fill=tk.BOTH, expand=True)

def load_pgn():
    global board, moves, move_index, white_player, black_player
    pgn = textbox.get("1.0", tk.END)
    pgn_io = io.StringIO(pgn)
    game = chess.pgn.read_game(pgn_io)
    if game:
        board = game.board()
        moves = list(game.mainline_moves())
        move_index = 0

        # --- Update player names ---
        white_player = game.headers.get("White", "Unknown")
        black_player = game.headers.get("Black", "Unknown")

        print(f"PGN loaded: {len(moves)} moves")
        print(f"White: {white_player}, Black: {black_player}")
        redraw_board()

load_button = tk.Button(root, text="Load PGN", command=load_pgn)
load_button.pack()


def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE_TILE if (row+col)%2==0 else BLACK_TILE
            pygame.draw.rect(screen, color, (col*TILE_SIZE + BOARD_OFFSET, row*TILE_SIZE + BOARD_OFFSET + 20, TILE_SIZE, TILE_SIZE))
            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                screen.blit(PIECE_IMAGES[piece.symbol()], (col*TILE_SIZE + BOARD_OFFSET, row*TILE_SIZE + BOARD_OFFSET + 20))

def step_forward():
    global move_index
    if move_index < len(moves):
        board.push(moves[move_index])
        move_index += 1

def step_backward():
    global move_index
    if move_index > 0:
        board.pop()
        move_index -= 1

def redraw_board():
    screen.fill((50,50,50))
    
    # Display player names at top
    font = pygame.font.SysFont(None, 40)
    screen.blit(font.render(f"White: {white_player}", True, (255,255,255)), (BOARD_OFFSET, 900))
    screen.blit(font.render(f"Black: {black_player}", True, (255,255,255)), (BOARD_OFFSET, 40))

    draw_board()

    # Draw buttons
    mouse_pos = pygame.mouse.get_pos()
    back_color = (150,150,150) if back_button.collidepoint(mouse_pos) else (100,100,100)
    next_color = (150,150,150) if next_button.collidepoint(mouse_pos) else (100,100,100)

    pygame.draw.rect(screen, back_color, back_button)
    pygame.draw.rect(screen, next_color, next_button)
    font_buttons = pygame.font.SysFont(None, 50)
    screen.blit(font_buttons.render("<", True, (255,255,255)), (back_button.x + 30, back_button.y + 30))
    screen.blit(font_buttons.render(">", True, (255,255,255)), (next_button.x + 30, next_button.y + 30))

    pygame.display.flip()

# Buttons
back_button = pygame.Rect(900, 700, 70, 100)
next_button = pygame.Rect(1000, 700, 70, 100)


running = True
while running:
    redraw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button.collidepoint(event.pos):
                step_backward()
            if next_button.collidepoint(event.pos):
                step_forward()

    root.update() 

pygame.quit()
