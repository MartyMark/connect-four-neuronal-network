from model_train import ConnectFourModelTrain
import csv


def train():
    trainingdata = []

    with open('src/trainingdata.csv', 'r', newline='') as f:
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
    model.save()


print(" * Loading Keras model and Train")
train()
print(" * Training finished")
