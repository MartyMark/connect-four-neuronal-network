"""
This Modules holds the ConnectFourModelLoad Class.
"""
import numpy as np
from tensorflow import keras


class ConnectFourModelLoad:
    """This Class loads the Model from the nn_Model Directory."""
    def __init__(self, number_of_inputs):
        """Init function of the Class."""
        self.number_of_inputs = number_of_inputs
        self.model = keras.models.load_model('nn_model')

    def predict(self, data, index):
        """Calls the Predict method of the Model."""
        return self.model.predict(np.array(data).reshape(-1, self.number_of_inputs))[0][index]
