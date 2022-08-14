"""
This Module holds the Game Class.
"""
import copy

from src.operation_util import winning_move

RED_PLAYER = 'R'
YELLOW_PLAYER = 'Y'
RED_PLAYER_VAL = -1
YELLOW_PLAYER_VAL = 1
EMPTY = ' '
EMPTY_VAL = 0
HORIZONTAL_SEPARATOR = ' | '
GAME_STATE_X = -1
GAME_STATE_O = 1
GAME_STATE_DRAW = 0
GAME_STATE_NOT_ENDED = 2
VERTICAL_SEPARATOR = '__'
NUM_ROWS = 6
NUM_COLUMNS = 7
REQUIRED_SEQUENCE = 4


class Game:
    """This Class holds all neccessary Methods to manage a Connect 4 Game"""

    def __init__(self):
        """Init function of the Game Class"""
        self.board = []
        self.board_history = []
        self.reset_board()

    def reset_board(self):
        """Emptys all Rows and Cols of the Gameboard."""
        self.board = [
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL],
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL],
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL],
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL],
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL],
            [EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL, EMPTY_VAL]
        ]
        self.board_history = []

    def get_game_result(self):
        """
        Check the Gameboard if a winner is found and returns the winner.
        If no winner is found return the Game State.
        """
        red_is_winner = winning_move(self.board, RED_PLAYER_VAL)

        yellow_is_winner = winning_move(self.board, YELLOW_PLAYER_VAL)

        if red_is_winner:
            return RED_PLAYER_VAL
        elif yellow_is_winner:
            return YELLOW_PLAYER_VAL
        else:
            draw_found = True
            # Check for draw
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j] == EMPTY_VAL:
                        draw_found = False
            if draw_found:
                return GAME_STATE_DRAW
            else:
                return GAME_STATE_NOT_ENDED

    def move(self, move, player):
        """Sets the move of the Player and saves it to the board_history."""
        self.board[move[0]][move[1]] = player
        self.board_history.append(copy.deepcopy(self.board))

    def get_board_history(self):
        """Return the board_history."""
        return self.board_history

    def get_board(self):
        """Returns the current board."""
        return self.board
