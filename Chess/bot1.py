import chess
import random

BOT_COLOR = chess.BLACK

def get_bot_move(board: chess.Board) -> chess.Move | None:

    if board.turn != BOT_COLOR:
        return None
    
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return None
    
    return random.choice(legal_moves)