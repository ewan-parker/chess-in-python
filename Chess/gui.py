import chess
import pygame
import capture_bot 

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

# BOT INFO 
BOT_DELAY_MS = 400   
bot_move_pending = False
bot_move_time = 0

def mouse_at_square(mouse_x, mouse_y):
    col = (mouse_x - OFFSET_X) // TILE_SIZE
    row = (mouse_y - OFFSET_Y) // TILE_SIZE

    if 0 <= row < 8 and 0 <= col < 8:
        return chess.square(col, 7 - row)
    return None


pygame.init()

screen = pygame.display.set_mode((1600,900),0,0,0,0)
pygame.display.set_caption("Chess (Python)")

font = pygame.font.SysFont(None, 95)  # None = default font, 60 = size

# images for pieces
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

clicked_square = None


running = True


# game loop
while running:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            square = mouse_at_square(*event.pos)

            if square is None:
                clicked_square = None
                continue

            if clicked_square is None:
                piece = board.piece_at(square)
                if piece and piece.color == board.turn:
                    clicked_square = square
            else:
                piece = board.piece_at(clicked_square)
                if piece is None:
                    clicked_square = None
                    continue

                # Handle promotion automatically
                if piece.piece_type == chess.PAWN and chess.square_rank(square) in [0,7]:
                    move = chess.Move(clicked_square, square, promotion=chess.QUEEN)
                else:
                    move = chess.Move(clicked_square, square)

                if move in board.legal_moves:
                    board.push(move)
                    bot_move_pending = True
                    bot_move_time = pygame.time.get_ticks() + BOT_DELAY_MS

                clicked_square = None

    # Handle bot move outside event loop
    if bot_move_pending and pygame.time.get_ticks() >= bot_move_time:
        bot_move = capture_bot.get_bot_move(board)
        if bot_move:
            board.push(bot_move)
        bot_move_pending = False

    # Board & pieces     
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

            piece_at_square = chess.square(col, 7 - row)
            
            piece = board.piece_at(piece_at_square)
            if piece:
                piece_symbol = piece.symbol()
                screen.blit(PIECE_IMAGES[piece.symbol()], (x-2, y))

    # Highlights
    if clicked_square is not None:
        row = 7 - chess.square_rank(clicked_square)
        col = chess.square_file(clicked_square)

        highlight_rect = pygame.Rect(
            col * TILE_SIZE + OFFSET_X,
            row * TILE_SIZE + OFFSET_Y,
            TILE_SIZE,
            TILE_SIZE
        )
        pygame.draw.rect(screen, HIGHLIGHT_COLOR, highlight_rect, 4)   

    pygame.display.flip()