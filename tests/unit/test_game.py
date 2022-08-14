import numpy as np

from src.game import Game, RED_PLAYER_VAL, YELLOW_PLAYER_VAL, GAME_STATE_DRAW, GAME_STATE_NOT_ENDED


def test_game_new_board():
    game = Game()

    assert not np.any(game.get_board())


def test_game_reset_board():
    game = Game()
    game.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, -1, 0, 0],
        [0, 0, 0, -1, 1, -1, 1],
        [0, 0, -1, -1, 1, 1, 1],
        [0, -1, 1, -1, 1, 1, -1],
    ]

    game.reset_board()

    assert not np.any(game.get_board())


def test_game_get_board_history():
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, -1, 0, 0],
        [0, 0, 0, -1, 1, -1, 1],
        [0, 0, -1, -1, 1, 1, 1],
        [0, -1, 1, -1, 1, 1, -1],
    ]

    game = Game()
    game.board_history = board

    assert game.get_board_history() == board


def test_game_move():
    board_before_move = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, -1],
    ]

    board_after_move = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, -1],
    ]

    game = Game()
    game.board = board_before_move
    game.move((5, 5), YELLOW_PLAYER_VAL)

    assert game.get_board() == board_after_move


def test_get_game_result_red_wins_horizontal():
    game = Game()
    game.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, -1, -1, -1, -1],
    ]

    assert game.get_game_result() == RED_PLAYER_VAL


def test_get_game_result_yellow_wins_vertical():
    game = Game()
    game.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, -1],
        [0, 0, 0, 0, 1, 0, -1],
        [0, 0, 0, 0, 1, -1, -1],
    ]

    assert game.get_game_result() == YELLOW_PLAYER_VAL


def test_get_game_result_red_wins_lower_left_diagonals():
    game = Game()
    game.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, -1],
        [0, 0, 0, 0, 0, -1, -1],
        [0, 0, 0, 0, -1, -1, 1],
        [1, 0, 0, -1, 1, 1, 1],
    ]

    assert game.get_game_result() == RED_PLAYER_VAL


def test_get_game_result_yellow_wins_upper_right_diagonals():
    game = Game()
    game.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [-1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, -1],
        [-1, -1, -1, 1, 0, 0, -1],
    ]

    assert game.get_game_result() == YELLOW_PLAYER_VAL


def test_get_game_result_draw():
    game = Game()
    game.board = [
        [1, -1, 1, -1, 1, -1, 1],
        [1, -1, 1, -1, 1, -1, 1],
        [1, -1, 1, -1, 1, -1, 1],
        [-1, 1, -1, 1, -1, 1, -1],
        [-1, 1, -1, 1, -1, 1, -1],
        [-1, 1, -1, 1, -1, 1, -1],
    ]

    assert game.get_game_result() == GAME_STATE_DRAW


def test_get_game_result_not_ended():
    game = Game()
    game.board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, -1],
        [0, 0, 0, 0, -1, -1, 1],
        [0, 0, 0, -1, 1, 1, 1],
    ]

    assert game.get_game_result() == GAME_STATE_NOT_ENDED
