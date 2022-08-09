import copy
import numpy as np
from tensorflow import keras

from util import one_hot


class ConnectFourModelLoadSecond:

    def __init__(self):
        self.model = keras.models.load_model('nn_model_second')
        self.model_2 = keras.models.load_model('nn_model_2_second')

    def predict(self, player, board):
        # converts current board state into the 27 length binary game state.
        if player == -1:
            pre = self.model.predict(np.asarray([one_hot(board)]), batch_size=1)[0]
        else:
            pre = self.model_2.predict(np.asarray([one_hot(board)]), batch_size=1)[0]

        highest = -1000
        num = -1
        for j in range(0, 7):
            if board[0][j] == 0:  # if square is empty, check prediction for that move. keep highest scoring move.
                if pre[j] > highest:
                    highest = copy.deepcopy(pre[j])
                    num = j

        for n in range(5, -1, -1):
            if board[n][num] == 0:  # if square is empty, make it 1.
                return n, num
