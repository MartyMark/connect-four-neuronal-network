"""
This Module holds the Method to train the Neural Network Model.
"""
import ast
import csv
from src.model_train import ConnectFourModelTrain


def train():
    """Trains the Neural Network Model with the Dataset from the CSV File."""
    trainingdata = []

    with open('src/trainingdata.csv', 'r', encoding="UTF-8", newline='') as file:
        reader = csv.reader(file, delimiter=';')

        for row in reader:
            board = ast.literal_eval(row[1])

            trainingdata.append((int(row[0]), board))

    # 42 inputs
    # 3 outputs
    # 50 batch size
    # 100 epochs
    model = ConnectFourModelTrain(42, 3, 50, 100)
    model.train(trainingdata)
    model.save()


print(" * Loading Keras model and Train")
train()
print(" * Training finished")
