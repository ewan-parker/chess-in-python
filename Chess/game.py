import chess

board = chess.Board()

print(board)

board.generate_legal_moves

print('Format for moves: 1. Nf3 should be written as g1f3')
while not board.is_game_over():
    
    print('')

    # Prompt user for move
    print("Make a move: ")
    move = chess.Move.from_uci(input())

    if board.is_legal(move):
        board.push(move)
        print(board)
    else:
        print("thats not a legal move... make another.")

    print('')
print('Game is over!')
    
