"""
This Module holds helper functions.
"""
import math

from src.game import NUM_ROWS, EMPTY_VAL, NUM_COLUMNS


def get_available_moves(board):
    """Returns all available moves, which the Neural Network can choose."""
    available_moves = []
    for j in range(NUM_COLUMNS):
        if board[NUM_ROWS - 1][j] == EMPTY_VAL:
            available_moves.append([NUM_ROWS - 1, j])
        else:
            for i in range(NUM_ROWS - 1):
                if board[i][j] == EMPTY_VAL and board[i + 1][j] != EMPTY_VAL:
                    available_moves.append([i, j])
    return available_moves


def round_half_up(n, decimals=0):
    """Rounds the value half up."""
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier
