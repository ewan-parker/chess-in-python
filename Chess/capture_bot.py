import chess
import random

BOT_COLOR = chess.BLACK

def get_bot_move(board: chess.Board) -> chess.Move | None:

    if board.turn != BOT_COLOR:
        return None
    
    legal_moves = list(board.legal_moves)

    captures = [m for m in legal_moves if board.is_capture(m)]

    if captures:
        return random.choice(captures)
    return random.choice(legal_moves)

   