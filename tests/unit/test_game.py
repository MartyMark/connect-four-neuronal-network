import numpy as np

from src.game import Game


def test_game_new_board():
    game = Game()

    assert not np.any(game.board)
