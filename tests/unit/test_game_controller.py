import numpy as np

from src.game import RED_PLAYER_VAL, YELLOW_PLAYER_VAL, Game
from src.game_controller import GameController
from src.model_load import ConnectFourModelLoad
from src.player import Player


def test_simulate_many_games_random():
    red_player = Player(RED_PLAYER_VAL, 'random')
    yellow_player = Player(YELLOW_PLAYER_VAL, 'random')

    game = Game()
    game_controller = GameController(game, red_player, yellow_player)
    game_controller.simulate_many_games(1, 'test')
    assert np.any(game_controller.get_training_history())


def test_simulate_many_games_random_neuronal_network():
    model = ConnectFourModelLoad(42)

    red_neural_player = Player(RED_PLAYER_VAL, 'model', model)
    yellow_player = Player(YELLOW_PLAYER_VAL, 'random')

    game = Game()
    game_controller = GameController(game, red_neural_player, yellow_player)
    game_controller.simulate_many_games(1, 'test')
    assert np.any(game_controller.get_training_history())
