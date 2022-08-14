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
    # Check horizontal locations for win
    for c in range(NUM_COLUMNS - 3):
        for r in range(NUM_ROWS):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(NUM_COLUMNS):
        for r in range(NUM_ROWS - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(NUM_COLUMNS - 3):
        for r in range(NUM_ROWS - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                    board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(NUM_COLUMNS - 3):
        for r in range(3, NUM_ROWS):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                    board[r - 3][c + 3] == piece:
                return True
