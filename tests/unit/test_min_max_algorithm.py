import numpy as np
import math

from src.min_max import MinMaxAlgorithm
from src.game import RED_PLAYER_VAL, YELLOW_PLAYER_VAL


def test_minimax_red_player_1():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, -1, -1, -1],
    ]

    np_board = np.array(board, dtype=np.float64)
    np_board = np.flipud(np_board)

    min_max = MinMaxAlgorithm(YELLOW_PLAYER_VAL, RED_PLAYER_VAL)

    col, minimax_score = min_max.minimax(np_board, 5, -math.inf, math.inf, True)

    row = min_max.get_next_open_row(np_board, col)

    row = 5 - row

    assert row == 5
    assert col == 3


def test_minimax_red_player_2():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0],
        [-1, -1, 1, 1, 1, 0, 0],
    ]

    np_board = np.array(board, dtype=np.float64)
    np_board = np.flipud(np_board)

    min_max = MinMaxAlgorithm(YELLOW_PLAYER_VAL, RED_PLAYER_VAL)

    col, minimax_score = min_max.minimax(np_board, 5, -math.inf, math.inf, True)

    row = min_max.get_next_open_row(np_board, col)

    row = 5 - row

    assert row == 5
    assert col == 5


def test_minimax_yellow_player_1():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, -1, -1],
        [-1, 0, 0, 0, 1, 1, 1],
    ]

    np_board = np.array(board, dtype=np.float64)
    np_board = np.flipud(np_board)

    min_max = MinMaxAlgorithm(RED_PLAYER_VAL, YELLOW_PLAYER_VAL)

    col, minimax_score = min_max.minimax(np_board, 5, -math.inf, math.inf, True)

    row = min_max.get_next_open_row(np_board, col)

    row = 5 - row

    assert row == 5
    assert col == 3


def test_minimax_yellow_player_2():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, -1, -1],
        [0, 0, 0, 1, -1, 1, 1],
    ]

    np_board = np.array(board, dtype=np.float64)
    np_board = np.flipud(np_board)

    min_max = MinMaxAlgorithm(RED_PLAYER_VAL, YELLOW_PLAYER_VAL)

    col, minimax_score = min_max.minimax(np_board, 5, -math.inf, math.inf, True)

    row = min_max.get_next_open_row(np_board, col)

    row = 5 - row

    assert row == 4
    assert col == 3
