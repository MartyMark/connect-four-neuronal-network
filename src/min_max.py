"""
This Class holds all neccessary Methods to manage the MinMax-Algorithm
"""
import random
import math
import copy

from src.operation_util import winning_move

ROW_COUNT = 6
COLUMN_COUNT = 7

EMPTY = 0
WINDOW_LENGTH = 4


def is_valid_location(board, col):
    """Determines whether it is a valid location."""
    return board[ROW_COUNT - 1][col] == 0


def get_valid_locations(board):
    """Get all valid locations."""
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


def get_next_open_row(board, col):
    """Fetches the next line in which another value can be set."""
    for row in range(ROW_COUNT):
        if board[row][col] == 0:
            return row

    raise ValueError('Es konnte beim Minmax-Algorithmus kein offene Reihe mehr gefunden werden.')


def drop_piece(board, row, col, piece):
    """Places the value on the board."""
    board[row][col] = piece


class MinMaxAlgorithm:
    """This Class holds all neccessary Methods to manage the MinMax-Algorithm."""

    def __init__(self, other_player, minmax_player):
        self.other_player = other_player
        self.minmax_player = minmax_player

    def is_terminal_node(self, board):
        """Determines whether it is the last move."""
        return winning_move(board, self.other_player) \
               or winning_move(board, self.minmax_player) \
               or len(get_valid_locations(board)) == 0

    def evaluate_window(self, window, piece):
        """
        Evaluates the game board and returns the
        score with which the minmax algorithm will work.
        """
        score = 0
        opp_piece = self.other_player
        if piece == self.other_player:
            opp_piece = self.minmax_player

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(EMPTY) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(EMPTY) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
            score -= 4

        return score

    def score_position(self, board, piece):
        """By means of the evaluation the set position can then be evaluated."""
        score = 0

        # Score center column
        center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Score Horizontal
        for row in range(ROW_COUNT):
            row_array = [int(i) for i in list(board[row, :])]
            for column in range(COLUMN_COUNT - 3):
                window = row_array[column:column + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Score Vertical
        for column in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:, column])]
            for row in range(ROW_COUNT - 3):
                window = col_array[row:row + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Score positive sloped diagonal
        for row in range(ROW_COUNT - 3):
            for column in range(COLUMN_COUNT - 3):
                window = [board[row + i][column + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        for row in range(ROW_COUNT - 3):
            for column in range(COLUMN_COUNT - 3):
                window = [board[row + 3 - i][column + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        """This method is used to start the minmax algorithm."""
        valid_locations = get_valid_locations(board)
        is_terminal = self.is_terminal_node(board)
        if depth == 0 or is_terminal:
            if is_terminal:
                if winning_move(board, self.minmax_player):
                    return None, 100000000000000
                if winning_move(board, self.other_player):
                    return None, -10000000000000
                # Game is over, no more valid moves
                return None, 0
            # Depth is zero
            return None, self.score_position(board, self.minmax_player)
        if maximizing_player:
            value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = get_next_open_row(board, col)
                b_copy = copy.deepcopy(board)
                drop_piece(b_copy, row, col, self.minmax_player)
                new_score = self.minimax(b_copy, depth - 1, alpha, beta, False)[1]
                if new_score > value:
                    value = new_score
                    column = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return column, value

        # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = copy.deepcopy(board)
            drop_piece(b_copy, row, col, self.other_player)
            new_score = self.minimax(b_copy, depth - 1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
