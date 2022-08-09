import ast

import numpy as np

from model_train_second import ConnectFourModelTrainSecond
import csv


def train():
    games = []

    with open('trainingdata.csv', 'r', newline='') as f:
        reader = csv.reader(f, delimiter=';')

        game = []

        for row in reader:
            board = ast.literal_eval(row[0])

            if not np.any(board) and game:
                games.append(game)
                game = []

            game.append(board)

    model = ConnectFourModelTrainSecond()
    model.train(games)
    model.save()


print(" * Loading Keras model and Train")
train()
print(" * Training finished")
