"""
This Module holds the test function which tests the Neural Network Model.
"""
from src.game import Game, RED_PLAYER_VAL, YELLOW_PLAYER_VAL
from src.player import Player
from src.game_controller import GameController
from src.model_load import ConnectFourModelLoad


def test():
    """Tests the Neural Network Model."""
    red_player = Player(RED_PLAYER_VAL, 'random')
    yellow_player = Player(YELLOW_PLAYER_VAL, 'random')

    model = ConnectFourModelLoad(42)

    red_neural_player = Player(RED_PLAYER_VAL, 'model', model)
    yellow_neural_player = Player(YELLOW_PLAYER_VAL, 'model', model)

    first_game = Game()
    game_controller = GameController(first_game, red_player, yellow_neural_player)
    print(" * Playing with yellow player as Neural Network")
    game_controller.simulate_many_games(100, 'src/trainingdata.csv')

    second_game = Game()
    game_controller = GameController(second_game, red_neural_player, yellow_player)
    print(" * Playing with red player as Neural Network")
    game_controller.simulate_many_games(100, 'src/trainingdata.csv')


print(" * Test the Model")
test()
print(" * Test finished")
