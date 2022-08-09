import ast
import copy
import math
import numpy as np

from flask import Flask
from flask import request

from model_load_second import ConnectFourModelLoadSecond
from util import split

app = Flask(__name__)

model_second = ConnectFourModelLoadSecond()


@app.route("/predict", methods=['POST'])
def predict():
    message = request.get_json(force=True)
    board = message['board']
    player_value = int(message['player'])

    board = ast.literal_eval(board)

    best_move = model_second.predict(player_value, board)

    return {"x": best_move[0], "y": best_move[1]}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
