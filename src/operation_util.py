"""
This Module holds helper functions.
"""
EMPTY_VAL = 0
NUM_ROWS = 6
NUM_COLUMNS = 7


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


def winning_move(board, piece):
    """Detects if there is a winner in the game board."""

    # Check horizontal locations for win
    for column in range(NUM_COLUMNS - 3):
        for row in range(NUM_ROWS):
            if board[row][column] == piece \
                    and board[row][column + 1] == piece \
                    and board[row][column + 2] == piece \
                    and board[row][column + 3] == piece:
                return True

    # Check vertical locations for win
    for column in range(NUM_COLUMNS):
        for row in range(NUM_ROWS - 3):
            if board[row][column] == piece \
                    and board[row + 1][column] == piece \
                    and board[row + 2][column] == piece \
                    and board[row + 3][column] == piece:
                return True

    # Check positively sloped diaganols
    for column in range(NUM_COLUMNS - 3):
        for row in range(NUM_ROWS - 3):
            if board[row][column] == piece \
                    and board[row + 1][column + 1] == piece \
                    and board[row + 2][column + 2] == piece \
                    and board[row + 3][column + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for column in range(NUM_COLUMNS - 3):
        for row in range(3, NUM_ROWS):
            if board[row][column] == piece \
                    and board[row - 1][column + 1] == piece \
                    and board[row - 2][column + 2] == piece \
                    and board[row - 3][column + 3] == piece:
                return True
