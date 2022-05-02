import numpy as np
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical


class ConnectFourModel:

    def __init__(self, numberOfInputs, numberOfOutputs, batchSize, epochs):
        self.numberOfInputs = numberOfInputs
        self.numberOfOutputs = numberOfOutputs
        self.batchSize = batchSize
        self.epochs = epochs
        self.model = Sequential()
        self.model.add(Dense(42, 'relu', (numberOfInputs,)))
        self.model.add(Dense(42, 'relu'))
        self.model.add(Dense(numberOfOutputs, 'softmax'))
        self.model.compile('categorical_crossentropy', "rmsprop", ['accuracy'])

    def train(self, dataset):
        input = []
        output = []
        for data in dataset:
            input.append(data[1])
            output.append(data[0])

        X = np.array(input).reshape((-1, self.numberOfInputs))
        y = to_categorical(output, 3)
        limit = int(0.8 * len(X))
        X_train = X[:limit]
        X_test = X[limit:]
        y_train = y[:limit]
        y_test = y[limit:]
        self.model.fit(X_train, y_train, (X_test, y_test), self.epochs, self.batchSize)

    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs))[0][index]