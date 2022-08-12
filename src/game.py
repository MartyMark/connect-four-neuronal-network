"""
This Module holds the Game Class.
"""
import copy

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
        winner_found = False
        current_winner = None
        # Find winner on horizontal
        for i in range(NUM_ROWS):
            if not winner_found:
                for j in range(NUM_COLUMNS - REQUIRED_SEQUENCE - 1):
                    if self.board[i][j] != 0 and self.board[i][j] == self.board[i][j + 1] \
                        and self.board[i][j] == \
                            self.board[i][j + 2] and \
                            self.board[i][j] == self.board[i][j + 3]:
                        current_winner = self.board[i][j]
                        winner_found = True

        # Find winner on vertical
        if not winner_found:
            for j in range(NUM_COLUMNS):
                if not winner_found:
                    for i in range(NUM_ROWS - REQUIRED_SEQUENCE - 1):
                        if self.board[i][j] != 0 and self.board[i][j] == self.board[i + 1][j] \
                            and self.board[i][j] == \
                                self.board[i + 2][j] and \
                                self.board[i][j] == self.board[i + 3][j]:
                            current_winner = self.board[i][j]
                            winner_found = True

        # Check lower left diagonals
        if not winner_found:
            for i in range(NUM_ROWS - REQUIRED_SEQUENCE - 1):
                j = 0
                while j <= i:
                    if self.board[i][j] != 0 and self.board[i][i] == self.board[i + 1][j + 1] \
                        and self.board[i][i] == \
                            self.board[i + 2][j + 2] and \
                            self.board[i][i] == self.board[i + 3][j + 3]:
                        current_winner = self.board[i][j]
                        winner_found = True
                    j = j + 1

        # Check upper right diagonals
        if not winner_found:
            for j in range(NUM_COLUMNS - REQUIRED_SEQUENCE - 1):
                i = j
                while i <= NUM_ROWS - REQUIRED_SEQUENCE - 1:
                    if self.board[i][j] != 0 and self.board[i][i] == self.board[i + 1][j + 1] \
                        and self.board[i][i] == \
                            self.board[i + 2][j + 2] and \
                            self.board[i][i] == self.board[i + 3][j + 3]:
                        current_winner = self.board[i][j]
                        winner_found = True
                    i = i + 1

        if winner_found:
            return current_winner
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
