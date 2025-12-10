import chess
import pygame

board = chess.Board()

print(board)

board.generate_legal_moves

while not board.is_game_over():
    
    print("Make a move: ")

    move = chess.Move.from_uci(input())

    if board.is_legal(move):
        board.push(move)
        print(board)
    else:
        print("thats not a legal move... make another.")

    
