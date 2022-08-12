"""
This Module holds the Player Class.
"""
import math
import random
import copy
import numpy as np
from min_max import MinMaxAlgorithm

from game import RED_PLAYER_VAL
from operation_util import get_available_moves


class Player:
    """This Class holds all neccessary Methods for a Player."""
    def __init__(self, value, strategy='random', model=None):
        self.value = value
        self.strategy = strategy
        self.model = model
        self.e_greedy = 0.3

    # [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
    def get_move(self, board):
        """Decides the next move, depending on the strategy and returns the move."""
        # [[5,0], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6]]
        available_moves = get_available_moves(board)

        if self.strategy == "random":
            if random.uniform(0, 1) <= self.e_greedy:
                return available_moves[random.randrange(0, len(available_moves))]

            np_board = np.array(board, dtype=np.float64)
            np_board = np.flipud(np_board)

            min_max = MinMaxAlgorithm()

            col, minimax_score = min_max.minimax(np_board, 5, -math.inf, math.inf, True)

            if col is None:
                return available_moves[random.randrange(0, len(available_moves))]

            row = min_max.get_next_open_row(np_board, col)

            row = 5 - row

            return row, col
        else:
            max_value = 0
            best_move = available_moves[0]
            for available_move in available_moves:
                board_copy = copy.deepcopy(board)
                board_copy[available_move[0]][available_move[1]] = self.value
                if self.value == RED_PLAYER_VAL:
                    value = self.model.predict(board_copy, 2)
                else:
                    value = self.model.predict(board_copy, 0)
                if value > max_value:
                    max_value = value
                    best_move = available_move
            return best_move

    def get_player(self):
        """Returns the current player."""
        return self.value
