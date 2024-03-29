"""
This Module holds the ConnectFourModelTrain Class.
"""
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.utils.np_utils import to_categorical


class ConnectFourModelTrain:
    """This Class holds all the Methods neccessary to train the Model."""
    def __init__(self, number_of_inputs, number_of_outputs, batch_size, epochs):
        self.number_of_inputs = number_of_inputs
        self.number_of_outputs = number_of_outputs
        self.batch_size = batch_size
        self.epochs = epochs
        self.model = Sequential()
        self.model.add(Dense(42, 'relu', (number_of_inputs,)))
        self.model.add(Dense(42, 'relu'))
        self.model.add(Dense(number_of_outputs, 'softmax'))
        # for a multi-class classification problem
        self.model.compile('rmsprop', 'categorical_crossentropy', ['accuracy'])

    def train(self, dataset):
        """Trains the Model with the given Dataset."""
        input_model = []
        output = []
        for data in dataset:
            input_model.append(data[1])
            output.append(data[0])

        x = np.array(input_model).reshape((-1, self.number_of_inputs))
        y = to_categorical(output, 3)
        limit = int(0.8 * len(x))
        x_train = x[:limit]
        x_test = x[limit:]
        y_train = y[:limit]
        y_test = y[limit:]
        self.model.fit(
            x=x_train,
            y=y_train,
            batch_size=self.batch_size,
            epochs=self.epochs,
            validation_data=(x_test, y_test)
        )

    def predict(self, data, index):
        """Returns the next move of the Neural Network."""
        return self.model.predict(np.array(data).reshape(-1, self.number_of_inputs))[0][index]
