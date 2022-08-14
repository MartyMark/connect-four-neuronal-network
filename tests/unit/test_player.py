from src.game import RED_PLAYER_VAL
from src.model_load import ConnectFourModelLoad
from src.player import Player


def test_get_move_random():
    player = Player(RED_PLAYER_VAL, 'random')

    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, -1],
        [0, 0, 0, 0, -1, -1, 1],
        [0, 0, 0, -1, 1, 1, 1],
    ]
    move = player.get_move(board)

    assert len(move) == 2
    assert all([isinstance(item, int) for item in move])


def test_get_move_neuronal():
    model = ConnectFourModelLoad(42)

    player = Player(RED_PLAYER_VAL, 'model', model)

    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, -1],
        [0, 0, 0, 0, -1, -1, 1],
        [0, 0, 0, -1, 1, 1, 1],
    ]
    move = player.get_move(board)

    assert len(move) == 2
    assert all([isinstance(item, int) for item in move])


def test_get_player():
    player = Player(RED_PLAYER_VAL, 'random')

    assert player.get_player() == RED_PLAYER_VAL
