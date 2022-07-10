import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from tensorflow import keras


class ConnectFourModelTrain:

    def __init__(self, number_of_inputs, number_of_outputs, batch_size, epochs):
        self.numberOfInputs = number_of_inputs
        self.numberOfOutputs = number_of_outputs
        self.batchSize = batch_size
        self.epochs = epochs
        self.model = Sequential()
        self.model.add(Dense(42, 'relu', (number_of_inputs,)))
        self.model.add(Dense(42, 'relu'))
        self.model.add(Dense(number_of_outputs, 'softmax'))
        # for a multi-class classification problem
        self.model.compile('rmsprop', 'categorical_crossentropy', ['accuracy'])

    def train(self, dataset):
        input = []
        output = []
        for data in dataset:
            input.append(data[1])
            output.append(data[0])

        x = np.array(input).reshape((-1, self.numberOfInputs))
        y = to_categorical(output, 3)
        limit = int(0.8 * len(x))
        x_train = x[:limit]
        x_test = x[limit:]
        y_train = y[:limit]
        y_test = y[limit:]
        self.model.fit(
            x=x_train,
            y=y_train,
            batch_size=self.batchSize,
            epochs=self.epochs,
            validation_data=(x_test, y_test)
        )

    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs))[0][index]

    def save(self):
        self.model.save('nn_model')

    def load(self):
        self.model = keras.models.load_model('nn_model')
