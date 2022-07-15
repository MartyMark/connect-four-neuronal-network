import ast
import copy

from flask import Flask
from flask import request

from game import RED_PLAYER_VAL
from model_load import ConnectFourModelLoad
from player import Player
from operation_util import get_available_moves

app = Flask(__name__)

model = ConnectFourModelLoad(42)


def get_move(board, player):
    available_moves = get_available_moves(board)

    max_value = 0
    best_move = available_moves[0]
    for availableMove in available_moves:
        board_copy = copy.deepcopy(board)
        board_copy[availableMove[0]][availableMove[1]] = player
        if player == RED_PLAYER_VAL:
            value = model.predict(board_copy, 2)
        else:
            value = model.predict(board_copy, 0)
        if value > max_value:
            max_value = value
            best_move = availableMove
    return best_move


@app.route("/predict", methods=['POST'])
def predict():
    message = request.get_json(force=True)
    board = message['board']
    player_value = int(message['player'])

    board = ast.literal_eval(board)

    player = Player(player_value, 'model', model)

    available_moves = get_available_moves(board)

    best_move = player.get_move(available_moves, board)

    board[best_move[0]][best_move[1]] = player_value

    return {"x": best_move[0], "y": best_move[1]}
