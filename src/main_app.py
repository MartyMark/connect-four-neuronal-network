import ast
import copy

from flask import Flask
from flask import request

from model_load import ConnectFourModelLoad
from player import Player
from operation_util import get_available_moves

app = Flask(__name__)

model = ConnectFourModelLoad(42)


@app.route("/predict", methods=['POST'])
def predict():
    message = request.get_json(force=True)
    board = message['board']
    player_value = int(message['player'])

    board = ast.literal_eval(board)

    player = Player(player_value, 'model', model)

    best_move = player.get_move(board)

    board[best_move[0]][best_move[1]] = player_value

    return {"x": best_move[0], "y": best_move[1]}
