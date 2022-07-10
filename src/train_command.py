from game import Game, RED_PLAYER_VAL, YELLOW_PLAYER_VAL
from player import Player
from game_controller import GameController
from model_train import ConnectFourModelTrain
from tensorflow import keras


def train():
    first_game = Game()
    red_player = Player(RED_PLAYER_VAL, 'random')
    yellow_player = Player(YELLOW_PLAYER_VAL, 'random')

    game_controller = GameController(first_game, red_player, yellow_player)
    print(" * Playing with both players with random strategies")
    game_controller.simulate_many_games(10)

    # 42 inputs
    # 3 outputs
    # 50 batch size
    # 100 epochs
    model = ConnectFourModelTrain(42, 3, 50, 100)
    model.train(game_controller.get_training_history())
    model.save()


print(" * Loading Keras model and Train")
train()
print(" * Training finished")
