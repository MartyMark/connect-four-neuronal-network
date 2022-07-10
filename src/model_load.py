import numpy as np
from tensorflow import keras


class ConnectFourModelLoad:

    def __init__(self, number_of_inputs):
        self.numberOfInputs = number_of_inputs
        self.model = keras.models.load_model('nn_model')

    def predict(self, data, index):
        return self.model.predict(np.array(data).reshape(-1, self.numberOfInputs))[0][index]