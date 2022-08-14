from src.game import RED_PLAYER_VAL, YELLOW_PLAYER_VAL
from src.operation_util import get_available_moves, winning_move


def test_get_move_random():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, -1],
        [0, 0, 0, 0, -1, -1, 1],
        [0, 0, 0, -1, 1, 1, 1],
    ]

    available_moves = get_available_moves(board)

    assert available_moves == [[5, 0], [5, 1], [5, 2], [4, 3], [3, 4], [2, 5], [2, 6]]


def test_winning_move_red_wins_horizontal():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, -1, -1, -1, -1],
    ]

    assert winning_move(board, RED_PLAYER_VAL)


def test_winning_move_yellow_wins_vertical():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, -1],
        [0, 0, 0, 0, 1, 0, -1],
        [0, 0, 0, 0, 1, -1, -1],
    ]

    assert winning_move(board, YELLOW_PLAYER_VAL)


def test_winning_move_red_wins_lower_left_diagonals():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, -1],
        [0, 0, 0, 0, 0, -1, -1],
        [0, 0, 0, 0, -1, -1, 1],
        [1, 0, 0, -1, 1, 1, 1],
    ]

    assert winning_move(board, RED_PLAYER_VAL)


def test_winning_move_yellow_wins_upper_right_diagonals():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [-1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, -1],
        [-1, -1, -1, 1, 0, 0, -1],
    ]

    assert winning_move(board, YELLOW_PLAYER_VAL)
