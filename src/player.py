import random
import copy

from game import RED_PLAYER_VAL


class Player:

    def __init__(self, value, strategy='random', model=None):
        self.value = value
        self.strategy = strategy
        self.model = model

    def get_move(self, available_moves, board):
        if self.strategy == "random":
            return available_moves[random.randrange(0, len(available_moves))]
        else:
            max_value = 0
            best_move = available_moves[0]
            for availableMove in available_moves:
                board_copy = copy.deepcopy(board)
                board_copy[availableMove[0]][availableMove[1]] = self.value
                if self.value == RED_PLAYER_VAL:
                    value = self.model.predict(board_copy, 2)
                else:
                    value = self.model.predict(board_copy, 0)
                if value > max_value:
                    max_value = value
                    best_move = availableMove
            return best_move

    def get_player(self):
        return self.value
