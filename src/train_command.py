# from game import Game, RED_PLAYER_VAL, YELLOW_PLAYER_VAL
# from player import Player
# from game_controller import GameController
from model_train import ConnectFourModelTrain
# from tensorflow import keras
import csv


def train():
    # first_game = Game()
    # red_player = Player(RED_PLAYER_VAL, 'random')
    # yellow_player = Player(YELLOW_PLAYER_VAL, 'random')

    # game_controller = GameController(first_game, red_player, yellow_player)
    # print(" * Playing with both players with random strategies")
    # game_controller.simulate_many_games(3)

    trainingdata = []

    with open('trainingdata.csv', 'r', newline='') as f:
        reader = csv.reader(f, delimiter=';')

        for row in reader:

            board = []

            for i in range(1, 7):
                board.append(list(map(int, row[i].split(','))))

            trainingdata.append((int(row[0]), board))

    # 42 inputs
    # 3 outputs
    # 50 batch size
    # 100 epochs
    model = ConnectFourModelTrain(42, 3, 50, 100)
    model.train(trainingdata)
    # model.train(game_controller.get_training_history())
    model.save()


print(" * Loading Keras model and Train")
train()
print(" * Training finished")
